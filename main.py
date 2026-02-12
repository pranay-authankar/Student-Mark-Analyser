


# Student class with calculations mathods
class Student:
    def __init__(self, roll, name, marks):
        self.roll = int(roll)
        self.name = name
        self.marks = []
        for mark in marks:
            self.marks.append(int(mark))
        self.subjects = len(self.marks)

    def total(self):
        return sum(self.marks)
    
    def avg(self):
        return float(f"{(self.total() / self.subjects):.2f}")
    
    def grade(self):

        if self.avg() >= 85:
            return "A"
        elif 60 <= self.avg() < 85:
            return "B"
        elif 40 <= self.avg() < 60:
            return "C"
        elif 28 <= self.avg() < 40:
            return "D"
        else:
            return "E"
    
    def verdict(self):
        return "Fail" if self.grade() == "E" else "Pass"

# takes raw file and covert it into python list (matrix) to perform operations
def txt_to_py(file_name): # returns students matrix

    try:
        # Opens raw student's file
        with open(file_name, "r") as f:
            reader = f.readlines()

    except FileNotFoundError:
        return False
    else:
        #Extracting data from txt to local python file as matrix
        students_matrix = []

        # each line represents ONE student's data
        for line in reader:
            line = line.strip()
            one_student = line.split(",")
            students_matrix.append(one_student)
        return students_matrix

# Helping Function - Appends a line in txt file, having python strings
def append_line_to_file(file_name, line_as_list):
    list_string = []
    for line in line_as_list:
        list_string.append(f"{line}")
    with open(file_name, "a") as f:
        f.write(",".join(list_string) + "\n")

# * performs operations with valid entries and store info as objects
def data_to_objects(valid_filename): # returns student's object list

    students_list = []
    try:
        student_matrix = txt_to_py(valid_filename)
        for student in student_matrix:
            #datatype conversion
            roll = int(student[0])
            name = student[1]
            subjects_list = student[2:]
            
            # creating object of student
            students_list.append(Student(roll, name, subjects_list))
    except TypeError:
        print("Valid-entries not found")
    else:
        

        # student's as objects list
        return students_list 

def check_string(string):
    if string.strip() == "":
        return False
    else:
        return True

# * differentiate between valid / non-valid entries
def validate_rawdata(raw_filename, valid_filename, invalid_filename, no_of_subjects):

    student_matrix = txt_to_py(raw_filename)
    valid_matrix = []
    unique_roll = set({})
    subjects_list = []
    student_length = no_of_subjects + 2
    

    for student in student_matrix:
        try:
            if len(student) != student_length:
                raise IndexError
            
            if int(student[0]) not in unique_roll:
                student[0] = int(student[0]) 
            else:
                raise ValueError

            if not check_string(student[1]):
                raise ValueError
            
            subjects_list = student[2:student_length]
            for subject in subjects_list:
                subject = int(subject)
                if not 0 <= subject <= 100:
                    raise ValueError
                
        except (ValueError, IndexError):
            append_line_to_file(invalid_filename, student)

            
        else:
            unique_roll.add(student[0])
            valid_matrix.append(student)
            append_line_to_file(valid_filename, student)

    student_object_list = data_to_objects(valid_filename)
    if student_object_list != []:
        return student_object_list
    else:
        return False

# Helping Function - formatting tool to center align text
def center_align(text, size, filler, last):
    text = str(text)
    print(text.center(size, filler), end = last)

# Helping variable - while displaying result
headings = ["Roll.no", "Name", "Total", "Average", "Grade", "Verdict"]

# Helping Function - insert row in table
def insert_newdata(row_data_list, size, last):
    for data in row_data_list:
        center_align(data, size, " ", last)
    print()

# Helping Function - insert border
def insert_borders(no_of_cells, size, char, fill, last):
    for x in range(0, no_of_cells):
        center_align(char, size, fill, last)
    print()

# Helping Function - Creates proper formatted table
def table_formatting(headings, student_object_list, size, last):
    insert_borders(len(headings), size, "=", "=", last)
    insert_newdata(headings, size, "|")
    insert_borders(len(headings), size, "=", "=", last)

    for student in student_object_list:
        insert_newdata([student.roll, student.name, student.total(), student.avg(), student.grade(), student.verdict()], size, last)
        insert_borders(len(headings), size, "-", "-", last)

    insert_borders(len(headings), size, "=", "=", last)

