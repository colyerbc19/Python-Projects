import random

# constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# the frequency dictionary of each symbol
symbol_count = {
    "$": 10,
    "&": 15,
    "%": 20,
    "!": 40,
    "#": 50,
    "*": 75
}

# multiplier dictionary for each symbol
symbol_values = {
    "$": 100,
    "&": 50,
    "%": 10,
    "!": 5,
    "#": 2,
    "*": 1
}


# function to explain the rules before the game
def rules():
    print("-----------------------------------------------------------------------------------")
    print("WELCOME TO WILD BRENT'S (TOTALLY NOT RIGGED) SLOT MACHINE")
    print("Here are the rules:")
    print("1. Betting on 1 line means you bet on the first line only, NO CHOOSING.")
    print("2. Winning lines are 3 symbols in a row.")
    print("3. Minimum bets are $1 and Max bets are $100.")
    print("4. Whole dollar amounts only.")
    print("5. Have Fun!")
    print("Symbols Guide:")
    print("'$'= 100 times bet")
    print("'&'= 50 times bet")
    print("'%'= 10 times bet")
    print("'!'= 5 times bet")
    print("'#'= 2 times bet")
    print("'*'= 1 time bet")
    print("-----------------------------------------------------------------------------------")
    print()
    print("Start by entering a deposit!")
    print()
    return


# function to check how much and which lines won money
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []  # empty list to hold the lines that the user won on
    for line in range(lines):  # loop through each row the user bet on
        symbol = columns[0][line]  # winning symbol is the first symbol of each column for each line
        for column in columns:  # loop through each column
            symbol_to_check = column[line]  # symbol_to_check is the symbol at each spot in the line
            if symbol != symbol_to_check:  # if symbols do not match, no winner
                break
        else:  # else all 3 symbols in a column match
            winnings += values[symbol] * bet  # winnings are equal to the value of that symbol times your bet on th line
            winning_lines.append(line + 1)  # add the winning line to the winning_lines list

    return winnings, winning_lines  # return both the winnings and winning lines


# function to create the random spin, takes in the rows, cols, and symbols_count of the machine
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # creates an empty list to store all the possible symbols
    # symbol = key, count = value in symbol_count dictionary
    for symbol, count in symbols.items():  # .items() returns key, value pairs in the symbols_count dictionary
        for _ in range(count):  # loops through each key, count number of times (ex. $ symbol loops 10 times)
            all_symbols.append(symbol)  # each time we loop an instance of the symbol is added to symbol list

    columns = []  # creates an empty list for the columns
    for _ in range(cols):  # generates the total number of column for the machine (3)
        column = []  # a single column of the slot machine
        current_symbols = all_symbols[:]  # ":" slice operator-creates copy
        for _ in range(rows):  # loop through the number of values we need to generate for each column (3)
            value = random.choice(current_symbols)  # find a random symbol from current_symbols
            current_symbols.remove(value)  # removes the random choice from the current_symbols list
            column.append(value)  # adds the random choice to the current column of the slot machine

        columns.append(column)  # adds the finished current column to the columns list

    return columns  # returns the results of the slot machine spin (3 columns will 3 randomly selected symbols)


# function to print the slot machine results, takes in the columns list with 3 columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):  # loop through each row in the columns list, starting at 0
        for i, column in enumerate(columns):  # loops through each column in columns list
            if i != len(columns) - 1:  # first two elements in the row
                print(column[row], end=" | ")  # print all the element in each row and transposes columns
            else:  # last element in the row
                print(column[row], end="")  # end tells the statement what to end the line with
        print()


# function to accept user deposit amount
def deposit():
    while True:
        amount = input("How much would you like to deposit? $")  # accepts user input for deposit
        if amount.isdigit():  # if the amount is a digit turn it into an int
            amount = int(amount)
            if amount > 0:  # if the amount is valid break the loop
                break
            else:  # else tell user amount must be more than 0
                print("Amount must be greater than 0.")
        else:  # tell user must be a number
            print("Please enter a number.")

    return amount  # results in the balance


# function to get the number of lines the user wants to bet on
def get_number_of_lines():
    while True:  # asks the user the number of lines they want to bet and accepts input
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():  # checks that the number of lines is a digit and turns it into an int
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:  # if the number of lines is valid, break
                break
            else:  # else tell user to enter a valid number of lines
                print("Enter a valid number of lines")
        else:  # tells user it must be a number
            print("Please enter a number.")

    return lines  # returns the number of lines to spin() function


# function to get user inout on how much they want to bet on each line
def get_bet():
    while True:  # asks user how much they want to bet on each line
        amount = input("How much would you like to bet on each line? $")
        if amount.isdigit():  # if the amount is a digit, convert to int
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:  # if amount is valid ($1-100), break
                break
            else:  # else tell user min bets are $1 and max bets are $100 (see rules)
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:  # else tell user to enter a number
            print("Please enter a number.")

    return amount  # returns amount to spin() function


# function to actually spin the machine, takes in the balance parameter
def spin(balance):
    lines = get_number_of_lines()  # calls get_number_of_lines() function
    while True:
        bet = get_bet()  # calls get_bet() function
        total_bet = bet * lines  # calculates total amount of bet

        if total_bet > balance:  # if funds are unavailable tell user and loop again
            print(f"Insufficient funds. Your current balance is: ${balance}")
        else:  # sufficient funds
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")  # notify user of total bet

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # calls get_slot_machine_spin() function to do random spin
    print_slot_machine(slots)  # calls print_slot_machine() function to format the spin for user
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)  # calls check_winnings() function
    print(f"You won ${winnings}.")  # tells user how much they won
    print(f"You won on lines:", *winning_lines)  # '*' splat operator passes all lines that won
    return winnings - total_bet  # returns the net winnings (what they won minus what they bet)


def main():
    rules()  # rules are displayed
    balance = deposit()  # balance is equal to the result of the deposit function
    while True:
        print(f"Current balance is ${balance}")  # display current balance
        answer = input("Press enter to play (q to quit).")  # asks user if they want to play
        if answer == "q":  # "q" breaks the loop
            break
        balance += spin(balance)  # balance is updated with the result of the spin function
        if balance == 0:  # if user runs out of money the program ends
            break

    print(f"You left with ${balance}")  # tells the user their final balance


main()
