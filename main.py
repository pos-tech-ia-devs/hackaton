from core import analyze_architecture

# Example usage
image_path = "resources/aws.png"
try:
    report = analyze_architecture(image_path)
    print(report)
except Exception as e:
    print(f"Error: {e}")