# sum = 0
# item = 0
# while True:
#     c = input('enter cost\n')
#     if c !='q':
#         item +=1
#         sum = sum+int(c)
#     else:
#         print(f'Grand total is {sum} May your output is correct.\nThanks')
#         break

# for d in range(1,item+1):
#     if True:
#         print('YOur Bill')
#         print(f'{d} = {c}')

# def factorial(number):
#     if number ==0 or number ==1:
#         return 1
#     else:
#         return number * factorial(number-1)
# def factorialtrailing(number):
#     fac = factorial(number)
#     print(fac)
#     count = 0
#     while(fac%10 ==0):
#         count = count+1
#         fac = fac/10
#     return count    
# if __name__ == '__main__':
#     print(factorialtrailing(34))



# def factorial(number):
#     if number ==0 or number ==1:
#         return 1
#     else:
#         return number * factorial(number-1)
# def factorialtrailing(number):        
#     count = 0
#     i = 5
#     while(number//i !=0):
#         count += int(number/i)
#         i = i*5
#     return count

# if __name__ == '__main__':
#     num = int(input('enter; '))
#     print(factorialtrailing(num))    