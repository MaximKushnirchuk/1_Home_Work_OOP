''' Задача про классный журнал '''

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses_finished(self, course_name):
        if course_name not in self.finished_courses :
            self.finished_courses.append(course_name)   
        else : print('Такой курс уже добавлен')

    def add_courses_progress(self, course_name):
        if course_name not in self.courses_in_progress :
            self.courses_in_progress.append(course_name)   
        else : print('Такой курс уже добавлен')

    def rate_to_lector(self, lector, cours, rate) :
        if cours in lector.courses_attached and cours in self.courses_in_progress :
            if cours in lector.rate_for_lectures :
                lector.rate_for_lectures[cours] += [rate]
            else : lector.rate_for_lectures[cours] = [rate]
        else :
            return print('Ошибка!! Либо курс не тот, либо лектор')
    
    def middle_rate(self) :
        con_rate = 0
        sum_rate = 0
        for i in self.grades.values() :
            for i2 in i :
                con_rate += 1
                sum_rate += i2
        res = sum_rate / con_rate
        return res        

    def __str__(self) :
            res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self.middle_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
            return res

    def __lt__(self, second) :
        if not isinstance(second, Student) :
            print('Данные классы не сравнить!!')
            return
        return self.middle_rate() < second.middle_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def add_cours(self, cours) :
        if cours not in self.courses_attached :
            self.courses_attached.append(cours)    
        return
    
class Lecturer(Mentor) :
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.rate_for_lectures = {}
    
    def middle_rate(self) :
        sum_rate = 0
        con_rate = 0
        if len(self.rate_for_lectures) == 0 : 
            print('Делить на ноль нельзя')
            return 
        for i in self.rate_for_lectures.values() :
            for i2 in i :
                con_rate += 1
                sum_rate += int(i2)
        
        res = sum_rate / con_rate
        return res
    
    def __str__(self) :
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {self.middle_rate()}'
        return res

    def __lt__(self, second) :
        ''' я вот тут не понял. Зачем нужна проверка на классы?? Ведь всё равно, если мы для других классов сравнение ">, <" не установили, то Питон выдает \\TypeError: '>' not supported between instances of 'Lecturer' and 'Reviewer'\\. И мой принт про ошибку никогда не срабатывает!'''
        if not isinstance(second, Lecturer) :
            print('Данные классы не сравнить!!')
            return
        return self.middle_rate() < second.middle_rate()


class Reviewer(Mentor) :
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')
        
    def __str__(self) :
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Max', 'Maximov', 'man')
student_2 = Student('Roman', 'Romanov', 'man') 
student_3 = Student('Lena', 'Lenina', 'woman') 
student_1.add_courses_finished('Sing_Song')
student_2.add_courses_finished('Sing_Song')
student_3.add_courses_finished('Swimming')
student_1.add_courses_progress('Java')
student_1.add_courses_progress('Python')
student_2.add_courses_progress('Java')
student_2.add_courses_progress('C++')
student_3.add_courses_progress('Python')
student_3.add_courses_progress('C++')

lector_1 = Lecturer('Fillip', 'Kirkorov')
lector_2 = Lecturer('Lev', 'Leschenko')

revier_1 = Reviewer('Anna', 'Semenovich')
revier_2 = Reviewer('Alla', 'Pugacheva')
revier_1.add_cours('Python')
revier_1.add_cours('C++')
revier_2.add_cours('Python')
revier_2.add_cours('Java')
revier_1.rate_hw(student_1, 'Python', 5)
revier_1.rate_hw(student_1, 'Python', 5)
revier_1.rate_hw(student_3, 'Python', 5)
revier_1.rate_hw(student_3, 'Python', 5)
revier_1.rate_hw(student_3, 'C++', 3)
revier_1.rate_hw(student_3, 'C++', 3)
revier_1.rate_hw(student_2, 'C++', 3)
revier_1.rate_hw(student_2, 'C++', 3)
revier_2.rate_hw(student_1, 'Python', 5)
revier_2.rate_hw(student_3, 'Python', 5)
revier_2.rate_hw(student_1, 'Java', 4)
revier_2.rate_hw(student_2, 'Java', 4)
revier_2.rate_hw(student_2, 'Java', 4)
revier_2.rate_hw(student_1, 'Java', 4)

lector_1.add_cours('Python')
lector_1.add_cours('Java')
lector_1.add_cours('C++')
lector_1.add_cours('Sing_Song')
lector_2.add_cours('Python')
lector_2.add_cours('C++')
lector_2.add_cours('Java')
lector_2.add_cours('Swimming')

student_1.rate_to_lector(lector_1, 'Python', 5)
student_1.rate_to_lector(lector_1, 'Java', 4)
student_2.rate_to_lector(lector_1, 'Java', 4)
student_2.rate_to_lector(lector_1, 'C++', 3)
student_3.rate_to_lector(lector_1, 'Python', 5)
student_3.rate_to_lector(lector_1, 'C++', 3)
student_1.rate_to_lector(lector_2, 'Python', 3)
student_1.rate_to_lector(lector_2, 'Java', 5)
student_2.rate_to_lector(lector_2, 'Java', 5)
student_2.rate_to_lector(lector_2, 'C++', 4)
student_3.rate_to_lector(lector_2, 'Python', 3)
student_3.rate_to_lector(lector_2, 'C++', 4)

print(student_1.__dict__)
print(student_2.__dict__)
print(student_3.__dict__)
print(lector_1.middle_rate(), lector_2.middle_rate())
print(student_1.middle_rate(), student_2.middle_rate())
print(revier_1.__dict__)
print(lector_1.rate_for_lectures)
print(lector_1.middle_rate())

'''Проверяем __lt__()'''
print(student_1 > student_2)
print(student_1 < student_3)
print(student_2 > student_3)
print(lector_1 > lector_2)


'''Проверяем __str__()'''
print(student_1)
print(student_2)
print(student_3)
print(revier_1)
print(revier_2)
print(lector_1)
print(lector_2)

def middle_rate_students_one_cours(list_students, cours) :
    '''для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса)'''
    con_all_rates_one_cours = 0
    sum_rate_one_cours = 0
    for i in list_students :
        for i2 in i.grades :
            if i2 == cours :
                for one_rate in i.grades[i2] :
                    con_all_rates_one_cours += 1
                    sum_rate_one_cours += one_rate
    res = sum_rate_one_cours / con_all_rates_one_cours
    return res

'''Проверяем работу middle_rate_one_cours()'''
students_list = [student_1, student_2, student_3]
print(middle_rate_students_one_cours(students_list, 'Python'))
print(middle_rate_students_one_cours(students_list, 'Java'))
print(middle_rate_students_one_cours(students_list, 'C++'))


def middle_rate_lectors_one_cours(lectures_list, cours) :
    con_all_rates_one_cours = 0
    sum_rate_one_cours = 0
    for i in lectures_list :
        for i2 in i.rate_for_lectures :
            if i2 == cours :
                for one_rate in i.rate_for_lectures[i2] :
                    con_all_rates_one_cours  += 1
                    sum_rate_one_cours += one_rate
    res = sum_rate_one_cours / con_all_rates_one_cours
    return res

'''Проверяем работу middle_rate_lectors_one_cours()'''
list_lectures = [lector_1, lector_2]
print(middle_rate_lectors_one_cours(list_lectures, 'Python'))
print(middle_rate_lectors_one_cours(list_lectures, 'C++'))
print(middle_rate_lectors_one_cours(list_lectures, 'Java'))
