from django.contrib import admin

from core.models import LearnigModel
from core.models import Investigation

admin.site.site_header = 'Панель администратора'


@admin.register(LearnigModel)
class LearnigModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'author', 'dataset_link',
    ]

@admin.register(Investigation)
class InvestigationAdmin(admin.ModelAdmin):
    list_display = [
        'lmodel', 'created',
    ]
