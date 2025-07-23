# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     def greet(self):
#             return 
        
        
# person1= Person("Alice",30)
# person2= Person("Bob",25)

# print(person1.name)
# print(person2.age)

# messsage = person1.greet()
# print(messsage)
              


 #single inheritance

# class Animal:
#     def speak(self):
#         return "Animal speaks"
    
#     class Dog(Animal):
#         def bark(self):
#             return "Dog barks"
        
# my_dog= Dog()
# print(my_dog.speaks())
# print(my_dog.barks())
    
    

#Multiple Inheritance

# class A:
#     def method_A(self):
#         return "Method A"
    
# class B:
#     def method_B(self):
#         return "Method B"

# class C(A,B):
#     def method_C(self):
#         return "Method C"   

#     obj_C =C()
#     print(obj_C.method_A())
#     print(obj_C.method_B())
#     print(obj_C.method_C())



#super

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def area(self):
#             return self.length*self.width
        
# class Square(Rectangle):
#     def __init__(self, side_length):
#                 super().__init__(side_length, side_length)

# rectangle=Rectangle(5,3)
# square= Square(4)

# print("Area of Rectangle",rectangle.area())
# print("Area os Square",square.area())



#########Access modifier############


class MyClass:
    def speak(self):
        return
 