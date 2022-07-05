#!/usr/bin/python3
import classes

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''You are the Grim Reaper. You have just finished a difficult job, but this never ending work brings you to the next target... Find and reap the target, don't reap the wrong target...
============
Commands:
go [north,east,south,west]
read [person]
scan [person]
hug [person]
reap [person]
''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the people in the room if anyone is in it
    if "people" in rooms[currentRoom]:
        print('People in the room: ')
        for person in rooms[currentRoom]['people']:
            print(person.name)
    else:
        print("There is no one in this room") 
    print("---------------------------")

#Person class
class Person():
    def __init__(self, name, read, scan, hug):
        self.name = name
        self.reap = 'Slowly the colors and the weight fade, frozen in time never to thaw'
        self.hug = hug
        self.read = read
        self.scan = scan
    
guy = Person('Guy', 'these are his thoughts', 'he lived a good life', 'you hug the guy')

receptionist = Person('Receptionist','read','scan','hug')

nurse_joy = Person('Nurse Joy','read','scan','hug')

ash = Person('Ash','read','scan','hug')

delia = Person('Delia','read','scan','hug')

grandma_betty = Person('Grandma Betty','read','scan','hug')

dr_oak = Person('Dr. Oak','read','scan','hug')

dr_bro = Person('Dr. Bro','read','scan','hug')

rooms = {
    'Hospital Entrance' : {
        'north' : 'Front Desk',
        'people'  : [guy]
    },

    'Front Desk' : {
        'north' : 'Patient Hallway',
        'east' : 'Emergency Room',
        'south' : 'Hospital Entrance',
        'west' : 'Office Hallway',
        'people' : [receptionist]
    },

    'Patient Hallway' : {
        'north' : 'Patient Room #2',
        'east' : 'Patient Room #3',
        'south' : 'Front Desk',
        'west' : 'Patient Room #1',
        'people' : [delia]
    
    },

    'Patient Room #1' : {
        'east' : 'Patient Hallway',
    },

    'Patient Room #2' : {
        'south' : 'Patient Hallway',
        'people' : [ash]
    },

    'Patient Room #3' : {
        'west' : 'Patient Hallway',
        'people' : [grandma_betty]
    },

    'Emergency Room' : {
        'west' : 'Front Desk',
        'north': 'Janitor Closet'
    },

    'Janitor Closet' : {
        'south' : 'Emergency Room',
        'people' : [nurse_joy]
    },

    'Office Hallway' : {
        'north' : 'Office #2',
        'west' : 'Office #1'
    },

    'Office #1' : {
        'east' : 'Office Hallway',
        'people' : [dr_oak]
    },

    'Office #2' : {
        'south' : 'Office Hallway',
        'people' : [dr_bro]
    }

}


#start the player in the Hall
currentRoom = 'Hospital Entrance'

reaped = ''

showInstructions()

#loop forever
while True:

    showStatus()

    command = ['go', 'reap', 'read','scan','hug']

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == command[0]:
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'reap' first
    if move[0] == command[1]:
        #if room has a person and the person is the person they want to reap
        if 'people' in rooms[currentRoom] and move[1].lower() == rooms[currentRoom]['people'][0].name.lower():
            print('You take your trusty scythe and take a calculated swing at '+move[1]+"'s neck...")
            #need to connect move[1] and the coressponding obj
            reaped = move[1].lower()
        else:
            print(move[1]+" is not in here!")
    
    #if they type 'read' first
    if move[0] == command[2]:
        if 'people' in rooms[currentRoom]:
            for person in rooms[currentRoom]['people']:
                if move[1].lower() == person.name.lower():
                    print(person.read)
        else:
            print(move[1]+" is not in here!")

    # if they type 'scan' first
    if move[0] == command[3]:
        if 'people' in rooms[currentRoom]:
            for person in rooms[currentRoom]['people']:
                if move[1].lower() == person.name.lower():
                    print(person.scan)
        else:
            print(move[1]+" is not in here!")

    # if they type 'hug' first
    if move[0] == command[4]:
        if 'people' in rooms[currentRoom]:
            for person in rooms[currentRoom]['people']:
                if move[1] == person.name.lower():
                    print(person.hug)
        else:
            print(move[1]+" is not in here!")

    #if they type something not in moves
    if move[0] not in command:
        print("Invalid command, try again")

    ## WIN CONDITION: HOW TO WIN
    if reaped == 'ash':
        print('You have reaped Ash, congrats you win... on to the next job I guess.')
        break

    ## LOSE CONDITION: YOU REAP ANYONE OTHER THAN ASH
    if reaped != '':
        print('YOU REAPED THE WRONG GUY\nSlowly the soul of the reaped spin around you as the balance has been tipped.\nImmense guilt has out grown your perfect record, oozing into your concience. \nDarkness follows as you set in motion the next apocolypse. \n\n----GAME OVER----')
        break