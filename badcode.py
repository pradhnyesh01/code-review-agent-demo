def calculateTotal(items):
    total = 0
    for item in items:
        try:
            total += item.price
        except:
            pass
    return total
