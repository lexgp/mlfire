from rest_framework.viewsets import ModelViewSet
from api import serializers as api_serializers

from core.models import LearnigModel
from core.models import Investigation

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from PIL import Image, ImageEnhance

import torch
from torchvision import transforms

import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

class InvestigationViewSet(ModelViewSet):
    serializer_class = api_serializers.InvestigationSerializer
    queryset = Investigation.objects.all()
    http_method_names = ['post', 'head', 'options']

    def preprocess_image(self, image_path, target_size):
        image = load_img(image_path, target_size=target_size)
        image_array = img_to_array(image)
        image_array = image_array / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array


    def create(self, request, **kwargs):
        serializer = api_serializers.InvestigationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        investigation = serializer.save()
        message = ''

        if investigation.lmodel.code == 'wildfire-satellite-roboflow-yolov8n':
            yolo_model = YOLO(investigation.lmodel.model_file.path)
            image_path = investigation.photo.path
            results = yolo_model.predict(source=image_path)
            for result in results:
                boxes = result.boxes
                message = f"Найдено объектов: {len(boxes)}\n"
                for box in boxes:
                    predicted_class_index = int(box.cls)
                    predicted_class_name = result.names[predicted_class_index]
                    conf = 100 *  box.conf.item()
                    message += f"Класс: {predicted_class_name}, Достоверность: {conf:.2f}%"
        elif investigation.lmodel.code == 'semushina-yolov8n':
            yolo_model = YOLO(investigation.lmodel.model_file.path)
            image_path = investigation.photo.path
            results = yolo_model.predict(source=image_path)
            probs = results[0].probs
            predicted_class_index = results[0].probs.top1
            predicted_class_name = results[0].names[predicted_class_index]
            predicted_confidence = 100 * probs.top1conf.item()
            message = f"Класс: {predicted_class_name} Вероятность: {predicted_confidence:.2f}"
        elif investigation.lmodel.code == 'forest-fire-KaterinaKuhne-yolov8n-cls':
            yolo_model = YOLO(investigation.lmodel.model_file.path)
            image_path = investigation.photo.path
            grayscale = Image.open(image_path).convert('L')
            enhancer = ImageEnhance.Contrast(grayscale)
            preprocessed_image = enhancer.enhance(1.4).point(lambda x: x * 0.6)
            results = yolo_model(preprocessed_image)
            probs = results[0].probs
            predicted_class_index = results[0].probs.top1
            predicted_class_name = results[0].names[predicted_class_index]
            predicted_confidence = 100 * probs.top1conf.item()
            message = f"Класс: {predicted_class_name} Вероятность: {predicted_confidence:.2f}"
        elif investigation.lmodel.code == 'Katrin-Pochtar-Wildfire-keras':
            img_size=(32, 32)
            keras_model = load_model(investigation.lmodel.model_file.path)
            test_image = self.preprocess_image(investigation.photo.path, img_size)
            predictions = keras_model.predict(test_image)
            probability = predictions[0][0] * 100  # Convert to percentage
            message = f"The probability of fire is {probability:.2f}%"
        elif investigation.lmodel.code == 'AndreyKotelnikov-resnet18_finetuned':
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            torch_model = torch.load(investigation.lmodel.model_file.path, map_location=device, weights_only=False)
            torch_model.eval()  # Переводим в режим оценки
            transform = transforms.Compose([
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406],
                                    [0.229, 0.224, 0.225])
            ])
            image_path = investigation.photo.path
            img = Image.open(image_path).convert('RGB')
            input_tensor = transform(img)
            input_batch = input_tensor.unsqueeze(0).to(device)
            with torch.no_grad():
                outputs = torch_model(input_batch)
                probs = torch.softmax(outputs, dim=1)
                p_fire = probs[0, 0].item()
                message = f'Fire probability: {p_fire:.4f}'
        investigation.result = message
        investigation.save()
        
        serializer = api_serializers.InvestigationSerializer(investigation)
        return Response(serializer.data, status=HTTP_201_CREATED)


class LearnigModelViewSet(ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    serializer_class = api_serializers.LearnigModelSerializer
    queryset = LearnigModel.objects.all()
