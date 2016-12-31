#Prometheus text editor to describe all programming days

#module
import sys
from pip._vendor.distlib.compat import raw_input
from datetime import datetime

#----------------------function----------------------
def menu (topic):
    if topic == "add":

        #open or create the file
        with open("prometheus.txt","a") as prometheus_file:

            """format log's day:
            |------------------------------------Day n------------------------------------|
            |
            |-Date (current date)
            |
            |-Progress (Current Progress)
            |
            |-Thoughts (Thoughts)
            |
            |-Links (Link to the project)
            |
            |------------------------------------------------------------------------------|
            """
            #day
            """................................."""

            #Date
            date = datetime.now()
            prometheus_file.write("Day" + " " + "(" + str(date.day) + " " + str(date.month) + " " + str(date.year) + ")\n")
            prometheus_file.write("\n")

            #Progress
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

            #Thought
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

            #Link
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

            prometheus_file.write("Thought :" + " " + link + "\n")
            prometheus_file.write("\n\n")





#----------------------main----------------------
if len(sys.argv) == 1:

    print ("welcome to Prometheus: Python text editor\n")

    print ("You can: \n"
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
    #call menu
     menu(sys.argv[1])
