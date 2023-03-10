
import random                                       # imports (random for number gen, time for timer, os for screen clear)
import time
import os

def sort(integers):
    swapped = False                                 # - Swapped variable set at the start of every function call to make sure
    for x in range(len(integers)):                  # the function can exit correctly.
        try:                                        # - Loops through list and determines which numbers need to be swapped.
            secondValue = integers[x+1]             # - The variable that will eventually error due to a list OOB error HAS to be first
            secondIndex = x+1                       # or else the other variables will have values assigned to them that are unwanted
            firstIndex = x                          # and will eventually override values with false ones.
            firstValue = integers[x]    
        except:
            pass
        if firstValue > secondValue:
            swapped = True
            try:
                integers[firstIndex], integers[secondIndex] = secondValue, firstValue 
            except:                                 # - The above is a simple way to swap values without assigning extra variables.
                pass
    if swapped:
        return sort(integers)                       # - return sort(integers) is here because without it the program will 
    else:                                           # return None instead of the actual list.
        return integers

def initialize():                                   # - Initializes the randomly generated list to be used for sorting.
    integers = []
    for x in range(1000):                           # - 1000 seems to be the maximum number of objects in the list the program can
        integers.append(random.randint(0, 1000))    # consistently run at before encountering recursion errors.
    return integers                                 # (everything greater than 1000 recurses into oblivion)

while True:                                         # - Unbreakable while loop for main runtime.
    integers = initialize()
    print(f"Unsorted List: {integers}, with {len(integers)} values.\n")
    initialTime = time.time_ns()                    # - initialTime and finalTime variables just for QoL and speedtesting :)
    sortedIntegers = sort(integers)
    finalTime = (time.time_ns()-initialTime)/1e9
    print(f"Sorted List: {sortedIntegers}, with {len(sortedIntegers)} values.\n")
    print(f"Completed in {finalTime} seconds!")
    query = input("Type 'Retry' to sort another randomly generated list or type 'Exit' to quit the program: ")
    if query.lower() == 'retry':
        os.system('cls')                            # - You can clear the screen in python, just have to not be in debug mode ;)
        continue                                    # - continue is here instead of just calling the init and sort function again
    elif query.lower() == 'exit':                   # to reduce complexity and runtime.
        quit()         