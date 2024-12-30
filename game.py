import pygame
import sys
from PIL import Image

# Importações organizadas
from componentes import StartButton, PauseButton, DeathButton, ScoreButton
from utils import recortar_imagem

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA_TELA = 1280
ALTURA_TELA = 720
TITULO_TELA = "Meu Jogo"
FPS = 60

# Cores
WHITE = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Caminho da pasta de imagens
CAMINHO_IMAGEM = "Imagem/Hub.png"

# Inicializa a janela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_TELA)

# Configura o relógio para controlar a taxa de quadros
relogio = pygame.time.Clock()

# Carregar a imagem com PIL (Pillow)
imagem_original = Image.open(CAMINHO_IMAGEM)


# Função para desenhar o texto na tela
def desenhar_texto(texto, cor, x, y, tamanho=44):
    fonte = pygame.font.Font(None, tamanho)
    texto_renderizado = fonte.render(texto, True, cor)
    tela.blit(texto_renderizado, (x, y))


def menu_inicial():
    rodando_menu = True
    mostrar_texto = True  # Controla o texto piscante
    contador_tempo = 0  # Controla o tempo para piscar
    start_button = StartButton(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2 + 50, 150, 50, imagem_original)

    while rodando_menu:
        tela.fill(WHITE)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenha o botão Start
        if start_button.draw(tela):
            rodando_menu = False  # Sai do menu e inicia o jogo

        contador_tempo += 1
        if contador_tempo >= 30:  # Alterna o efeito de piscar
            mostrar_texto = not mostrar_texto
            contador_tempo = 0

        if mostrar_texto:
            desenhar_texto("APERTE START", VERMELHO, LARGURA_TELA // 2 - 150, ALTURA_TELA // 2 - 50, 50)

        pygame.display.flip()
        relogio.tick(FPS)


# Função principal do jogo
def principal():
    global score, mortes, jogo_pausado  # Para modificar variáveis
    score = 0
    mortes = 0
    jogo_pausado = False
    rodando = True
    imagem_exibida = None  # Variável para imagem recortada

    # Criação dos botões
    start_button = StartButton(10, 10, 150, 50, imagem_original)
    pausa_button = PauseButton(200, 10, 150, 50, imagem_original)
    mortes_button = DeathButton(400, 10, 50, 50, imagem_original)
    score_button = ScoreButton(600, 10, 150, 50, imagem_original)

    while rodando:
        tela.fill(WHITE)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        if pausa_button.draw(tela):
            imagem_exibida = recortar_imagem(150, 0, 300, 50, imagem_original)
            jogo_pausado = not jogo_pausado

        if not jogo_pausado:
            # Verifica cliques em outros botões
            if start_button.draw(tela):
                imagem_exibida = recortar_imagem(0, 0, 150, 50, imagem_original)
            elif mortes_button.draw(tela):
                imagem_exibida = recortar_imagem(300, 0, 450, 50, imagem_original)
                mortes += 1
            elif score_button.draw(tela):
                imagem_exibida = recortar_imagem(450, 0, 600, 50, imagem_original)
                score += 10

            desenhar_texto(f"Score: {score}", PRETO, 10, 44)
            desenhar_texto(f"Mortes: {mortes}", PRETO, 200, 44)

        if jogo_pausado:
            desenhar_texto("Jogo Pausado", VERMELHO, LARGURA_TELA - 235, 20, 45)

       # if imagem_exibida:
       #      tela.blit(imagem_exibida, (500, 200))

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    menu_inicial()
    principal()
