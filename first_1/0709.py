import datetime


name = raw_input("what is your name?")

print("Hello {0}").format(name)

# a = datetime.date.today()
today = datetime.date.today().strftime("%d-%m-%Y")

# print("{0}").format(a)
# print("{1}-{2}-{0}").format(a)

print("today is " +today)


