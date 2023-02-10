# FILE
def file_to_list(filename: str):
    try:
        with open(filename) as file:
            words = [word.strip() for word in file]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    return words

def get_names(filename: str):
    first_names = file_to_list(filename)
    if not first_names:
        raise Exception(f"Error: The file '{filename}' does not exist or is empty.")
    return first_names

# FUNCTIONS
def generate_initials(first_name: str, middle_name: str, last_name: str) -> str:
    return f"{first_name}{middle_name}{last_name}"

def generate_csv(filename: str, field_headings: list[str], data: list[list[object]]) -> None:
    try:
        with open(filename, "w") as file:
            headings = ",".join(field_headings)
            file.write(headings + "\n")

            for record in data:
                if type(record) == str:
                    record = add_quotes(record)
                line = ",".join(record)
                file.write(line + "\n")
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def add_quotes(s: str) -> str:
    return f'"{s}"'

def get_count(prompt: str) -> int:
    count = int(input(prompt))
    if count <= 0:
        print("Count must be greater than 0. Quitting program.")
        quit()
    return count

# RANDOM
# to generate random number, use "random.randint(min, max)"

import random

def get_random_name(names: list[str]) -> str:
    index = random.randint(0, len(names) - 1)
    return names[index]

def random_day(include_weekends = False) -> str:
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    if include_weekends:
        days_of_week.append("Saturday")
        days_of_week.append("Sunday")
    
    return random.choice(days_of_week)

def random_room() -> str:
    rooms = ["Ma1", "Ma2", "Ma3", "Ma4", "Ma5", "Ma6", "Ma7", "Ma8", "Ma9", "DT1", "DT2", "DT3", "DT4", "DT5", "IT1", "IT2", "IT3", "La1", "La2", "La3", "La4", "La5", "History1", "History2", "History3", "Geography1", "Geography2", "Geography3", "Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6", "Sc7", "Sc8", "Eng1", "Eng2", "Eng3", "Eng4", "Eng5", "Eng6", "Eng7", "Eng8", "Music1", "Music2", "Drama1", "Drama2", "PE"]

    return random.choice(rooms)

def generate_random_length_random_list() -> list(int):
    length = random.randint(1, 10)
    output = []

    for i in range(0, length):
        random_number = random.randint(10, 10)
        output.append(random_number)

    return output

def random_teacher_type(type_type: str) -> str:
    names = ["Teacher", "Cover Teacher", "Trainee Teacher", "Head of Department"]
    display_names = ["Teacher", "Cover", "Trainee", "Head"]

    match type_type:
        case "name":
            return random.choice(names)
        case "displayName":
            return random.choice(display_names)
        case other:
            raise RuntimeError("Incorrect value for 'type_type' when calling 'random_teacher_type'")