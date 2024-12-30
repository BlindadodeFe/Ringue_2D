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
    global jogo_pausado  # Permite alterar o estado global da pausa
    rodando_menu = True
    mostrar_texto = True  # Controla o texto piscante
    contador_tempo = 0  # Controla o tempo para piscar

    # Botões no menu inicial
    start_button = StartButton(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2 + 50, 150, 50, imagem_original)
    exit_button = ScoreButton(LARGURA_TELA // 2 - 74, ALTURA_TELA // 2 + 100, 150, 50, imagem_original)  # Botão EXIT

    while rodando_menu:
        tela.fill(WHITE)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Lógica do botão START
        if start_button.draw(tela):
            jogo_pausado = False  # Garante que o jogo recomeça não pausado
            rodando_menu = False  # Sai do menu e inicia o jogo

        # Lógica do botão EXIT
        if exit_button.draw(tela):
            pygame.quit()
            sys.exit()  # Encerra o jogo

        contador_tempo += 1
        if contador_tempo >= 30:  # Alterna o efeito de piscar
            mostrar_texto = not mostrar_texto
            contador_tempo = 0

        # Texto "APERTE START" piscando
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

    # Criação dos botões no jogo
    pausa_button = PauseButton(10, 10, 150, 50, imagem_original)
    menu_button = PauseButton(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2, 150, 50, imagem_original)  # Centralizado
    mortes_button = DeathButton(180, 10, 150, 50, imagem_original)

    while rodando:
        tela.fill(WHITE)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            # Detecta se a tecla ESC é pressionada
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                jogo_pausado = not jogo_pausado  # Alterna o estado de pausa

        if jogo_pausado:
            desenhar_texto("Jogo Pausado", VERMELHO, LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 50, 45)

            # Botão de menu reposicionado para o centro
            if menu_button.draw(tela):
                menu_inicial()  # Retorna ao menu inicial

        else:
            if pausa_button.draw(tela):
                jogo_pausado = True  # Pausa o jogo

            # Verifica cliques no botão de mortes
            if mortes_button.draw(tela):
                imagem_exibida = recortar_imagem(300, 0, 450, 50, imagem_original)
                mortes += 1

            # Lógica para pontuação futura
            if mortes > 0 and mortes % 5 == 0:
                score += 5  # Exemplo: incrementa 5 pontos a cada 5 mortes

            desenhar_texto(f"Pontos: {score}", PRETO, 10, 55)
            desenhar_texto(f"M: {mortes}", PRETO, 224, 30)

        pygame.display.flip()
        relogio.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    menu_inicial()
    principal()
