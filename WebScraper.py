from Monster import monster
from Indeed import indeed
from Reed import reed
from LinkedIn import linkedin

print("Choose field: ")
a = input()
print("Choose location (UK): ")
b = input()

monster(a, b)
indeed(a, b)
r = reed(a, b)
l = linkedin(a, b)
