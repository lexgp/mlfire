import json
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
# from core.models import Category
# from core.models import FaqCategory
from api import serializers as api_serializers
from core import serializers as core_serializers

from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

# class SearchFormBaseView(TemplateView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         categories = Category.objects.filter(parent=None).all()
#         serializer = api_serializers.CategorySerializer(categories, many=True)
#         context['categories'] = json.dumps(serializer.data)
#         return context


# class HomeListView(TemplateView):
#     template_name = 'core/index_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


# class HomeView(SearchFormBaseView):
class HomeView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Главная страница'
        # context['padding_search_form'] = True
        # context['top_services'] = get_top_services()
        # context['about_icons'] = IconAbout.objects.all()
        # context['popular_categories'] = Category.objects.filter(is_popular=True).all()[:6]
        return context


