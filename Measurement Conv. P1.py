convert_from = input("Enter starting unit of measurement(inches,feet,yards):")
convert_to = input("Enter unit of measurement to convert to(inches,feet,yards):")
##number_of_inches = input("enter starting measurement in inches:")
##number_of_feet = input("enter starting measurement in feet:")
##number_of_yards = input("enter starting measurement in yards:")

if convert_from.lower() in ["inches","in","inch"]: 
    number_of_inches = int(input("enter starting measuremnt in inches:"))
    if convert_to.lower() in ["feet","ft","foot"]:
       print("Result: " + str(number_of_inches) + " Inches = " + str(round(number_of_inches / 12,2)) + " Feet")
    elif convert_to .lower() in ["yards","yd","yard","yds"]:
       print("Result: " + str(number_of_inches) + " Inches = " + str(round(number_of_inches / 36,2)) + " Yards")
    else:
       print("Please enter either Inches, Feet, Yards")

elif convert_from.lower() in ["feet","ft","foot"]:
    number_of_feet = int(input("enter starting measurement in feet:"))
    if convert_to.lower() in ["inches","in","inch"]: 
       print("Result: " + str(number_of_feet) + " Feet = " + str(round(number_of_feet * 12)) + " Inches")
    elif convert_to.lower() in ["yards","yd","yard","yds"]:
       print("Result: " + str(number_of_feet) + " Feet = " + str(round(number_of_feet / 3,2)) + " Yards")
    else:
       print("Please enter either Inches, Feet, Yards")

elif convert_from.lower() in ["yards","yd","yard","yds"]:
    number_of_yards = int(input("enter starting measurement in yards:"))
    if convert_to.lower() in ["inches","in","inch"]:
       print("Result: " + str(number_of_yards) + " Yards = " + str(round(number_of_yards * 36)) + " Inches")
    elif convert_to .lower() in ["feet","ft","foot"]: 
        print("Result: " + str(number_of_yards) + " Yards = " + str(round(number_of_yards * 3)) + " Feet")
    else:
       print("Please enter either Inches, Feet, Yards")
else:
    print("Please enter either Inches, Feet, Yards")