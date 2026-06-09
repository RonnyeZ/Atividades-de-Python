import tkinter as tk
from tkinter import ttk
import re

"""
PROJETO: Identificador de Linguagem de Programação

Este programa simula uma etapa inicial de um compilador: a análise léxica.
Ele recebe um trecho de código e usa expressões regulares, Regex, para
identificar padrões característicos de algumas linguagens de programação.

O código não compila de verdade, ou seja, não gera código de máquina.
Ele apenas analisa o texto e classifica qual linguagem parece mais provável.
"""

# ==================================================
# PARTE DO "COMPILADOR" / ANALISADOR LÉXICO
# ==================================================

# Dicionário com as linguagens suportadas pelo sistema.
# Cada linguagem possui uma lista de padrões Regex.
# Esses padrões representam estruturas comuns de cada linguagem.
linguagens = {
    "Python": [
        r'^\s*def\s+\w+\(.*\):',
        r'^\s*print\(.*\)',
        r'^\s*import\s+\w+',
        r'^\s*if\s+.*:',
        r'^\s*for\s+\w+\s+in\s+.*:',
        r'^\s*#.*'
    ],

    "JavaScript": [
        r'^\s*function\s+\w+\(.*\)\s*\{?',
        r'^\s*console\.log\(.*\);?',
        r'^\s*(let|const|var)\s+\w+',
        r'=>',
        r'^\s*if\s*\(.*\)\s*\{?'
    ],

    "Java": [
        r'^\s*public\s+class\s+\w+',
        r'^\s*public\s+static\s+void\s+main',
        r'^\s*System\.out\.println\(.*\);',
        r'^\s*(int|double|String|boolean)\s+\w+\s*=',
        r'^\s*import\s+java\.'
    ],

    "C": [
        r'^\s*#include\s*<.*>',
        r'^\s*int\s+main\s*\(.*\)',
        r'^\s*printf\(.*\);',
        r'^\s*scanf\(.*\);',
        r'^\s*(int|float|char|double)\s+\w+\s*=',
    ],

    "PHP": [
        r'^\s*<\?php',
        r'^\s*echo\s+.*;',
        r'^\s*\$\w+',
        r'^\s*function\s+\w+\(.*\)\s*\{',
    ]
}


# Função que identifica qual linguagem mais combina
# com o código informado pelo usuário.
def identificar_linguagem(codigo):

    # Dicionário que armazenará a pontuação de cada linguagem.
    pontuacao = {}

    # Percorre cada linguagem cadastrada no dicionário.
    for linguagem, padroes in linguagens.items():

        # Contador de pontos da linguagem atual.
        pontos = 0

        # Percorre cada expressão regular daquela linguagem.
        for padrao in padroes:

            # re.search procura se o padrão Regex aparece no código.
            # O parâmetro re.MULTILINE permite analisar códigos com várias linhas,
            # fazendo o símbolo ^ representar o início de cada linha.
            if re.search(padrao, codigo, re.MULTILINE):

                # Se o padrão for encontrado, a linguagem ganha 1 ponto.
                pontos += 1

        # Salva a pontuação final da linguagem.
        pontuacao[linguagem] = pontos

    # Descobre qual foi a maior pontuação obtida.
    maior_pontuacao = max(pontuacao.values())

    # Se nenhuma linguagem marcou pontos,
    # o sistema considera que não conseguiu identificar.
    if maior_pontuacao == 0:
        return "Linguagem não identificada", pontuacao

    # Lista para guardar linguagens que tiveram a maior pontuação.
    provaveis = []

    # Verifica se uma ou mais linguagens empataram na maior pontuação.
    for linguagem, pontos in pontuacao.items():
        if pontos == maior_pontuacao:
            provaveis.append(linguagem)

    # Se apenas uma linguagem teve a maior pontuação,
    # ela é retornada como resultado final.
    if len(provaveis) == 1:
        return provaveis[0], pontuacao

    # Se mais de uma linguagem teve a mesma pontuação,
    # o resultado é considerado ambíguo.
    else:
        return "Ambíguo: " + ", ".join(provaveis), pontuacao


# Função executada quando o botão de análise é clicado.
def analisar():

    # Captura todo o código digitado pelo usuário.
    codigo = entrada_codigo.get("1.0", tk.END)

    # Chama o analisador léxico.
    resultado, pontuacao = identificar_linguagem(codigo)

    # Exibe o resultado principal na interface.
    resultado_var.set(f"> RESULTADO: {resultado}")

    # Limpa a tabela antes de mostrar uma nova análise.
    for item in tabela.get_children():
        tabela.delete(item)

    # Insere a pontuação de cada linguagem na tabela.
    for linguagem, pontos in pontuacao.items():
        tabela.insert("", tk.END, values=(linguagem, pontos))


