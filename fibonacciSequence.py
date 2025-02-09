print("Enter a number:")
print('Fibonacci sequence')
num=int(input())
num1=0
num2=1
count=0
print(num1,end="")
print(num2,end="")
while count<num:
     result=num1+num2
     print(result,end="")
     num1=num2
     num1=result
     count=count+1
