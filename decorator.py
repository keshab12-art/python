#without parameter function and eithout parameter dectetor
def decorator1(x):#say_hello
    def wrapper():
        print("something before function runs")
        print("start time")
        x()#say_hello()
        print("end time-starttime")
        return wrapper
    


    @decorator1
    def say_hello():
        print("hello")
        say_hello()
    

#with parameter function and with parameter dectetor
def decorator1 (fun):
    def wrpper(*args,**kwargs):
        print(f"(greetings)before function runs")

        fun(*args,**kwargs)
        print("something after the functin runs")
        return wrapper
    return 





 
gwueyeuydufdtrd      