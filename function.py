#  #type1: parameter less and non return type function
# def add():
#     a=10
#     b=20
#     result=a+b
#     print(result)
#     add()


#     #type2: with parameter and non return type function
#     def add(a,b):
#         result=a+b
#         print(result)

#         x=5
#         y=10
#         add(x,y)

#         add(20,40)



#         #type type3: with parameter and return type function
#         def add(a,b):
#             result=a+b

#             return result
#         final_result=add(5,6)
#         print(final_result)


#         # type4: parameter less and return type function
#         def add():
#             a=6
#             b=10
#             result=a+b
#             return result
#         final_result=add


        


  

# def subtract(a, b):
#     """Return the subtraction of b from a."""
#     return a - b

# def main():
#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#     except ValueError:
#         print(" Invalid input. Please enter valid numbers.")
#         return

#     choice = input("Type 'add' to add, or 'subtract' to subtract: ").strip().lower()
    
#     if choice == 'add':
#         result = add(num1, num2)
#         print(f"{num1} + {num2} = {result}")
#     elif choice == 'subtract':
#         result = subtract(num1, num2)
#         print(f"{num1} - {num2} = {result}")
#     else:
#         print("! Invalid operation choice.")10

# if __name__ == "__main__":
#     main()
 


# def get_stats(numbers):
#     min_value=min(numbers)
#     max_value=max(numbers)
#     sum_value = sum(numbers)
#     return min_value, max_value, sum_value

# #calling the function
# numbers=[1,2,3,4,5]
# result=get_stats(numbers)

# print(result)
# print(f"min value is{result[0]}")
# print(f"max value is {result[1]}")
# print(f"sum value is {result[2]}")
 


# def my_function():
#     global x
#     x=10
#     print("Inside finction",x)
# my_function()


# #Args
# def addition(*args):
#     print("args",args)

# final_result=addition(1,2,3,4,5,6,7)    


# #kwargs
# def addition(**kwargs)
#     print("kwargs",kwargs)

# final_result = addition(cat = "xyz", doog="abc")   




# def  fact(n):
#     if n == 0 or n==1: 
#       return 1
#     return n* fact(n-1)
# result=fact(5)
# print("rresult",result)
    
    







#fibonacci series
def fibonacci(n): 
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n_terms=10
for i in range(n_terms):
    print(fibonacci(i),end="")
 