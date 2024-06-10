# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:02:46 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 14:17:11 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = "The right format"

def main():
	print(f"{kata.rjust(42, '-')}", end="")

if  __name__ == "__main__":
	main()

# def main():
#     num_hyphens = 42 - len(kata)
#     print('-' * num_hyphens + kata, end="")

# if  __name__ == "__main__":
# 	main()