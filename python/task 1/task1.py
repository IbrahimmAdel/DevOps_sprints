def change_char():

    while True:
    
        x = input("do you want to enter a string? [yes/no] ")
        if x == "no":
            break
        elif x == "yes":

            # take inputs from user
            string = input("please enter the string : ")
            string_list = list(string)  # put string in list to modify it

            index = int(input("please enter index of the character you want to change : "))
            if index >= len(string_list):  # check if index is in range of string
                print("sorry you have entered invalid index,please try again")
                
            else:
                new_char = input("please enter the new character : ")
                string_list[index] = new_char  # modify the list
                string = ''.join(string_list)
                print("the new string is : {} ".format(string))  # print the new string


change_char()  # call function
