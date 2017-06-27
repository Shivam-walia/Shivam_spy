#import or adding previous file to main file
from spy_detail import spy,Spy,chat_message,friends
from  steganography.steganography import Steganography
from datetime import datetime
now=datetime.now()

# list contains pre-status
STATUS_MESSAGES = ["I'm busy", "At Gym", "At Movies"]
# lists with different names of new friend


# Display hello as output
print (" *************Hello**************")

print("welcome to spy chat appication")

choice = raw_input("would you like to continue as default user ..? (Y/N)..:")



# function defination
def add_status(current_status_message):

    updated_status_message = None
    # the current status is not empty

    if spy.current_status_message != None:

        print "your current status message is" + current_status_message + "\n"

    else:

        print "you dont have any status message currently"
        # Either select from the previous messages

        default = raw_input("Do you want to select from older status (Y or N)...?")

        if default.upper() == "N":

            new_status_message = raw_input("What status message do you want to set...?")

            # validation its value must be greater than 0

            if len(new_status_message) > 0:
                # Append adds new sting at hte end of previous string

                STATUS_MESSAGES.append(new_status_message)

                updated_status_message = new_status_message

        elif default.upper() == "Y":

            Item_position = 1
            # loops for

            for message in STATUS_MESSAGES:

                print '%d. %s' % (Item_position, message)

                Item_position = Item_position + 1

            message_selection = int(raw_input("\n choose from the above messages...!"))

            # checks if length of status messages i greater than msg selection

            if len(STATUS_MESSAGES) >= message_selection:

                updated_status_message = STATUS_MESSAGES[message_selection - 1]

            else:

                print "The selected  option is incorrect! Please enter Y or n...?"

            if updated_status_message:

                print "Your updated status message is" + updated_status_message + "\n"

            else:

                print "Your status is not updated please try again...!"

            # returns the value to the variable named updated status message

            return updated_status_message


# function defination for adding new friend in spy

def add_friend():

    new_friend=Spy('','',0,0.0)

    new_friend.name = raw_input("please enter your friends name")
    new_friend.salutation = raw_input("May we call them Mr. or Ms. ...?")
    new_friend.name = '%s %s' % (new_friend.salutaton, new_friend.name)
    new_friend.age = int(raw_input("what is  their Age"))
    new_friend.rating = float(raw_input("spy_rating"))

    # conditional check whether value is entered or not

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= 0:
        friends.append(new_friend)
    else:
        print("Sorry please fill the correct details ,Invalid entry...!")

    return len(friends)

#function for select friends

def select_friend():

    count=0
    for friend in friends:
        print '%d. %s age is %d rating %.1f is online' % (count + 1, friend.name,friend.age,friend.rating)
        count=count+1
    friend_choice =raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

#function send message to friends

def send_message():

    friend_choice=select_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = ("output.jpg")
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    new_chat=chat_message(text,True)

    friends[friend_choice].chats.append(new_chat)
    print "Here is your secret message"

#Read messages of friends

def read_message():

    sender=select_friend()

    output_path=raw_input("what is Image name" )
    secret_text=Steganography.decode(output_path)
    print(secret_text)

    new_chat=chat_message(secret_text,False)

    friends[sender].chats.append(new_chat)
    print"Here your secret is saved"
#read previous chat history of friends

def read_chat_history():

    read_for=select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s %s '%(chat.time.strftime("%d %B %y"),'you said',chat.message)
        else:
            print '[%s] %s said: %s' %(chat.time.strftime("%d %B %y"),friends[read_for].name,chat.message)




# defination for start chat

def start_chat(spy):
    current_status_message = None
    show_menu = True
#while loop The program continues untill the value is true
    while show_menu:
        menu_choices = "what you want to do? \n 1.Add a status updae \n 2.Add a spy friend \n 3.select a friend \n 4.send secret message \n 5.Read secret message \n 6. Read chat from user \n 7.Exit close application"

        menu_choice = raw_input(menu_choices)
#menu choices to enter details of spy user
        if len(menu_choice) > 0:

            menu_choice = int(menu_choice)

            if menu_choice == 1:
                spy.current_status_message = add_status(current_status_message)

            elif menu_choice == 2:
                number_of_friends = add_friend()
                print "%d friends added"%(number_of_friends)
            elif menu_choice==3:
                select_friend()
            elif menu_choice==4:
                send_message()
            elif menu_choice==5:
                read_message()
            elif menu_choice==6:
                read_chat_history()

            elif menu_choice ==7:
                show_menu = False

#continue as a default user...
if choice == 'y' or choice == 'Y':

    print("welcome %s we are glad to have you back.." % (spy.name))
    print("%s %s" % (spy.salutaton, spy.name))
    print("your age is %d" % (spy.age))
    print("your rating is %.1f " % (spy.rating))
    start_chat(spy)
#New user will be created
elif choice == 'n' or choice == 'N':

    spy.name = raw_input("Welcome to the spy chat ! what is your name...?")

    if len(spy.name) > 0:

        print("welcome " + spy.name + "We are happy to have you back")

        spy_salutation = raw_input("what should i call you  Mister or Miss...?")
        # variable updated
        spy.name = spy.salutaton + " " + spy.name

        print("Alright" + spy.name + "I would like to know more about you before we proceed...")

        # new variable takes input as your age
        spy.age = raw_input("what is your age...")

        print type(spy.age)
        # Type casting is done
        spy.age = int(spy.age)
        print type(spy.age)

        # codition checked wheher entered value is true or false
        if spy.age > 12 and spy.age <= 50:

            spy.rating = raw_input("what is your spy rating...")

            spy.rating = float(spy.rating)

            print type(spy.rating)
        #spy rating range to tell user experience
            if spy.rating > 4.5:
                print("excellent ace...!")
            elif spy.rating > 3.5 and spy.rating <= 4.5:
                print("you bears a good value...!")
            elif spy.rating >= 2.5 and spy.rating <= 3.5:
                print ("You can always do better...!")
            else:
                print ("We can always use somebody to help in the office...!")

            spy.online = raw_input("True")

            # sucessfull login message

            print (
            "Authentication complete. Welcome " + str(spy.name) + " age: " + str(spy.age) + " and rating of: " + str(
                spy.rating) + " Proud to have you onboard...!")

            # codition fails again re-enter the details

            start_chat(spy.salutaton, spy.name, spy.age)



        else:

            print("please enter valid age for spy")
    else:

        print("please enter the valid name or Try again ")









