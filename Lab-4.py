import pickle
class Customer:
    def __init__(self):
        self.name = ""
        self.cid = ""
        self.account_number = ""
        self.balance = ""
        self.credit_card = ""


    def create_customer(self):
        self.name = input("Please enter your name: ")
        self.cid = input("Please enter your customer ID: ")
        self.account_number = input("Please enter your number: ")
        self.balance = input("Please enter your balance: ")
        self.credit_card = input("Please enter your credit card: ")


    def display_customer(self):
        print(self.name)
        print(self.cid)
        print(self.account_number)
        print(self.balance)
        print(self.credit_card)


    def transfer_funds(self):
        self.balance = input("Please enter your balance: ")
        self.ammount = input("Please enter the ammount you want to transfer: ")
        self.beneficiary = input("Please enter your beneficiary: ")
        self.credit_card = input("Please enter your credit card: ")
        self.transfer_funds()


    #def trasnfer_funds (beneficiary_cust_object, amount):
       # self_balance -= amount
       # bene_cust_obj.balance += amount

   # def assing_user_card (card_object):
       # self.credit_card.append(card_object)


class Card:
    def __init__ (self):
        self.card_number = ""
        self.cvv = ""
        self.exiration_date = ""
        self.balance = ""

    def create_card (self):
        self.card_number = input("Please enter your card number: ")
        self.cvv = input("Please enter your cvv: ")
        self.expiration_date = input("Please enter your exiration date: ")
        self.balance = input("Please enter your balance: ")

    def display_card(self):
        print(self.card_number)
        print(self.cvv)
        print(self.expiration_date)
        print(self.balance)

Customers = []
Cards = []


while True:
    print("1. Create New Customer")
    print("2. Create New Credit Card")
    print("3. Transfer Funds")
    print("4. Assign User Card")
    print("5. Display Customer Info")
    print("6. Display Credit Card Info")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        customer = Customer()
        customer.create_customer()
        book_file = open("customer.dat", "wb")
        pickle.dump(customer, book_file)
        book_file.close()

    elif choice == "2":
        credit_card = CreditCard()
        credit_card.create_new_credit_card()
        book_file = open("credit_card.dat", "wb")
        pickle.dump(credit_card, book_file)
        book_file.close()

    elif choice == "3":
        transfer_funds = TransferFunds()
        transfer_funds.new_transfer_funds()
        book_file = open("transfer_funds.dat", "wb")
        pickle.dump(transfer_funds, book_file)
        book_file.close()

    elif choice == "4":
        assign_user_card = UserCard()
        assign_user_card.create_new_user_card()
        book_file = open("user_card.dat", "wb")
        pickle.dump(assign_user_card, book_file)
        book_file.close()

    elif choice == "5":
        read_customer_file = open("customer.dat", "rb")
        display_customer = pickle.load(read_customer_file)
        for customer in display_customer:
            customer.display_customer()
            read_customer_file.close()

    elif choice == "6":
        read_credit_card_file = open("credit_card.dat", "rb")
        display_credit_card = pickle.load(read_credit_card_file)
        for credit_card in display_credit_card:
            credit_card.display_credit_card()
            read_credit_card_file.close()

    elif choice == "7":
        break

