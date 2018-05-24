

# l = [2, 3, 5]
# p = [n*2 for n in l]
# print(p)



# p = []
# for n in l:
#     p.append(n * 2)
    
    
# print(p)

# [0, 2, 4, 6, 8, 10, 12]
# print([i*2 for i in range(7)])

# List Comprehension Challenges
# Example:
# Question 
#                 range(10) 
#                 -> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Answer
#                 [n * 2 for i in range(10)]
# 1. 
# range(5) 
# -> ["*", "*", "*", "*", "*"]

# print(["*" for i in range(5)])

# 2. words = ["Hi", "There", "Everyone"] 
# -> [2, 5, 8]
# print([len(i) for i in words])

# 3. range(8) 
#  [0, 1, 4, 9, 16, 25, 36, 49]

# print([i**2 for i in range(8)])

# 4. range(5) 
# -> [(0,1), (1,2), (2,3), (3,4), (4,5)]

# print([(i,i+1) for i in range(5)])
# 5. 'woohoo' 
# -> ['w', 'o', 'o', 'h', 'o', 'o']
# print([c for c in 'woohoo'])


#6. 
# words = ['car', 'cat', 'maps', 'if', 'level'] 
# print([(i,len(i))for i in words])

# #7
# object = ['car', 'cat', 'maps', 'if', 'level']
# print([(i, len(i)) for i in object])

# (x,y) = (1,2)
# print(x)
# print(y)

# 8. 
# values = [(False, False), (False, True), (True, False), (True, True)]
# print([(i or j) for i,j in values])


# ->[False, False, False, True]

[k  for  k in  newdict.keys()]