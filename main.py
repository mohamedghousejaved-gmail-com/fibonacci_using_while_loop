a= int(input("enter"))
n1, n2 = 0, 1
count = 0
if a<= 0:
   print("enter positive integer")
elif a == 1:
   print(a)
   print(n1)
else:
   while count < a:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1