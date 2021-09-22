secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_guess =(input)("guess here:")

while user_guess != secret_number:
    print("WRONG!! try again Fool!")
    user_guess =int(input("guess again:"))
print("SUCCESS! YOU GUESSED CORRECTLY:",(+ user_guess))
#FAULT: whilst the code works, if the use guesses correctly first time it regards it as wrong discuss with Chris H