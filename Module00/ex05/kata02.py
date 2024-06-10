# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 13:49:20 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 14:01:51 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (2019, 9, 25, 3, 30)

def main():
    year, month, day, hour, min = kata
    form_day = "{:02}".format(day)
    form_month = "{:02}".format(month)
    form_time = "{:02}:{:02}".format(hour, min)
    print(f"{form_month}/{form_day}/{year} {form_time}")

if __name__ == "__main__":
    main()