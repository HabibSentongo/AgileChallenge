from user_controls import UserConcerns
if __name__ =='__main__':
    user=UserConcerns()

    username=input("Enter your username:  ")
    password=None
    
    while username in user.database:
        user.login_user(username,password)
        print("{} you are logged in".format(username))     
     
    else:
        print("Please sign up")
        user.create_user(username,password)

    print ("Select Option")
    print(20 * "-", "MENU", 20 * "-")
    print("0.Login")
    print("1. Write a comment")
    print("2. Edit a comment")
    print("3. Delete a comment")
    print("4. Deleting all comments")
    print("5. Logout")

    loop = True #this keeps app running until it meets false
    task=''    
    while loop:
        selection = int(input("selection: "))

        if selection== 1:
            print("1.Write a comment")

        elif selection ==2 :
            print("2.Edit a comment")
            task=str(input("Enter comment_id you want to edit: "))
           
        elif selection ==3:
            print("3. Delete a comment")
            task=str(input("Enter comment_id you want to delete: "))
         
        elif selection==4:
            print("3.Deleting all comments")

        elif selection ==5:
            print("5. You are leaving application")
            loop=False #this will set the loop to close, hence end program
        else:
            print("Selection doesnot exist. Enter a valid selection ")  #when one enters a number out of the menu range