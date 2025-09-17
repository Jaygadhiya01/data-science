
import numpy as np
# 1.Create an array with NaN values and replace them with the column mean.

a1=np.array([10, 20,np.nan, 30])

print("original array:", a1)
mean=np.nanmean(a1)
print("mean of the array:", mean)


# qustions 2
# 2.Given student marks [45, 67, 89, 34, 56, 78, 90], calculate mean, median, std, and 75th percentile.

studentmark=np.array([45,67,89,34,56,78,90])

mean=np.mean(studentmark)
print("mean :",mean)




# qustions :3
# 3.Generate 50 random ages between 18–30 and find unique ages.

age=np.random.randint(18,30,size=50)

print("age :",age)

uniqeage=np.unique(age)
print("uniqe age : ",uniqeage)


# qustion 4

# 4.Normalize the dataset [100, 200, 300, 400, 500] using broadcasting.

dataset=np.array([100,200,300,400,500])
norm_data=(dataset-dataset.min())/(dataset.max()-dataset.min())
print("norm_dataset",norm_data)

