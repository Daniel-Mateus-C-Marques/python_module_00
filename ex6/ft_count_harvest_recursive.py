# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicamp <danicamp@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/08 12:21:13 by danicamp          #+#    #+#              #
#    Updated: 2026/06/08 15:36:58 by danicamp         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def recursive_print(days) -> None:
    if days == 0:
        return
    recursive_print(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_print(days)
    print("Harvest time!")
