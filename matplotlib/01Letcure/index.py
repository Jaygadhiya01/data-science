import matplotlib.pyplot as plt
import numpy as np



# Task 1: Simple Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
# plt.plot(x, y)
# plt.show()

# Task 2: Customize Line Style
# plt.plot(x, y, color='red', linestyle='--', marker='o')
# plt.show()

# Task 3: Bar Plot of Student Marks

# students = ["A", "B", "C", "D"]
# marks = [78, 85, 90, 95]
# plt.bar(students, marks, color='blue')
# plt.show()

# Task 4: Scatter Plot with Random Data
# np.random.seed(0) 
# x_rand = np.random.rand(50)
# y_rand = np.random.rand(50)
# plt.scatter(x_rand, y_rand)
# plt.show()

 
# Task 5: Histogram of Age Data

# ages = [22,25,30,22,30,35,40,22,28,30,35,40,50]
# plt.hist(ages, bins=5, color='green', edgecolor='black')
# plt.show()


# Task 6: Add Titles and Labels
# months = [1,2,3,4,5,6]
# sales = [10, 20, 25, 30, 40, 50]
# plt.plot(months, sales, marker='o')
# plt.title("Monthly Sales")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()



# Task 7: Multiple Lines on Same Graph
y1 = [2,4,6,8,10]
y2 = [1,3,5,7,9]
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")
plt.legend()
plt.show()

# Task 8: Subplots Example

x_vals = np.arange(1, 10)

plt.subplot(1,2,1)
plt.plot(x_vals, x_vals**2, color='blue')

plt.subplot(1,2,2)
plt.plot(x_vals, x_vals**3, color='red')

plt.show()

# Task 9: Save Your Plot

plt.plot(x, y)
plt.savefig("myplot.png") 
plt.show()

# ---------------------------
# Task 10: Apply Different Styles
# ---------------------------
styles = ['ggplot', 'seaborn-v0_8', 'dark_background']
for style in styles:
    plt.style.use(style)
    plt.plot(x, y, marker='o')
    plt.show()
