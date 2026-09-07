# Power BI Practice Tasks (Beginner Level)

## Task 1: Total Sales Overview Dashboard

Create the following visuals:

### 1. Card Visuals

-   Total Sales (sum of total_amount)
-   Total Orders (count of order_id)
-   Total Quantity Sold (sum of quantity)

### 2. Clustered Column Chart

-   X-axis: category
-   Y-axis: total_amount
-   Title: Sales by Category

### 3. Pie Chart

-   Values: total_amount
-   Legend: payment_method
-   Title: Payment Method Share

### 4. Line Chart

-   X-axis: order_date (month)
-   Y-axis: total_amount
-   Title: Sales Trend Over Time

------------------------------------------------------------------------

## Task 2: Best-Selling Products Dashboard

### 1. Bar Chart

-   X-axis: total_amount
-   Y-axis: product_name
-   Filter: top 10
-   Title: Top 10 Products by Revenue

### 2. Column Chart

-   X-axis: product_name
-   Y-axis: quantity
-   Title: Top Products by Quantity Sold

### 3. Treemap

-   Group: category
-   Details: product_name
-   Values: total_amount
-   Title: Category vs Product Sales

------------------------------------------------------------------------

## Task 3: Geography-Based Sales

### 1. Map (Filled Map or Standard Map)

-   Location: state
-   Size/Color: total_amount
-   Title: Sales by State

### 2. Bar Chart

-   X-axis: city
-   Y-axis: total_amount
-   Title: Top Cities by Sales

------------------------------------------------------------------------

## Task 4: Order Status Insights

### 1. Donut Chart

-   Values: order_id (count)
-   Legend: order_status
-   Title: Order Status Distribution

### 2. Column Chart

-   X-axis: order_status
-   Y-axis: total_amount
-   Title: Revenue by Order Status

------------------------------------------------------------------------

## Task 5: Customer Analysis

### 1. Card Visual

-   Distinct count of customer_id

### 2. Bar Chart

-   X-axis: state
-   Y-axis: distinct count of customer_id
-   Title: Customers by State

### 3. Scatter Chart

-   X-axis: quantity
-   Y-axis: total_amount
-   Title: Quantity vs Sales Scatter Plot

------------------------------------------------------------------------

## Task 6: Sales Comparison Dashboard

### 1. Stacked Column Chart

-   X-axis: category
-   Y-axis: total_amount
-   Legend: payment_method
-   Title: Category vs Payment Method Sales

### 2. Line and Clustered Column Chart

-   Column: total_amount
-   Line: quantity
-   X-axis: order_date (month)

------------------------------------------------------------------------

## Final Project: Ecommerce Dashboard

Combine all charts into a single-page dashboard including: - KPIs
(Sales, Orders, Quantity, Customers) - Sales trend line chart -
Category-wise sales bar chart - Payment method pie chart - Top 10
products chart - Sales by state map - Order status donut chart
