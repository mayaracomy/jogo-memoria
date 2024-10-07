import tkinter as tk
from tkinter import messagebox
import random


# Função para criar o tabuleiro do jogo
def criar_tabuleiro():
    # Lista de emojis
    emojis = ["😀", "😂", "😍", "😎", "🤔", "😢", "😡", "🥳"]
    pares = emojis * 2
    random.shuffle(pares)
    return pares


# Função para exibir o estado das cartas
def mostrar_cartas():
    for i, botao in enumerate(botoes):
        if visiveis[i]:
            botao.config(text=tabuleiro[i])
        else:
            botao.config(text="")


# Função para lidar com o clique em um botão
def clique(botao, i):
    global primeiro_clique, segundo_clique, visiveis
    if visiveis[i] or segundo_clique is not None:
        return

    visiveis[i] = True
    mostrar_cartas()

    if primeiro_clique is None:
        primeiro_clique = i
    elif segundo_clique is None:
        segundo_clique = i
        janela.after(1000, verificar_pares)


def verificar_pares():
    global primeiro_clique, segundo_clique
    if tabuleiro[primeiro_clique] != tabuleiro[segundo_clique]:
        visiveis[primeiro_clique] = False
        visiveis[segundo_clique] = False
    primeiro_clique = None
    segundo_clique = None
    mostrar_cartas()
    if all(visiveis):
        messagebox.showinfo("Fim de Jogo", "Você ganhou!")


# Função para atualizar o timer
def atualizar_timer():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        timer_label.config(text=f'Tempo: {tempo_restante} s')
        janela.after(1000, atualizar_timer)
    else:
        messagebox.showinfo("Fim de Jogo", "O tempo acabou!")
        desativar_jogo()


# Função para desativar o jogo
def desativar_jogo():
    for botao in botoes:
        botao.config(state=tk.DISABLED)


# Função para iniciar o jogo
def iniciar_jogo():
    global tabuleiro, visiveis, primeiro_clique, segundo_clique, botoes, tempo_restante
    tabuleiro = criar_tabuleiro()
    visiveis = [False] * len(tabuleiro)
    primeiro_clique = None
    segundo_clique = None

    # Limpa botões existentes
    for botao in botoes:
        botao.destroy()

    # Cria a nova grade de botões para o tabuleiro
    botoes = []
    for i in range(len(tabuleiro)):
        botao = tk.Button(janela, bg="light pink", text="", width=8, height=4, font=("Arial", 20),
                          command=lambda i=i: clique(botao, i))
        botao.grid(row=i // 4 + 3, column=i % 4, padx=10, pady=10, sticky='nsew')
        botoes.append(botao)

    # Iniciar o timer
    tempo_restante = 60
    timer_label.config(text=f'Tempo: {tempo_restante} s')
    atualizar_timer()


# Função para exibir os autores
def mostrar_autores():
    autores = "Autores:\nAna Clara Finkbeiner\nJulia Kluck\nLaura Berkenbrock\nMayara Kozanda"
    messagebox.showinfo("Sobre o Jogo", autores)


# Função para sair do jogo
def sair_jogo():
    janela.quit()


# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Jogo da Memória")
janela.config(bg="light blue")
janela.geometry("800x800")

# Criando o título do jogo
titulo = tk.Label(janela, text="Jogo da Memória", font=("Arial", 36), bg="light blue")
titulo.grid(row=0, column=0, columnspan=4, pady=30, sticky='nsew')

# Criando o label do timer
timer_label = tk.Label(janela, text="Tempo: 60 s", font=("Arial", 24), bg="light blue")
timer_label.grid(row=1, column=0, columnspan=4, pady=20, sticky='nsew')

# Criando os botões do menu
menu_frame = tk.Frame(janela, bg="light blue")
menu_frame.grid(row=2, column=0, columnspan=4, pady=30, sticky='nsew')

# Centralizando os botões no menu
btn_iniciar = tk.Button(menu_frame, text="Iniciar", command=iniciar_jogo, width=12, bg="light green", height=1, font=("Arial", 16))
btn_iniciar.grid(row=0, column=0, padx=10, sticky='ew')

btn_autores = tk.Button(menu_frame, text="Autores", command=mostrar_autores, width=12, bg="light yellow", height=1, font=("Arial", 16))
btn_autores.grid(row=0, column=1, padx=10, sticky='ew')

btn_sair = tk.Button(menu_frame, text="Sair", command=sair_jogo, width=12, bg="light coral", height=1, font=("Arial", 16))
btn_sair.grid(row=0, column=2, padx=10, sticky='ew')

# Configurando o grid para que os botões se expandam
menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=1)
menu_frame.grid_columnconfigure(2, weight=1)

# Configurar o grid para que as linhas e colunas se expandam
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

# Variáveis do jogo
tabuleiro = []
visiveis = []
primeiro_clique = None
segundo_clique = None
botoes = []
tempo_restante = 60  # Inicializando em 60 segundos

janela.mainloop()
