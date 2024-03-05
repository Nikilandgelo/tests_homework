def task_3(mentors) -> str:
    courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
    durations = [14, 20, 12, 20]

    courses_list = [{"title": course_name, "mentors": course_mentors, "duration": course_duration} for course_name, course_mentors, course_duration in zip(courses, mentors, durations)]
    courses_list.sort(key = lambda dict_: dict_.get("duration"), reverse=True)
    return f'Самый короткий курс(ы): {courses_list[-1].get("title")},\nСамый длинный курс(ы): {courses_list[0].get("title")}'