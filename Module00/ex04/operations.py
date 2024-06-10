# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:57:29 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 12:12:37 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    if len(sys.argv) != 3:
        print("Error: more or less than 2 arguments")
    try:
        n1 = int(sys.argv[1])
        n2 = int(sys.argv[2])
    
    except ValueError:
        print("Error: AssertionError: only integers")
    
    print("Sum:        ", n1 + n2)
    print("Difference: ", n1 - n2)
    print("Product:    ", n1 * n2)
    if n2 == 0:
        print("Quotient:    ERROR, (divison by zero)")
        print("Remainder:   ERROR, (modulo by zero)")
    else:
        print("Quotient:   ", n1 / n2)
        print("Remainder:  ", n1 % n2)

if __name__ == "__main__":
    main()