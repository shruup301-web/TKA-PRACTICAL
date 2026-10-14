# Task 1: Shopping Bill Calculator

def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    total = amount + gst
    return total


def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    total = amount + gst
    return total


def calculateFoodGST(e):
    gst = e * 7 / 100
    total = e + gst
    return total


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Given prices
a = 100
b = 100
c = 100
d = 100
e = 100

# Calculate bills
electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

# Display the bill
print("Electronics Bill:", electronics)
print("Fashion Bill:", fashion)
print("Food Bill:", food)
print("Total Bill After GST:", total)
print("Discount:", discount)
print("Final Payable Amount:", final_amount)