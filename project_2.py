class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True

        return False

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += transaction["amount"]

        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(
                amount,
                f"Transfer to {category.name}"
            )

            category.deposit(
                amount,
                f"Transfer from {self.name}"
            )

            return True

        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        result = f"{self.name:*^30}\n"

        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount = transaction["amount"]

            result += f"{description:<23}{amount:>7.2f}\n"

        result += f"Total: {self.get_balance()}"

        return result


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    # Calculate spending for each category.
    spending = []

    for category in categories:
        category_spending = 0

        for transaction in category.ledger:
            if transaction["amount"] < 0:
                category_spending += abs(transaction["amount"])

        spending.append(category_spending)

    total_spending = sum(spending)

    # Convert spending into percentages rounded down
    # to the nearest 10.
    percentages = []

    for amount in spending:
        if total_spending == 0:
            percentage = 0
        else:
            percentage = int((amount / total_spending) * 10) * 10

        percentages.append(percentage)

    # Create the percentage bars.
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "

        for percentage in percentages:
            if percentage >= level:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    # Horizontal line.
    chart += "    " + "-" * (len(categories) * 3 + 1)

    # Find the longest category name.
    max_name_length = max(len(category.name) for category in categories)

    # Write names vertically.
    for i in range(max_name_length):
        chart += "\n     "

        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "

    return chart