#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
    'Hospital Entrance' : {
        'north' : 'Front Desk',
        'people'  : ['Guy']
    },

    'Front Desk' : {
        'north' : 'Patient Hallway',
        'east' : 'Emergency Room',
        'south' : 'Hospital Entrance',
        'west' : 'Office Hallway',
        'item'  : 'sign-in sheet',
        'people' : ['the receptionist','nurse Joy']
    },

    'Patient Hallway' : {
        'north' : 'Patient Room #2',
        'east' : 'Patient Room #3',
        'south' : 'Front Desk',
        'west' : 'Patient Room #1',
    },

    'Patient Room #1' : {
        'east' : 'Patient Hallway'
    },

    'Patient Room #2' : {
        'south' : 'Patient Hallway',
        'people' : ['Ash','Delia']
    },

    'Patient Room #3' : {
        'west' : 'Patient Hallway',
        'people' : ['Grandma Betty', "Frank"]
    },

    'Emergency Room' : {
        'west' : 'Front Desk',
    },

    'Office Hallway' : {
        'north' : 'Office #2',
        'west' : 'Office #1'
    },

    'Office #1' : {
        'east' : 'Office Hallway',
        'people' : ['Dr. Oak']
    },

    'Office #2' : {
        'south' : 'Office Hallway',
        'people' : ['Dr. Bro']
    }

}