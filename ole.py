import random

def phoneNumber(operator):
    endNum = random.randint(10000000,99999999)
    number = f"01{operator}{endNum}"
    print(number)

print('''                
                      CHOICE YOUR OPERATOR
                
                       (1)GRAMEENPHONE
                       (2)BANGLALINK
                       (3)ROBI
                       (4)TELETALK
                       (5)AIRTEL
''')

choice = input("Enter your choice: ")
amount = int(input("How many number you want:"))
if choice == '1':
    for i in range(amount+1):
        phoneNumber(7)
elif choice == '2':
    for i in range(amount+1):
        phoneNumber(9)
elif choice == '3':
    for i in range(amount+1):
        phoneNumber(8)
elif choice == '4':
    for i in range(amount+1):
        phoneNumber(5)
elif choice == '5':
    for i in range(amount+1):
        phoneNumber(6)
else:
    print("🙄ツবোকাচোদা,আবাল🤦")