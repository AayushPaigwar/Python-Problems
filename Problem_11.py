# 10) write a program to get a list of odd number from the list of numbers given by user (use list comprehension)

ip=[int(num) for num in input("Enter the numbers:").split()]
odd=[num for num in ip if num%2==1]
print(odd)