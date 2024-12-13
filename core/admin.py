from django.contrib import admin

from core.models import LearnigModel
from core.models import Investigation
# from core.models import ServicePhoto
# from core.models import FaqCategory
# from core.models import FaqQuestion

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


# class ServicePhotoInline(admin.TabularInline):

#     model = ServicePhoto
#     extra = 0
#     can_delete = True

#     fields = (
#         'photo',
#     )


# @admin.register(ServiceItem)
# class ServiceItemAdmin(admin.ModelAdmin):
#     list_display = [
#         'title', 'category', 'is_popular', 'user',
#     ]
#     inlines = (
#         ServicePhotoInline,
#     )


# @admin.register(FaqCategory)
# class FaqCategoryAdmin(admin.ModelAdmin):
#     list_display = [
#         'title', 'ordering'
#     ]


# @admin.register(FaqQuestion)
# class FaqQuestionAdmin(admin.ModelAdmin):
#     list_display = [
#         'category', 'question'
#     ]


