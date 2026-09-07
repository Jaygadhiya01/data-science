
# Lecture: Donut Chart, Funnel Chart, and Line Chart in Power BI

## 1. Theory

## Donut Chart
A donut chart is similar to a pie chart but has a blank center. It is used to show category-wise proportions or percentage distribution out of a whole.

### When to Use
- Category-wise sales contribution
- Market share comparison
- Revenue distribution across departments

### Fields Used
- Legend: Category
- Values: Numeric field (Sales, Profit, Quantity)

---

## Funnel Chart
A funnel chart represents stages in a process or workflow. Each stage narrows down, showing how values decrease from start to end.

### When to Use
- Sales pipeline
- Lead conversion funnel
- Recruitment funnel
- Process drop-off analysis

### Fields Used
- Group: Stages
- Values: Numeric field

---

## Line Chart
A line chart displays trends over time. It is ideal for showing changes in data across days, months, or years.

### When to Use
- Weekly sales trend
- Monthly revenue trend
- Daily temperature trend
- Year-wise performance

### Fields Used
- X-Axis: Date or Time
- Y-Axis: Numeric values such as sales, revenue, or counts

---

# 2. Practical Steps

## Donut Chart
1. Import the dataset into Power BI.
2. Select the Donut chart visual.
3. Drag "Category" into Legend.
4. Drag "Sales" into Values.
5. Format the chart.

## Funnel Chart
1. Import the dataset.
2. Select the Funnel chart.
3. Drag "Stage" into Group.
4. Drag "Value" into Values.
5. Analyze stage-wise drop-offs.

## Line Chart
1. Import the dataset.
2. Select the Line chart visual.
3. Drag "Date" into X-axis.
4. Drag "Sales" into Y-axis.
5. Format time hierarchy if needed.

---

# 3. Practice Datasets

## Dataset 1: Donut Chart
| Category | Sales |
|----------|--------|
| Electronics | 45000 |
| Clothing | 32000 |
| Groceries | 28000 |
| Furniture | 15000 |
| Sports | 10000 |

## Dataset 2: Funnel Chart
| Stage | Leads |
|--------|--------|
| Initial Contact | 1000 |
| Qualified Leads | 700 |
| Proposal Sent | 450 |
| Negotiation | 250 |
| Deal Closed | 120 |

## Dataset 3: Line Chart
| Month | Sales |
|--------|--------|
| Jan | 15000 |
| Feb | 17000 |
| Mar | 21000 |
| Apr | 25000 |
| May | 23000 |
| Jun | 28000 |
| Jul | 32000 |
| Aug | 30000 |
| Sep | 27000 |
| Oct | 35000 |
| Nov | 37000 |
| Dec | 40000 |

---

# 4. Practice Questions

1. Create a donut chart using Dataset 1 and identify the highest category.
2. Calculate the percentage contribution of Electronics.
3. Create a funnel chart using Dataset 2 and find drop-off between stages.
4. Identify the smallest stage.
5. Create a line chart and identify the peak month.
6. Format the X-axis to display quarters.
7. Sort donut categories by descending sales.
8. Add percentage labels to funnel chart.
9. Create a combo chart for monthly sales.
10. Add a slicer and analyze filtered months.
