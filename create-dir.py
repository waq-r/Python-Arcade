#  create directory if it does not exist
# import list of directory names from text file
import os

# import lines from text file
with open("titles.txt", "r") as f:
    lines = f.read().splitlines()

def create_directory_if_not_exists(number, directory):
    if not os.path.exists(directory):
        os.makedirs(number+" "+directory)
        # create a text file inside new directory
        with open(os.path.join(number+" "+directory, "README.md"), "w") as f:
            f.write("> ### Meet Python \n --- \n # " + directory + "\n #### Source: [codesignal.com](https://codesignal.com/) Python Arcade \n --- \n")
        # create a python .py extension file inside new directory
        with open(os.path.join(number+" "+directory, kebab_case(directory)+".py"), "w") as f:
            f.write("# " + directory + "\n")

#function to create kebab case name from lines
def kebab_case(name):
    return name.lower().replace(" ", "-")

for line in lines:
    #  if line is text run function if line is number set number to line
    if line.isnumeric():
        #fill with preceding 0 zeros if length is less than 2
        number = str(line).zfill(2)
    else:
        create_directory_if_not_exists(number,line)

