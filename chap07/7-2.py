def open_account():
    print("새로운 계좌가 생성되었습니다.")

# 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withDraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money

    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)
balance = withDraw(balance, 500)