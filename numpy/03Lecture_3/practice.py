import numpy as np 


# load salse.scv and calcualte total sales(quantity *price).
# extract onlu the second colum of a csv and find its mean and stateand divations

# save a new csv file containg product,quantity,and total sales


print("load salse.csv ")

# data=np.loadtxt(fname='salse.csv',delimiter=',',skiprows=1,usecols=(1,2))
# print(data)

data=np.genfromtxt(fname='salse.csv',delimiter=',',skip_header=1)
qan=data[:,1]
print(qan)
price=data[:,2]
print(price)

multi=qan*price
print(multi)
print(data)

print("sceond colum mean and std")
mean=np.nanmean(qan)
print("mean=",mean)
std=np.nanstd(qan)
print("std=",std)


total_sales=np.column_stack((data,multi))
np.savetxt('total_sales.csv',total_sales,delimiter=',',header='product,quantity,price,total_sales',fmt='%s',comments='')
print(total_sales)




