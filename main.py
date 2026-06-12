from art import logo,vs
from game_data import data
import random

def format_data(account):
    name=account['name']
    description=account['description']
    country=account['country']
    return f"{name}, a {description} from {country}"

def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return True

    else:
        return False


print(logo)
score = 0
should_continue= True
account_b= random.choice(data)

while should_continue:
    account_a= account_b
    account_b= random.choice(data)

    if account_a == account_b:
        account_b= random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess=input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n"*20)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct= check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}.")
    else:
        print(f"Sorry, you're wrong. final score is {score}.")
        should_continue = False

