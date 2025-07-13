#--------------------------------------------Task:-------------------------------------------------#

# #Write in file named task_best_students_scores.py
# Represent the information given in student_scores table in appropriate data structure.
# From student_scores data, create a new data structure named best_students_scores, storing the information (name and score) only for students with scores greater than 4.00
# Print out the names and scores from best_students_scores

student_scores = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "Georgy": 5.00
}


best_students_scores = {name: score for name, score in student_scores.items() if score > 4.00}


for name, score in best_students_scores.items():
    print(f"{name} - {score:.2f}")
#--------------------------------------------------------------------------------------------------#