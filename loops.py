# prime_numbers = []
# for num in range (1, 21):
#     if num > 1:
#         for i in range (2, num):
#             if (num % i) == 0:
#                 print(num)
#         else:
#             #print(num)
#             prime_numbers.append(num)

# print(prime_numbers)
prime_num = []
for num in range(1, 21):
    if num>1:
        print(f"this value is greater than {num}")
        for i in range(2, num):
            if (num % i) == 0:
                print(f'this is even {num}')
                break
            # else:
            #     print('hello')
            # print(f"this is the num: {num}")
        else:
            prime_num.append(num)
            print(f'this is prime{num}')
