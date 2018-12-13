"""
This function takes in rows and columns parameters and draws a playing board with the specifie parameters.
"""

def PlayingBoard(rows,columns):
	rows = int(rows)
	columns = int(columns)		
	for num in range(rows):
		if rows > 21 or columns > 21:
			return False	# if the board is larger than 21 rows or 21 columns break out of the loop
			break		

		if num%2 == 0:					
			print(" | "*rows)
		else:
			print("---"*columns)

	





PlayingBoard(20,20)

