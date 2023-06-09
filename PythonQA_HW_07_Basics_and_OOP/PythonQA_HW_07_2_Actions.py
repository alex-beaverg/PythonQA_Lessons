# Homework 07-2 (2023.06.01)
# Actions

from PythonQA_HW_07_1_Classes import Human, Parent, Kid

print('\nHomework 07 (2023.06.01)')
print('-' * 24)
print()


# Create all class objects:
firstHuman = Human("Alex", "Black")
firstParent = Parent("Dima", "Brown", 35, "office", 1000, "High", 15000, "Soccer")
firstKid = Kid("School", "Sasha", "Smith")


# Print all class objects:
print(firstHuman)
print(firstParent)
print(firstKid)
print()


# Create list of Parent objects:
parents = [
    Parent("Dima", "Horsemen", 35, "Driver", 1000, "High", 22000, "Hockey"),
    Parent("Vadim", "Hitachi", 25, "Office", 500, "Medium", 15000, "Watching TV"),
    Parent("John", "Travolta", 45, "Hollywood", 10000, "Super High", 45000, "Fishing"),
    Parent("Pavel", "Green", 30, "Office", 800, "High", 27000, "Football"),
    Parent("Yoki", "Suzuki", 57, "Home", 35000, "High", 250000, "Cars")
]


# Using "foreach" and "if" for list of Parent objects:
min_salary = 600
sum_salary = 0
count = 0
for current_parent in parents:
    count += 1
    sum_salary += current_parent.salary
    if current_parent.age > 30 and current_parent.salary > 1000:
        print(f"{current_parent.name} {current_parent.surname} with age > 30 and salary > 1000")
print()


# Print sum result:
print(f"Average salary = {sum_salary / count}")
print()


# Using "while" and "if" for list of Parent objects:
current_parent_id = 0
while current_parent_id < len(parents):
    current_parent = parents[current_parent_id]
    current_parent_id += 1
    if len(current_parent.name) > 4:
        print(f"Parent with long (> 4 letters) name is {current_parent.name} {current_parent.surname}")
print()


# Using "for", "if" and "continue" for list of Parent objects:
for i in range(len(parents)):
    if parents[i].accumulation < 20000:
        continue
    print(f"Parent with high accumulation is {parents[i].name} {parents[i].surname}. He likes {parents[i].hobby}")
print()


# Using "while True", "break" and "if" for list of Parent objects:
current_parent_id = 0
while True:
    i = current_parent_id
    if parents[i].job == "Home":
        print(f"First parent from list who works from home is {parents[i].name} {parents[i].surname}. "
              f"He has {parents[i].education} education")
        break
    current_parent_id += 1
print()


# Using "foreach", "break" and "if" for list of Parent objects:
for current_parent in parents:
    if current_parent.hobby == "Football":
        print(f"First parent from list who likes football is {current_parent.name} {current_parent.surname}")
        break
print()


# Using "for", "continue" and "if" for list of Parent objects:
for i in range(len(parents)):
    if parents[i].job == "Office":
        continue
    print(f"Parent who works not from office is {parents[i].name} {parents[i].surname}. "
          f"He has salary: {parents[i].salary}")
print()


# Using "foreach" and "if-elif-else" for list of Parent objects:
for current_parent in parents:
    if current_parent.accumulation < 10000:
        print(f"Parent with accumulation less then 10000 is {current_parent.name} {current_parent.surname}")
    elif 10000 <= current_parent.accumulation < 20000:
        print(f"Parent with accumulation more then 10000 and less then 20000 "
              f"is {current_parent.name} {current_parent.surname}")
    else:
        print(f"Parent with accumulation more then 20000 is {current_parent.name} {current_parent.surname}")
print()


# Using "while True", "break" and "if" for list of Parent objects:
current_parent_id = 0
while True:
    i = current_parent_id
    if i == len(parents):
        break
    if parents[i].education == "Super High":
        print(f"Parent from list who has Super High education is {parents[i].name} {parents[i].surname}. "
              f"He works in {parents[i].job}")
    current_parent_id += 1
print()


# Using "for" and "if" for list of Parent objects:
for i in range(len(parents)):
    if parents[i].accumulation / parents[i].salary < 24:
        print(f"Parent with quick accumulation is {parents[i].name} {parents[i].surname}")
print()


# Using "foreach", "break" and "if" for list of Parent objects:
min_sum_salary = 0
parents_count = 0
for current_parent in parents:
    min_sum_salary += current_parent.salary
    parents_count += 1
    if min_sum_salary > 10000:
        print(f"Salaries sum more then 10000 have {parents_count} first parents. "
              f"Salaries sum is equals to {min_sum_salary}")
        break
