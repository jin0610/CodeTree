class Product:
    def __init__(self, name="codetree", code="50"):
        self.name = name
        self.code = code

name, code = input().split()
prod1=Product()
prod2 = Product(name, code)

print(f"product {prod1.code} is {prod1.name}")
print(f"product {prod2.code} is {prod2.name}")