import random

computer_num = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_num = int(input("type 0 for rock, 1 for paper and 2 for scissors: "))

if computer_num == 0 and player_num == 0:
    print(f"Computer chose:\n {rock}")
    print(f"you chose:\n{rock}")
    print("match draw")
elif computer_num == 0 and player_num == 1:
    print(f"Computer chose:\n {rock}")
    print(f"you chose:\n{paper}")
    print("you win")
elif computer_num == 0 and player_num == 2:
    print(f"Computer chose:\n {rock}")
    print(f"you chose:\n{scissors}")
    print("you lose")
elif computer_num == 1 and player_num == 0:
    print(f"Computer chose:\n {paper}")
    print(f"you chose:\n{rock}")
    print("you lose")
elif computer_num == 1 and player_num == 1:
    print(f"Computer chose:\n {paper}")
    print(f"you chose:\n{paper}")
    print("match draw")
elif computer_num == 1 and player_num == 2:
    print(f"Computer chose:\n {paper}")
    print(f"you chose:\n{scissors}")
    print("you win")
elif computer_num == 2 and player_num == 0:
    print(f"Computer chose:\n {scissors}")
    print(f"you chose:\n{rock}")
    print("you win")
elif computer_num == 2 and player_num == 1:
    print(f"Computer chose:\n {scissors}")
    print(f"you chose:\n{paper}")
    print("you lose")
elif computer_num == 2 and player_num == 2:
    print(f"Computer chose:\n {scissors}")
    print(f"you chose:\n{scissors}")
    print("match draw")
else:
    print("enter valid number.")
