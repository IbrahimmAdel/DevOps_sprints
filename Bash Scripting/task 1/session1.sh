#!/bin/bash
echo "This script will print variables, and execute Linux commands"

#There will be errors within the script, it needs to be modified to run and the meet a specific output
#Print env details, including current directory,current user, and list files in the home directory with the addition to the exit code for   each command
#Use functions for each command including exit code
#Provide screenshots of the output

#Enter rest of code here

print_current_directory(){
                           echo "current directory : "$PWD 
                           echo $?
                         }
                       
print_current_user(){
                         echo "user :"$USER
                         echo $?
                    }
list_files(){
                 echo "files in home directory: "
                 cd 
                 ls
                 echo $? 
            }
                    
print_current_directory 
print_current_user
list_files
