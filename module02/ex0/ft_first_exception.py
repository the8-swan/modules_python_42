def  check_temperature():
	print("=== Garden Temperature Checker ===")
	temp_str = input("Testing temperature: ")
	try : 
		tmp = int(temp_str)
		if tmp > 0 and tmp < 40 :
			print(f"Temperature {tmp}°C is perfect for plants!")
		elif(tmp > 40):
				print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
		else :
			print(f"Error: {tmp}°C is too cold for plants (min 0°C)")

	except :
		print(f"Error: '{temp_str}' is not a valid number")
	print("All tests completed - program didn't crash!")


if __name__ == "__main__":
	 check_temperature()