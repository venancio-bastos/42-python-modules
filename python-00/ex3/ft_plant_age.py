# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 18:01:59 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 18:01:59 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
	try:
		plant_age = int(input("Enter plant age in days: "))
		if plant_age < 0:
			print("Must be a positive number")
			return
		if plant_age > 60:
			print("Plant is ready to harvest!")
		else:
			print("Plant needs more time to grow.") 
	except ValueError:
		print("Must be a number!")
