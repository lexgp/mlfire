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

