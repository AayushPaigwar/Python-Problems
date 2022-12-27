#Write a function which prints all the numbers divisible by 3 and 5.

num1=[]
def DivisibleBy(num):
    for i in range (0,num+1):
        if (i % 3 == 0 and i % 5 == 0):
          num1.append(i)
         
DivisibleBy(100)
print(num1)