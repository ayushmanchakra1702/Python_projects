
# method 1 while loop
def digit(a):
    b = 0 
    i = 0
    while a>0:
        b = b + a%10
        a = a//10
    print(b)


 

val = int(input("enter the digits of a number you want to find the sum of: "))

digit(val)

# method 2 recursion method 
def sum_of_didgit(b):
    if b == 0:
        return b 
    else:
        return b%10 + sum_of_didgit(b//10)


val2 = int(input("enter the digits of a number you want to find the sum of: "))
print(sum_of_didgit(val2))