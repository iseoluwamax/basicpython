

def is_valid_nin(nin):


    """confirm if argument is an intejer and 
    if argument is less or greater than 11 in lenght."""
    try:
        nin = int(nin)
        if nin == int(nin):
            print(int(nin))
    except ValueError:
        print("The value you inputed is not an intejer.")
    nin_lenght = len(str(nin))
    if nin_lenght < 11:
        print("The value you inputed is only " + str(nin_lenght) + " digits. Your National Identity Number should be 11 digits.")
    elif nin_lenght > 11:
        print("The value you inputed is only " + str(nin_lenght) + " digits. Your National Identity Number should be 11 digits.")
    elif nin_lenght == 11:
        print("You have inputed your National Identity Number.")


is_valid_nin('jiji')