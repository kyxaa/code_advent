from expense import EXPENSE_LIST

for expense in EXPENSE_LIST:
    found_answer = False
    for expense1 in EXPENSE_LIST:
        if EXPENSE_LIST.index(expense) == EXPENSE_LIST.index(expense1):
            continue
        elif int(expense) + int(expense1) == 2020:
            print (f"{expense} * {expense1} == {int(expense)*int(expense1)}")
            found_answer = True
            break
    if found_answer:
        break