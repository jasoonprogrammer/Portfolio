from latest_sold_v2 import main_function
import time
loop_timer_seconds = 20
looped = 1 #start with 1
max_loop = 2

while True:
	main_function()
	print(f"Looped every {loop_timer_seconds} seconds, {looped} times.")
	looped += 1
	if looped > max_loop:
		break
	time.sleep(loop_timer_seconds)
	print("\n\n\n")
