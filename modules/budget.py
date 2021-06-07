
class Budget:
    def __init__(self, income):
        self.set_monthly_income(income)

    # Users should be able to update their monthly income.
    def set_monthly_income(self, income):
        self.income = income

    # It should know how much the user's monthly costs are.
    def get_monthly_cost(self, month):
        monthly_costs = 0
        for txn in self.transactions:
            if txn.month == month:
                monthly_costs += txn.amount
        return monthly_costs
    
    def get_month_costs_by_category(self):
        mon

    def add_transaction(self, txn):
        self.transactions.append(x)

    def percent_report(self, month):
        total = self.get_monthly_cost(month)
