prime = []
for num in range(1, 21):
    if num>1:
       print(num)
       for i in range(2, num):
           if (num % i) == 0:
               print(f"this is {num}")
               break
        #    else:
        #        print(f"this is the result{num}")
       else:
           prime.append(num)
           print(f"this is prime {num}")
print(prime)
