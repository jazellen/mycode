#!/usr/bin/env python3

loginfail = 0	#set a counter called loginfail and initialize it at 0
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')  	#file-object called, keystone_file, by using the open() function on the file we just downloaded, with read privledges (which is the tiny r at the end).
keystone_file_lines=keystone_file.readlines()	# use readlines() which allows us to create a list called keystone_file_lines where each item in the list is a new line read from our file, keystone_file.
for i in range(len(keystone_file_lines)):  #create a for loop.
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:	#Indent 4 white sapces, since we are inside of a for loop. If the pattern, - - - - -] Authorization failed is found within the list keystone_file_lines
        loginfail += 1 # this is the same as loginfail = loginfail + 1	#increase the log in failure counter, loginfail. This is inside a for-loop, inside of an if statement, so indent a total of 8 whitespaces.
print('The number of failed log in attempts is ' + str(loginfail)) 	#print the number of failed log in attempts to the screen, which is now stored in loginfail. You don’t need to indent here.
