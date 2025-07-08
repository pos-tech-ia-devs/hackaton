import base64
import io


def convert_base64_image(img):
    buffered = io.BytesIO()
    image_format = img.format or "PNG"
    img.save(buffered, format=image_format)
    img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
    image_uri = f"data:image/{image_format.lower()};base64,{img_base64}"
    return image_uri
