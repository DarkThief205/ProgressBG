#--------------------------------------------Task:-------------------------------------------------#
#Make a BMI Calculator. 
weight_in_kilogram = float(input("Enter your weight: "))
height_in_meters = float(input("Enter your height: "))

BMI = weight_in_kilogram / (height_in_meters**2)
print(f"Your BMI is: {BMI:.2f}")

#--------------------------------------------------------------------------------------------------#