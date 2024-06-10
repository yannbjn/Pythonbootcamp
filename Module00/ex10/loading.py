# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 17:47:16 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 18:15:04 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import time

def ft_progress(lst):
    start_time = time.time()
    total_items = len(lst)
    for index, item in enumerate(lst):
        elapsed_time = time.time() - start_time
        if elapsed_time > 0:
            items_per_second = index / elapsed_time
            remaining_items = total_items - index
            eta = remaining_items / items_per_second if items_per_second > 0 else 0
        else:
            eta = 0
        percentage = (index / total_items) * 100
        bar_length = 20
        filled_length = int(bar_length * index // total_items)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)
        sys.stdout.write(f'\rETA: {eta:.2f}s [{percentage:.0f}%][{bar}] {index}/{total_items} | elapsed time {elapsed_time:.2f}s')
        sys.stdout.flush()
        
        yield item
    
    sys.stdout.write('\n')


if __name__ == "__main__":
    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        time.sleep(0.001)  # Simulate some processing time
    print()
    print(ret)