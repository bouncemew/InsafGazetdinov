list_of_prices = [40.6, 200.8, 15.3]
print("A.")
def my_func():
    for list in list_of_prices:
        rub = int(list)
        kop = round(list % 1 * 100)
        print(rub, "руб.", kop, "коп")
my_func()
list_of_prices.sort()
print("B.")
my_func()
list_reverse = list_of_prices.sort(reverse=True)
print("C.")
my_func()
print("D.")
max_price = max(list_of_prices)
rub = math.floor(max_price)
kop = round(max_price % 1 * 100)
print(rub, "руб.", kop, "коп")
