i=1

while i<=100:
    print(i)
    i+=1

#Print all odd numbers from 1 to 50


i = 1

while i <= 50:
    print(i)
    i += 2

num=int(input("Enter number:"))
fact=1

for i in range(1,num+1):
    fact=fact*1
    print("Factorial number",num,"is",fact)

num=input("Enter number:")
reverse=num[::-1]
print("Reverse_number:",reverse)

num=input("Enter number:")
print("The no of digits:",len(num.lstrip('-')))

num = input("Enter a number: ")

total = sum(int(digit) for digit in num if digit.isdigit())

print("Sum of digits:", total)

num=int(input("Enter number:"))

if num <=0:
    print("Not a prime number")
else:
    for i in range(num,2):
        if i % 2==0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


print("New line added")
