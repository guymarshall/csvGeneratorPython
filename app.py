import random
from functions import generate_csv, generate_initials, generate_random_length_random_list, get_count, get_names, get_random_name, random_day, random_room, random_teacher_type


csv_fields = {
	"curriculum": [
		"id", # int
		"studentID", # int
		"subjectID", # int
		"numberOfLessonsPerWeek" # int
	],
	"period_schedule": [
		"id", # int
		"dayOfWeek", # ?str?
		"numberOfPeriods" # int
	],
	"room": [
		"id", # int
		"name", # str
		"maximumClassSize", # int
		"subjectsTaught", # ?
		"teachers" # ?
	],
	"student": [
		"id", # int quoted e.g. "1"
		"firstName", # str
		"middleNames", # str
		"surname", # str
		"initials" # str
	],
	"subject": [
		"id", # int
		"subjectName", # str
		"subjectYear", # int
		"set", # int quoted e.g "3"
		"maximumClassSize", # int
		"teachers", # ?
		"roomsTaught" # list[int] quoted e.g. "2, 3, 4, 5"
	],
	"teacher": [
		"id", # int
		"firstName", # str
		"middleNames", # str
		"surname", # str
		"initials", # str
		"teacherType", # int
		"subjectsTaught", # list[int] quoted e.g. "1, 2, 3"
		"roomsTaught" # list[int] quoted e.g. "2, 3, 4, 5"
	],
	"teacher_type": [
		"id", # int
		"name", # str
		"displayName" # str
	],
}

def main():
	print("CSV Generator - Enter counts for the following prompts to generate your .CSV file.")
	curriculum_count = get_count("Curriculum Count: ")
	period_schedule_count = get_count("Period Schedule Count: ")
	room_count = get_count("Room Count: ")
	student_count = get_count("Student Count: ")
	subject_count = get_count("Subject Count: ")
	teacher_count = get_count("Teacher Count: ")
	teacher_type_count = get_count("Teacher Type Count: ")

	curriculum_fields = [
		"id", # int
		"studentID", # int
		"subjectID", # int
		"numberOfLessonsPerWeek" # int
	]
	curriculum_data = []
	for i in range(0, curriculum_count + 1):
		curriculum_data.append([
			i + 1,
			random.randint(1, student_count + 1),
			random.randint(1, subject_count + 1),
			random.randint(1, 10)
		])
	generate_csv("Curriculum.csv", ["id", "studentID", "subjectID", "numberOfLessonsPerWeek"], curriculum_data)

	period_schedule_fields = [
		"id", # int
		"dayOfWeek", # ?str?
		"numberOfPeriods" # int
	]
	period_schedule_data = []
	for i in range(0, period_schedule_count + 1):
		period_schedule_data.append([
			i + 1,
			random_day(),
			random.randint(1, 10)
		])
	generate_csv("PeriodSchedule.csv", ["id", "dayOfWeek", "numberOfPeriods"], period_schedule_data)

	room_fields = [
		"id", # int
		"name", # str
		"maximumClassSize", # int
		"subjectsTaught", # ?
		"teachers" # ?
	]
	room_data = []
	for i in range(0, room_count):
		room_data.append([
			i + 1,
			random_room(),
			random.randint(20, 32),
			# subjectsTaught
			# teachers
		])
	generate_csv("Room.csv", ["id", "name", "maximumClassSize", "subjectsTaught", "teachers"], room_data)

	student_fields = [
		"id", # int quoted e.g. "1"
		"firstName", # str
		"middleNames", # str
		"surname", # str
		"initials" # str
	]
	student_data = []
	for i in range(0, student_count + 1):
		first_name = get_random_name(get_names("first_names.txt"))
		middle_name = get_random_name(get_names("middle_names.txt"))
		last_name = get_random_name(get_names("last_names.txt"))
		student_data.append([
			str(i + 1),
			first_name,
			middle_name,
			last_name,
			generate_initials(first_name, middle_name, last_name)
		])
	generate_csv("Student.csv", ["id", "firstName", "middleName", "surname", "initials"], student_data)

	subject_fields = [
		"id", # int
		"subjectName", # str
		"subjectYear", # int
		"set", # int quoted e.g "3"
		"maximumClassSize", # int
		"teachers", # ?
		"roomsTaught" # list[int] quoted e.g. "2, 3, 4, 5"
	]
	subject_data = []
	for i in range(0, subject_count + 1):
		subject_data.append([
			i + 1,
			# subjectName
			random.randint(1, 5),
			str(random.randint(1, 8)),
			random.randint(20, 32),
			# teachers
			# roomsTaught list(int) quoted e.g. "2, 3, 4, 5"
		])
	generate_csv("Subject.csv", ["id", "subjectName", "subjectYear", "set", "maximumClassSize", "teachers", "roomsTaught"], subject_data)

	teacher_fields = [
		"id", # int
		"firstName", # str
		"middleNames", # str
		"surname", # str
		"initials", # str
		"teacherType", # int
		"subjectsTaught", # list[int] quoted e.g. "1, 2, 3"
		"roomsTaught" # list[int] quoted e.g. "2, 3, 4, 5"
	]
	teacher_data = []
	for i in range(0, teacher_count + 1):
		first_name = get_random_name(get_names("first_names.txt"))
		middle_name = get_random_name(get_names("middle_names.txt"))
		last_name = get_random_name(get_names("last_names.txt"))
		teacher_data.append([
			i + 1,
			first_name,
			middle_name,
			last_name,
			generate_initials(first_name, middle_name, last_name),
			random.randint(1, teacher_type_count + 1),
			", ".join(map(str, generate_random_length_random_list())),
			", ".join(map(str, generate_random_length_random_list()))
		])
	generate_csv("Teacher.csv", ["id", "firstName", "middleName", "surname", "initials", "teacherTypeID", "subjectTaughtIDs", "roomTaughtIDs"], teacher_data)

	teacher_type_fields = [
		"id", # int
		"name", # str
		"displayName" # str
	]
	teacher_type_data = []
	for i in range(0, teacher_type_count + 1):
		teacher_type_data.append([
			i + 1,
			random_teacher_type("name"),
			random_teacher_type("displayName")
		])
	generate_csv("TeacherType.csv", ["id", "name", "displayName"], teacher_type_data)

if __name__ == "__main__":
	main()