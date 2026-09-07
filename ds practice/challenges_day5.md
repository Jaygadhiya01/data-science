
# Day 5 — Classification (admissions_day5.csv)

**Your Goals:**
1) Split data into train/test (e.g., 80/20).
2) Train LogisticRegression to predict `Admitted` from `GRE`, `GPA`, `Rank`.
3) Report accuracy, precision, recall, and confusion matrix.
4) Try DecisionTreeClassifier; compare performance.
5) Feature scaling: Does StandardScaler help LogisticRegression here?

**Hints:**
- `train_test_split`
- `LogisticRegression(max_iter=1000)`
- `classification_report`, `confusion_matrix`
- `Pipeline` to combine scaler + model
