# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 19:22:07 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 19:22:07 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
	try:
		garden_name = input("Enter garden name: ")
		total_plants = input("Enter number of plants: ")
		print(f"Garden: {garden_name}")
		print(f"Plants: {total_plants}")
		print("Status: Growing well!")
	except ValueError:
		print("Must be a number")