import random

from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Schoolkid

COMPLIMENTS = ['Молодец!', 'Отлично!', 'Хорошо!',
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


def get_kid_name(child_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
        return child
    except Schoolkid.DoesNotExist:
        print(f'{child_name} не найден(а)')
    except Schoolkid.MultipleObjectsReturned:
        print(f'Hайдено несколько учеников с именем {child_name}')


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=child, points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
    chastisements_kid = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements_kid.delete()


def create_commendation(child, subject_lesson):
    lessons = Lesson.objects.filter(subject__title=subject_lesson). \
        order_by('-date')
    last_lesson = lessons.first()
    compliment = random.choice(COMPLIMENTS)
    Commendation.objects.create(text=compliment,
                                created=last_lesson.date,
                                schoolkid=child,
                                subject=last_lesson.subject,
                                teacher=last_lesson.teacher)
