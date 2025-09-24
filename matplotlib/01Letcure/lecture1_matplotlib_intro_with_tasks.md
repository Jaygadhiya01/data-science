
#  Lecture 1: Introduction to Matplotlib  

##  Learning Objectives  
By the end of this lecture, you will be able to:  
- Understand the basics of Matplotlib and its role in visualization.  
- Install and import Matplotlib.  
- Create different types of plots (line, bar, scatter, histogram).  
- Customize plots (labels, titles, legends, colors, styles).  
- Save plots as image files.  

---

##  1. What is Matplotlib?  
- A **data visualization library** in Python.  
- Provides 2D plotting, supports 3D via `mplot3d`.  
- Highly customizable (style, size, color, annotations).  
- Alternative libraries: **Seaborn, Plotly**, but Matplotlib is the foundation.  

---

##  2. Installation and Import  
```bash
pip install matplotlib
```
```python
import matplotlib.pyplot as plt
```

---

##  3. Creating a Simple Line Plot  
```python
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y)
plt.show()
```

---

##  4. Types of Plots in Matplotlib  

###  (a) Line Plot  
```python
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.show()
```

###  (b) Bar Plot  
```python
students = ["A", "B", "C", "D"]
marks = [85, 90, 78, 92]

plt.bar(students, marks, color="green")
plt.show()
```

###  (c) Scatter Plot  
```python
import numpy as np
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color="blue")
plt.show()
```

###  (d) Histogram  
```python
data = [1,2,2,3,3,3,4,4,4,4,5,5,6,7,8,8,9]
plt.hist(data, bins=5, color="orange", edgecolor="black")
plt.show()
```

---

##  5. Customizing a Plot  

### Adding Title & Labels  
```python
plt.plot(x, y)
plt.title("Growth of Sales")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.show()
```

### Adding Legend  
```python
plt.plot(x, y, label="Sales")
plt.legend()
plt.show()
```

### Changing Figure Size  
```python
plt.figure(figsize=(6,4))
plt.plot(x, y)
plt.show()
```

---

##  6. Subplots (Multiple Plots in One Figure)  
```python
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 20, 15, 10, 5]

plt.subplot(1, 2, 1)
plt.plot(x, y1, color="blue")
plt.title("Square")

plt.subplot(1, 2, 2)
plt.plot(x, y2, color="red")
plt.title("Decreasing")

plt.show()
```

---

##  7. Saving a Plot as an Image  
```python
plt.plot(x, y)
plt.savefig("plot.png")   # Save as PNG
plt.savefig("plot.pdf")   # Save as PDF
```

---

##  8. Styles in Matplotlib  
```python
plt.style.use("ggplot")   # use built-in style
plt.plot(x, y)
plt.show()
```

Other styles: `seaborn`, `fivethirtyeight`, `dark_background` etc.  

---

##  9. Real-World Applications of Matplotlib  
- Data analysis (sales trends, stock market).  
- Machine learning model visualization.  
- Research papers and scientific graphs.  
- Dashboard visualizations.  

---

##  Summary  
- Matplotlib is the foundation of Python visualization.  
- Supports multiple charts: line, bar, scatter, histogram.  
- Highly customizable with labels, legends, figure size, and styles.  
- Supports subplots and saving graphs.  

---

##  Practical Tasks (10 Exercises)

### Task 1: Simple Line Plot
- Plot x = [1,2,3,4,5], y = [2,4,6,8,10].

### Task 2: Customize Line Style
- Create a line plot with red color, dashed line, and circle markers.

### Task 3: Bar Plot of Student Marks
- Students = ["A","B","C","D"], Marks = [78,85,90,95].  
- Plot a bar chart with blue color.

### Task 4: Scatter Plot with Random Data
- Generate 50 random x and y values using NumPy.  
- Plot them as a scatter plot.

### Task 5: Histogram of Age Data
- Ages = [22,25,30,22,30,35,40,22,28,30,35,40,50].  
- Create a histogram with 5 bins.

### Task 6: Add Titles and Labels
- Create a line plot and add title “Monthly Sales”, x-label “Months”, y-label “Sales”.

### Task 7: Multiple Lines on Same Graph
- Plot y1 = [2,4,6,8,10] and y2 = [1,3,5,7,9] on the same plot.  
- Add legends to differentiate.

### Task 8: Subplots Example
- Create two subplots:  
  1. Line plot of y = x^2  
  2. Line plot of y = x^3

### Task 9: Save Your Plot
- Create any plot and save it as “myplot.png”.

### Task 10: Apply Different Styles
- Use different Matplotlib styles like `ggplot`, `seaborn`, `dark_background` and compare outputs.


