"""Asks for a name and age, then estimates and displays the birth year.

Input:
Name: string from user input.
Age: integer from user input.
Current year: integer from the system.

Process:
  Convert the age to an integer and subtract it from the current year.

Output:
Personalized message: string displayed in the console.

Typical usage example:
What is your name? Jordan
What is your age? 25
Hello Jordan! You were born in 2001.
    
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("What is your name? ")
    age = int(input("What is your age? "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===

