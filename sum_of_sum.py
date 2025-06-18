#part 1 determination of n natural numbers 
def n_natural(a):
    number= 0
    val = []
    for i in range(0,a):
        number = number + 1
        val.append(number)
    print(val)

#part 2 calculation of first n natural numbers as sum  
    sum = 0
    val2 = []
    for i in val:
        sum = sum + i
        val2.append(sum)
    print(val2)
#part 3 calculation of sum of sum series of those numbers 
    sum1 = 0
    val3 = []
    for j in val2:
        sum1 = sum1 + j
        val3.append(sum1)
    print(val3)




integers = int(input("enter the number of n naturals number you want to find the sum of: "))
n_natural(integers) 
