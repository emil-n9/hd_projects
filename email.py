#Message diplayed to the user
usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

#An Email Simulation
class Email:

    #Initilisation function
    def __init__(self, from_address, subject_line, email_contents):
        #Initialises instance variables
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
    
        #Initialises class variables
        self.has_been_read = False
        self.is_spam = False

    #Function that marks the email as read
    def mark_as_read(self):
        self.has_been_read = True
    
    #Function that marks the email as spam
    def mark_as_spam(self):
        self.is_spam = True


#An Inbox Simulation
class Inbox:

    #Initilisation function
    def __init__(self):
        #Initialises empty list to store emails
        self.inbox = []
    
    #Function to add emails to list
    def add_email(self, from_address, subject_line, email_contents):
        self.email_object = Email(from_address, subject_line, email_contents)
        self.inbox.append(self.email_object)

    #Function that displays email's subjects from specific sender
    def list_messages_from_sender(self, sender_address):
        for count, value in enumerate(self.inbox):
            if value.from_address == sender_address:
                print(f"\n{count}. {value.subject_line}")

    #Function that displays contents of email from specific sender and mark it as read                      
    def get_email(self, sender_address, index):
        while True:
            try:
                if self.inbox[index].from_address == sender_address:
                    print("\n" + self.inbox[index].subject_line)
                    print(self.inbox[index].email_contents)
                    self.inbox[index].mark_as_read()
                    break
                else:
                    print("Wrong index entered. Please try again.")
                    index = int(input("Please enter the index of the email that you wold like to read: "))
            except IndexError:
                print("Wrong index entered. Please try again.")
                index = int(input("Please enter the index of the email that you wold like to read: "))

    #Function to mark email from specific sender as spam    
    def mark_as_spam(self, sender_address, index):
        while True:
            try:
                if self.inbox[index].from_address == sender_address:
                    self.inbox[index].mark_as_spam()
                    break
                else:
                    print("Wrong index entered. Please try again.")
                    index = int(input("Please enter the index of the email to be marked as spam: "))
            except IndexError:
                print("Wrong index entered. Please try again.")
                index = int(input("Please enter the index of the email to be marked as spam: "))
    
    #Function that displays all unread emails 
    def get_unread_emails(self):
        for i in range(len(self.inbox)):
            if self.inbox[i].has_been_read == False:
                print("\n" + self.inbox[i].subject_line)

    #Function that displays all spam emails
    def get_spam_emails(self):
        for i in range(len(self.inbox)):
            if self.inbox[i].is_spam == True:
                print("\n" + self.inbox[i].subject_line)
    
    #Function that deletes selected email from specifis sender
    def delete(self, sender_address, index):
        while True:
            try:
                if self.inbox[index].from_address == sender_address:
                    del self.inbox[index]
                    break
                else:
                    print("Wrong index entered. Please try again.")
                    index = int(input("Please enter the index of the email to be deleted: "))
            except IndexError:
                print("Wrong index entered. Please try again.")
                index = int(input("Please enter the index of the email to be deleted: "))



user_choice = ""

#Object of the Inbox Class
inbox_object = Inbox()

while True:
    user_choice = input(usage_message).strip().lower()
    if user_choice == "s":
        # Send an email (Create a new Email object)
        sender_address = input("Please enter the address of the sender\n:")
        subject_line = input("Please enter the subject line of the email\n:")
        contents = input("Please enter the contents of the email\n:")

        # Now add the email to the Inbox
        inbox_object.add_email(sender_address, subject_line, contents)

        # Print a success message
        print("Email has been added to inbox.")

    elif user_choice == "l":
        # List all emails from a sender_address
        sender_address = input("Please enter the address of the sender\n:")

        #Empty list used to store all email addresses from inbox
        address_list = []

        for i in range(len(inbox_object.inbox)):
            address_list.append(inbox_object.inbox[i].from_address)

        #Checks if email address entered by user is in the address list
        while sender_address not in address_list:
            print("Address not found, please try again.")
            sender_address = input("Please enter the address of the sender\n:")

        # Now list all emails from this sender
        inbox_object.list_messages_from_sender(sender_address)

    elif user_choice == "r":
        # Read an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox_object.list_messages_from_sender(sender_address)

        # Step 3: ask the user for the index of the email
        while True:
            try:
                email_index = int(input("Please enter the index of the email that you would like to read\n:"))
                break
            except ValueError:
                print("Wrong input entered. Please try again.")

        # Step 4: display the email
        inbox_object.get_email(sender_address, email_index)

    elif user_choice == "m":
        # Mark an email as spam
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox_object.list_messages_from_sender(sender_address)

        # Step 3: ask the user for the index of the email
        while True:
            try:
                email_index = int(input("Please enter the index of the email to be marked as spam\n:"))
                break
            except ValueError:
                print("Wrong input entered. Please try again.")

        # Step 4: mark the email as spam
        inbox_object.mark_as_spam(sender_address, email_index)

        # Step 5: print a success message
        print("Email has been marked as spam")

    elif user_choice == "gu":
        # List all unread emails
        inbox_object.get_unread_emails()

    elif user_choice == "gs":
        # List all spam emails
        inbox_object.get_spam_emails()

    elif user_choice == "e":
        print("Goodbye")
        break
    
    elif user_choice == "d":
        # Delete an email
        # Step 1: show emails from the sender
        sender_address = input("Please enter the address of the sender of the email\n:")

        # Step 2: show all emails from this sender (with indexes)
        inbox_object.list_messages_from_sender(sender_address)

        # Step 3: ask the user for the index of the email
        while True:
            try:
                email_index = int(input("Please enter the index of the email to be deleted\n:"))
                break
            except ValueError:
                print("Wrong input entered. Please try again.")

        # Step 4: delete the email
        inbox_object.delete(sender_address, email_index)

        # Step 5: print a success message
        print("Email has been deleted")

    else:
        print("Oops - incorrect input")
