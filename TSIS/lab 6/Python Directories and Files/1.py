#Write a Python program to list only directories, files and all directories, files in a specified path.
import os

def listDirectories(path):
    print("Directories: ")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def listFiles(path):
    print("Files: ")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def listAll(path):
    print("All directories and files: ")
    for item in os.listdir(path):
        print(item)

path = 'C:/pp2/lab6/Python Directories and Files'
listDirectories(path)
listFiles(path)
listAll(path)