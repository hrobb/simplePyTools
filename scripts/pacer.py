from PyQt6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QLabel, QTimeEdit, QTextEdit, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt

class Pacer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pacer")

        # Input Section
        input_group = QGroupBox("Input")
        input_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        self.startTimeLabel = QLabel("Start Time:")
        self.startTime = QTimeEdit()
        row1.addWidget(self.startTimeLabel)
        row1.addWidget(self.startTime)

        row2 = QHBoxLayout()
        self.endTimeLabel = QLabel("End Time:")
        self.endTime = QTimeEdit()
        row2.addWidget(self.endTimeLabel)
        row2.addWidget(self.endTime)

        self.reps = QTextEdit()

        input_layout.setSpacing(10)
        input_layout.addLayout(row1)
        input_layout.addLayout(row2)
        input_layout.addWidget(self.reps)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_group.setLayout(input_layout)

        # Output Section
        output_group = QGroupBox("Output")
        output_layout = QVBoxLayout()

        action_section = QWidget()
        action_layout = QHBoxLayout()
        self.checkButton = QPushButton("Check Progress", action_section)
        #
        self.addButton = QPushButton("Increment", action_section)
        #
        action_layout.addWidget(self.checkButton)
        action_layout.addWidget(self.addButton)

        self.outputBox = QTextEdit()
        self.outputBox.setReadOnly(True)

        output_layout.setSpacing(10)
        output_layout.addWidget(action_section)
        output_layout.addWidget(self.outputBox)
        output_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        output_group.setLayout(output_layout)

        # Parent Layout
        layout = QVBoxLayout()

        layout.addWidget(input_group)
        layout.addSpacing(10)
        layout.addWidget(output_group)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Apply Layout
        self.setLayout(layout)





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