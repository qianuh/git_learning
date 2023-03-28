basket = {'apple': 50, 'pen': 20, 'banana': 30}
method_num = basket.__len__()
money = 0
for i in basket:
    money += basket[i]

print("total money: %d" % (money))

