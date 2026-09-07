
# Day 6 — Regression (housing_day6.csv)

**Your Goals:**
1) Train-test split; fit LinearRegression predicting `price`.
2) Report MAE, RMSE, and R^2.
3) Add interaction/features: `price_per_sqft = price/area_sqft` (EDA).
4) Try `RandomForestRegressor`; compare metrics.
5) Plot predicted vs. actual on the test set.

**Hints:**
- `mean_absolute_error`, `mean_squared_error` (square-root for RMSE)
- Avoid data leakage (compute metrics only on test set)
- `plt.scatter(y_test, y_pred)`
