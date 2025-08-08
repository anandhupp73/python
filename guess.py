# guess=int(input("enter a number : "))
# if guess==5:
#     print("you win")
# else:
#     print("you lose")

guess=int(input("enter a number between 1-10 : "))
while guess!=5:
    print("you lose")
    guess=int(input("enter a number : "))
print("you win")