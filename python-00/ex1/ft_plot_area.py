# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vebastos <vebastos@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/19 16:45:05 by vebastos          #+#    #+#              #
#    Updated: 2026/01/19 16:45:05 by vebastos         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	ft_plot_area():
	try:
		length = int(input("Enter length: "))
		width = int(input("Enter width: "))
		if length <= 0 or width <= 0:
			print("Error: Values must be positive number")
			return
		total = length * width
		print(f"Plot area: {total}")
	except ValueError:
		print("Error: Must be a number")
