# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 17:21:27 by yabejani          #+#    #+#              #
#    Updated: 2024/06/11 11:07:38 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def main():
    rd_nbr = random.randint(1, 99)
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    tries = 0
    while True:
        print("What's your guess between 1 and 99?")
        print()
        inp = input(">> ")
        if inp == "exit":
            print("Goodbye!")
            return
        tries += 1
        try:
            intinp = int(inp)
        except ValueError:
            print("That's not a number.")
            continue
        if intinp < rd_nbr:
            print("Too low!")
        elif intinp > rd_nbr:
            print("Too high!")
        else:
            if rd_nbr == 42 and tries == 1:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulations! you got it on your first try!")
                break
            elif rd_nbr == 42 and tries != 1:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
                print("Congratulations, you've got it!")
                print(f"You won in {tries} attempts!")
                break
            elif tries == 1:
                print("Congratulations! you got it on your first try!")
                break
            else:
                print("Congratulations, you've got it!")
                print(f"You won in {tries} attempts!")
                break
                
            

if __name__ == "__main__":
    main()