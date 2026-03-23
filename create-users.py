#!/usr/bin/python3

# INET4031
# Christina
# 3/21/26
# 3/22/26

#os is used to run linux system commands from the python script
#re is used to check whether a line starts with # so it can be skipped
#sys is used to read input line by line from the input file

import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    #reads each line from input (create-users.input)
    for line in sys.stdin:

        #checks if the line start with #, means it's commented out and should be skipped
        match = re.match("^#",line)

        #removes extra whitespace and split the line into fields using colons, each line should contain username, password, last name, first name, and groups
        fields = line.strip().split(':')

        #skips the line if it's commented out or doesn't contain the 5 fields, prevents script from processing invalid input
        if match or len(fields) != 5:
            continue

        #stores the username and password from input, build the fields using first and last name so that the full name will be stored in /etc/passwd
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #split the group field by commas so it can process multiple groups for one user by the script
        groups = fields[4].split(',')

        #print a message showing that the script is preparing to create a user account
        print("==> Creating account for %s..." % (username))

        #builds the linux adduser command to create accounts without prompting for a password and sets the username
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #during a dry run, print the command that would be executed
        print(cmd)
        os.system(cmd)

        #print a message shwoing that the password is about to be set
        print("==> Setting the password for %s..." % (username))

        #build the command that sends the password into passwd so the user's password can be set
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #during a dry run, print out the command that will be executed
        print(cmd)
        os.system(cmd)

        #go through each group listed for the user
        for group in groups:

            #the dash means the user shouldn't be added to any extra groups, if the value is not a dash, add the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
