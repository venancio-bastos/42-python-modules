# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 18:11:43 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 18:11:43 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_water_reminder():
	try:
		days = int(input("Days since last watering: "))
		if days < 0:
			print("Must be a positive number")
			return
		if days > 2:
			print("Water the plants!")
		else:
			print("Plants are fine")
	except ValueError:
		print("Must be a number!")
