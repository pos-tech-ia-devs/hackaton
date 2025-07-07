from .image_analyzer import analyze_image
from .stride import stride
from .fixed_report import generate_fixed_report
from .mermaid_diagram import generate_mermaid_diagram


def get_toolkit():
    toolkit = [
        analyze_image,
        stride,
        generate_fixed_report,
        generate_mermaid_diagram,
    ]
    return toolkit
