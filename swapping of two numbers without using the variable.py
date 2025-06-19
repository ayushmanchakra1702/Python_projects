def swap(a,b):
    
    a= a+b
    b=a-b
    a= a-b
    print(a,b)


val1 = int(input("enter the number you want to enter as A: "))
val2 = int(input("enter the number you want to enter as B: "))

swap(val1,val2)