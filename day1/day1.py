from expense import EXPENSE_LIST

## Part 1 to find 2 #'s in the list that add up to 2020 and multipy them

for expense in EXPENSE_LIST:
    found_answer = False
    for b in EXPENSE_LIST:
        if EXPENSE_LIST.index(expense) == EXPENSE_LIST.index(b):
            continue
        elif int(expense) + int(b) == 2020:
            print (f"{expense} * {b} == {int(expense)*int(b)}")
            found_answer = True
            break
    if found_answer:
        break

## Part 2 to find 3 #'s in the list that add up to 2020 and multipy them

for a in EXPENSE_LIST:
    found_answer = False
    for b in EXPENSE_LIST:
        if EXPENSE_LIST.index(a) == EXPENSE_LIST.index(b):
            continue
        else:
            for c in EXPENSE_LIST:
                if any([EXPENSE_LIST.index(b) == EXPENSE_LIST.index(c), EXPENSE_LIST.index(a) == EXPENSE_LIST.index(b), EXPENSE_LIST.index(a) == EXPENSE_LIST.index(c)]):
                    continue
                elif int(a) + int(b) + int(c) == 2020:
                    print (f"{a} * {b} * {c} == {int(a)*int(b)*int(c)}")
                    found_answer = True
                    break
            if found_answer:
                break
    if found_answer:
        break

        
        
        # int(expense) + int(b) == 2020:
        #     print (f"{expense} * {b} == {int(expense)*int(b)}")
        #     found_answer = True
        #     break
    # if found_answer:
    #     break
