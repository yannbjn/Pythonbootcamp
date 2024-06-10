# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:42:20 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 10:57:58 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	check_number(arg):
    try:
        number = int(arg)
    except ValueError:
        print("Error: Argument must be an integer")
        return
    
    if number == 0:
        print("I'm Zero")
    elif number % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")

def main():
    if len(sys.argv) == 0:
        print("Usage: python whois.py 12")
    if len(sys.argv) > 2:
        print("Error: too many args")
    else:
        check_number(sys.argv[1])

if __name__ == "__main__":
    main()