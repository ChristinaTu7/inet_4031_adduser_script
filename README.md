# INET 4031 Add Users Script and User List
# Program Description
This program uses a Python script to automate adding multiple users to a Linux system. A system administrator would have to manually run commands such as "adduser" to create accounts and "passwd" to set passwords, along with additional commands to assign users to groups. 
This script simplifies that process by reading user information from an input file and automatically generate and run the linux commands. Instead of typing everything out manually, the script will handle the creation of the user, assigning the passwords, and grouping the members all at once. This makes the process fast, consistent, and easier to manage.

# Program User Operation
This program works by reading user data from an input file and processing each line within that file. The lines represent single users and contain all the information needed to create accounts. The script builds the linux commands based on the given data and either displays or executes them to create the users. 

# Input File Format
The input file uses colons to represent a user. Each line contains 5 fields in order of: username, password, last name, first name, and group list. The group list can contain multiple groups separated by commas. If a user has a dash, then that user shouldn't be added to any groups. If a line starts with a #, then the script will skip that line. This allows users to comment out entries without deleting them. If a line doesn't contain the 5 fields, it's invalid and will be skipped.

# Command Execution
To run the script, the user must make sure the file is executable. After that, the script can run by redirecting the input file into the script. The script then reads each line from the input file and processes it. The script can run normally with privileges so that it can create users and modify the system settings.

# Dry Run
A dry run allows the user to test the script without actually running the entire program and without making any changes to the system. The script will go through the logic and print out the commands that would be executed, without actually running them. This can be useful to verify and make sure the input file is correct and that the commands are accurate before making any changes. It helps prevent mistakes and makes sure that users and groups will be created correctly.
