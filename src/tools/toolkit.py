from .image_analyzer import analyze_image
from .stride import stride


def get_toolkit():
    toolkit = [analyze_image, stride]
    return toolkit
