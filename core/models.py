from django.db import models
from urllib.parse import unquote
from django.utils import timezone


class LearnigModel(models.Model):

    class Meta:
        verbose_name = 'Обучаемая модель'
        verbose_name_plural = 'Обучаемые модели'

    name = models.CharField(verbose_name="Понятное название", max_length=255, null=False, blank=False)
    author = models.CharField(verbose_name="Кто обучал", max_length=255, null=False, blank=False)
    code = models.CharField(verbose_name="Код", max_length=255, null=False, blank=False)
    description = models.TextField(verbose_name="Описание модели", null=False, blank=True)
    dataset_link = models.CharField(verbose_name="Ссылка на датасет", null=False, blank=False)
    model_file = models.FileField(verbose_name="Файл с моделью", upload_to='model-files', null=True, default=None)

    def __str__(self):
        return self.name + ' (' + self.author + ')'

class Investigation(models.Model):

    class Meta:
        verbose_name = 'Исследование'
        verbose_name_plural = 'Исследования'

    lmodel = models.ForeignKey('LearnigModel', verbose_name="Обучаемая модель", related_name="investigations", null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.ImageField(verbose_name="Исследуемое фото", upload_to='photos')
    photo_out = models.ImageField(verbose_name="Фото-результат", upload_to='photos_out')
    result = models.TextField(verbose_name="Результат", null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lmodel.__str__() if self.lmodel else 'Investigation ' + str(self.created)


# class ServiceItem(models.Model):

#     class Meta:
#         verbose_name = 'Услуга'
#         verbose_name_plural = 'Услуги'

#     title = models.CharField(verbose_name="Заголовок", max_length=255, null=False, blank=False)
#     description = models.TextField(verbose_name="Описание", null=False, blank=False)
#     category = models.ForeignKey('Category', verbose_name="Категория услуги", related_name="services", null=True, blank=True, on_delete=models.SET_NULL)
#     wish_categories = models.ManyToManyField('Category', verbose_name="Желаемые ответные услуги", related_name='wish_services', blank=True)
#     is_popular = models.BooleanField(default=False, verbose_name="Популярная услуга", help_text='Будет отображаться в соответсвующем блоке на главной странице. Значение обновляется автоматически на основе статистики.')
#     user = models.ForeignKey('auth.User', default=None, null=True, related_name='services', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# class AbstractPhoto(models.Model):
#     photo = models.ImageField(upload_to='photos', verbose_name='Photo')
#     item = models.ForeignKey('AbstractOwner', null=True, related_name='photos', on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
    
#     class Meta:
#         abstract = True
    
#     @classmethod
#     def update_owner(AbstractPhoto, photo_id, owner):
#         if photo_id:
#             photo = AbstractPhoto.objects.filter(id=photo_id).last()
#             if photo:
#                 photo.owner = owner
#                 photo.save()


# class ServicePhoto(AbstractPhoto):
#     item = models.ForeignKey(ServiceItem, on_delete=models.CASCADE, related_name='photos', null=True)
#     photo = models.ImageField(upload_to="services")

#     def __str__(self):
#         title = self.item.title if self.item else ''
#         return "Photo for %s" % (title)


# class FaqCategory(models.Model):

#     class Meta:
#         verbose_name = 'Категория вопросов'
#         verbose_name_plural = 'Категории вопросов'
#         ordering = ['ordering']

#     title = models.CharField(verbose_name="Заголовок", max_length=255, null=False, blank=False)

#     ordering = models.PositiveIntegerField(default=0, verbose_name="Порядок очереди")
#     def __str__(self):
#         return self.title


# class FaqQuestion(models.Model):

#     class Meta:
#         verbose_name = 'Вопрос FAQ'
#         verbose_name_plural = 'Вопросы FAQ'

#     question = models.TextField(verbose_name="Текст вопроса", null=False, blank=False)
#     answer = models.TextField(verbose_name="Текст ответа", null=False, blank=False)
#     category = models.ForeignKey('FaqCategory', verbose_name="Категория вопроса", related_name="questions", null=True, blank=False, on_delete=models.PROTECT)
#     created_at = models.DateTimeField("Дата создания", auto_now_add=True)
#     updated_at = models.DateTimeField("Дата последнего обновления", auto_now=True)

#     def __str__(self):
#         return self.question

