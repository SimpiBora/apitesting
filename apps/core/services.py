from io import BytesIO
from PIL import Image, UnidentifiedImageError
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError

# class ImageFileService:
#     @staticmethod
#     def update_image(user, data):
#         image = data["image"]
#         # Crop logic using `top`, `left`, `height`, and `width` can be added
#         # For example, crop using PIL
#         # Save the updated image
#         user.image.save(image.name, image)
#         return user


class FileService:
    @staticmethod
    def add_video(post, video):
        """
        Handles video upload for a post.
        """
        post.video.save(video.name, video)
        return post


class ImageFileService:
    @staticmethod
    def update_image(user, data):
        image_file = data.get("image")
        try:
            height = int(data.get("height"))
            width = int(data.get("width"))
            top = int(data.get("top"))
            left = int(data.get("left"))
        except (TypeError, ValueError):
            raise ValidationError("Invalid crop dimensions provided.")

        if not image_file:
            raise ValidationError("No image file provided.")

        try:
            # Open image and convert to safe RGB mode
            with Image.open(image_file) as img:
                if img.mode not in ("RGB", "RGBA"):
                    img = img.convert("RGB")

                # Limit image size (e.g., max 10MB)
                if image_file.size > 10 * 1024 * 1024:
                    raise ValidationError("Image file too large (max 10MB).")

                # Limit dimensions (e.g., no image larger than 5000x5000)
                max_dimension = 5000
                if img.width > max_dimension or img.height > max_dimension:
                    raise ValidationError("Image dimensions too large.")

                # Crop image safely
                cropped = img.crop((left, top, left + width, top + height))

                # Convert to RGB to strip alpha and metadata
                safe_img = cropped.convert("RGB")

                # Save to buffer as JPEG
                buffer = BytesIO()
                safe_img.save(buffer, format="JPEG", quality=85, optimize=True)
                buffer.seek(0)
                image_content = ContentFile(buffer.read())

                # Store with a new name if you want to prevent name collisions
                user.image.save(f"{user.username}_avatar.jpg", image_content, save=True)

        except UnidentifiedImageError:
            raise ValidationError("Uploaded file is not a valid image.")
        except Exception as e:
            raise ValidationError(f"Image processing failed: {str(e)}")
