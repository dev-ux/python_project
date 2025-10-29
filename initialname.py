

def get_initial_name (name, force_uppercase=True):
    if force_uppercase:
        initial= name[0:1].upper()
    else:
        initial= name[0:1]
    return initial

first_name = input ('enter your first name: ')
first_name_initial = get_initial_name (force_uppercase=True, \
    name= first_name)

print ('Your first name initial is: ' + first_name_initial)