import csv
import datetime
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self, filename='data/transactions.csv'):
        self.filename = filename

    def add_transaction(self, date, amount, category, description):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])
        print(f"Transaction added: {amount} on {date} for {category} - {description}")

    def view_transactions(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)

    def generate_report(self):
        categories = {}
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[2]
                amount = float(row[1])
                if category in categories:
                    categories[category] += amount
                else:
                    categories[category] = amount

        # Plotting
        plt.bar(categories.keys(), categories.values())
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.show()

# Example usage
if __name__ == "__main__":
    tracker = FinanceTracker()

    # Add some transactions
    tracker.add_transaction(str(datetime.date.today()), -500, 'Groceries', 'Bought some food')
    tracker.add_transaction(str(datetime.date.today()), 1000, 'Salary', 'Monthly salary')
    tracker.add_transaction(str(datetime.date.today()), -30, 'Transport', 'Bus fare')

    # View transactions
    print("All transactions:")
    tracker.view_transactions()

    # Generate report
    tracker.generate_report()
