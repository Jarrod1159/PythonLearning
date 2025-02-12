# Binary Search

# Given: A list of names, a list of phone numbers and a phone number to search for

# Function to open file using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        # Begin exception handling
        try:
            # Try to open the file using the name given
            dataFile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid filename, please try again ... ")
    return dataFile

# Function to read the names and phones into lists
def getLists():
    infile = openFile()
    line = infile.readline()

    names = []
    numbers = []

    while line != "":
        line = line.strip()
        name, number = line.split(',')
        names = names + [name]
        numbers = numbers + [number]
        line = infile.readline()

    infile.close()
    return names, numbers

# Function to find the name and return the associated phone number
def binarySearch(names, phones, name):
    # left side of list    
    left = 0    
    # right side of the list                
    right = len(names) - 1        
    found = 0

    while right >= left and found == 0:
        # find the middle of the list
        m = (left + right) // 2    

        # Fill in the code that examines the middle
        # number and decides what to do next
        if names[m] == name :
            found =1
        elif names[m] > name:
            right = m -1
        else:    
            left = m +1
        

        # Recall that you are going to compare m to 
        # the number you are searching for and decide how
        # to search the part of the list where the name
        # should be.  

        # Hint:  Use left and right to specify the portion
        # of the list to search next

    if found == 0:
        return ""
    else:
        return phones[m]

    
# Main Function

def main():
    # Get the lists
    names, phones = getLists()
    # Get the name to search for
    theName = input("Enter the name to search for: ")

    # Find the phone number for the given name
    phoneNum = binarySearch(names, phones, theName)
    if phoneNum == "":
        print("Name not found")
    else:
        print("The phone number for ", theName, " is ", phoneNum)
