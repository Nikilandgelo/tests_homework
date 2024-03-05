def task2(mentors) -> str:
    all_techers_name = [teacher.split(" ")[0] for mentor in mentors for teacher in mentor]
    all_unique_techers_name = set(all_techers_name)
    teacher_names_counter = [[name, all_techers_name.count(name)] for name in all_unique_techers_name]
    teacher_names_counter.sort(key=lambda teacher: (teacher[1], teacher[0]), reverse= True)
    
    top_3 = ""
    for top in teacher_names_counter[:3]:
        top_3 += f"{top[0]}: {top[1]} раз(а), "
    return top_3.rstrip(", ")