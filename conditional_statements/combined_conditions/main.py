discounted = True
low_in_stock = True
movingProduct = discounted or low_in_stock
promotion = not movingProduct
print(f"Is the item eligible for promotion? {promotion}")