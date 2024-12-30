def recortar_imagem(x1, y1, x2, y2, imagem_original):
    return imagem_original.crop((x1, y1, x2, y2))