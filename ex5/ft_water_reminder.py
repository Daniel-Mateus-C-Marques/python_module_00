#!/usr/bin/env python3

# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 12:15:06 by danicamp            #+#    #+#            #
#   Updated: 2026/06/26 18:45:34 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))
    if days <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")
