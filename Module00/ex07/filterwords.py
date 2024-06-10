# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 16:15:34 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 17:05:28 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

def	filterwords(S, N):
    stringnopunct = "".join(word for word in S if word not in string.punctuation)
    filteredtab = [word for word in stringnopunct.split() if len(word) > N]
    print(filteredtab)

# def filterwords(S, N):
#     table = str.maketrans('', '', string.punctuation)
#     nopunct = S.translate(table)
#     tab = nopunct.split()
#     filtered = [bite for bite in tab if len(bite) > N]
#     print(filtered)

def main():
    if len(sys.argv) != 3:
        print("Error: Prog must have 2 args")
        return
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("Error: Second arg must be an integer")
        return
    if not isinstance(sys.argv[1], str):
        print("Error: first argument must be a string.")
        return
    else:
        S = sys.argv[1]
        filterwords(S, N)
        

if __name__ == "__main__":
    main()