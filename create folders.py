import os
import sys
from tkinter import *
from tkinter import filedialog

print("\nPython version: ", sys.version, "\n")

def main():

    location_of_folders = input('Where do you want the folders: ')
    name_of_folders = input("What should the prefix for the folders be: ")
    number_of_folders = int(input("How many folders do you want: "))

    if number_of_folders <= 0:
        print('You have to create at least 1 folder.')
        terminate()
    else:
        create_folders(location_of_folders, name_of_folders, number_of_folders)
        terminate()

def create_folders(location_of_folders, name_of_folders, number_of_folders):
    for x in range(1, number_of_folders + 1):

        #concatenates names and numbers of folders
        name_of_folder = name_of_folders + " " + str(x)

        #define name of directory to be created
        path = os.path.join(location_of_folders, name_of_folder)

        try: os.mkdir(path)
        except OSError:
            print("Creation of the directory", name_of_folders, x, "failed")
        else:
            print("Successfully created the directory", name_of_folders, x)

def terminate():
    print(f"Do you want to try again? Y = yes, N = no:")
    run_again = input("")
    run_again = str.lower(run_again)
    if run_again == "yes":
        main()
    elif run_again == "no":
        exit()
    else:
        print("Please type either yes or no")
        terminate()

main()