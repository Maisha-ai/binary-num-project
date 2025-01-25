def bide(bistr):
    
    if all(char in '01' for char in bistr):
        
        decimal_number = int(bistr, 2)
        return decimal_number
    else:
        
        return print("Invalid binary number.")


bininput = input("Enter a binary number: ")
decioutput = bide(bininput)
print("The decimal of the binary ",bininput ,"is" ,decioutput)
