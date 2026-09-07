# ============================
# CLEAN & FIXED STOCK DASHBOARD
# ============================

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, accuracy_score, classification_report
import plotly.graph_objs as go

st.set_page_config(layout="wide", page_title="Stock Predictor & Risk Dashboard")

# ---------------------------------------
# Download stock data
# ---------------------------------------
def download_data(ticker, period="2y", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval, progress=False)
    if df is None or df.empty:
        return None
    return df.dropna()


# ---------------------------------------
# Technical Indicators
# ---------------------------------------
def add_technical_indicators(df):
    df = df.copy()

    df["return"] = df["Close"].pct_change()

    df["ma10"] = df["Close"].rolling(10).mean()
    df["ma20"] = df["Close"].rolling(20).mean()
    df["ma50"] = df["Close"].rolling(50).mean()

    # RSI
    delta = df["Close"].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    rs = up.rolling(14).mean() / (down.rolling(14).mean() + 1e-9)
    df["rsi14"] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = df["Close"].ewm(span=12, adjust=False).mean()
    ema26 = df["Close"].ewm(span=26, adjust=False).mean()
    df["macd"] = ema12 - ema26
    df["macd_signal"] = df["macd"].ewm(span=9, adjust=False).mean()

    # Bollinger Bands
    df["bb_mid"] = df["Close"].rolling(20).mean()
    df["bb_std"] = df["Close"].rolling(20).std()
    df["bb_upper"] = df["bb_mid"] + 2 * df["bb_std"]
    df["bb_lower"] = df["bb_mid"] - 2 * df["bb_std"]

    # ATR
    tr = pd.concat([
        (df["High"] - df["Low"]),
        (df["High"] - df["Close"].shift()).abs(),
        (df["Low"] - df["Close"].shift()).abs()
    ], axis=1).max(axis=1)
    df["atr14"] = tr.rolling(14).mean()

    # Volatility
    df["vol20"] = df["return"].rolling(20).std() * np.sqrt(252)

    # Drawdown
    running_max = df["Close"].cummax()
    df["drawdown"] = (df["Close"] - running_max) / running_max

    return df.dropna()


# ---------------------------------------
# Feature Engineering
# ---------------------------------------
def make_features(df, n_lags=5):
    df = df.copy()

    for lag in range(1, n_lags + 1):
        df[f"lag_close_{lag}"] = df["Close"].shift(lag)
        df[f"lag_return_{lag}"] = df["return"].shift(lag)

    # Explicit targets
    df["target_return_1d"] = df["Close"].shift(-1) / df["Close"] - 1
    df["target_close_1d"] = df["Close"].shift(-1)

    return df.dropna()


# ---------------------------------------
# Risk scoring
# ---------------------------------------
def compute_risk_score(row):
    try:
        vol = float(row.get("vol20", 0))
        atr = float(row.get("atr14", 0)) / float(row.get("Close", 1))
        draw = abs(float(row.get("drawdown", 0)))
        score = (vol * 50 + atr * 30 + draw * 20) * 100
        return score
    except:
        return 0


def risk_bucket(score):
    if score < 3:
        return "Low"
    elif score < 8:
        return "Medium"
    return "High"


