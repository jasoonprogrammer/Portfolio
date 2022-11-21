
while True:
	print("Search Market Using?")
	print("1. axie.txt\n2. ronin.txt")
	choice = input("")
	if choice == "1":
		import axie_searcher_v3
		break
	elif choice == "2":
		import ronin_searcher_v3
		break
	else:
		print("Invalid Choice. Please select a valid choice.")