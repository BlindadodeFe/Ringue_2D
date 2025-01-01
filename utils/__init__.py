import pygame  # Importação necessária para as funções do pygame
from PIL import Image


def recortar_imagem(start_x, start_y, end_x, end_y, original_image):
    """
    Recorta uma porção da imagem original (pygame.Surface) usando coordenadas.
    Retorna um novo pygame.Surface.
    """
    if original_image is None:
        raise ValueError("A imagem original não pode ser None")

    # Converte pygame.Surface para PIL.Image
    pil_image = Image.frombytes("RGBA", original_image.get_size(), pygame.image.tostring(original_image, "RGBA"))

    # Faz o recorte da imagem usando Pillow
    cropped_image = pil_image.crop((start_x, start_y, end_x, end_y))

    # Converte de volta para pygame.Surface
    tamanho_recortado = (end_x - start_x, end_y - start_y)
    nova_superficie = pygame.image.fromstring(cropped_image.tobytes(), tamanho_recortado, "RGBA")

    return nova_superficie
