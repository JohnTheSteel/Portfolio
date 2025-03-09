# # Greet employees by name  *******************
# 
# def greet_employee(name, surname, age):
#     print("Welcome! You are logged in", name, surname, "...", age,"years old?! Wow! Why so old ??")
# 
# 
# 
# greet_employee("Greta", "Guntberg", 14)
# 
# 
# Explore 'return' *********************************

# Return info from a function

def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage

percentage = calculate_fails(4, 1)

print("Procent nieudanych logowań wynosi:" ,percentage*100,"%.","Gdy ta liczba wyniesie 50% - zostaniesz zablokowany.")

if (percentage >= 0.5):
    print("account is locked")
    
else:
    print(" - - - - - - -  ", "Try again later.")


# # Explore input and output of 'print()' ***************
# print("This is string, but", 75, "is a number.")
# 
# print(type("security"))
#       
# print(type(73.2))
# 
# 
# # Explore 'max()' *************************************
# 
# a = 3
# b = 9
# c = 6
# 
# print(max(a,b,c))
# 
# print(min(a,b,c))
# 
# 
# #Use the 'sorted()' function *************************
# #parameters 'key' 'reverse' **************************

# tenisisci_stolowi = [
#     "Ma Long",
#     "Fan Zhendong",
#     "Zhang Jike",
#     "Dimitrij Ovtcharov",
#     "Timo Boll",
#     "Xu Xin",
#     "Wang Hao",
#     "Tomokazu Harimoto",
#     "Hugo Calderano",
#     "Joo Sae-hyuk"
# ]
# 
# print(sorted(tenisisci_stolowi, key=len, reverse=0))

# # Define a function named `analyze_logins()` that takes in three parameters, ******
# # `username`, `current_day_logins`, and `average_day_logins` **********************
# 
# def analyze_logins(username, current_day_logins, average_day_logins):
# 
#     # Display a message about how many login attempts the user has made that day
# 
#     print("Current day login total for", username, "is", current_day_logins)
# 
#     # Display a message about average number of login attempts the user has made that day
# 
#     print("Average logins per day for", username, "is", average_day_logins)
# 
#     # Calculate the ratio of the logins made on the current day to the logins made on an average day,
#     # storing in a variable named `login_ratio`
# 
#     login_ratio = current_day_logins / average_day_logins
# 
#     # Display a message about the ratio
# 
#     print(username, "logged in", login_ratio, "times as much as they do on an average day.")
# 
# # Call `analyze_logins()`
# 
# analyze_logins("ejones", 4, 2)

# # Define a function named `analyze_logins()` that takes in three parameters, `username`, *****
# # `current_day_logins`, and `average_day_logins` *********************************************
# 
# def analyze_logins(username, current_day_logins, average_day_logins):
# 
#     # Display a message about how many login attempts the user has made that day
# 
#     print("Current day login total for", username, "is", current_day_logins)
# 
#     # Display a message about average number of login attempts the user has made that day
# 
#     print("Average logins per day for", username, "is", average_day_logins)
# 
#     # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
# 
#     login_ratio = current_day_logins / average_day_logins
# 
#     # Return the ratio
# 
#     return login_ratio
# 
# # Call `analyze_logins() and store the output in a variable named `login_analysis`
# 
# login_analysis = analyze_logins("ejones", 9, 3)
# 
# # Conditional statement that displays an alert about the login activity if it's more than normal
# 
# if login_analysis >= 3:
#     print("Alert! This account has more login activity than normal.")
