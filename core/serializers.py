from rest_framework import serializers
# from core.models import Category
# from core.models import ServiceItem
# from core.models import ServicePhoto
# from core.models import AbstractPhoto
# from home.models import IconAbout

from easy_thumbnails.files import get_thumbnailer

# class AbstractPhotoSerializer(serializers.ModelSerializer):
#     preview = serializers.SerializerMethodField()
#     # owner_id = serializers.CharField(required=False, allow_null=True, source='owner.id')

#     class Meta:
#         model = AbstractPhoto
#         fields = ('id', 'photo', 'preview', 'item_id')


#     def create(self, validated_data):
#         return super().create(validated_data)

#     @staticmethod
#     def get_preview(obj):
#         # crop_options = {'size': (100, 100), 'crop': True}
#         crop_options = {'size': (250, 250), 'crop': 'scale'}
#         try:
#             return get_thumbnailer(obj.photo).get_thumbnail(crop_options).url
#         except Exception as e:
#             pass
#         # return obj.file.storage._strip_signing_parameters(obj.file.url)


# class ServicePhotoSerializer(AbstractPhotoSerializer):

#     class Meta:
#         model = ServicePhoto
#         fields = "__all__"


# class ServiceItemSerializer(serializers.ModelSerializer):

#     def create(self, validated_data):
#         photos = validated_data.pop('photos', [])
#         wish_categories = validated_data.pop('wish_categories', [])
#         request = self.context.get("request")
#         if request and hasattr(request, "user"):
#             user = request.user
#             validated_data['user'] = user
#         result = ServiceItem.objects.create(**validated_data)
#         for photo in photos:
#             photo.item = result
#             photo.save()
#         result.wish_categories.set(wish_categories)
#         return result

#     def update(self, instance, validated_data):
#         photos = validated_data.get('photos', [])
#         request = self.context.get("request")
#         if request and hasattr(request, "user"):
#             user = request.user
#             instance.user = user
#             instance.save()
#         for photo in photos:
#             photo.item = instance
#             photo.save()
#         result = super().update(instance, validated_data)
#         wish_categories = validated_data.get('wish_categories', [])
#         result.wish_categories.set(wish_categories)
#         return result

#     photos_detail =  ServicePhotoSerializer(source='photos', many=True, read_only=True)
#     wish_categories = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, queryset=Category.objects.all())

#     class Meta:
#         model = ServiceItem
#         fields = [
#             'id',
#             'title',
#             'description',
#             'category',
#             'photos',
#             'photos_detail',
#             'wish_categories',
#             'user',
#         ]

# class ServiceItemListSerializer(ServiceItemSerializer):

#     category_title = serializers.CharField(read_only=True, source="category.title")

#     class Meta:
#         model = ServiceItem
#         fields = [
#             'id',
#             'title',
#             'description',
#             'category',
#             'category_title',
#             'photos',
#             'photos_detail',
#             'wish_categories',
#             'user',
#         ]


# class ServicePrototypeItemSerializer(ServiceItemSerializer):

#     photos_detail = serializers.SerializerMethodField(read_only=True)
#     wish_categories = serializers.SerializerMethodField(read_only=True)

#     def get_photos_detail(self, obj):
#         return []

#     def get_wish_categories(self, obj):
#         return []

#     class Meta:
#         model = ServiceItem
#         fields = [
#             'id',
#             'title',
#             'description',
#             'category',
#             'photos',
#             'photos_detail',
#             'wish_categories',
#             'user',
#         ]
