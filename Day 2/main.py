print("Welcome to the tip calculator!")

a = float(input("What was the total bill? $"))
b = int(input("How much tip would you like to give? 10, 12 or 15? "))
c = int(input("How many people to split the bill? "))

result = ((a * (b / 100)) + a) / c
final = "{0:.2f}".format(result)
message = f"Each person should pay: ${final}"
print(message)
