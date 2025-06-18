# function for determining whether it ia binary number or not 
def binary_number(a):
        original_number = a
        while a>0:
            sum = a%10
            if sum>1:
                print("number is not binary")
                return 
            a = a//10
        print(f"the binary number is {original_number}")
      
input = int(input("enter the number you want to check: "))
binary_number(input)