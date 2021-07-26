# Even or Odd

# num = int(input("Enter any number: "))
#
# if num % 2 == 0:
#     print(f"Even Number: {num}")
# else:
#     print(f"Odd Number: {num}")

# nep = float(input("Enter nepali mark: "))
# if nep > 100:
#     print("Enter mark less the 100")
#     exit()
# eng = float(input("Enter english mark: "))
# if eng > 100:
#     print("Enter mark less the 100")
#     exit()
#
# math = float(input("Enter math mark: "))
# if math > 100:
#     print("Enter mark less the 100")
#     exit()
# population = float(input("Enter pop mark: "))
# if population > 100:
#     print("Enter mark less the 100")
#     exit()
# health = float(input("Enter health mark: "))
#
# if health > 100:
#     print("Enter mark less the 100")
#     exit()
#
# total = nep + eng + math + population + health
# percentage = total / 5
# division = ''
#
# if percentage > 35 and percentage <= 45:
#     division += "Third"
# elif percentage > 45 and percentage <= 60:
#     division += "Second"
# elif percentage > 60 and percentage <= 75:
#     division += "First"
#
# elif percentage > 75 and percentage <= 100:
#     division += "Top"
#
# print("============================")
# print("=========Result==============")
# print("============================")
#
# print(f"Total mark: {total} Percentage: {percentage} Division:{division}")


print("===================================")
print("==========Computer Bazar ==========")
print("======Product List==========")
print("1. Dell (20000) 2. Toshiva (30000) 3. Mac(50000)")
option = int(input("Enter any option: "))
qt = 0
dell = 20000
toshiva = 30000
mac = 50000
total = 0
if option == 1:
    qt += int(input("Enter quantity: "))
    total += qt * dell

elif option == 2:
    qt += int(input("Enter quantity: "))
    total += qt * toshiva

elif option == 3:
    qt += int(input("Enter quantity: "))
    total += qt * mac

else:
    print("Invalid option")
    exit()

print("Select delivery option:")
print("1. Home (Rs: 1000) 2. Pickup(Free)")
opt = int(input("Select any option: "))
delivery_price = 0
if opt == 1:
    delivery_price += 1000

print("Select Packing options:")
print("1. Plastic (Rs: 500) 2.Bag (Rs:1000) 3. Gift Box(Rs: 5000) 4. None")
pq = int(input("Enter any option: "))
packaging_option = 0

if pq == 1:
    packaging_option += 500
elif pq == 2:
    packaging_option += 1000
elif pq == 3:
    packaging_option += 5000
else:
    packaging_option += 0

print("Select Location: 1. KTM (13%) 2. LTP(Free) 3. BTK(free)")
lq = int(input("Enter any option: "))

tax_amount = 0
if lq == 1:
    tax_amount += total * 0.13

gt = total + tax_amount + delivery_price + packaging_option

print("=============Result========")
print(f"Total: {total}")
print(f"Total Quantity: {qt}")
print(f"Tax amount: {tax_amount}")
print(f"GT: {gt}")
