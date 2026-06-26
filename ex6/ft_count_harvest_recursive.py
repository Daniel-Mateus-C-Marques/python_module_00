#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/08 12:21:13 by danicamp            #+#    #+#            #
#   Updated: 2026/06/26 18:46:24 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def recursive_print(days: int) -> None:
    if days == 0:
        return
    recursive_print(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    recursive_print(days)
    print("Harvest time!")
