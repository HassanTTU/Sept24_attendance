import random
import time

# Greeting and name input
print("🎉 Welcome to the PowerBall Number Generator!")
varUserName = input("What's your name? ")

# Personalized greeting
print(f"\nHi {varUserName}, let's get your lucky numbers!\n")

# Generate white balls (1–69)
white_ball_1 = random.randint(1, 69)
time.sleep(0.5)
white_ball_2 = random.randint(1, 69)
time.sleep(0.5)
white_ball_3 = random.randint(1, 69)
time.sleep(0.5)
white_ball_4 = random.randint(1, 69)
time.sleep(0.5)
white_ball_5 = random.randint(1, 69)
time.sleep(0.5)

# Generate red ball (1–26)
red_ball = random.randint(1, 26)
time.sleep(0.5)

# Format and print numbers
print("Your PowerBall numbers are:")
print(f"{white_ball_1}  {white_ball_2}  {white_ball_3}  {white_ball_4}  {white_ball_5}    {red_ball}")

# Farewell message
print(f"\nGood luck, {varUserName}! 🍀 Hope your numbers hit the jackpot!")