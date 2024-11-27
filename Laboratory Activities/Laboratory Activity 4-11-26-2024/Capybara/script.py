from Capybara import Capybara

capybaras = [
    Capybara("Biscoff", "M", 5),
    Capybara("Luffy", "M", 3),
    Capybara("Franky", "F", 7),
    Capybara("Robin", "M", 2),
    Capybara("Grinch","F", 6)
]

# Prompt the user to select a test case
try:
    test_case = int(input("Enter the test case number: "))
    if 1 <= test_case <= len(capybaras):
        selected_capybara = capybaras[test_case - 1]
        print(f"Test Case {test_case}: Name: {selected_capybara.name}, "
              f"Gender: {selected_capybara.gender}, "
              f"Age: {selected_capybara.age} years old")
    else:
        print("Invalid test case number. Please enter a number between 1 to 5.")
except ValueError:
    print("Invalid input. Please enter a valid number.")