from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyForm
import base64
import numpy as np
import cv2
from PIL import Image
import io
import matplotlib.pyplot as plt
from .colorizerengine.main import colorize_image


def index(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST, request.FILES)
        image = request.FILES["image"].read()

        colorized_image, original_image = colorize_image(image)
        context = {
            "form": form,
            "base64_string": colorized_image,
            "image": original_image,
        }
        return render(request, "colorizer/index.html", context)
    else:
        return render(
            request,
            "colorizer/index.html",
            {
                "form": form,
            },
        )
