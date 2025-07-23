# #Tuple

# tup=(1,2)
# print(type(tup))
# lst=[1]
# print(type(lst))



# tup=("abc",1,3,4,5)
# lst=list(tup)
# print(lst)
# lst.append(6)
# tup=tuple(lst)


# for x in tup:
#     print(x)
#     for y in range(tup):
#         print(y)

# print(tup[5])

# print(tup[1,5])



# #tuple unpacking


# tup=(1,2,3,4,5,)

# x,y,*z = tup

# x,*y,z = tup




# #SET
# 1.mutable
# 2. order

# set1={"apple","abc","xyz","abc","abc","abc"}
# print(set1)

# for x in set1:
#     print(x)


# set1 = {"apple"}
# print(type(set1))

# set1={}
# print(type(set1))

# set1=set()
# print(type(set1))




# set1={1,2,3,4}

  
# set1.add(15)

# set1.add(1)

# set1.remove(1)

# set1.discard(3)

# print(set1.pop())





# #SET OPERATION
# set1={1,2,3,4}
# set2={3,4,5,6}

# #Union
# print(set1/set2) #output:{1,2,3,4,5,6}

# #Intersection
# print(set1&set2) # output:(3,4)

# #Difference
# print(set1-set2) #output:{1,2}

# #symmetric Difference
# print(set1^set2) #output{1,2,5,6}


# #frozen set
# fs=frozenset({1,2,3})
# print(fs) #output:frozenset({1,2,3})
