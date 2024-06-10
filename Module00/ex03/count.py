# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 11:07:59 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 11:54:43 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def text_analyzer(text=None):
    """
    Analyze the input text and print the counts of upper-case characters, lower-case characters,
    punctuation characters, and spaces.

    Args:
    text (str): The string to be analyzed. If None or not provided, the user is prompted to input a string.

    Returns:
    None: This function does not return anything. It prints the counts directly.

    Raises:
    TypeError: If the input is not a string and not None.
    """
    if text is None:
        text = input("Please provide a string to analyze: ")
    if not isinstance(text, str):
        print("Error: Argument must be a string.")
        return
    
    try:
        int(text)
        print("Error: input must be a text string")
        return
    
    except ValueError:
        pass
    
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_count = sum(1 for char in text if char in string.punctuation)
    space_count = text.count(' ')

    print(f"Upper-case characters: {upper_count}")
    print(f"Lower-case characters: {lower_count}")
    print(f"Punctuation characters: {punctuation_count}")
    print(f"Spaces: {space_count}")

def	main():
    if len(sys.argv) > 2:
        print("Error: Please provide only one string as an argument.")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
    

if __name__ == "__main__":
    main()