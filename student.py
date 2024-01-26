class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = {}
    def enroll(self, course):
        if course.course_code not in self.enrolled_courses:
            self.enrolled_courses[course.course_code] = Enrollment(self, course)
            print(f"{self.name} enrolled in {course.course_name}")
    def assign_grade(self, course, grade):
        if course.course_code in self.enrolled_courses:
            self.enrolled_courses[course.course_code].assign_grade(grade)
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")
    def calculate_gpa(self):
        total_credit_points = 0
        total_credits = 0
        for enrollment in self.enrolled_courses.values():
            credit_points, credits = enrollment.calculate_credit_points()
            total_credit_points += credit_points
            total_credits += credits
        if total_credits == 0:
            return 0.0
        else:
            return total_credit_points / total_credits
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None
    def assign_grade(self, grade):
        self.grade = grade
        print(f"Grade {grade} assigned to {self.student.name} for {self.course.course_name}")
    def calculate_credit_points(self):
        if self.grade is None:
            return 0,0
        credit_points = self.course.credit_hours * self.grade_to_point(self.grade)
        return credit_points, self.course.credit_hours
    def grade_to_point(self, grade):
        if grade == 'A':
            return 4.0
        elif grade == 'B':
            return 3.0
        elif grade == 'C':
            return 2.0
        elif grade == 'D':
            return 1.0
        else:
            return 0.0
if __name__ == "__main__":
    math_course = Course("MATH101", "Mathematics", 3)
    physics_course = Course("PHYS101", "Physics", 4)
    cs_course = Course("CS101", "Computer Science", 3)
    student1 = Student(1, "John Doe")
    student2 = Student(2, "Jane Smith")
    student1.enroll(math_course)
    student1.enroll(physics_course)
    student2.enroll(cs_course)
    student1.assign_grade(math_course, 'A')
    student1.assign_grade(physics_course, 'B')
    student2.assign_grade(cs_course, 'C')
    gpa1 = student1.calculate_gpa()
    gpa2 = student2.calculate_gpa()
    print(f"{student1.name}'s GPA: {gpa1:.2f}")
    print(f"{student2.name}'s GPA: {gpa2:.2f}")