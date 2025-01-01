import pygame


class Personagem:
    def __init__(self, x, y, largura, altura):
        self.retangulo = pygame.Rect(x, y, largura, altura)
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.gravidade = 1

    def handle_event(self, evento):
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:  # Esquerda
                self.velocidade_x = -5
            if evento.key == pygame.K_RIGHT:  # Direita
                self.velocidade_x = 5
            if evento.key == pygame.K_UP:  # Pular
                if self.retangulo.bottom >= 720:  # Solo fictício em ALTURA_TELA
                    self.velocidade_y = -20
        if evento.type == pygame.KEYUP:
            if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                self.velocidade_x = 0

    def atualizar(self, altura_tela):
        self.velocidade_y += self.gravidade
        self.retangulo.x += self.velocidade_x
        self.retangulo.y += self.velocidade_y

        # Limitar o personagem para não cair além do chão
        if self.retangulo.bottom > altura_tela:
            self.retangulo.bottom = altura_tela
            self.velocidade_y = 0

    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), self.retangulo)  # Desenha o personagem como um retângulo