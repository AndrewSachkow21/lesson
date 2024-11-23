from datetime import date

now = date.today()
birth = date(int(input("1")),int(input("2")),int(input("3")))
b = (now - birth)/365
b = str(b).split()[0]
print("Вам - " + b)
