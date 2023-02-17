import controller, motors
print("hello world")

lastSpeed = 0
lastTurn = 0

# main program loop
while True:
	
	# emergency brake, cross on controller exits program
	if controller.button["CROSS"] == 1:
		exit()
	controller.mapPlayStation4W()
	#print(controller.button)
	
	# get the speed
	speed = 20 * controller.axis["RTRIGGER"]
	# check for reverse
	motors.setReverse(controller.button["RBUMP"] == 1)

	turn = controller.axis["RSTICKX"]
	if turn < 0.2 and turn > -0.2:
		turn = 0
	#print(speed)
	#print(turn)
	
	
	if turn == 0 and lastSpeed != speed:
		motors.acc(speed)
		print(speed)
	if turn != 0 and (lastSpeed != speed or lastTurn != turn):
		motors.speed = speed
		motors.turn(turn)
		
	lastSpeed = speed
	lastTurn = turn

	
