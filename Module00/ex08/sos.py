# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 17:07:33 by yabejani          #+#    #+#              #
#    Updated: 2024/06/11 10:15:37 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

def main():
    if len(sys.argv) < 2:
        print("ERROR: example usage : python3 sos.py <string to encode> <...>")
    input_string = " ".join(sys.argv[1:])
    encoded_message = []
    for char in input_string:
        if char == ' ':
            encoded_message.append('/')
        elif char.upper() in MORSE_CODE_DICT:
            encoded_message.append(MORSE_CODE_DICT[char.upper()])
        else:
            print("ERROR")
            return
    print(" ".join(encoded_message))
    

if __name__ == "__main__":
    main()