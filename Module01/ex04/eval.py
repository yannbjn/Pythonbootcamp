# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/12 13:51:51 by yabejani          #+#    #+#              #
#    Updated: 2024/06/12 14:24:05 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(len(word) * coef for word, coef in zip(words, coefs))
    
    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        return sum(len(words[i]) * coefs[i] for i in enumerate(words))