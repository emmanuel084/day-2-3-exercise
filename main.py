# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
data_age = int(age)

age_days = (round((90 * 365) - data_age * 365))
age_weeks = (round((90 * 52) - data_age * 52))
age_months = (round((90 * 12) - data_age * 12))

print(f"You have {age_days}, {age_weeks} and {age_months} left.")












