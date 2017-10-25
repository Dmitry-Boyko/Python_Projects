import datetime

filename = datetime.datetime.now()

def create_filename():
    """This method create empty file"""
    with open (filename.strftime("%m_%d_%Y_%H_%M") + ".txt", "w") as file:
        file.write("")

create_filename()



