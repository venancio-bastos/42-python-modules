# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 17:43:41 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 17:43:41 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	try:
		i = 1
		total = 0

		while i <= 3:
			number = int(input(f"Day {i} harvest: "))
			if number < 0:
				print("Must be a positive number")
				return
			total += number
			i += 1
		print(f"Total harvest: {total}")
	except ValueError:
		print("Error: Must be a number")
