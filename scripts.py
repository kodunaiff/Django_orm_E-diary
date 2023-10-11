import random

from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Schoolkid

# 4
schoolkids_all = Schoolkid.objects.all()
print(schoolkids_all)

# 5
school_kid = Schoolkid.objects.filter(full_name__contains="Фролов Иван")
child = school_kid[0]
print(child.full_name)

# 6
grades = Mark.objects.filter(schoolkid=child)
print(grades)

# 7
bad_grades = Mark.objects.filter(schoolkid=child, points__lt=4)
print(bad_grades)

# 8, 9, 10
print(bad_grades.count())


def fix_marks(schoolkid):
    bad_grades = Mark.objects.filter(schoolkid=child, points__lt=4)
    for grade in bad_grades:
        grade.points = 5
        grade.save()


# 11
chastisements = Chastisement.objects.all()
print(chastisements)

# 12, 13
chastisements_iv = Chastisement.objects.filter(schoolkid=child)
chastisements_iv.delete()


# 14
def remove_chastisements(schoolkid):
    chastisements_kid = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements_kid.delete()


# 15
lesson_all = Lesson.objects.all()
print(lesson_all)

# 16
lesson_class = Lesson.objects.filter(year_of_study=6, group_letter="А")

# 17
lesson_class_math = Lesson.objects.filter(year_of_study=6,
                                          group_letter="А",
                                          subject__title="Математика")

# 18
date_praise = lesson_class_math[0].date
teacher_praise = lesson_class_math[0].teacher
subject_praise = lesson_class_math[0].subject

Commendation.objects.create(text='Хвалю!',
                            created=date_praise,
                            schoolkid=child,
                            subject=subject_praise,
                            teacher=teacher_praise)


# 19
def create_commendation(child, subject_lesson):
    lessons = Lesson.objects.filter(year_of_study=6,
                                    group_letter="А",
                                    subject__title=subject_lesson).\
        order_by('-date')
    last_lesson = lessons.first()
    compliments = ['Молодец!', 'Отлично!', 'Хорошо!',
                   'Гораздо лучше, чем я ожидал!',
                   'Ты меня приятно удивил!',
                   'Великолепно!', 'Прекрасно!',
                   'Ты меня очень обрадовал!',
                   'Именно этого я давно ждал от тебя!',
                   'Сказано здорово – просто и ясно!',
                   'Ты, как всегда, точен!',
                   'Очень хороший ответ!', 'Талантливо!',
                   'Ты сегодня прыгнул выше головы!',
                   'Я поражен!', 'Уже существенно лучше!',
                   'Потрясающе!', 'Замечательно!',
                   'Прекрасное начало!',
                   'Так держать!', 'Ты на верном пути!',
                   'Здорово!', 'Это как раз то, что нужно!',
                   'Я тобой горжусь!',
                   'С каждым разом у тебя получается всё лучше!',
                   'Мы с тобой не зря поработали!',
                   'Я вижу, как ты стараешься!', 'Ты растешь над собой!',
                   'Ты многое сделал, я это вижу!',
                   'Теперь у тебя точно все получится!']
    compliment = random.choice(compliments)
    Commendation.objects.create(text=compliment,
                                created=last_lesson.date,
                                schoolkid=child,
                                subject=last_lesson.subject,
                                teacher=last_lesson.teacher)


# 20
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def get_kid_name(child_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
        return child
    except Schoolkid.DoesNotExist:
        print(f'{child_name} не найден(а)')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Hайдено несколько учеников с именем {child_name}')
