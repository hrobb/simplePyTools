from PyQt6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QLabel, QTimeEdit, QTextEdit, QHBoxLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
import datetime
import time

# Potential future adds:

class Pacer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pacer")

        self.startTime = datetime.datetime.now()
        self.endTime = datetime.datetime.now()
        self.currentTime = datetime.datetime.now().time()
        self.reps = 0
        self.activeTotal = 0

        # Input Section
        input_group = QGroupBox("Input")
        input_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        self.startTimeLabel = QLabel("Start Time:")
        self.startTimeHolder = QTimeEdit()
        row1.addStretch()
        row1.addWidget(self.startTimeLabel)
        row1.addWidget(self.startTimeHolder)
        row1.addStretch()

        row2 = QHBoxLayout()
        self.endTimeLabel = QLabel("End Time:")
        self.endTimeHolder = QTimeEdit()
        row2.addStretch()
        row2.addWidget(self.endTimeLabel)
        row2.addWidget(self.endTimeHolder)
        row2.addStretch()

        row3 = QHBoxLayout()
        self.repsLabel = QLabel("Number of Sets:")
        self.repsHolder = QLineEdit()
        self.repsHolder.setValidator(QIntValidator())
        self.repsHolder.setFixedWidth(100)
        row3.addStretch()
        row3.addWidget(self.repsLabel)
        row3.addWidget(self.repsHolder)
        row3.addStretch()

        self.beginButton = QPushButton("Begin")
        self.beginButton.setFixedSize(200, 30)
        self.beginButton.clicked.connect(self.startPacer)

        input_layout.setSpacing(10)
        input_layout.addLayout(row1)
        input_layout.addLayout(row2)
        input_layout.addLayout(row3)
        input_layout.addWidget(self.beginButton, alignment=Qt.AlignmentFlag.AlignCenter)
        input_layout.addSpacing(10)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_group.setLayout(input_layout)

        # Output Section
        output_group = QGroupBox("Output")
        output_layout = QVBoxLayout()

        action_section = QWidget()
        action_layout = QHBoxLayout()
        self.checkButton = QPushButton("Check Progress", action_section)
        self.checkButton.setEnabled(False)
        self.checkButton.setFixedSize(200, 50)
        self.checkButton.clicked.connect(self.updateDisplay)
        self.addButton = QPushButton("Increment", action_section)
        self.addButton.setEnabled(False)
        self.addButton.setFixedSize(200, 50)
        self.addButton.clicked.connect(self.incrementActive)
        action_layout.addWidget(self.checkButton)
        action_layout.addWidget(self.addButton)
        action_section.setLayout(action_layout)

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

    def holdingFunc(self, testFunc):
        match testFunc:
            case 1:
                self.outputBox.setText("Check button working")
            case 2:
                self.outputBox.setText("Increment button working")
        
    def startPacer(self):
        if not self.repsHolder.text():
            self.outputBox.setText("Please enter number of sets.")
            return

        self.startTime = self.startTimeHolder.time()
        self.endTime = self.endTimeHolder.time()
        self.reps = int(self.repsHolder.text())
        self.totalTime = self.startTime.secsTo(self.endTime)
        self.calcPace = self.totalTime/self.reps

        if (self.startTime < self.endTime) and self.reps > 0:
            self.beginButton.setEnabled(False)
            self.checkButton.setEnabled(True)
            self.addButton.setEnabled(True)
            self.activeTotal = 0

            self.updateDisplay()
            
        else:
            self.outputBox.setText("Please ensure:\n"
            "- End Time is after Start Time\n"
            "- Number of sets is above 0")

    def updateDisplay(self):
        # Variable calculations
        self.currentTime = datetime.datetime.now().time()
        currentSecs = (self.currentTime.hour * 3600) + (self.currentTime.minute * 60) + self.currentTime.second
        startSecs = (self.startTime.hour() * 3600) + (self.startTime.minute() * 60) + self.startTime.second()
        onPaceFlag = ""
        finishedFlag = "Last Updated: "

        # Calc Average Pace
        avgPace = f"{int(self.calcPace / 3600):02d}:{int((self.calcPace % 3600) / 60):02d}"

        # Calc Current Pace
        if self.activeTotal == 0:
            currentPace = "NULL"
        else:
            currentPaceSecs = int((currentSecs - startSecs) / self.activeTotal)
            currentPace = f"{int(currentPaceSecs / 3600):02d}:{int((currentPaceSecs % 3600) / 60):02d}"

        # On Pace Flag
        if (self.activeTotal == self.reps):
            onPaceFlag = "Congrats! You finished."
            finishedFlag = "Completed At: "
        elif (startSecs + (self.activeTotal * self.calcPace)) > currentSecs:
            onPaceFlag = "On Pace"
        else:
            onPaceFlag = "Falling Behind"

        # Update display
        self.outputBox.setText(self.startTime.toString("HH:mm") + " -> " + self.endTime.toString("HH:mm") + "\n\n" +
        "Average Pace needed: " + avgPace + "\n" +
        "Your Pace: " + currentPace + "\n" +
        "Current Progress: " + onPaceFlag + " (" + str(self.activeTotal) + "/" + str(self.reps) + ")\n\n" +
        finishedFlag + str(time.strftime("%H:%M:%S"))) 
       

    def incrementActive(self):
        self.activeTotal += 1
        self.updateDisplay()
        
        if (self.activeTotal == self.reps):
            self.beginButton.setEnabled(True)
            self.checkButton.setEnabled(False)
            self.addButton.setEnabled(False)
