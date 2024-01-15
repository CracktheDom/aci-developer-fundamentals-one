try:
    file = open("myfile.txt", "r")
    # Perform some operations on the file
except FileNotFoundError:
    print("The file could not be found.")
except IOError:
    print("An error occurred while reading the file.")
else:
    print("File contents:", file.read())
finally:
    if "file" in locals():
        file.close()
        print("File closed.")
