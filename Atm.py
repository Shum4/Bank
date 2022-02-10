class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balanceinquiry(self):
        print("Your balance is 100$")

    def cashwidthdrawl(self, amount):
        new_amount=100-amount
        print("You withdrawed: "+str(amount) + "Your remaining balance is: "+str(new_amount))
        
def main():
    name = input("Hi, whats your name?")
    print("Hey, "+ name)
    cardnumber=input("Enter in your card number: ")
    pin= input("Input your pin: ")
    new_user= Atm(cardnumber, pin)

    print("Choose your activity")
    print("Activity 1: Balance inquiry")
    print("Activity 2: Cash withdrawal")
    activity=int(input("Enter chosen activity: "))

    if(activity == 1):
        new_user.balanceinquiry()
    elif(activity==2):
        amount=int(input("Enter the amount: "))
        new_user.cashwidthdrawl(amount)
    else:
        print("Enter the correct number")

if __name__ == "__main__":
    main()