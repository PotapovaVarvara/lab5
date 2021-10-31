class Payment:
    total = None

    def __init__(self, total):
        self.total = total

    def print_info(self):
        print("Total= ", self.total)


class CashPayment(Payment):
    paid = None

    def __init__(self, total, paid):
        super().__init__(total)
        self.paid = paid

    def print_info(self):
        super().print_info()
        print("Cash Payment")

    def get_change(self):
        print("Paid", self.paid)
        change = self.paid - self.total;
        print("Change", change)
        return change


class CreditCardPayment(Payment):
    credit_card_number = None
    credit_card_date = None
    credit_card_balance_after_paid = None

    def __init__(self, total, number, date, credit_card_balance_after_paid):
        super().__init__(total)
        self.credit_card_number = number
        self.credit_card_date = date
        self.credit_card_balance_after_paid = credit_card_balance_after_paid

    def print_info(self):
        super().print_info()
        print("Credit Card Payment")
        print("Credit Card number: ", self.credit_card_number)
        print("Credit Card date: ", self.credit_card_date)

    def print_credit_card_balance_after_paid(self):
        print("Credit card balance", self.credit_card_balance_after_paid)


class CheckPayment(Payment):
    check_number = None
    check_date = None

    def __init__(self, total, number, date):
        super().__init__(total)
        self.check_number = number
        self.check_date = date

    def print_info(self):
        super().print_info()
        print("Check Payment")
        print("Check number: ", self.check_number)
        print("Check date: ", self.check_date)


cashPayment = CashPayment(1000, 2000)
creditCardPayment = CreditCardPayment(1000, "8355952", "10/7/2021", 500)
check = CheckPayment(1000, "9958222", "11/25/2020")

print("-----------------------")
cashPayment.print_info()
cashPayment.get_change()
print("-----------------------")
creditCardPayment.print_info()
creditCardPayment.print_credit_card_balance_after_paid()
print("-----------------------")
check.print_info()