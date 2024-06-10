# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 13:40:12 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 13:48:04 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
	'Python': 'Guido van Rossum',
	'Ruby': 'Yukihiro Matsumoto',
	'PHP': 'Rasmus Lerdorf',
	}

def	main():
    for language, creator in kata.items():
        print(f"{language} was created by {creator}")

if __name__ == "__main__":
	main()