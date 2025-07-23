
# file_path='Users/Lenovo\Desktop\pythonclass/data.csv'
# #Reading CSV file using csv.reader
# with open(file_path,mode='r') as file:
#     csv_reader=csv.reader(file)
#     header=next(csv_reader)
#     for row in csv_reader:
#         print(row)
#         print(header)


#     print(type(row))  
#     print(header)

 
# import csv
# with open("hello.csv")as f:
#     csv_reader=csv.reader(f)

#     header=next(csv_reader)

#     for row in csv_reader:
#         print(row) #[ram,13,57,60,70]
#         sum=0
#         for x in range(2,len(row)):
#             sum+=int(row[x])
            # print("name",row[0])
            # print("total_marks",sum)

    

 
# import csv
# file_path= "hello.csv"

# with open(file_path,mode="r")as f1:
#     csv_reader=csv.reader(f1)
#     header=next(csv_reader)

#     with open("new_file_text","w")as f2:
#         for row in csv_reader:
#             marks=(int(x) for x in row[2:])
#             total_marks=sum(marks)
 
#             content=f"Name:{row[0]}, Age: {row[1]} Total marks:{total_marks}\n"
#             f2.write(content)
#             print(content)


# import csv
# # Example data to write csv
# data=[
#     ['Alice',30,'london']
#     ['Bob',25,'Paris']
#     ['Charlie',35,'berlin']
# ]


# file_path='output.csv'
# with open(file_path,mode='w',newline='')as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(['name','age','city'])
#     for row in data:
#         csv_writer.writerow(row)
    



# # dict reader and writer###################


# import csv
# file_path='data.csv'
# with open(file_path,mode="r")as file:
#     csv_reader=csv.DictReader(file)
#     for row in csv_reader:
#         print(row['Name'],row['City'])
    


# import csv
# data=[
#     { 'Name':'Alice','Age':30,'City':'London'},
#     { 'Name':'Bob','Age':25,'City':'paris'},
#     { 'Name':'Charlie','Age':35,'City':'Berlin'},
# ]
# file_path='output.csv'
# fieldnames=['Name','Age','City']

# with open(file_path,mode='w',newline='') as file:
#     writer=csv.DictWriter(file,fieldnames=fieldnames)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)



##########lambda##################3 

# square=lambda x:x**2
# print(square(5))


# add=lambda a,b: a+b
# print(add(3,4))


# numbers=[1,2,3,4,5]
# squared=list(map(lambda x: x**2,numbers))




# def sq(x):
#     return x**2

# new-sq = List(map(sq,lst))

# fruits=["apple","banana","cherry","pine"]
# new_fruits=["APPLE","BANANA","CHERRY","PINE"]



# #########filter##########
# numbers=[1,2,3,4,5,6,7,8,9,10] 
# def sq(x):
#     if x%2==0:
#         return True
    

# fruits=["apple","banana","cherry","pine"]
# new_fruits=list(filter(lambda x : "a" in x. lower(),fruits))



#from function import reduce################


# numbers=[1,2,3,4,5]
# sum= reduce(lambda x,y: x+y,numbers)
# print(sum)


# numbers=[3,8,1,6,2]
# max_num=reduce(lambda x,y:x if x>y else y,numbers)
# print(max_num)


# words=["hello","","World","!"]
# sentence=reduce(lambda x,y:x+y,words)
# print(sentence)

########## OS library############

# import os
# current_dir=os.getcwd()
# files=os.listdir(current_dir)
# print(files)



# ##########randomlibrary  
# import random
# random_number= random.randint(1,10)

# my_list=[1,2,3,4,5]
# random.shuffle(my_list)


# ########### math library

# import math
# sqrt_value=math.squrt(25)

# factorial_value=math.factorial(5)





# import csv
# file_path=''
# with open ("file1.csv")as f:
#     csv_reader=csv.reader(f)
#     header=next(csv_reader)
#     for row in csv_reader:
#         print(row)
#         print(header)


# import pandas as pd

# df = pd.read_csv('data.csv')

# df.fillna(130, inplace = True)
# print(df.to_string())




# import pandas as pd

# df = pd.read_csv('data.csv')

# df.fillna({"Calories": 130}, inplace=True)
# print(df.to_string())




# import pandas as pd

# df = pd.read_csv('data1.csv')

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# print(df.to_string())


# import pandas as pd

# df = pd.read_csv('data1.csv')

# df.loc[7, 'Duration'] = 45

# print(df.to_string())


# import pandas as pd

# df = pd.read_csv('data1.csv')

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.loc[x, "Duration"] = 120


# print(df.to_string())


# import pandas as pd

# df = pd.read_csv('data1.csv')

# for x in df.index:
#   if df.loc[x, "Duration"] > 120:
#     df.drop(x, inplace = True)


# print(df.to_string())


# import pandas as pd

# df = pd.read_csv('data1.csv')

# print(df.duplicated())
 

 

# df.to_csv("output.csv",index=False)

