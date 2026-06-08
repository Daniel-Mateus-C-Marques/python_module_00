# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicamp <danicamp@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/07 10:01:46 by danicamp          #+#    #+#              #
#    Updated: 2026/06/08 15:38:52 by danicamp         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    d1 = int(input("Day 1 harvest: "))
    d2 = int(input("Day 2 harvest: "))
    d3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {d1 + d2 + d3}")
