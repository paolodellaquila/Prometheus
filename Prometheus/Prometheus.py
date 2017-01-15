# Prometheus text editor to describe all programming days

# module
import sys
from datetime import datetime
import os.path
import os
import json
# ----------------------function----------------------

# modify number of day in json
def update_json_day(day):
    # open config.json file (read)
    with open("config.json", "r") as data_file:
        data = json.load(data_file)
        data["Day"] = str(day)

    # open config.json file (write)
    with open("config.json", "w") as data_file:
        data_file.write(json.dumps(data))

    # close
    data_file.close()


# load user data from json
def data_json():
    # open config.json file(read)
    with open("config.json", "r") as data_file:
        data = json.load(data_file)
        # open in (a) file with progress
        with open("log.md", "a") as prometheus_file:
            # Date
            date = datetime.now()
            day = int(data["Day"])
            day += 1
            prometheus_file.write(
                "### ----------Day " + "[" + data["Day"] + "]" + " on Date " + "(" + str(date.day) + "/" + str(
                    date.month) + "/" + str(date.year) + ")" + "----------" + "\n\n")

            # call update_json_day
            update_json_day(day)

            # Name and Surname
            prometheus_file.write(
                "* [Name] - " + data["Name"] + "\n\n" + "* [Surname] - " + data["Surname"] + "\n\n")

        # close json
        data_file.close()
        #close file
        prometheus_file.close()

#rewrite_check
def rewrite():
    check_response = False
    while check_response == False:
        response = input ("Rewrite Progress?(yes/no): ").lower()
        if response == "yes" or response == "no":
            if response == 'yes':
                return False
            else:
                return True
        else:
            print("\n wrong action")

# load data from user input
def data_user():
    # open in (a) file with progress
    with open("log.md", "a") as prometheus_file:
        # Progress
        check_response = False
        while check_response == False:
            progress = input("Write your progress: ").lower()
            check_response = rewrite()
        # Thought
        check_response = False
        while check_response == False:
            thought = input("Write your thought: ").lower()
            check_response = rewrite()
        # Link
        check_response = False
        while check_response == False:
            link = input("Write your link: ").lower()
            check_response = rewrite()

        # write from progress to link on file in markdown sintax
        prometheus_file.write(
            "* [Progress] - " + " " + progress + "\n\n" + "* [Thought] - " + " " + thought + "\n\n" + "* [Link] - " + " " + link + "\n\n\n")

        # tweet
        print(
            "https://twitter.com/intent/tweet/?text=" + " " + "Progress :" + " " + progress + " " + "Thought :" + " " + thought +
            " " + "Link :" + " " + link + " " + " " + "100daysofcode")

    print("\n\nOpen this link on browser to send tweet\n\n")

    #close file
    prometheus_file.close()

def push():
    path = os.path.abspath('Prometheus')
    commit = str(input("\n\nInsert commit: "))
    os.system("cd/" + path)
    os.system("git add .")
    os.system("git commit -m" + "\"" + commit + "\"")
    os.system("git push")

# add all progress to file
def add():

    """format log's day:
    *** ------------------------------------Day [N] on Date (current date)------------------------------------|

    * [Name] - (user data)

    * [Surname] - (user data)
                                      ------from json
    * [Progress] - (Current Progress)

    * [Thoughts] - (Thoughts)

    * [Links] - (Link to the project)

                                      ------from user
    """

    # data from json
    data_json()

    # data from user
    data_user()

    #push on repo
    push()

    print("\nOk... all things have been saved. Now we'll push on repo...\n")


# read all file and print
def read_a():
    if os.path.exists("log.md") == False:
        print("You haven't write yet")
    else:
        with open("log.md", "r") as prometheus_file:
            print(prometheus_file.read())


# read and print specific progress
def help():
    print (
        "\n     prometheus.py:                           open the complete interface of the tool\n" +
        "\n     prometheus.py add:                       add progress to file and push on repo\n" +
        "\n     prometheus.py read_a:                    read all file and print contens on screen\n")
# menu function
def menu(topic):
    if topic == "add":
        add()
    elif topic == "read_a":
        read_a()
    elif topic == "help":
        help()


# ----------------------main----------------------
if len(sys.argv) == 1:

    print("\nWelcome to Prometheus: Python text editor\n")

    print("You can: \n"
          "- (Add) new thing\n"
          "- (Read_A) all file\n"
          "- (Help) show possible command\n\n")

    check_topic = False

    while check_topic == False:
        topic = input("What do you want to do?").lower()
        if topic == "add" or topic == "read_a" or topic == "help":
            check_topic = True
        else:
            print("\nwrong action")
    # call menu
    menu(topic)
else:
    if sys.argv[1].lower() == "add" or sys.argv[1].lower() == "read_a" or sys.argv[1].lower() == "help":
        # call menu
        menu(sys.argv[1].lower())
    else:
        print("\ncommand not found")
