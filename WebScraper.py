from Monster import monster
from Indeed import indeed
from Reed import reed
from LinkedIn import linkedin

print("Choose field: ")
a = input()
print("Choose location (UK): ")
b = input()

m = monster(a, b)
i = indeed(a, b)
r = reed(a, b)
l = linkedin(a, b)
