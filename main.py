# You are making a ticketing system.
# The price of a single ticket is $100.
# For children under 3 years of age, the ticket is free.
#
# Your program needs to take the ages of 5 passengers as input and
# output the total price for their tickets.

#     ----- using a while loop -----

ticket_price = 100
total_price = 0
passenger_num = 1
print("Enter the ages of 5 passengers, press enter after each one:  ")
while passenger_num <= 5:
    age = int(input())
    if age >= 3:
        total_price += ticket_price
        passenger_num += 1
        print("Total price: $" + str(total_price))

#     ----- using a for loop -----

# ticket_price = 100
# total_price = 0
# print("Enter the ages of the 5 passengers:")
# for i in range(5):
#     age = int(input())
#     if age >= 3:
#         total_price += ticket_price
#         print("Total price: $" + str(total_price))
