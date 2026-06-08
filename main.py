# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: danicamp <danicamp@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/06/07 09:29:04 by danicamp          #+#    #+#              #
#    Updated: 2026/06/08 15:35:36 by danicamp         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from ex0.ft_hello_garden import ft_hello_garden
from ex1.ft_garden_name import ft_garden_name
from ex2.ft_plot_area import ft_plot_area
from ex3.ft_harvest_total import ft_harvest_total
from ex4.ft_plant_age import ft_plant_age
from ex5.ft_water_reminder import ft_water_reminder
from ex6.ft_count_harvest_iterative import ft_count_harvest_iterative
from ex6.ft_count_harvest_recursive import ft_count_harvest_recursive
from ex7.ft_seed_inventory import ft_seed_inventory


def main():
	# ex00
	ft_hello_garden()
	# ex01
	ft_garden_name()
	# ex02
	ft_plot_area()
	# ex03
	ft_harvest_total()
	# ex04
	ft_plant_age()
	# ex05
	ft_water_reminder()
	# ex06
	ft_count_harvest_iterative()
	# ex6
	ft_count_harvest_recursive()
	# ex7
	ft_seed_inventory("lettuce", 10, "grams")

	if __name__ == "__main__":
		main()
