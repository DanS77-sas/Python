# Write your solution here
def exam_exercises():
    exam_point = []
    exercises_complete = []

    while True:
        result = input("Exam points and exercises completed: ")
        if len(result) == 0:
            break

        parts = result.split()
        exam_point.append(int(parts[0]))
        exercises_complete.append(int(parts[1]))

    return exam_point, exercises_complete

def convert_exercise_point(excercises_complete : list):
    converted_points = []

    for points in excercises_complete:
        converted_points.append(points // 10)

    return converted_points

def final_grade(exam_point, converted_points):
    grades = []
    total_points = 0
    for x, y in zip(exam_point, converted_points):
        points = x + y
        total_points += points

        if x < 10:
            grade = 0
        elif points <= 14:
            grade = 0
        elif points <= 17:
            grade = 1
        elif points <= 20:
            grade = 2
        elif points <= 23:
            grade = 3
        elif points <= 27:
            grade = 4
        else:
            grade = 5

        grades.append(grade)

    return grades, total_points
    
def statistics(grades, total_points):
    print("Statistics: ")
    mean = total_points / (len(grades))
    print(f"Points average: {mean:.1f}")


    counter = 0
    for grade in grades:
        if grade > 0:
            counter += 1
    
    pass_rate = (counter / len(grades)) * 100
    print(f"Pass percentage: {pass_rate:.1f}")

    #Grade distribution
    grade_count = [0] * 6
    
    for grade in grades:
        grade_count[grade] += 1

    print("Grade distribution: ")
    for grade in range(5, -1, -1):
        print(f"  {grade}: {'*' * grade_count[grade]}")

def main():
    points, exercises = exam_exercises()
    converted_exercises = convert_exercise_point(exercises)
    grades, total_points = final_grade(points, converted_exercises)
    statistics(grades, total_points)

main()