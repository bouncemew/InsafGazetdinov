cost_price = int(input("Введите себестоимость: "))
sales_price = int(input("Введите цену товара: "))
profitability = (sales_price - cost_price) / sales_price
profitability = round((sales_price - cost_price) / sales_price * 100, 1)
print(f'Доходность : {profitability!r}%')