#=====importing libraries=====
from datetime import date 
from datetime import datetime

#====Login Section====
login = input("Enter username: ")
password = input("Enter password: ")

#Empty list used to store username and password
user_list = []

#Contents of user_info are stored in user_list in the form of a tuple
with open('user.txt', 'r') as f1:
    for line in f1:
        user_info = line.split(", ")
        user_list.append((user_info[0], user_info[1]))

#user_list is converted to a dictionary user_dict
user_dict = dict(user_list)

#Checks if right login credentials were entered
while True:
    if login in user_dict and password == str(user_dict[login]).strip('\n'):
        break
    else:
        print("Incorrect credentials entered, please try again")
        login = input("Enter username: ")
        password = input("Enter password: ")


#Function that lets the admin register a new user
def reg_user():
    new_user = input("Enter a new username: ")
    new_pass = input("Enter a new password: ")
    ver_pass = input("Confirm password: ")

    #Checks if the username alredy exits
    while True:
        if new_user in user_dict.keys():
            print("Username already exists!")
            new_user = input("Enter a new username: ")
            new_pass = input("Enter a new password: ")
            ver_pass = input("Confirm password: ")
            continue
        else:
            break

    #Checks if password was entered correctly twice
    while new_pass != ver_pass:
        print("Passwords don't match, please try again")
        new_pass = input("Enter a new password: ")
        ver_pass = input("Confirm password: ")
    
    #Adds new user details to user.txt file in the right format
    with open('user.txt', 'a') as f1:
        f1.write(f"\n{new_user}, {ver_pass}")   


#Function that let's you add a task
def add_task():
    #Asks the user for all the details
    user = input("Enter the username the task is assigned to: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the desription of the task: ")
    due_date = input("Enter the date the task is due on (format: 'day' 'month abbreviation' 'year'): ")

    #Used the date library to get todays date and formated it the right way
    today = date.today()
    assign_date = today.strftime("%d %b %Y")

    #Adds the task info to tasks.txt file in the right format
    with open('tasks.txt', 'a') as f2:
        f2.write(f"\n{user}, {title}, {description}, {assign_date}, {due_date}, No")


#Function that let's you displays all tasks
def view_all():
    #Reads each line and splits each detail into task_list
    with open('tasks.txt', 'r') as f2:
        for line in f2:
            task_list = line.split(", ")
            #task_list is then used to display each detail in the following format
            print(f'''______________________________________________________

Task:               {task_list[1]}
Assigend to:        {task_list[0]}
Date assigned:      {task_list[3]}
Due date:           {task_list[4]}
Task Complete?      {task_list[5]}
Task description:
 {task_list[2]}
______________________________________________________''')


#Funtction for displaying only the users task
def view_mine():
    with open('tasks.txt', 'r+') as f2:
        contents = f2.readlines()  #Contents of 'tasks.txt' are saved in the variable contents
        for value, task in enumerate(contents):  #Used th enumerate function so that each line in contents can be identified
            task_list = task.split(", ")
            if login == task_list[0]:
                print(f'''______________________________________________________

Task number:        {value}
Task:               {task_list[1]}
Assigend to:        {task_list[0]}
Date assigned:      {task_list[3]}
Due date:           {task_list[4]}
Task Complete?      {task_list[5]}
Task description:
 {task_list[2]}
______________________________________________________
''')
        #Asks user to select the task they'd like to edit or to return to the main menu
        edit_num = int(input("Enter the task number of the task you'd like to edit or -1 to return to the menu: "))
        if edit_num != -1:
            split_data = contents[edit_num].split(", ")
            edit = input("Would you like to 'mark the task as completed (m)' or 'edit the task (e)'? (m/e): ")
            #Changes the 'No' to a 'Yes' to indicate the tasks is complete
            if edit.lower() == "m":
                split_data[5] = "Yes\n"
            elif edit.lower() == "e" and split_data[5].strip("\n") == "No": #Checks that the task isn't completed yet
                #Lets user assign the task to someone else
                assign = input("Would you like to assign the task to someone else? (y/n): ")
                if assign.lower() == "y":
                    assigned_to = input("Enter the username to whom the task is now assigned to: ")
                    split_data[0] = assigned_to
                #Lets user change the due date of the task
                edit_date = input("Would you like to edit the due date of the task? (y/n): ")
                if edit_date.lower() == "y":
                    new_date = input("Enter the new date the task is due on (format: 'day' 'month abbreviation' 'year'): ")
                    split_data[4] = new_date
            else:
                print('''
                Wrong input or task already completed!
                ''')
            join_data = ", ".join(split_data)
            contents[edit_num] = join_data 
        
    #Overwrites 'tasks.txt' with the changes made
    with open('tasks.txt', 'w') as f3:
        for line in contents:
            f3.write(line)


