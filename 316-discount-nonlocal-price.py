def discount_price(price, discount):
    
    def apply_discount():
        nonlocal price
        price = price - price*float(discount)
        return price
    
    apply_discount()
    return price
print(discount_price(100, 0.2))