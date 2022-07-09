''' Painting job quotation module '''


sq_feet = int(input("What is the square feet of wall space to be painted?: "))
paint_price = int(input("What is the price(in dollars) of the paint per gallon?: "))

paint_total = round((sq_feet / 115), 2)
job_hours = round((sq_feet / 115 * 8), 1)
paint_cost = round((paint_total * paint_price), 2)
labour_cost = round((job_hours * 20), 2)
total_cost = paint_cost + labour_cost

print("\nQuotation")
print("==========================================================")
print("Amount of paint required: {} gallons".format(paint_total))
print("Total labor time: {} hours".format(job_hours))
print("Total cost of the paint: ${}".format(paint_cost))
print("Labor charges: ${}".format(labour_cost))
print("Grand total cost: ${}".format(total_cost))
