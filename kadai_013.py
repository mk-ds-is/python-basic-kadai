def calculate_total(price, tax):
    tax_amount = price * (tax / 100)
    total_price = price + tax_amount
    print(f"{total_price}円")

calculate_total(100, 10)