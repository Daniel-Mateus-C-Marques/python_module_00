# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicamp <danicamp@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/08 12:20:57 by danicamp          #+#    #+#              #
#    Updated: 2026/06/08 15:37:44 by danicamp         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    while (i <= days):
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
