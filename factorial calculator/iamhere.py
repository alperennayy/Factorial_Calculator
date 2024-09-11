                #factorial calculator#

a = int(input("enter the number whose factorial you want to calculate: "))
result = 1
i = 1

while i <= a: 
    result = result*i 
    i = i + 1
print(a,"! = ",result)
    
 