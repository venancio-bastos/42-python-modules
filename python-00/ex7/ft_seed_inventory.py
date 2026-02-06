# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 19:30:48 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 19:30:48 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	name = seed_type.capitalize()
	match unit:
		case "packets":
			print(f"{name} seeds: {quantity} {unit} available")
		case "grams":
			print(f"{name} seeds: {quantity} {unit} total")
		case "area":
			print(f"{name} seeds: covers {quantity} square meters")
		case _:
			print("Unknown unit type")
