import pygame
from PIL import Image  # Missing dependency added for better clarity


def converter_para_surface_pygame(pil_image: Image.Image) -> pygame.Surface:

    pil_image = pil_image.convert("RGBA")
    return pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode)


def recortar_imagem(start_x: int, start_y: int, end_x: int, end_y: int, original_image: Image.Image) -> pygame.Surface:
    """
    Function to crop and convert an image segment into a Pygame surface.

    Parameters:
        start_x (int): Initial X-coordinate of the crop rectangle.
        start_y (int): Initial Y-coordinate of the crop rectangle.
        end_x (int): Final X-coordinate of the crop rectangle.
        end_y (int): Final Y-coordinate of the crop rectangle.
        original_image (PIL.Image.Image): The original image to crop from.

    Returns:
        pygame.Surface: The cropped and converted Pygame surface.
    """
    # Crop the image
    cropped_image = original_image.crop((start_x, start_y, end_x, end_y))
    # Convert the cropped image to Pygame surface
    return converter_para_surface_pygame(cropped_image)


__all__ = ["recortar_imagem"]
