# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 11:56:04 by yabejani          #+#    #+#              #
#    Updated: 2024/06/12 13:47:13 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yields the substrings.
    option specifies if an action is performed on the substrings before they are yielded.
    '''
    if not isinstance(text, str):
        yield "ERROR"
        return
    
    if option not in (None, "shuffle", "unique", "ordered"):
        yield "ERROR"
        return
    
    words = text.split(sep)
    if option == "shuffle":
        for i in range(len(words) - 1, 0, -1):
            j = random.randint(0, i)
            words[i], words[j] = words[j], words[i]
    elif option == "unique":
        seen = set()
        words = [x for x in words if not (x in seen or seen.add(x))]
    elif option == "ordered":
        words.sort()
    for word in words:
        yield word