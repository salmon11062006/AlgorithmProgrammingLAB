
def usd_converter(currency, amount):
    if currency == True:
        return (amount * 15000)
    else:
        return (amount / 15000)
    

num = usd_converter(True, 20)

print(num)