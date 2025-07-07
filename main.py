print("Quiz Game by Tendo\n")
namePlayer = input("Enter your name:")
agePlayer = input("Enter your age:")
print("Hello " + namePlayer + "! You are " + agePlayer + " years old.")
if int(agePlayer) <= 10:
  print("Sorry, you are too young to play this game.")
else:
  print("Let's play the game!")
  score = 0
  print("\n Question 1: Solve  3x+2=11")
  answer1 = input("Enter your answer:")
  if answer1 == "3":
    print("Correct!")
    score += 1
  else:
    print("Sorry wrong answer.")

  print("\n Question 2: Give two multiples of 7")
  lowestMultiple = input("Enter the lowest multiple:")
  if lowestMultiple == "7":
    print("Correct!")

  else:
    print("Sorry wrong answer.")

  secondBiggestMultiple = input("Enter the second biggest multiple:")
  if secondBiggestMultiple == "14":
    print("Correct!")

  else:
    print("Sorry wrong answer.")

  if lowestMultiple == "7" and secondBiggestMultiple == "14":
    score += 1

  print("\n Question 3: What is the square root of 25?")
  answer3 = input("Enter your answer:")
  if answer3 == "5":
    print("Correct!")
    score += 1
  else:
    print("Sorry wrong answer.")

  print("\n Question 4: how many sides does a nanogon have")
  answer4 = input("Enter your answer:")
  if answer4 == "9":
    print("Correct!")
    score += 1
  else:
    print("Sorry wrong answer.")

  print("\n Question 5: What is the smallest prime number?")
  answer5 = input("Enter your answer:")
  if answer5 == "2":
    print("Correct!")
    score += 1
  else:
    print("Sorry wrong answer.")
  print("\n\n End of the game,Your score is " + str(score) + "/5")
