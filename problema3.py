b = int(input("Enter base value: "))
e = int(input("Enter exponent value: "))
c=b
i=1
while i < e:
    c = c * b
    i = i + 1
print("%s to the %s'th power is %s" %(b,e,c))
