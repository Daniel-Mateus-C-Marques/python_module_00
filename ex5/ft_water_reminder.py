# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicamp <danicamp@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/08 12:15:06 by danicamp          #+#    #+#              #
#    Updated: 2026/06/08 15:38:18 by danicamp         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
