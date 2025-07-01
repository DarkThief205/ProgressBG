# ---------------------------------- Task 4 ---------------------------------- #
# """
# DESCRIPTION:
#     Write a Body mass index (BMI) calculator program, which asks the user for:
#     weight in kilograms
#     height in meters

#     Calculate the BMI = W / (H*H)
#     where:
#     W = weight in kilograms
#     H = height in meters

#     Display to the user the BMI and basic category, using next table:

#     | ------------------------------- | ----------- |
#     | category                        | BMI         |
#     | ------------------------------- | ----------- |
#     | Underweight (Severe thinness)   | < 16.0      |
#     | Underweight (Moderate thinness) | 16.0 - 16.9 |
#     | Underweight (Mild thinness)     | 17.0 - 18.4 |
#     | Normal range                    | 18.5 - 24.9 |
#     | Overweight (Pre-obese)          | 25.0 - 29.9 |
#     | Obese (Class I)                 | 30.0 - 34.9 |
#     | Obese (Class II)                | 35.0 - 39.9 |
#     | Obese (Class III)               | ≥ 40.0      |
#     | ------------------------------- | ----------- |
# """

# Your code here:
user_weight = float(input("Enter weight in kilograms: "))
user_height = float(input("Enter height in meters: "))


bmi = user_weight / (user_height * user_height)


if bmi < 16.0:
    category = "Underweight (Severe thinness)"
elif bmi < 17.0:
    category = "Underweight (Moderate thinness)"
elif bmi < 18.5:
    category = "Underweight (Mild thinness)"
elif bmi < 25.0:
    category = "Normal range"
elif bmi < 30.0:
    category = "Overweight (Pre-obese)"
elif bmi < 35.0:
    category = "Obese (Class I)"
elif bmi < 40.0:
    category = "Obese (Class II)"
else:
    category = "Obese (Class III)"


print(f"Your BMI = {bmi:.2f}, Category: {category}")
