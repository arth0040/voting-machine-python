"""A simple command-line voting machine."""

PARTIES = {
    1: "BJP",
    2: "Congress",
    3: "CJP",
    4: "NOTA",
}


def get_age():
    """Ask for and validate the voter's age."""
    while True:
        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if age < 0 or age > 120:
            print("Please enter a valid age between 0 and 120.")
            continue

        return age


def display_parties():
    """Display the available voting choices."""
    print("\nParties")
    for number, party in PARTIES.items():
        print(f"{number}. {party}")


def get_choice():
    """Ask for and validate the voter's party choice."""
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Please enter a number from 1 to 4.")
            continue

        if choice in PARTIES:
            return choice

        print("Invalid choice. Please select a number from 1 to 4.")


def main():
    """Run the voting machine."""
    print("!!!!! Welcome to the Voting Machine !!!!".center(50))

    age = get_age()

    if age < 18:
        print("You are not eligible to vote.")
        return

    print("\nYou are eligible to vote!")
    display_parties()
    selected_party = PARTIES[get_choice()]
    print(f"You have chosen {selected_party}.")
    print("Thank you for voting!")


if __name__ == "__main__":
    main()
