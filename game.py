import pygame
import sys
from PIL import Image

import constants as const # Importa as constantes do projeto

# Importações organizadas
from componentes import StartButton, PauseButton, DeathButton, ScoreButton, MenuButton
from utils import recortar_imagem
from ringue import desenhar_ringue  # Importa a função para desenhar o ringue

# Inicializa o pygame
pygame.init()

# Inicializa a tela no modo fullscreen
tela = pygame.display.set_mode((const.LARGURA_TELA_PADRAO, const.ALTURA_TELA_PADRAO), pygame.FULLSCREEN)
pygame.display.set_caption(const.TITULO_TELA)

# Obtém a largura e altura reais da tela para o modo fullscreen
LARGURA_TELA, ALTURA_TELA = tela.get_size()

# Relógio para controle do FPS
relogio = pygame.time.Clock()

class Game:
    def __init__(self): # Construtor da classe
        # Carregar a imagem
        try:
            imagem_pil = Image.open(const.CAMINHO_IMAGEM)  # Leitura via PIL
            self.imagem_original = self.carregar_imagem_para_pygame(imagem_pil)  # Conversão para pygame
        except FileNotFoundError:
            print(f"Erro: A imagem '{const.CAMINHO_IMAGEM}' não foi encontrada.")
            self.imagem_original = None

    # Função para converter imagem PIL para pygame
    def carregar_imagem_para_pygame(self, imagem_pil):
        modo = imagem_pil.mode
        tamanho = imagem_pil.size
        dados = imagem_pil.tobytes()
        return pygame.image.fromstring(dados, tamanho, modo)

    # Função para exibir texto na tela
    def desenhar_texto(self, texto, cor, x, y, tamanho=44):
        fonte = pygame.font.Font(None, tamanho)
        texto_renderizado = fonte.render(texto, True, cor)
        tela.blit(texto_renderizado, (x, y))


    # Menu inicial
    def menu_inicial(self, background_surface=None):
        global jogo_pausado
        rodando_menu = True
        mostrar_texto = True
        contador_tempo = 0

        # Botões no menu inicial
        start_button = StartButton(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2 + 50, 150, 50, self.imagem_original)
        exit_button = ScoreButton(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2 + 120, 150, 50, self.imagem_original)

        while rodando_menu:
            # Usa o fundo capturado se fornecido
            if background_surface:
                tela.blit(background_surface, (0, 0))  # Exibe o jogo em segundo plano no menu
            else:
                tela.fill(const.WHITE)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Desenha os botões
            if start_button.draw(tela):
                jogo_pausado = False
                rodando_menu = False

            if exit_button.draw(tela):
                pygame.quit()
                sys.exit()

            contador_tempo += 1
            if contador_tempo >= 30:
                mostrar_texto = not mostrar_texto
                contador_tempo = 0

            # Texto piscante no menu inicial
            if mostrar_texto:
                self.desenhar_texto("APERTE START", const.VERMELHO, LARGURA_TELA // 2 - 150, ALTURA_TELA // 2 - 50, 50)

            pygame.display.flip()
            relogio.tick(const.FPS)


    # Loop principal do jogo
    def principal(self):
        global score, mortes, jogo_pausado
        score = 0
        mortes = 0
        jogo_pausado = False
        rodando = True
        imagem_exibida = None

        # Botões no jogo
        pausa_button = PauseButton(10, 10, 150, 50, self.imagem_original)
        menu_button = MenuButton(LARGURA_TELA // 2 - 75, ALTURA_TELA // 2, 150, 50, self.imagem_original)
        mortes_button = DeathButton(180, 10, 150, 50, self.imagem_original)

        # Criar uma surface preta semi-transparente
        overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA))
        overlay.set_alpha(0)  # Define a transparência (0 a 255). 128 é metade transparente
        overlay.fill((0, 0, 0))  # Preenche a surface com a cor preta

        while rodando:
            tela.fill(const.WHITE)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    rodando = False
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    jogo_pausado = not jogo_pausado

            if jogo_pausado:
                # Salvar o estado do jogo para usar no menu
                jogo_background = pygame.Surface(tela.get_size())
                jogo_background.blit(tela, (0, 0))

                # Desenhar o filtro preto transparente
                tela.blit(overlay, (0, 0))
                self.desenhar_texto("Jogo Pausado", const.VERMELHO, LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 50, 45)

                # Chamar o menu com o jogo em segundo plano
                if menu_button.draw(tela):
                    self.menu_inicial(jogo_background)
            else:
                if pausa_button.draw(tela):
                    jogo_pausado = True

                if mortes_button.draw(tela):
                    imagem_exibida = recortar_imagem(300, 0, 450, 50, self.imagem_original)
                    mortes += 1

                # Desenhar o quadrado com perspectiva
                desenhar_ringue(tela)

                self.desenhar_texto(f"Pontos: {score}", const.PRETO, 10, 55)
                self.desenhar_texto(f"M: {mortes}", const.PRETO, 224, 30)

            pygame.display.flip()
            relogio.tick(const.FPS)

        pygame.quit()
        sys.exit()


# Executa o código
if __name__ == "__main__":
    # Inicializa o menu antes do loop
    jogo_background = pygame.Surface(tela.get_size())
    tela.fill(const.WHITE)
    jogo_background.blit(tela, (0, 0))

    game = Game()
    game.menu_inicial(jogo_background)
    # Loop principal
    game.principal()