# ---------------------------------------
# Regression Model
# ---------------------------------------
def train_price_model(df, feature_cols):
    if "target_close_1d" not in df.columns:
        raise ValueError("target_close_1d missing!")

    X = df[feature_cols]
    y = df["target_close_1d"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    model = GradientBoostingRegressor(
        n_estimators=200, learning_rate=0.05, max_depth=5, random_state=42
    )
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    return model, X_test, y_test, preds


# ---------------------------------------
# Risk classifier
# ---------------------------------------
def train_risk_classifier(df):
    df = df.copy()
    df["risk_score_calc"] = df.apply(compute_risk_score, axis=1)
    df["risk_bucket"] = df["risk_score_calc"].apply(risk_bucket)

    map_label = {"Low": 0, "Medium": 1, "High": 2}
    df["risk_label"] = df["risk_bucket"].map(map_label)

    features = ["vol20", "atr14", "rsi14", "macd", "ma20", "drawdown"]
    df = df.dropna()

    X = df[features]
    y = df["risk_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)

    return clf, X_test, y_test, preds, features


# ---------------------------------------
# Timing Signal
# ---------------------------------------
def timing_signal(row, predicted_next_close):
    score = 0
    pred_return = predicted_next_close / row["Close"] - 1

    if pred_return > 0.005:
        score += 1

    if row["rsi14"] < 35:
        score += 1
    elif row["rsi14"] > 70:
        score -= 1

    if row["macd"] > row["macd_signal"]:
        score += 1
    else:
        score -= 0.5

    if row["Close"] > row["ma20"]:
        score += 0.5
    else:
        score -= 0.5

    if row["Close"] < row["bb_lower"]:
        score += 1.5

    if score >= 2:
        return "Strong Buy"
    if score >= 0.5:
        return "Buy"
    if score > -1:
        return "Hold"
    return "Sell"


# ---------------------------------------
# Streamlit UI
# ---------------------------------------
# st.title("📈 Stock Predictor, Risk & Investment Timing Dashboard")

with st.sidebar:
    ticker = st.text_input("Ticker", value="RELIANCE.NS")
    period = st.selectbox("Period", ["1y", "2y", "3y", "5y"], index=1)
    interval = st.selectbox("Interval", ["1d", "1wk"], index=0)
    n_lags = st.slider("Lag Features", min_value=3, max_value=10, value=5)
    run_button = st.button("Run / Refresh")

# ---------------------------------------
# PIPELINE
# ---------------------------------------
if run_button:
    st.info("⏳ Fetching and processing...")
    df = download_data(ticker, period, interval)
    df.columns = df.columns.map(lambda x: x[0] if isinstance(x, tuple) else x)

    if df is None or df.shape[0] < 100:
        st.error("Not enough data.")
        st.stop()

    df = add_technical_indicators(df)
    df = make_features(df, n_lags=n_lags)

    df["risk_score_calc"] = df.apply(compute_risk_score, axis=1)
    df["risk_bucket"] = df["risk_score_calc"].apply(risk_bucket)

    # 🔥 Safe feature selection
    feature_cols = [
        c for c in df.columns
        if isinstance(c, str) and (c.startswith("lag_close_") or c.startswith("lag_return_"))
    ] + ["rsi14", "macd", "ma20", "vol20", "atr14"]

    feature_cols = [c for c in feature_cols if c in df.columns]

    model, X_test, y_test, preds = train_price_model(df, feature_cols)

    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)

    clf, Xr_test, yr_test, yr_preds, risk_feat_cols = train_risk_classifier(df)
    acc = accuracy_score(yr_test, yr_preds)

    last = df.iloc[-1]
    # pred_close = model.predict(df[feature_cols].iloc[-1:].values)[0]
    pred_close = model.predict(df[feature_cols].iloc[-1:])[0]

    pred_return = pred_close / last["Close"] - 1
    signal = timing_signal(last, pred_close)

    # ---------------------------------------
    # Summary
    # ---------------------------------------
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Current Price", f"{last['Close']:.2f}")
    col2.metric("Predicted Next Close", f"{pred_close:.2f}", f"{pred_return*100:.2f}%")
    col3.metric("Risk Bucket", last["risk_bucket"], f"{last['risk_score_calc']:.2f}")
    col4.metric("Signal", signal)

    st.subheader("Model Performance")
    st.write(f"MAE: **{mae:.4f}**, R²: **{r2:.4f}**")
    st.write(f"Risk Classifier Accuracy: **{acc:.3f}**")

    # ---------------------------------------
    # Chart
    # ---------------------------------------
    st.subheader("Price Chart")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df["Close"], name="Close"))
    fig.add_trace(go.Scatter(x=df.index, y=df["ma20"], name="MA20"))
    st.plotly_chart(fig, use_container_width=True)

    st.success("Done!")

else:
    st.info("Enter ticker → Run to start.")
