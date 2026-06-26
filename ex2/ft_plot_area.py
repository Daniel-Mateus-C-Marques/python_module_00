#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: danicamp <danicamp@student.42porto.com>      +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/07 09:51:21 by danicamp            #+#    #+#            #
#   Updated: 2026/06/26 18:45:18 by danicamp           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area() -> None:
    lenght = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f"Plot area: {lenght * width}")
