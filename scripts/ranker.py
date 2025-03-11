from PyQt6.QtWidgets import QWidget, QGroupBox, QVBoxLayout, QLabel, QTextEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt

# Potential future adds:

class ListRanker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List Ranker")

        self.inputList = [
            "Apple", "Orange", "Grape", "Banana", 
            "Pineapple", "Mango", "Pomegranate", "Watermelon"
        ]

        # Input Section
        input_group = QGroupBox("Input List")
        input_layout = QVBoxLayout()

        self.instructionsLabel = QLabel("Enter all list items (comma or return delimited):")
        self.listInput = QTextEdit()
        self.listInput.setPlaceholderText("Item 1, Item 2, Item 3")

        self.setListButton = QPushButton("Set List")
        self.setListButton.setFixedSize(200, 30)
        #self.setListButton.clicked.connect(self.updateList)

        input_layout.setSpacing(10)
        input_layout.addWidget(self.instructionsLabel)
        input_layout.addWidget(self.listInput)
        input_layout.addWidget(self.setListButton, alignment=Qt.AlignmentFlag.AlignCenter)
        input_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_group.setLayout(input_layout)

        # Output Section
        output_group = QGroupBox("Ranker and Output")
        output_layout = QVBoxLayout()

        ranking_section = QWidget()
        ranking_layout = QHBoxLayout()

        self.optionOneButton = QPushButton("Option 1", ranking_section)
        self.optionOneButton.setFixedSize(200, 50)
        self.optionTwoButton = QPushButton("Option 2", ranking_section)
        self.optionTwoButton.setFixedSize(200, 50)
        ranking_layout.addWidget(self.optionOneButton)
        ranking_layout.addWidget(self.optionTwoButton)
        ranking_section.setLayout(ranking_layout)

        output_layout.setSpacing(10)
        output_layout.addWidget(ranking_section)
        output_group.setLayout(output_layout)

        # Parent Layout
        layout = QVBoxLayout()

        layout.addWidget(input_group)
        layout.addSpacing(10)
        layout.addWidget(output_group)

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Apply layout
        self.setLayout(layout)


# # Bubble sort for smaller lists

# def bubble_sort(items):
#     total = len(items)
#     rankedList = items[:]

#     for i in range(total):
#         for j in range (total - i - 1):
#             print(f"A: {rankedList[j]} or B: {rankedList[j+1]}")
#             choice = input(" A OR B: ").strip().upper()
#             if choice == 'B':
#                 rankedList[j], rankedList[j+1] = rankedList[j+1], rankedList[j]
#             elif choice != 'A':
#                 print ("Invalid")
#                 return bubble_sort(items)
            
#     return rankedList

# # Merge or quick sort for larger lists

# def merge_sort(items):

#     if len(items) <= 1:
#         return items

#     # Split the list
#     mid = len(items) // 2
    
#     # Recursively sort both halves
#     left = merge_sort(items[:mid])
#     right = merge_sort(items[mid:])

#     # Merge sorted halves
#     merged = merge(left, right)
#     return merged

# def merge(left, right):
#     result = []
#     i = j = 0

#     # Comparison
#     while i < len(left) and j < len(right):
#         print(f"\n1: {left[i]} or 2: {right[j]}")
#         choice = input("1 or 2: ").strip()
#         if choice == '1':
#             result.append(left[i])
#             i += 1
#         elif choice == '2':
#             result.append(right[j])
#             j += 1
#         else:
#             print("Invalid choice, try again.")

#     # Append remaining elements from left and right
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# # Script running
# if __name__ == "__main__":
#     while True:
#         input_list = [
#             "Apple", "Orange", "Grape", "Banana", 
#             "Pineapple", "Mango", "Pomegranate", "Watermelon"
#         ]

#         choice = input("(S)mall or (L)arge list?: ").strip().upper()
#         if choice == 'S':
#             rankedList = bubble_sort(input_list)
#         elif choice == 'L':
#             rankedList = merge_sort(input_list)
        

#         print("\nFinal Ranked List:")
#         print("Ranked list: ", rankedList)