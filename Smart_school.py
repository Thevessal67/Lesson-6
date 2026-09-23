print("==========Smart School Day Planner===============")
print("answer 3 quick questions and I will plan your day \n ")
day=input("what day is it ?(monday to sunday): ").strip().capitalize()
weather=input("what is the weather?(sunny/rainy/cloudy): ").strip().lower()
homework=input("is your homework done?(yes/no): ").strip().lower()
print()
print(f"===your plan for {day}===")
print("-"*35)
# Smart School Day Planner - Topic 1
if day in ("Saturday", "Sunday"):
    print("Day type : Weekend - enjoy your free time!")
elif day == "Monday":
    print("Day type : First day of the week.")
elif day == "Friday":
    print("Day type : Last school day.")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type : Regular school day.")
else:
    print("Day type : Day not recognised.")

# Topic 2 - AND operator
if weather == "sunny" and homework == "yes":
    print("After school: Head to the park!")

# Topic 3 - OR operator
if weather == "rainy" or weather == "cloudy":
    print("Weather tip : Pack your umbrella!")

# Topic 4 - NOT operator
if not (homework == "yes"):
    print("Homework : Not done yet. Finish it before going out!")
# not-equal operator
if day != "Saturday":
    print("It is a school week day.")

# Topic 5 - Combining AND + OR + NOT
if weather == "rainy" and not (homework == "yes"):
    print("Best plan : Stay in, finish homework first.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan : All set for a great school day!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan : Perfect weekend - head outside!")
else:
    print("Best plan : Take it one step at a time!")

print()
print("-"*35)
print("plan complente. have a wonderful day")