# Função usada para limpar a área de código e a tabela.
def limpar():

    # Apaga o código digitado.
    entrada_codigo.delete("1.0", tk.END)

    # Restaura o texto inicial do resultado.
    resultado_var.set("> AGUARDANDO ENTRADA...")

    # Limpa os dados da tabela.
    for item in tabela.get_children():
        tabela.delete(item)


# ==================================================
# INTERFACE
# ==================================================

janela = tk.Tk()
janela.title("Code Language Scanner")
janela.geometry("900x650")
janela.minsize(760, 540)
janela.resizable(True, True)
janela.configure(bg="#0b0f14")


def alternar_tela_cheia(event=None):
    janela.attributes("-fullscreen", not janela.attributes("-fullscreen"))


def sair_tela_cheia(event=None):
    janela.attributes("-fullscreen", False)


janela.bind("<F11>", alternar_tela_cheia)
janela.bind("<Escape>", sair_tela_cheia)

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="#111827",
    foreground="#00ffd5",
    fieldbackground="#111827",
    rowheight=28,
    font=("Consolas", 11)
)

style.configure(
    "Treeview.Heading",
    background="#00ffd5",
    foreground="#0b0f14",
    font=("Consolas", 11, "bold")
)

style.map(
    "Treeview",
    background=[("selected", "#ff00ff")],
    foreground=[("selected", "#ffffff")]
)

container = tk.Frame(janela, bg="#0b0f14")
container.pack(fill="both", expand=True, padx=25, pady=20)

titulo = tk.Label(
    container,
    text="CODE LANGUAGE SCANNER",
    font=("Consolas", 20, "bold"),
    bg="#0b0f14",
    fg="#00ffd5"
)
titulo.pack(pady=(0, 5))

subtitulo = tk.Label(
    container,
    text="Analisador léxico baseado em padrões RegEx",
    font=("Consolas", 10),
    bg="#0b0f14",
    fg="#9ca3af"
)
subtitulo.pack(pady=(0, 20))

frame_codigo = tk.Frame(
    container,
    bg="#111827",
    highlightbackground="#00ffd5",
    highlightthickness=1
)
frame_codigo.pack(fill="x")

label_codigo = tk.Label(
    frame_codigo,
    text="> COLE SEU CÓDIGO ABAIXO:",
    font=("Consolas", 10, "bold"),
    bg="#111827",
    fg="#00ffd5"
)
label_codigo.pack(anchor="w", padx=10, pady=(8, 0))

entrada_codigo = tk.Text(
    frame_codigo,
    height=8,
    font=("Consolas", 12),
    bg="#020617",
    fg="#e5e7eb",
    insertbackground="#00ffd5",
    relief="flat",
    padx=10,
    pady=10,
    wrap=tk.WORD
)
entrada_codigo.pack(fill="both", expand=True, padx=10, pady=10)

frame_botoes = tk.Frame(container, bg="#0b0f14")
frame_botoes.pack(pady=15)

btn_analisar = tk.Button(
    frame_botoes,
    text="EXECUTAR ANÁLISE",
    command=analisar,
    width=22,
    bg="#00ffd5",
    fg="#0b0f14",
    activebackground="#00bfa6",
    activeforeground="#000000",
    font=("Consolas", 10, "bold"),
    relief="flat",
    cursor="hand2"
)
btn_analisar.pack(side="left", padx=6)

btn_limpar = tk.Button(
    frame_botoes,
    text="LIMPAR",
    command=limpar,
    width=14,
    bg="#ff00ff",
    fg="#ffffff",
    activebackground="#c000c0",
    activeforeground="#ffffff",
    font=("Consolas", 10, "bold"),
    relief="flat",
    cursor="hand2"
)
btn_limpar.pack(side="left", padx=6)

resultado_var = tk.StringVar()
resultado_var.set("> AGUARDANDO ENTRADA...")

label_resultado = tk.Label(
    container,
    textvariable=resultado_var,
    font=("Consolas", 13, "bold"),
    bg="#0b0f14",
    fg="#00ff88"
)
label_resultado.pack(pady=10)

tabela = ttk.Treeview(
    container,
    columns=("Linguagem", "Pontos"),
    show="headings",
    height=7
)

tabela.heading("Linguagem", text="LINGUAGEM")
tabela.heading("Pontos", text="PONTUAÇÃO")

tabela.column("Linguagem", width=350, anchor="center")
tabela.column("Pontos", width=180, anchor="center")

tabela.pack(pady=(10, 25), fill="both", expand=True)

rodape = tk.Label(
    container,
    text="STATUS: SISTEMA PRONTO PARA ANÁLISE | F11: TELA CHEIA | ESC: SAIR",
    font=("Consolas", 9),
    bg="#0b0f14",
    fg="#6ee7b7"
)
rodape.pack(pady=(10, 0))

janela.mainloop()
