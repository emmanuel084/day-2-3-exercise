# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
data_age = int(age)

age_days = (round((90 * 365) - data_age * 365))
age_weeks = (round((90 * 52) - data_age * 52))
age_months = (round((90 * 12) - data_age * 12))

print(f"You have {age_days}, {age_weeks} and {age_months} left.")

#My teacher's way.

# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining *12

# message = (f"You have {days_remaining}, {weeks_remaining} and {months_remaining} left.")

# print(message)









