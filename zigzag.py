#!
# This program displays a zigzag pattern of asterisks(*) till you terminate the program

import time, sys # Import the time and sys modules

indent = 0 # How many spaces to indent
indent_increasing = True # whether indentation is increasing or not

try:
    while(True): # The main program loop
        print(' ' * indent, end='')
        print('********')

        time.sleep(0.1) # Pause for 1/10 of a second

        if indent_increasing:
            # Increase the number of spaces
            indent += 1 # indent = indent + 1
            if indent == 20:
                indent_increasing = False # Change direction
        else:
            # Decrease the number of spaces
            indent -= 1 # indent = indent - 1
            if indent == 0:
                indent_increasing = True # Change direction
except KeyboardInterrupt:
    sys.exit() # Terminate the program when user enter's cntrl -C