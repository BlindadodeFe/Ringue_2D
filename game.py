from tabnanny import check

import pygame
import sys


from pygame.examples.go_over_there import event

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA_TELA = 1280
ALTURA_TELA = 720
TITULO_TELA = "Meu Jogo"
FPS = 60

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Inicializa a janela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_TELA)

# Configura o relógio para controlar a taxa de quadros
relogio = pygame.time.Clock()

# Variáveis de jogo
score = 0
mortes = 0
jogo_pausado = False
jogo_funcionando = True

# Função para desenhar o texto na tela
def desenhar_texto(texto, cor, x, y, tamanho=74):
    fonte = pygame.font.Font(None, tamanho)  # Fonte padrão
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, (x, y))

# Função para desenhar os botões
def desenhar_botao(texto, x, y, largura, altura, cor):
    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    desenhar_texto(texto, BRANCO, x + 10, y + 10, 30)

# Função para verificar se o clique está dentro de um botão
def verificar_click(x, y, largura, altura, pos_x, pos_y):
    return pos_x >= x and pos_x <= x + largura and pos_y >= y and pos_y <= y + altura

def principal():
    global score, mortes, jogo_funcionando, jogo_pausado  # Para modificar essas variáveis dentro da função
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Pega a posição do clique
                pos_x, pos_y = evento.pos



                # Verifica se clicou no botão Score
                if verificar_click(10, 10, 150, 50, pos_x, pos_y):
                    score += 10  # Incrementa o score
                # Verifica se clicou no botão Mortes
                if verificar_click(200, 10, 150, 50, pos_x, pos_y):
                    mortes += 1  # Incrementa o número de mortes
                # Verifica se clicou no botão Pausa
                if verificar_click(400, 10, 150, 50, pos_x, pos_y):
                    jogo_pausado = not jogo_pausado  # Alterna o estado



        # Logica do jogo
        if jogo_pausado:
            desenhar_texto("Jogo Pausado", VERMELHO,  LARGURA_TELA - 235, 20, 45)

        else:
            # Atualiza o score e mortes na tela
            desenhar_texto(f"Score: {score}", PRETO, 10, 20)
            desenhar_texto(f"Mortes: {mortes}", PRETO, 200, 20)

        # Desenha os botões
        desenhar_botao("Score", 10, 10, 150, 50, AZUL)
        desenhar_botao("Mortes", 200, 10, 150, 50, VERDE)
        desenhar_botao("Pausa", 400, 10, 150, 50, VERMELHO)

        # Atualiza a tela
        pygame.display.flip()

        # Controla a taxa de quadros
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    principal()
