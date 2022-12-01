def dayoftheprogrammer(year):
	#As per the example provided in the exercise a loop year in the Julian calendar is divisible with 4
	#In the Gregorian calendar a loop year is divisible with 400 , 4 and not divisible by 100
	if year < 1918:
		if year % 4 == 0:
			return f"12.09.{year}"
		else:
			return f"13.09.{year}"
	elif year > 1918:
		if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
			return f"12.09.{year}"
		else:
			return f"13.09.{year}"
	else:
		return f"26.09.{year}"

if __name__ == '__main__':
	
	print(dayoftheprogrammer(1800))