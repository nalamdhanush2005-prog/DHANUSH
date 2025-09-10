
class FinanceChatbot:
    def __init__(self):
        self.balance = 0.0
        self.income = 0.0
        self.expenses = 0.0

    def greet(self):
        print("Hello! I am your Personal Finance Chatbot.")
        print("You can tell me to add income or expense, or ask for your balance.")
        print("Type 'help' to see commands, 'exit' to quit.")

    def help(self):
        print("""
Commands:
- add income <amount>: Add income
- add expense <amount>: Add expense
- balance: Show current balance
- summary: Show income and expenses summary
- exit: Quit chatbot
        """)

    def add_income(self, amount):
        self.income += amount
        self.balance += amount
        print(f"Income of ${amount:.2f} added.")

    def add_expense(self, amount):
        self.expenses += amount
        self.balance -= amount
        print(f"Expense of ${amount:.2f} added.")

    def show_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def show_summary(self):
        print(f"Total income: ${self.income:.2f}")
        print(f"Total expenses: ${self.expenses:.2f}")
        print(f"Balance: ${self.balance:.2f}")

    def run(self):
        self.greet()
        while True:
            user_input = input("\nYou: ").strip().lower()
            if user_input == "exit":
                print("Goodbye! Take care of your finances.")
                break
            elif user_input == "help":
                self.help()
            elif user_input.startswith("add income"):
                try:
                    amount = float(user_input.split("add income")[1].strip())
                    self.add_income(amount)
                except:
                    print("Please enter a valid amount after 'add income'. Example: add income 1000")
            elif user_input.startswith("add expense"):
                try:
                    amount = float(user_input.split("add expense")[1].strip())
                    self.add_expense(amount)
                except:
                    print("Please enter a valid amount after 'add expense'. Example: add expense 500")
            elif user_input == "balance":
                self.show_balance()
            elif user_input == "summary":
                self.show_summary()
            else:
                print("Sorry, I didn't understand that. Type 'help' for commands.")

if __name__ == "__main__":
    bot = FinanceChatbot()
    bot.run()