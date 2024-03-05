def task_1(mentors) -> str:
    all_techers_name = set([teacher.split(" ")[0] for mentor in mentors for teacher in mentor])
    all_names_sorted = sorted(all_techers_name)
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'