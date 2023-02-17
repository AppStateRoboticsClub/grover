import pygame

pygame.init()

pygame.joystick.init()

joy = pygame.joystick.Joystick(0)
joy.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

''' # button key, all values, 1 or 0
START -> start button; SELECT -> select button;
SQUARE -> left button; CIRCLE -> right button; TRIANGLE -> top button; CROSS -> bottom button;
LBUMP -> left bumper; RBUMP -> right bumper; LSTICK -> left stick button;
RSTICK -> right stick button;
''' # stores the values for the buttons
button: dict[str, float]= {"START": 0, "SELECT": 0, "LEFT": 0, "RIGTH": 0, "UP": 0, "DOWN": 0, 
    "SQUARE": 0, "CIRCLE": 0, "TRIANGLE": 0, "CROSS": 0, "LBUMP": 0, "RBUMP": 0, "LSTICK": 0, 
    "RSTICK": 0, "LTRIGGER": 0, "RTRIGGER": 0, "LSTICKX": 0, "LSTICKY": 0, "RSTICKX": 0, "RSTICKY": 0}

''' # axis key, trigger values from 0 -> 1; stick values from -1 -> 1, -1 left / up, 1 right / down
LTRIGGER -> left trigger; RTRIGGER -> right trigger; LSTICKX, LSTICKY -> left stick x, y;
RSTICKX, RSTICKY -> right stick x, y
''' # store the values for the axis
axis: dict[str, tuple[float, float]] = {"LTRIGGER": 0, "RTRIGGER": 0, "LSTICKX": 0, "LSTICKY": 0,
    "RSTICKX": 0, "RSTICKY": 0}

'''
 - mapXboxOneW
 - Maps the button data to the variables for Xbox One WIRELESS controllers. Note: tested on Avery's
 Xbox One Wireless controller.
 - @return None
'''
def mapXboxOneW() -> None:
    
    # start select
    button["START"] = joy.get_button(15)
    button["SELECT"] = joy.get_button(11)

    # d-pad
    hat = joy.get_hat(0)
    if hat[0] == -1:
        button["LEFT"] = 1
        button["RIGHT"] = 0
    elif hat[0] == 1:
        button["LEFT"] = 0
        button["RIGHT"] = 1
    else:
        button["LEFT"] = 0
        button["RIGHT"] = 0

    if hat[1] == -1:
        button["UP"] = 0
        button["DOWN"] = 1
    elif hat[1] == 1:
        button["UP"] = 1
        button["DOWN"] = 0
    else:
        button["UP"] = 0
        button["DOWN"] = 0

    # buttons
    button["SQUARE"] = joy.get_button(3)
    button["CIRCLE"] = joy.get_button(1)
    button["TRIANGLE"] = joy.get_button(4)
    button["CROSS"] = joy.get_button(0)

    # bumpers
    button["LBUMP"] = joy.get_button(6)
    button["RBUMP"] = joy.get_button(7)

    # stick buttons
    button["LSTICK"] = joy.get_button(13)
    button["RSTICK"] = joy.get_button(14)

    # triggers
    axis["LTRIGGER"] = round((joy.get_axis(5) + 1) / 2, 3)
    axis["RTRIGGER"] = round((joy.get_axis(4) + 1) / 2, 3)

    # lstick
    axis["LSTICKX"] = round(joy.get_axis(0), 1)
    axis["LSTICKY"] = round(joy.get_axis(1), 1)

    # rstick
    axis["RSTICKX"] = round(joy.get_axis(2), 1)
    axis["RSTICKY"] = round(joy.get_axis(3), 1)
    
# PS4
def mapPlayStation4W() -> None:
    
    # start select
    button["START"] = joy.get_button(8)
    button["SELECT"] = joy.get_button(9)

    # d-pad
    hat = joy.get_hat(0)
    if hat[0] == -1:
        button["LEFT"] = 1
        button["RIGHT"] = 0
    elif hat[0] == 1:
        button["LEFT"] = 0
        button["RIGHT"] = 1
    else:
        button["LEFT"] = 0
        button["RIGHT"] = 0

    if hat[1] == -1:
        button["UP"] = 0
        button["DOWN"] = 1
    elif hat[1] == 1:
        button["UP"] = 1
        button["DOWN"] = 0
    else:
        button["UP"] = 0
        button["DOWN"] = 0

    # buttons
    button["SQUARE"] = joy.get_button(3)
    button["CIRCLE"] = joy.get_button(1)
    button["TRIANGLE"] = joy.get_button(2)
    button["CROSS"] = joy.get_button(0)

    # bumpers
    button["LBUMP"] = joy.get_button(4)
    button["RBUMP"] = joy.get_button(5)

    # stick buttons
    button["LSTICK"] = joy.get_button(11)
    button["RSTICK"] = joy.get_button(12)

    # triggers
    axis["LTRIGGER"] = round((joy.get_axis(2) + 1) / 2, 3)
    axis["RTRIGGER"] = round((joy.get_axis(5) + 1) / 2, 3)

    # lstick
    axis["LSTICKX"] = round(joy.get_axis(0), 1)
    axis["LSTICKY"] = round(joy.get_axis(1), 1)

    # rstick
    axis["RSTICKX"] = round(joy.get_axis(3), 1)
    axis["RSTICKY"] = round(joy.get_axis(4), 1)
    
    # if pygame exit, exit
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit()
            '''
        if (event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION or
         event.type == pygame.JOYAXISMOTION):
            #print(axis, button)
            print(event)
            '''
            
    
'''
while True:
    mapPlayStation4W()
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            exit()
        if (event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYHATMOTION or
         event.type == pygame.JOYAXISMOTION):
            print(axis, button)
            #print(event)
'''
