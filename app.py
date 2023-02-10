import random
from functions import generate_csv, generate_initials, generate_random_length_random_list, get_count, get_random_name, random_day


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
	curriculum_count = get_count("Curriculum Count:")
	period_schedule_count = get_count("Period Schedule Count:")
	room_count = get_count("Room Count:")
	student_count = get_count("Student Count:")
	subject_count = get_count("Subject Count:")
	teacher_count = get_count("Teacher Count:")
	teacher_type_count = get_count("Teacher Type Count:")

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

	student_fields = [
		"id", # int quoted e.g. "1"
		"firstName", # str
		"middleNames", # str
		"surname", # str
		"initials" # str
	]
	student_data = []

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
		first_name = get_random_name("first_names.txt")
		middle_name = get_random_name("middle_names.txt")
		last_name = get_random_name("last_names.txt")
		teacher_data.append([
			i + 1,
			first_name,
			middle_name,
			last_name,
			generate_initials(first_name, middle_name, last_name),
			random.randint(1, teacher_type_count + 1),
			generate_random_length_random_list(),
			generate_random_length_random_list()
		])
	generate_csv("Teacher.csv", ["id", "firstName", "middleName", "surname", "initials", "teacherTypeID", "subjectTaughtIDs", "roomTaughtIDs"], teacher_data)

	teacher_type_fields = [
		"id", # int
		"name", # str
		"displayName" # str
	]
	teacher_type_data = []

if __name__ == "__main__":
	main()