from django.db import models


TYPE_CHOICES = (
    ('1', 'Лекция'),
    ('2', 'Практика'),
    ('3', 'Лабораторная'),
)


NAME_WEEKDAY_CHOICES = (
    ('0', 'Понедельник'),
    ('1', 'Вторник'),
    ('2', 'Среда'),
    ('3', 'Четверг'),
    ('4', 'Пятница'),
    ('5', 'Суббота'),
    ('6', 'Воскресенье'),
)


PARITY_CHOICES = (
    ('0','Четная неделя'),
    ('1', 'Нечетная неделя')
)


class Lesson(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название пары',
    )
    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        verbose_name='Тип пары',
    )
    teacher = models.CharField(
        max_length=200,
        verbose_name='Препод',
    )
    place = models.CharField(
        max_length=200,
        verbose_name='Корпус-аудитория'
    )


    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return f'{self.name}'
    

class Weekday(models.Model):
    name = models.CharField(
        max_length=50,
        choices=NAME_WEEKDAY_CHOICES,
        verbose_name='День недели',
    )
    parity = models.CharField(
        max_length=200,
        choices=PARITY_CHOICES,
        verbose_name='Четность дня недели',
    )
    first_lesson = models.ForeignKey(
        Lesson,
        verbose_name='Первая пара',
        related_name='first_lesson',
        on_delete= models.CASCADE,
    )
    second_lesson = models.ForeignKey(
        Lesson,
        verbose_name='Вторая пара',
        related_name='second_lesson',
        on_delete= models.CASCADE,

    )
    third_lesson = models.ForeignKey(
        Lesson,
        verbose_name='Третья пара',
        related_name='third_lesson',
        on_delete= models.CASCADE,
    )
    fourth_lesson = models.ForeignKey(
        Lesson,
        verbose_name='Четвертая пара',
        related_name='fourth_lesson',
        on_delete= models.CASCADE,
    )
    fifth_lesson = models.ForeignKey(
        Lesson,
        verbose_name='Пятая пара',
        related_name='fifth_lesson',
        on_delete= models.CASCADE,
    )
    
    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

    def __str__(self):
        return f'{self.name}'