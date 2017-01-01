# Prometheus text editor to describe all programming days

# module
import sys
from pip._vendor.distlib.compat import raw_input
from datetime import datetime
import os.path
import json
import twitter
# ----------------------function----------------------

#add all progress to file
def add():
    # open or create file with progress
    with open("prometheus.txt", "a") as prometheus_file:

        """format log's day:
        |------------------------------------Day n------------------------------------|
        |
        |Name and Username (user data)
        |
        |Nickname (nickanme twitter)
        |
        |Date (current date)
        |
        |Progress (Current Progress)
        |
        |Thoughts (Thoughts)
        |
        |Links (Link to the project)
        |
        |------------------------------------------------------------------------------|
        """
        #open config.json file
        with open("config.json") as data_file:
            data = json.load(data_file)

            # day
            """................................."""

            #Name and Surname
            prometheus_file.write("Name: " + data["Name"] + "\n")
            prometheus_file.write("\n")
            prometheus_file.write("Surname: " + data["Surname"] + "\n")
            prometheus_file.write("\n")

            #Nickname
            prometheus_file.write("Nickname: " + data["Nickname"] + "\n")
            prometheus_file.write("\n")

            # Date
            date = datetime.now()
            prometheus_file.write("Day" + " " + "(" + str(date.day) + "/" + str(date.month) + "/" + str(date.year) + ")\n")
            prometheus_file.write("\n")

        # Progress
        check_progress = False
        while check_progress == False:
            check_response = False
            progress = raw_input("Write your progress: ")
            progress.lower()
            while check_response == False:
                response = raw_input("Rewrite progress? (yes/no): ")
                response.lower()
                if response == "yes" or response == "no":
                    check_response = True
                else:
                    print("wrong action")
            if response == "no":
                check_progress = True

        prometheus_file.write("Progress :" + " " + progress + "\n")
        prometheus_file.write("\n")

        # Thought
        check_thought = False
        while check_thought == False:
            check_response = False
            thought = raw_input("Write your thought: ")
            progress.lower()
            while check_response == False:
                response = raw_input("Rewrite thought? (yes/no): ")
                response.lower()
                if response == "yes" or response == "no":
                    check_response = True
                else:
                    print("wrong action")
            if response == "no":
                check_thought = True

        prometheus_file.write("Thought :" + " " + thought + "\n")
        prometheus_file.write("\n")

        # Link
        check_link = False
        while check_link == False:
            check_response = False
            link = raw_input("Write your link: ")
            progress.lower()
            while check_response == False:
                response = raw_input("Rewrite link? (yes/no): ")
                response.lower()
                if response == "yes" or response == "no":
                    check_response = True
                else:
                    print("wrong action")
            if response == "no":
                check_link = True

        prometheus_file.write("Link :" + " " + link + "\n")
        prometheus_file.write("\n\n")

        #tweet
        if(data["Username_twitter"]!= " " and data["Password_twitter"]!= " "):
            tweet=twitter.Api(username=data["Username_twitter"], password=data["Password_twitter"])
            update=tweet.PostUpdate(prometheus_file.read())

        #close file
        prometheus_file.close()

#read all file and print
def read_a():
        if os.path.exists("prometheus.txt") == False:
            print("non hai mai scritto nulla")
        else:
            with open("prometheus.txt", "r") as prometheus_file:
               print(prometheus_file.read())

#read and print specific progress
def read_s():
        if os.path.exists("prometheus.txt") == False:
            print("non hai mai scritto nulla")




#menu function
def menu(topic):
    if topic == "add":
        add()
    elif topic == "read_a":
        read_a()
    elif topic == "read_s":
        read_s()
    
# ----------------------main----------------------
if len(sys.argv) == 1:

    print("Welcome to Prometheus: Python text editor\n")

    print("You can: \n"
          "- (Add) new thing\n"
          "- (Read_A) all file\n"
          "- (Read_S) specify thing\n\n")

    check_topic = False

    while check_topic == False:
        sys.argv[1] = raw_input("What do you want to do?")
        sys.argv[1].lower()
        if sys.argv[1] == "add" or sys.argv[1] == "read_a" or sys.argv[1] == "read_s":
            check_topic = True
        else:
            print("wrong action")
else:
    # call menu
    menu(sys.argv[1])
