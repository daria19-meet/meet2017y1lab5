##c=0
##for  number in range(1,100+1):
##    print(number)
##    c=c+number
##print(c)

def add_numbers (start,end):
    c=0
    for numbers in range(start,end+1):
        print (numbers)
        c=c+numbers
    return(c)
    
test=add_numbers(333,777)
print(test)


