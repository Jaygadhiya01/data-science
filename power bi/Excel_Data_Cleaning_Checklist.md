# Excel Data Cleaning Checklist (Simple, No Formulas)

## 1. Clean Names

-   Remove hidden spaces: Data → Text to Columns → Finish\
-   Remove double spaces\
-   Remove unwanted symbols\
-   Fix capitalization using Flash Fill

## 2. Clean Emails

-   Remove spaces\
-   Replace `..` with `.`\
-   Fix domains: gmail → gmail.com\
-   Filter "Does Not Contain @" and fix manually

## 3. Clean Phone Numbers

-   Remove symbols: (), -, +, ext, phone:\
-   Remove spaces\
-   Keep only 10--11 digit numbers

## 4. Clean Dates

-   Use Text to Columns → Choose correct Date format\
-   Fix words like "today", "yesterday" manually

## 5. Clean Salary

-   Remove ₹, \$, commas, approx\
-   Fix "k" values manually (35k → 35000)\
-   Remove "not disclosed"

## 6. Clean Department

Replace: - finanace → Finance\
- sale → Sales\
- engg → Engineering\
- mktg → Marketing\
- support → Support

## 7. Clean Status

Standardize: - active → Active\
- inactive, left → Inactive

## 8. Clean Score

-   Remove N/A\
-   Sort A→Z and fix text values

## 9. Remove Duplicates

-   Data → Remove Duplicates

## 10. Remove Empty Rows

-   F5 → Special → Blanks → Delete Row
