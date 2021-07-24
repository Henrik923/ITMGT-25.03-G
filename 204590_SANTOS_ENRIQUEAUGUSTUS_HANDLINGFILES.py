products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

for i in products:
    products[i]["quantity"] = 0
    products[i]["subtotal"] = 0
# 
def get_product(code):
    return products[code]

def get_property(code,property):
    return products[code][property]

def main():
    receipt = set()
    total = 0
    while True:
        prod_quant = input()
        if prod_quant == "/":
            break
        else:
            prod = prod_quant.split(",")[0]
            quant = int(prod_quant.split(",")[1])
            receipt.add(prod)
            products[prod]["quantity"] += quant
            products[prod]["subtotal"] += get_property(prod,"price") * quant
            total += products[prod]["subtotal"]     
    receipt = sorted(receipt)
    
    with open("receipt.txt", "w") as f:
        f.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n''')
        for i in receipt:
            f.write(f'{i}\t\t{products[i]["name"]}\t\t{products[i]["quantity"]}\t\t\t\t\t{products[i]["subtotal"]}\n')

        f.write(f'''Total:\t\t\t\t\t\t\t\t\t\t\t\t{total}
==
''')
    
    
main()
