import numpy as np

# print("numpy")


# 1D array

arr=np.array([10,20,30,40])
print(arr)


#2D array
arr2d=np.array([[10,20,30],[40,50,60]])
print(arr2d)



#3D array
arr3d=np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr3d)


# size of array

print("arr",arr.size)
print("arr2",arr2d.size)
print("arr3",arr3d.size)

#shape of array

print("arr",arr.shape)
print("arr2",arr2d.shape)
print("arr3",arr3d.shape)


# datatype of array

print("arr",arr.dtype)
print("arr2",arr2d.dtype)
print("arr3",arr3d.dtype)



# zeros and ones

print(np.zeros(2))
print(np.zeros((2,3)))
print(np.zeros((2,3,4)))


# ones
print(np.ones(2))
print(np.ones((2,3)))
print(np.ones((2,3,4)))


# sqrt
a=[1,4,9,16,25,36,49,64,81]
print(np.sqrt(a))

# sum
print(np.sum(arr))


# mean
print(np.mean(arr2d))

# max
print(np.max(arr3d))


# random
print(np.random.rand(3,3))
print(np.random.randint(0,10,5))

# transpose
print(arr)
print(np.transpose(arr))

print(arr2d)
print(np.transpose(arr2d))

print(arr3d)
print(np.transpose(arr3d))


# ravel
print(arr)
print(np.ravel(arr))

print(arr2d)
print(np.ravel(arr2d))

print(arr3d)
print(np.ravel(arr3d))





