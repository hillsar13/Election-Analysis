# Create two variables called `name` and `country` that will hold strings.
name = "Sarah"
country = "USA"

# Create two variables called `age` and `hourly_wage` that will hold integers.
age = 40
hourly_wage = 10

# Create a variable called `satisfied` which will hold a boolean.
satisfied = True

# Create a variable called `daily_wage` that will hold the value of `hourly_wage` multiplied by 8.
daily_wage = hourly_wage * 8

# Use traditional string concatenation to print the `name`, `country`, `age`, and `hourly_wage` variables.
print("My name is " + name)
print("I am from " + country)
print("My age is " + str(age))
print("I make " + str(hourly_wage) + "dollars an hour")


# With an `f-string`, print the `daily_wage` and `satisfied` variables.
print(f"{daily_wage} + {satisfied}")

