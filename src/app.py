from user_controls import UserConcerns
from comments import Comment
if __name__ =='__main__':
    user=UserConcerns(username="",password='')
    comment =Comment(author_id=1, message='some comment')
    user1= {"testuser","pass"}
    user.database=[user1]

    

    print ("Select Option")
    print(20 * "-", "MENU", 20 * "-")
    print("0.Login")
    print("1.SignUp")
    print("2. Write a comment")
    print("3. Edit a comment")
    print("4. Delete a comment")
    print("5. Deleting all comments")
    print("6. Logout")

    loop = True #this keeps app running until it meets false
    task=''    
    while loop:
        selection = int(input("selection: "))

        if selection== 0:
            print("0.Login")
            username=input("Enter your username:  ")
            password=''
            
            # while username in user.database:
            user.login_user(username,password)
            print("{} you are logged in".format(username))     
            
        elif selection == 1:
                print("1.Please sign up")
                user.create_user(username,password)
        elif selection== 2:
            print("2.Write a comment")
            comment.to_dict()
            comment.save_comment()
        elif selection ==3 :
            print("3.Edit a comment")

            comment_id=str(input("Enter comment_id you want to edit: "))
            comment.edit_comment(comment_id)
        elif selection ==4:
            print("4. Delete a comment")
            comment=str(input("Enter comment_id you want to delete: "))
         
        elif selection==5:
            print("5.Deleting all comments")

        elif selection ==6:
            print("6. You are leaving application")
            loop=False #this will set the loop to close, hence end program
        else:
            print("Selection doesnot exist. Enter a valid selection ")  #when one enters a number out of the menu range