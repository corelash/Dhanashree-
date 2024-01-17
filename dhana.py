students = [
    {"name": "Amit Shar", "subjects": [
        {"name": "English", "total_marks": 100, "scored_marks": 60},
        {"name": "Hindi", "total_marks": 100, "scored_marks": 70},
        {"name": "Math 1", "total_marks": 70, "scored_marks": 40},
        {"name": "Math 2", "total_marks": 70, "scored_marks": 60},
        {"name": "Science", "total_marks": 100, "scored_marks": 80}
    ]},
    {"name": "manish", "subjects": [
        {"name": "English", "total_marks": 100, "scored_marks": 60},
        {"name": "Hindi", "total_marks": 100, "scored_marks": 70},
        {"name": "Math 1", "total_marks": 70, "scored_marks": 40},
        {"name": "Math 2", "total_marks": 70, "scored_marks": 60},
        {"name": "Science", "total_marks": 100, "scored_marks": 40}
    ]},
    {"name": "sunil", "subjects": [
        {"name": "English", "total_marks": 100, "scored_marks": 50},
        {"name": "Hindi", "total_marks": 100, "scored_marks": 70},
        {"name": "Math 1", "total_marks": 70, "scored_marks": 70},
        {"name": "Math 2", "total_marks": 70, "scored_marks": 35},
        {"name": "Science", "total_marks": 100, "scored_marks": 80}
    ]},
    {"name": "Anuja", "subjects": [
        {"name": "English", "total_marks": 100, "scored_marks": 60},
        {"name": "Hindi", "total_marks": 100, "scored_marks": 70},
        {"name": "Math 1", "total_marks": 70, "scored_marks": 40},
        {"name": "Math 2", "total_marks": 70, "scored_marks": 60},
        {"name": "Science", "total_marks": 100, "scored_marks": 80}
    ]},{"name": "sayali", "subjects": [
        {"name": "English", "total_marks": 100, "scored_marks": 40},
        {"name": "Hindi", "total_marks": 100, "scored_marks": 70},
        {"name": "Math 1", "total_marks": 70, "scored_marks": 30},
        {"name": "Math 2", "total_marks": 70, "scored_marks": 60},
        {"name": "Science", "total_marks": 100, "scored_marks": 70}
    ]},{"name": "Amit Shar", "subjects": [
        {"name": "English", "total_marks": 100, "scored_marks": 60},
        {"name": "Hindi", "total_marks": 100, "scored_marks": 90},
        {"name": "Math 1", "total_marks": 70, "scored_marks": 80},
        {"name": "Math 2", "total_marks": 70, "scored_marks": 60},
        {"name": "Science", "total_marks": 100, "scored_marks": 80}
    ]},
    {"name": "neeraj", "subjects": [
        {"name": "English", "total_marks": 100, "scored_marks": 60},
        {"name": "Hindi", "total_marks": 100, "scored_marks": 50},
        {"name": "Math 1", "total_marks": 70, "scored_marks": 40},
        {"name": "Math 2", "total_marks": 70, "scored_marks": 20},
        {"name": "Science", "total_marks": 100, "scored_marks": 80}
    ]},
    # Add more students here
]

# Function to calculate the total marks scored by a student
def calculate_total_marks(student):
    total_marks = 0
    for subject in student["subjects"]:
        total_marks += subject["total_marks"]
    return total_marks

# Function to calculate the marks scored by a student in all subjects
def calculate_scored_marks(student):
    scored_marks = 0
    for subject in student["subjects"]:
        scored_marks += subject["scored_marks"]
    return scored_marks

# Function to sort the students based on the total marks scored
def sort_students(students):
    return sorted(students, key=lambda student: calculate_total_marks(student), reverse=True)

# Function to get the top N students
def get_top_students(students, n):
    sorted_students = sort_students(students)
    return sorted_students[:n]

# Get the top 5 students
top_5_students = get_top_students(students, 5)

# Print the top 5 students
for i, student in enumerate(top_5_students, 1):
    print(f"{i}. {student['name']} - Total Marks: {calculate_total_marks(student)}, Scored Marks: {calculate_scored_marks(student)}")


