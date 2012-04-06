from django.conf import settings

# path where will be saved the images
FLATPAGE_IMAGES_PATH = getattr(settings, 'FLATPAGE_IMAGES_PATH', 'flatpage_images')
