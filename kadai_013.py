def calculate_total(price, tax):
    tax_amount = price * (tax / 100)
    total_price = price + tax_amount
    return total_price
calculate_total(100, 10)