# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 18:19:03 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 18:19:03 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(i = 1, days_left = None):
	try:
		if days_left is None:
			days_left = int(input("Days until harvest: "))
			if days_left < 0:
				print("Must be a positive number!")
				return
		print(f"Day {i}")
		if i < days_left:
			i += 1
			ft_count_harvest_recursive(i, days_left)
		else:
			print("Harvest time!")
	except ValueError:
		print("Must be a number")
