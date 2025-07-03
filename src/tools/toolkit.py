from .image_analyzer import analyze_image
from .stride import stride
from .generate_new_diagram import (
    generate_new_diagram_report,
    generate_new_diagram_image,
)


def get_toolkit():
    toolkit = [
        analyze_image,
        stride,
        generate_new_diagram_report,
        generate_new_diagram_image,
    ]
    return toolkit
