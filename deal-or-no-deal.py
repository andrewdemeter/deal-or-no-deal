import time
import random

# Create a list of cases ranging from 1 to 26
cases = list(range(1, 26+1))

# Create a list of dollar amounts ranging from $0.01 to $1,000,000
dollar_amounts = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

# FIRST TURN
# The player picks the case that they think contains $1,000,000
original_case = input("Which case contains $1 million? Enter a number between 1-26... \n")

# If the player doesn't enter a valid case number
while original_case.isnumeric() is False or int(original_case) not in cases:
    original_case = input("Please enter a valid case number... \n")

# Convert case number from string to integer
original_case = int(original_case)

# Remove the player's case from the list of cases
cases.remove(original_case)

print("You believe Case #" + str(original_case) + " contains $1 million. We'll reveal that later...\n")

time.sleep(2)

# SECOND THROUGH PENULTIMATE TURN
while len(cases) > 1:

    # The banker will make an offer to the player when 20, 15, 10, and 5 cases remain
    if len(cases) == 20 or len(cases) == 15 or len(cases) == 10 or len(cases) == 5:

        # The banker's offer will be 25% of the average of the remaining dollar amounts, rounded to the nearest thousand
        banker_offer = int(round(average / 4, -3))
        print("The banker has made you an offer of $" + str("{:,}".format(banker_offer)) + " if you quit now...")
        time.sleep(2)
        offer_response = input("Type ACCEPT to accept the banker's offer.\nType REJECT to reject the banker's offer.\n")

        # If the player doesn't type ACCEPT or REJECT...
        while offer_response.upper() != "ACCEPT" and offer_response.upper() != "REJECT":
            offer_response = input("Please type ACCEPT or REJECT to proceed...\n")

        if offer_response.upper() == "ACCEPT":
            print("You've accepted the banker's offer of $" + str("{:,}".format(banker_offer)))
            time.sleep(2)

            # Randomly assign a remaining dollar amount to the original case
            original_case_dollar_amount = random.choice(dollar_amounts)
            print("Your original case would have contained $" + str("{:,}".format(original_case_dollar_amount)))

            time.sleep(2)
            print("Thanks for playing!")
            quit()

        if offer_response.upper() == "REJECT":
            print("You've rejected the banker's offer of $" + str("{:,}".format(banker_offer)) + "\n")
            time.sleep(2)

    # Remind the player what cases are still in play
    print("Here are your remaining cases: " + str(cases)[1:-1])
    time.sleep(2)

    # Create a new list that will contain remaining dollar amounts formatted with $ and ,
    formatted_dollar_amounts = []

    # Add each dollar amount to the new list and format it with comma(s) if necessary
    for dollar_amount in dollar_amounts:
        formatted_dollar_amounts.append(str("{:,}".format(dollar_amount)))

    # Add the $ symbol to each dollar amount in the list
    formatted_dollar_amounts = ["$" + str(dollar_amount) for dollar_amount in formatted_dollar_amounts]

    # Remove extraneous characters from the formatted list
    characters_to_remove = "[']"
    for character in characters_to_remove:
        formatted_dollar_amounts = str(formatted_dollar_amounts).replace(character, "")

    # Remind the player what dollar amounts are still in play
    print("Here are your remaining dollar amounts: " + formatted_dollar_amounts)

    time.sleep(2)

    # Prompt the player to eliminate another case
    case = input("What case would you like to eliminate next?\n")

    # If the player doesn't enter a valid case number
    while case.isnumeric() is False or int(case) not in cases:
        case = input("Please enter a valid case number...\n")

    # Convert case number from string to integer
    case = int(case)

    # Remove that case from the list of cases
    cases.remove(case)

    # Assign a random remaining dollar amount to the case
    random_amount = random.choice(dollar_amounts)

    # Calculate the average of the remaining dollar amounts
    average = sum(dollar_amounts) / len(dollar_amounts)

    # Remove the randomly assigned dollar amount from the list
    dollar_amounts.remove(random_amount)

    # If the player eliminates a low dollar amount
    if random_amount > average:
        print("\nOuch... Case #" + str(case) + " contained $" + "{:,}".format(random_amount))

    # If the player eliminates a high dollar amount
    if random_amount < average:
        print("\nWell done! Case #" + str(case) + " contained $" + "{:,}".format(random_amount))

    time.sleep(1)

# LAST TURN
if len(cases) == 1:
    print("Now, only two cases remain...\n")

    time.sleep(2)

    print("Your original case is #" + str(original_case) + " and the other case is #" + str(cases)[1:-1])

    time.sleep(2)

    print("One of these cases contains $" + str("{:,}".format(dollar_amounts[0])) + ". The other contains $" + str("{:,}".format(dollar_amounts[1])) + ".\n")

    time.sleep(2)

    keep_or_swap = input("Type KEEP to keep your original case.\nType SWAP to swap your original case for Case #" + str(cases)[1:-1] + "...\n")

    # If the player doesn't type KEEP or SWAP...
    while keep_or_swap.upper() != "KEEP" and keep_or_swap.upper() != "SWAP":
        keep_or_swap = input("Please type KEEP or SWAP to proceed...\n")

    # Randomly assign remaining dollar amounts to each case
    original_case_amount = random.choice(dollar_amounts)
    dollar_amounts.remove(original_case_amount)
    other_case_amount = dollar_amounts[0]

    if keep_or_swap.upper() == "KEEP":
        print("You chose to stick with your original case. Let's see what's inside...")

        time.sleep(2)

        # Determine whether keeping the original case was a good or bad choice

        if original_case_amount > other_case_amount:
            print("Nice work! Your original case contained $" + str("{:,}".format(original_case_amount)))

        if original_case_amount < other_case_amount:
            print("Ouch! Your original case contained $" + str("{:,}".format(original_case_amount)))

    if keep_or_swap.upper() == "SWAP":
        print("You chose to swap out your original case. Let's see what's inside your new case...")

        time.sleep(2)

        # Determine whether swapping out the original case was a good or bad choice

        if other_case_amount > original_case_amount:
            print("Nice work! Your new case contained $" + str("{:,}".format(other_case_amount)))

        if other_case_amount < original_case_amount:
            print("Ouch! Your new case contained $" + str("{:,}".format(other_case_amount)))

time.sleep(2)

print("Thanks for playing!")