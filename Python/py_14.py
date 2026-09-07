#map 

# numbers = [1, 2, 3, 4, 5]
# # Expected: [1, 4, 9, 16, 25]


# def square(x):
#     return x * x

# ans=map(square,numbers)

# print(list(ans))

# words = ["hello", "world", "python"]
# # Expected: ["HELLO", "WORLD", "PYTHON"]

# def to_uppercase(s):
#     return s.upper()

# x=map(to_uppercase,words)
# print(list(x))



#filter

# numbers = [10, 15, 20, 25, 30]
# # Expected: [10, 20, 30]

# def is_even(x):
#     return x%2==0

# ans=filter(is_even,numbers)
# print(list(ans))


# words = ["madam", "python", "level", "world", "radar"]
# # Expected: ["madam", "level", "radar"]
# def is_palindrome(s):
#     return s == s[::-1]

# ans=filter(is_palindrome,words)
# print(list(ans))



#reduce

# from functools import reduce

# # numbers = [1, 2, 3, 4]
# # numbers = [5, 10, 15, 20]
# numbers = [3, 8, 2, 10, 15, 7]


# ans=reduce(lambda x,y:x if x>y else y ,numbers)
# print(ans)




# map
# words = ["python", "ai", "beautiful", "sky"]
# # Expected: [1, 2, 5, 0]

# def count_vowels(s):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count   
# ans=map(count_vowels,words)
# print(list(ans))

# reduce
# from functools import reduce

# numbers = [2, 3, 4, 5]
# # Expected: 120

# def multiply(x, y):
#     return x * y
# ans=reduce(multiply,numbers)
# print(ans)



# filter

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# # Expected: [2, 3, 5, 7, 11]


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# ans=filter(is_prime,numbers)
# print(list(ans))



# map and reduce
words = ["python", "map", "reduce", "filter"]
# Expected: {"python": 6, "map": 3, "reduce": 6, "filter": 6}

def word_length(s):
    return (s, len(s))
ans=map(word_length,words)
print(dict(ans))    