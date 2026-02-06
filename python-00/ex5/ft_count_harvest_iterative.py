# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 18:18:56 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 18:18:56 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_count_harvest_iterative():
	try:
		days_left = int(input("Days until harvest: "))
		if days_left < 0:
			print("Must be a positive number")
			return
		for i in range (1, days_left + 1):
			print(f"Day {i}")
		print("Harvest time!")
	except ValueError:
		print("Must be a number")
