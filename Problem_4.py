# Write a program to check whether a given letter is vowel or consonant.

ip = input("Enter the Letter:")
if (ip == 'a' or ip == 'e' or ip == 'i' or ip == 'o' or ip == 'u' or
        ip == 'A' or ip == 'E' or ip == 'I' or ip == 'O' or ip == 'U'):
    print(ip, "Its a vowel")
else:
    print(ip, "Its a consonant")
