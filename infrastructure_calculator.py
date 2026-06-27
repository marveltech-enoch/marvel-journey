name = input("What is your name?: ")
hours_per_day = float(input("How many hours per day will you code?: "))
days_per_week = int(input("How many days per week?: "))
years = int(input("How many years commitment?: "))          
total_hours = hours_per_day * days_per_week * 52 * years
lines_of_code = total_hours * 50
print("--------------PROJECT 2-------------")
print(f"{name} will code:")
print(f"-{hours_per_day} hours per day")
print(f"-{days_per_week} days per week:")
print(f"-For {years} years") 
print(f"Total Hours: {total_hours:,}")
print(f"Total Lines of Code: {lines_of_code:,}")
print(f"This is enough to build infrastructure that powers billions.")
