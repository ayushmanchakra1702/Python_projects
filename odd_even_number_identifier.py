def values(b):
    val = []
    for i in range(0,b):
        number = int(input("enter your number you want to check: "))
        i=+1
        val.append(number)
    print(val)
    for i in val:
        if i%2==0:
            print(f"the number {i} is even")
        else:
            print(f"the number {i} is odd")
    i+=1
                  
#entering how many number we want to print
terms = int(input("enter the number of terms you want to check: "))

values(terms)