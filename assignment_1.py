from datetime import datetime


cr_time = datetime.now().hour
user_name = input("Enter your name please: ")

if cr_time < 12:
    greeting = "good morning"
elif cr_time <= 16:
    greeting = "good afternoon"
elif cr_time > 16:
    greeting = "good evening"


print(f"{user_name} {greeting}!")