# * Helping Function - Checks raw_file, valid/invalid
def check_all_file_status(raw_filename, valid_filename, invalid_filename, no_of_subjects):
    validate_rawdata(raw_filename, valid_filename, invalid_filename, no_of_subjects)
    existing_file = []
    try:
        with open(raw_filename, "r") as f:
            existing_file.append(raw_filename)
    except FileNotFoundError:
        print("Raw Students file NOt found")    
    
    try:
        with open(valid_filename, "r") as f:
            existing_file.append(valid_filename)
    except FileNotFoundError:
        print("Valid Students file NOt found")    
    
    try:
        with open(invalid_filename, "r") as f:
            existing_file.append(invalid_filename)
    except FileNotFoundError:
        print("Not - Valid Students file NOt found")    

    return existing_file

# Function_1 - takes raw file, validate, shows result in tabular form
def display_result(headings, valid_filename):
    
    student_list = data_to_objects(valid_filename)
    table_formatting(headings, student_list, 25, "|")

# Function_2 - Shows invalid entries
def show_not_valid_entries(invalid_filename):
    try:
        students_matrix = txt_to_py(invalid_filename)
        size = 50
        # Table formatting
        insert_borders(1, size, "=", "=", "|")
        insert_newdata(["Roll no. and Name of invalid entries"], size, "|")
        insert_borders(1, size, "=", "=", "|")
    
        for student in students_matrix:
            insert_newdata([f"{student[0]} - {student[1]}"], size, "|")
            insert_borders(1, size, "-", "-", "|")

    # error handling if there are no invalid entries
    except (IndexError, TypeError):
        print("No Invalid entries found !!")
    else:
        
        # tab;e formatting if there are invalid entries
        insert_borders(1, size, "=", "=", "|")
        print()
        insert_borders(1, size, "=", "=", "|")
        insert_newdata(["Their Entries"], size, "|")
        insert_borders(1, size, "=", "=", "|")
        with open(invalid_filename, "r") as f:
            reader = f.readlines()
            for line in reader:
                insert_newdata([line.replace("\n", "")], size, "|")
                insert_borders(1, size, "-", "-", "|")
            insert_borders(1, size, "=", "=", "|")

# Function_3 - Shows Top 3 students
def show_top_3(valid_filename):
    student_objects = data_to_objects(valid_filename)

    try:
        pos_1 = 0
        pos_1_obj = student_objects[0]
        pos_2 = 0
        pos_2_obj = student_objects[1]
        pos_3 = 0
        pos_3_obj = student_objects[2]

    except IndexError:
        print("There are less than 3 students, therefore top 3 couldn't be displayed")
    else:
        for student in student_objects:
            if student.total() > pos_1:
                pos_1 = student.total()
                pos_1_obj = student
        student_objects.remove(pos_1_obj)

        for student in student_objects:
            if pos_2 < student.total() <= pos_1:
                pos_2 = student.total()
                pos_2_obj = student
        student_objects.remove(pos_2_obj)

        for student in student_objects:
            if pos_3 < student.total() <= pos_2:
                pos_3 = student.total()
                pos_3_obj = student
        student_objects.remove(pos_3_obj)


        topper = [pos_1_obj, pos_2_obj, pos_3_obj]

        insert_borders(1, 92, "=", "=", "|")
        center_align("Top - 3", 92, " ", "|\n")
        insert_borders(3, 30, "=", "=", "|")
        insert_newdata(["Position", "Name", "Marks"], 30, "|")
        insert_borders(3, 30, "=", "=", "|")

        i = 1
        for student in topper:
            insert_newdata([i, student.name, student.total()], 30, "|")
            insert_borders(3, 30, "-", "-", "|")
            i += 1
        insert_borders(3, 30, "=", "=", "|")

# Function_4 - takes raw file do operations
def main(raw_filename, valid_filename, invalid_filename, no_of_subjects):
    try:
        open(valid_file, "w").close()
        open(invalid_file, "w").close()
    except FileNotFoundError:
        pass

    existing_files = check_all_file_status(raw_filename, valid_filename, invalid_filename, no_of_subjects)

    if raw_filename in existing_files:
        if valid_filename in existing_files:
            display_result(headings, valid_filename)
            show_top_3(valid_filename)
            

        if invalid_filename in existing_files:
            show_not_valid_entries(invalid_filename)
            
        

# required files
raw_file = "students.txt"
valid_file = "valid-students.txt"
invalid_file = "not_valid_students.txt"
subjects_valid = 10

# Run the program
main(raw_file, valid_file, invalid_file, subjects_valid)