#Function that genetrates reports on users and tasks
def generate_reports():
    #Checs the status of each task
    with open('tasks.txt', 'r') as f2:
        task_count = 0
        completed_count = 0
        overdue_count = 0
        for line in f2:
            task_count += 1
            task_list = line.split(", ")
            if task_list[5].strip("\n") == "Yes":
                completed_count += 1
            elif task_list[5].strip("\n") == "No":
                todays_date = datetime.today()
                due_date = datetime.strptime(task_list[4], "%d %b %Y")
                if due_date < todays_date:
                    overdue_count += 1

        uncompleted_count = task_count - completed_count
        uncompleted_percent = uncompleted_count / task_count * 100
        overdue_percent = overdue_count / task_count * 100
    
    #Writes the report in a new file 'task_overview.txt' in a presentable way
    with open('task_overview.txt', 'w') as f4:
        f4.write(f'''Total number of tasks: {task_count}
Total number of completed tasks: {completed_count}
Total number of uncompleted tasks: {uncompleted_count}
Total number of overdue tasks: {overdue_count}
Percentage of tasks that are incomplete: {uncompleted_percent}%
Percentage of tasks that are overdue: {overdue_percent}%''')

    #Counts the number of users
    with open('user.txt', 'r') as f1:
        user_count = 0
        for line in f1:
            user_count += 1
    
    #Generates and opens new file 'user_overview.txt'
    f3 = open('user_overview.txt', 'w')

    #Writes the user and task count in the new file
    f3.writelines(f"Total number of users: {user_count}\n")
    f3.writelines(f"Total number of tasks: {task_count}\n")

    #For each user, the status of their task/s is checked
    with open('tasks.txt', 'r') as f2:
        contents = f2.readlines()
        enumerate(contents)
        for key in user_dict.keys():
            u_tasks = 0
            u_uncompleted = 0
            u_overdue = 0
            for i in range(0, len(contents)):
                task_list = contents[i].split(", ")
                todays_date = datetime.today()
                due_date = datetime.strptime(task_list[4], "%d %b %Y")
                if key == task_list[0]:
                    u_tasks += 1
                    if task_list[5].strip("\n") == "No":
                        u_uncompleted += 1
                        if due_date < todays_date:
                            u_overdue += 1
            
            u_completed = u_tasks - u_uncompleted
            if u_tasks == 0:
                u_tasks_percentage = 0
                u_completed_percentage = 0
                u_uncompleted_percentage = 0
                u_overdue_percentage = 0
            else:
                u_tasks_percentage = u_tasks / task_count * 100
                u_completed_percentage = u_completed / u_tasks * 100
                u_uncompleted_percentage = u_uncompleted / u_tasks * 100
                u_overdue_percentage = u_overdue / u_tasks * 100
            
            #Writes the report in 'user_overview.txt' in a presentable way
            f3.writelines(f"{key} - Task count: {u_tasks}, Percentage of tasks: {u_tasks_percentage}%, Percentage complete: {u_completed_percentage}%, Percentage incomplete: {u_uncompleted_percentage}%, Percentage overdue: {u_overdue_percentage}%\n")            

    f3.close() #Closes the file


#Function that allows the admin to see statistics
def stats():
    with open('task_overview.txt', 'r') as f2:
        for line in f2:
            print(line)

    print("\n")

    with open('user_overview.txt', 'r') as f1:
        for line in f1:
            print(line)



#Menu screen for admin
while login == "admin":
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
s - statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
    
    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr':
        generate_reports()

    elif menu == 's':
        stats()

    #Ends program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #Prints message if option from menu screen wasn't selected
    else:
        print("You have made a wrong choice, Please Try again")

#Menu screen for all other users 
while login != "admin":
    menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
        
    elif menu == 'vm':
        view_mine()

    #Ends program
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #Prints message if option from menu screen wasn't selected
    else:
        print("You have made a wrong choice, Please Try again")
