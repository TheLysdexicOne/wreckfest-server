import random
from random import randint

with open('E:/SteamLibrary/steamapps/common/Wreckfest Dedicated Server/eventloops/racing_maps.txt') as f:
    racing_maps = f.read().splitlines()

with open('E:/SteamLibrary/steamapps/common/Wreckfest Dedicated Server/eventloops/arena_maps.txt') as f:
    arena_maps = f.read().splitlines()

with open('E:/SteamLibrary/steamapps/common/Wreckfest Dedicated Server/eventloops/figure_8_maps.txt') as f:
    figure_8_maps = f.read().splitlines()


class_restrictions = ['a','b','c','a','b','c','special']
figure_8_class_restrictions = ['a','b','c','special']
arena_restrictions = ['school bus','lawn mower','bumper car','honey pot']
figure_8_restrictions = ['school bus','school bus','school bus','school bus','motor home','sofa car']
racing_restrictions = ['school bus','school bus','school bus','school bus','school bus','school bus','school bus','school bus','motor home','sofa car','bugzilla']
laps = ['5', '6', '7']

x = 0
while x <= 100:
    y = randint(0,100)

    if y > 90:
        z_map = random.choice(arena_maps)

        z_class_restriction = random.choice(class_restrictions)
        z_car_restriction = ''
        if z_class_restriction == 'special':
            z_class_restriction = ''
            z_car_restriction = random.choice(arena_restrictions)
        print('el_add=',z_map)
        print('el_gamemode=derby deathmatch')
        print('el_bots=',randint(10,20))
        print('el_car_class_restriction=',z_class_restriction)
        print('el_car_restriction=',z_car_restriction)
        print('')
    
    elif y < 20:
        z_map = random.choice(figure_8_maps)

        z_class_restriction = random.choice(figure_8_class_restrictions)
        z_car_restriction = ''
        if z_class_restriction == 'special':
            z_class_restriction = ''
            z_car_restriction = random.choice(figure_8_restrictions)
        
        print("el_add=",z_map)
        print('el_gamemode=racing')
        print('el_laps=12')
        print('el_bots=24')
        print('el_car_class_restriction=',z_class_restriction)
        print('el_car_restriction=',z_car_restriction)
        print('')
    
    else:
        z_map = random.choice(racing_maps)

        z_class_restriction = random.choice(class_restrictions)
        z_car_restriction = ''
        if z_class_restriction == 'special':
            z_class_restriction = ''
            z_car_restriction = random.choice(racing_restrictions)
        
        print("el_add=",z_map)
        print('el_gamemode=racing')
        print('el_laps=5')
        print('el_bots=',randint(6,20))
        print('el_car_class_restriction=',z_class_restriction)
        print('el_car_restriction=',z_car_restriction)
        print('')

    # racing_map = random.choice(racing_maps)
    # print("el_add=",racing_map)
    # print(y)
    x += 1




# Event Loop (el) settings.
#-------------------------------------------------------------------------------
#  If enabled, server will automatically rotate pre-configured events.
#  Using "el_add=trackname" you can add as many events to the rotation as you wish.
#  Note that "el_*" parameters override corresponding global settings for the event.
#  Remove the first # from setup parameters to enable.
#  Use the console command /eventloop to enable/disable rotation.

## Add first event to Loop
#el_add=gravel1_main_loop
#el_gamemode=racing
#el_laps=3
#el_bots=3
#el_car_reset_disabled=0
#el_wrong_way_limiter_disabled=0
#el_car_class_restriction=a
#el_car_restriction=
#el_weather=

## Add second event to Loop
#el_add=tarmac1_main_circuit
#el_gamemode=team race
#el_num_teams=2
#el_laps=3
#el_bots=3
#el_car_reset_disabled=0
#el_wrong_way_limiter_disabled=0
#el_car_class_restriction=a
#el_car_restriction=
#el_weather=

## Add third event to Loop
#el_add=speedway2_demolition_arena
#el_gamemode=derby deathmatch
#el_bots=3
#el_car_reset_disabled=0
#el_car_class_restriction=a
#el_car_restriction=
#el_weather=
