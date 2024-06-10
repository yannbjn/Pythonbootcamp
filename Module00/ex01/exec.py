# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:11:39 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 10:37:08 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

import sys

def rev_swap_str(str):
    rev_str = str[::-1]
    swapped_str = rev_str.swapcase()
    return swapped_str

def main():
    if len(sys.argv) > 1:
        str = ' '.join(sys.argv[1:])
        res = rev_swap_str(str)
        print(res)
    else:
        print("Usage: python exec.py <string>")
 
if __name__ == "__main__":
    main()