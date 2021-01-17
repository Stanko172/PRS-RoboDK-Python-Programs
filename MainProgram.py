from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
from random import randint
import time
RDK = Robolink()

# Pridruživanje varijabli programima:
start_point = RDK.Item('StartPoint')
pick_prog1 = RDK.Item('PickProg1')
pick_prog2 = RDK.Item('PickProg2')
pick_prog3 = RDK.Item('PickProg3')
pick_prog4 = RDK.Item('PickProg4')
place_prog = RDK.Item('PlaceProg')
pick_place_track_prog = RDK.Item('PickPlaceToTrack')
paint_prog = RDK.Item('PaintProg')
rotate_cube1 = RDK.Item('RotateCube1')
rotate_cube2 = RDK.Item('RotateCube2')
move_to_track = RDK.Item('MoveToTrack')
run_conveyor = RDK.Item('RunConveyor')
spray_on_red = RDK.Item('SprayOnRed')
spray_on_blue = RDK.Item('SprayOnBlue')

blue_values = '[0.0, 0.0, 1.0, 1.0]'
red_values = '[1.0, 0.0, 0.0, 1.0]'
white_values = '[0.929411768913269, 0.9333333373069763, 1.0, 1.0]'

x = True
red_counter = 0
blue_counter = 0
#print(item)

run_conveyor.RunProgram()

item = RDK.Item('RobotiQ 2-Finger-140 Open')
prog_array = [pick_prog1, pick_prog2, pick_prog3, pick_prog4]

while(x):
    random_number = randint(0, len(prog_array) - 1)
    print(random_number)

    choosen_prog = prog_array[random_number]
    choosen_prog_number = choosen_prog.Name()[-1]
    #print(choosen_prog_number)
    choosen_prog.RunProgram()

    time.sleep(4)

    print(str(RDK.Item('Part ' + str(choosen_prog_number)).Color()))
    if(str(RDK.Item('Part ' + str(choosen_prog_number)).Color()) == white_values):

        if(blue_counter > red_counter):
            spray_on_red.RunProgram()
        elif(red_counter > blue_counter):
            spray_on_blue.RunProgram()
        else:
            sprays = [spray_on_red, spray_on_blue]
            sprays[randint(0, 1)].RunProgram()
            
        place_prog.RunProgram()
        time.sleep(4)
        for i in range(4):
            rotate_cube1.RunProgram()
            time.sleep(2)
            paint_prog.RunProgram()
            time.sleep(2)
            

        for j in range(1, 5):
            rotate_cube2.RunProgram()
            time.sleep(2)
            if(j % 2 == 0):
                paint_prog.RunProgram()
                time.sleep(2)

        pick_place_track_prog.RunProgram()
        time.sleep(4)
        
    else:
        if(str(RDK.Item('Part ' + str(choosen_prog_number)).Color()) == red_values):
            red_counter += 1
        else:
            blue_counter += 1
        
        move_to_track.RunProgram()
        time.sleep(4)
        
    prog_array.pop(random_number)

    print(choosen_prog.Name())
    

    if(len(prog_array) == 0 ):
        x = False
