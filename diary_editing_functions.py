import random
from datacenter.models import (Schoolkid,
                               Mark,
                               Chastisement,
                               Lesson,
                               Commendation)


COMMENDABLE_TEXT = [
    'Молодец!',
    'Очень хороший ответ!',
    'Так держать!',
    'Ты на верном пути!',
    'С каждым разом у тебя получается всё лучше!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!'
]


def get_schoolkid(child_name):
    try:
        return Schoolkid.objects.get(full_name__contains=child_name)
    except Schoolkid.DoesNotExist:
        print('Ученик с таким именем не найден. Проверьте имя.')
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено несколько учеников с таким именем. Уточните имя.')


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()


def create_commendation(schoolkid, subject):
    try:
        lesson = Lesson.objects.filter(
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter,
            subject__title=subject
        ).order_by('-date').first()
        Commendation.objects.create(
            text=random.choice(COMMENDABLE_TEXT),
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
    except ObjectDoesNotExist:
        print('Предмет не найден. Проверьте название.')
