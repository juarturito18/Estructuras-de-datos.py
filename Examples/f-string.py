from datetime import datetime

name = "Juan"
edad = 16 
text_if =  f"Hola{name}, eres menor de edad por tener esta edad {edad}"
print(text_if)

bank_balance = 120000000
text = f"Tu saldo en la cuenta bancaria es: {bank_balance:,}"
print(text)

stock_price = 1.405
text = f"El valor del stock es : {stock_price:.2f}"
print(text)

text = f"El valor del stock es : {stock_price:.1f}"
print(text)

user_id = 100
text = f"Su id es: {user_id:04d}"
print(text)

user_id = 1
text = f"Su id es: {user_id:04d}"
print(text)

product = "Laptop"
price = 1000
text = f"Producto: {product:>15} | Precio: {price:>10}"
print(text)

date = datetime(2024,12,5,10,10)
text =  f"La fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
print(text)


