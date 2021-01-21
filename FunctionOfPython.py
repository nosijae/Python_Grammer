def open_account():
    print("creat new account")


def deposit(balance, money):
    print("complete receiving money. balance = {0}".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("complete drawing money. balance = {0}".format(balance - money))
        return balance - money
    else:
        print("incomplete drawing money. balance = {0}".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("commission = {0}, balance = {1}".format(commission, balance))
