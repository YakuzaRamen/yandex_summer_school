import csv

vacancies = {}
applicants = []
finalists = []

# Чтение входных данных
with open('/path/to/input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    read_mode = 0  # режим чтения (вакансии = 1, кандидаты = 2)
    for row in csv_reader:
        if len(row) == 1:
            read_mode += 1
            continue
        if read_mode == 1:  # вакансии
            vacancies[row[0]] = int(row[1])
        if read_mode == 2:  # кандидаты
            applicants.append({
                'name': row[0],
                'job_request': row[1],
                'task_count': int(row[2]),
                'penalty': int(row[3]),
            })

# Отбор кандидатов
for applicant in sorted(applicants, key=lambda x: (-x['task_count'], x['penalty'])):
    if vacancies.get(applicant['job_request'], 0) > 0:
        finalists.append(applicant['name'])
        vacancies[applicant['job_request']] = vacancies[applicant['job_request']] - 1

# Вывод финалистов в алфавитном порядке
for name in sorted(finalists):
    print(name)

passed()
