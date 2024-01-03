class User:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +Rs.{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -Rs.{amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transfer to {recipient.user_id}: -Rs.{amount}")
        else:
            print("Insufficient funds!")

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


class ATM:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        user = self.users.get(user_id)
        if user and user.pin == pin:
            return user
        else:
            return None


def main():
    atm = ATM()
    print("HI".center(50,'-'))
    print("WELCOME TO STATE BANK OF INDIA".center(50,'-'))

    # Create users
    user1 = User(user_id="Annapoorna", pin="1234", balance=1000)
    user2 = User(user_id="Druthi", pin="5678", balance=500)

    atm.add_user(user1)
    atm.add_user(user2)

    # User login
    user_id = input("\nEnter User ID: ")
    pin = input("Enter PIN: ")

    current_user = atm.authenticate_user(user_id, pin)

    if current_user:
        while True:
            print("\n1. Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                current_user.show_transaction_history()
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                current_user.withdraw(amount)
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                current_user.deposit(amount)
            elif choice == "4":
                recipient_id = input("Enter recipient's User ID: ")
                recipient = atm.users.get(recipient_id)
                if recipient:
                    amount = float(input("Enter transfer amount: "))
                    current_user.transfer(recipient, amount)
                else:
                    print("Recipient not found!")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid User ID or PIN.")


if __name__ == "__main__":
    main()
