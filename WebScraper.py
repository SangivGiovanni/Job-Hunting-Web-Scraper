from Monster import monster
from Indeed import indeed

print("Chose field: ")
a = input()
print("Chose location (UK): ")
b = input()

monster(a, b)
indeed(a, b)


# role = True
#
# while role:
#
#     print("Chose job role: ")
#     c = input()
#     if c == "/exit":
#         break
#
#     myJobs = results.find_all('h2', string=lambda text: c in text.lower())
#     print(len(myJobs))
#
#     if len(myJobs) < 1:
#         continue
#     else:
#         print("Serch results from Monster: ")
#         print("\n")
#         for j in myJobs:
#             link = j.find('a')['href']
#             print(j.text.strip())
#             print(f"Apply here: {link}\n")
#         break
