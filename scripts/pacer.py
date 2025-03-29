from PyQt6.QtWidgets import QWidget

class Pacer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pacer")

        # Input Section

        # Output Section

        # Parent Layout

        # Apply Layout






# import datetime

# exitFlag = 0

# startTime = datetime.datetime.now()
# endTime = datetime.datetime.now()
# startTimeVal = input("What time are you starting?    ")
# endTimeVal = input("What time do you want to finish up?    ")

# startTime = startTime.replace(hour=int(startTimeVal), minute=0, second=0, microsecond=0)
# endTime = endTime.replace(hour=int(endTimeVal), minute=0, second=0, microsecond=0)
# totalTime = endTime-startTime

# desiredTotal = 0
# activeTotal = 0
# desiredTotal = int(input("How many sets are you doing?    "))
# calcPace = totalTime/desiredTotal

# def calcRemainingTime(endTime):
#     currTime = datetime.datetime.now()
#     currTime = currTime.replace(microsecond=0)
#     final = endTime-currTime
#     return final

# def onPace():
#     if (startTime+(activeTotal*calcPace) > datetime.datetime.now()):
#         return "You are on pace"
#     else:
#         return "You're falling behind"

# while (exitFlag != 1): 
#     inVal = input("\nCheck, Add, Exit:    ")

#     if inVal == "Check":
#         if (activeTotal >= desiredTotal):
#             print("Congrats, you're done for the day!")
#         else:
#             print("You have completed " + str(activeTotal) + " out of " + str(desiredTotal) + " sets.")
#             print("You have " + str(calcRemainingTime(endTime)) + " remaining.")
#             print(onPace())
#     elif inVal == "Add":
#         activeTotal+=1
#     elif inVal == "Exit":
#         exitFlag = 1