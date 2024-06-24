import random
import string

def password(a,b):
    if a==1:
        combination = string.ascii_letters
    elif a==2:
        combination = string.ascii_letters + string.digits
    elif a== 3:
        combination = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid")
    return ''.join(random.choice(combination) for _ in range(b))


def main():
    print("Welcome to Password generator")
    print("Enter the length of the password you want to have:\n1.6\n2.7\n3.8\n4.9\n5.10\n6.More than 10")
    n=int(input("Enter your choice:"))

    j = {1:6,2:7,3:8,4:9,5:10,6:11}
    length = j[n]
    print("Choose the difficulty level of the password you want:\n1.Simple\n2.Medium\n3.Hard")
    m=int(input("Enter your choice:"))

    c= password(m,length)
    print("Your password is:",c)

if __name__ == "__main__":
    main()
