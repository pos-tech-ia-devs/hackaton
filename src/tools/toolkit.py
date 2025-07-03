from .image_analyzer import analyze_image
from .stride import stride
from .generate_new_diagram import generate_new_diagram


def get_toolkit():
    toolkit = [analyze_image, stride, generate_new_diagram]
    return toolkit
