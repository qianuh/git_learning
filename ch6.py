def reco_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


a = int(input("input a number : "))
if reco_even(a) == False:
    print("this number is odd")
else:
    print("this number is even")

