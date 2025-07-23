# try :
#     x=int(input("enter the number first"))
#     y=int(input("enter the number second"))
#     result=x / y
#     print("result",result)


# except ZeroDivisionError as e:
#     print(e)
#     print("you have enter the zero value for number second")
#     x=int(input("enter the number first"))
#     y=int(input("enter the number second"))
#     result = x / y
#     print("result",result)



# except TypeError as e:
#     print(e)
#     print("you have enter the character instead of number")
#     x=int(input)




# try:
#     x=int(input("enter the number first"))
#     y=int(input("enter the number second"))
#     result = x / y
#     print("result",result)


# except Exception as e:
#     print(e)
#     x=int(input("enter the number first"))
#     y=int(input("enter the number second"))
#     result = x / y
#     print("result",result)    




# def add():
#         try:
#             x=int(input("enter the number first"))
#             y=int(input("enter the number second"))
#             result = x / y
#             print("result",result)

#         except Exception as e:
#              print(e)
#              print("you have not")
#              result = x / y
#              print("result",result)






# try:
#      if x >100:
#           raise Exception("Sorry,no numbers above 100")
     
#      elif x == 0:
#           raise Exception("Sorry,age is zero")
#      print(f"my age is {x}")

# except Exception as e:
#      print(e)
#      x =int(input("Re - Enter the age"))
#      print(F"my age is(x): ")
        



# class negative_error(Exception):
#      def __init__ (self,message):
#      super().__init__(message)


# class zero_error (Exception):
#      def __init__(self,message):
#      super().__init__(message) 


# x=int(input("enter the age"))  
# try:
#      if x < 0:
#           raise negative_error("Sorry,no numbers below zero")

#      elif x == 0:
#           raise zero_error("Sorry,age is zero")

# except negative_error as e:
#      print(e)
#      print("you have enter the negative number") 
#      x= int(input("Re- Enter the age"))
                