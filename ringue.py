import pygame


def desenhar_ringue(tela):
    """
    Função para desenhar um quadrado com perspectiva no centro da tela.
    """
    # Configurações das dimensões do ringue
    largura = 300
    altura = 200

    # Centralização do ringue na tela
    centro_x, centro_y = tela.get_width() // 2, tela.get_height() // 2

    # Cor do ringue
    cor_ringue = (100, 100, 255)  # Azul claro
    borda_cor = (50, 50, 150)  # Azul escuro (borda)

    # Vértices do quadrado com perspectiva
    pontos = [
        (centro_x - largura, centro_y + altura),  # Inferior esquerdo
        (centro_x + largura, centro_y + altura),  # Inferior direito
        (centro_x + largura // 2, centro_y - altura),  # Superior direito
        (centro_x - largura // 2, centro_y - altura)  # Superior esquerdo
    ]

    # Desenhar o ringue com perspectiva
    pygame.draw.polygon(tela, cor_ringue, pontos)

    # Adicionar bordas ao ringue
    pygame.draw.polygon(tela, borda_cor, pontos, width=5)
