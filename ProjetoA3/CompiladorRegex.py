import tkinter as tk
from tkinter import ttk
import re


"""
==================================================
PARTE DO COMPILADOR / ANALISADOR LÉXICO
==================================================
"""

# Dicionário com as linguagens suportadas pelo sistema.
# Cada linguagem possui uma lista de padrões Regex.
# Esses padrões representam estruturas comuns de cada linguagem.
linguagens = {
    "Python": [
        r'^\s*[a-zA-Z_]\w*\s*=\s*.*',
        r'^\s*input\w*\s*=',
        r'^\s*def\s+[a-zA-Z_]\w*\s*\(.*\)\s*:',
        r'^\s*class\s+[a-zA-Z_]\w*\s*:',
        r'^\s*print\s*\(.*\)',
        r'^\s*(?:import\s+[a-zA-Z_]\w*|from\s+[a-zA-Z_]\w*\s+import\s+.*)',
        r'^\s*(?:if|elif)\s+.*:',
        r'^\s*else\s*:',
        r'^\s*for\s+[a-zA-Z_]\w*\s+in\s+.*:',
        r'^\s*while\s+.*:',
        r'^\s*(?:try|finally)\s*:',
        r'^\s*except\s+.*:',
        r'^\s*with\s+.*\s+as\s+[a-zA-Z_]\w*\s*:',
        r'^\s*return\s+.*',
    ],

    "JavaScript": [
        r'^\s*function\s+[a-zA-Z_$][\w$]*\s*\(.*\)\s*\{?',
        r'^\s*console\.(?:log|error|warn)\s*\(.*\)\s*;?',
        r'^\s*(?:let|const|var)\s+[a-zA-Z_$][\w$]*',
        r'^\s*(?:if|while)\s*\(.*\)\s*\{?',
        r'^\s*else\s*\{?',
        r'^\s*for\s*\(.*;.*;.*\)\s*\{?',
        r'^\s*document\.(?:getElementById|querySelector)\s*\(.*\)',
        r'^\s*addEventListener\s*\(.*\)',
        r'^\s*import\s+.*\s+from\s+.*;?',
        r'^\s*export\s+default\s+.*',
        r'^\s*class\s+[a-zA-Z_$][\w$]*\s*\{?'
    ],

    "Java": [
        r'^\s*(?:public|private|protected)\s+class\s+[a-zA-Z_]\w*',
        r'^\s*public\s+static\s+void\s+main\s*\(',
        r'^\s*System\.out\.print(?:ln)?\s*\(.*\)\s*;',
        r'^\s*(?:int|double|float|String|boolean|char|long)\s+[a-z_]\w*\s*=\s*.*;',
        r'^\s*(?:public|private|protected)\s+(?:static\s+)?(?:void|int|double|float|String|boolean|char|long)\s+[a-zA-Z_]\w*\s*\(',
        r'^\s*import\s+java\..*;',
        r'^\s*package\s+[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*\s*;',
    ],

    "C": [
        r'^\s*#include\s*<[^>]+>',
        r'^\s*#define\s+[a-zA-Z_]\w*',
        r'^\s*int\s+main\s*\(.*\)',
        r'^\s*(?:printf|scanf)\s*\(.*\)\s*;',
        r'^\s*(?:int|float|char|double|long)\s+[a-z_]\w*\s*=\s*.*;',
        r'^\s*(?:int|float|char|double|void)\s+[a-z_]\w*\s*\(.*\)\s*\{?',
        r'^\s*free\s*\(.*\)\s*;',
        r'^\s*return\s+0\s*;'
    ],

    "PHP": [
        r'^\s*<\?php',
        r'^\s*\?>',
        r'^\s*(?:echo|print)\s+.*;',
        r'^\s*\$[a-zA-Z_]\w*\s*=\s*.*;',
        r'^\s*function\s+[a-zA-Z_]\w*\s*\(.*\)\s*\{',
        r'^\s*(?:if|while)\s*\(.*\)\s*\{?',
        r'^\s*foreach\s*\(.*\s+as\s+.*\)\s*\{?',
        r'^\s*class\s+[a-zA-Z_]\w*',
        r'^\s*(?:public|private|protected)\s+function\s+[a-zA-Z_]\w*\s*\(',
        r'^\s*(?:include|require)(?:_once)?\s+[\'"].*[\'"]\s*;'
    ],

    "C#": [
        r'^\s*using\s+(?:System|UnityEngine)\s*;',
        r'^\s*namespace\s+[a-zA-Z_]\w*',
        r'^\s*(?:public|private|protected)\s+class\s+[a-zA-Z_]\w*',
        r'^\s*(?:public\s+)?static\s+void\s+Main\s*\(',
        r'^\s*Console\.(?:WriteLine|ReadLine)\s*\(.*\)\s*;',
        r'^\s*(?:int|float|double|string|bool|char|long)\s+[a-z_]\w*\s*=\s*.*;',
        r'^\s*var\s+[a-zA-Z_]\w*\s*=',
        r'^\s*(?:public|private|protected)\s+(?:static\s+)?(?:void|int|float|double|string|bool|char|long)\s+[a-zA-Z_]\w*\s*\(',
        r'^\s*public\s+(?:int|float|double|string|bool|char|long)\s+[a-zA-Z_]\w*\s*\{',
        r'^\s*List<.*>\s+[a-zA-Z_]\w*',
        r'^\s*new\s+[a-zA-Z_]\w*\s*\(.*\)\s*;',
        r'^\s*void\s+(?:Start|Update|Awake|FixedUpdate)\s*\(',
        r'^\s*Debug\.Log\s*\(.*\)\s*;',
    ]
}

# Função responsável por analisar uma linha de código
# e descobrir qual linguagem mais combina com ela.
def identificar_linguagem(codigo):

    # Dicionário que guarda quantos padrões cada linguagem conseguiu reconhecer.
    pontuacao = {}

    # Percorre cada linguagem cadastrada.
    for linguagem, padroes in linguagens.items():

        pontos = 0

        # Percorre os Regex da linguagem atual.
        for padrao in padroes:

            # re.search verifica se o padrão aparece no código.
            # Neste projeto, a função normalmente recebe uma linha por vez,
            if re.search(padrao, codigo, re.MULTILINE):
                pontos += 1

        # Salva a quantidade de padrões encontrados para aquela linguagem.
        pontuacao[linguagem] = pontos

    # Pega a maior pontuação obtida entre todas as linguagens.
    maior_pontuacao = max(pontuacao.values())

    # Se nenhuma linguagem marcou ponto, a linha não foi reconhecida.
    if maior_pontuacao == 0:
        return "Linguagem não identificada", pontuacao

    # Guarda todas as linguagens que tiveram a maior pontuação.
    provaveis = []

    for linguagem, pontos in pontuacao.items():
        if pontos == maior_pontuacao:
            provaveis.append(linguagem)

    # Se só uma linguagem venceu, retorna ela.
    if len(provaveis) == 1:
        return provaveis[0], pontuacao

    # Se mais de uma linguagem empatou, retorna todas como ambíguas.
    else:
        return "Ambíguo: " + ", ".join(provaveis), pontuacao


# Função executada ao clicar no botão de análise.
# Ela pega o texto completo, divide em linhas e analisa uma por uma.
def analisar():

    codigo = entrada_codigo.get("1.0", tk.END)

    # Divide o texto em linhas.
    # Cada linha será tratada como um trecho de código separado.
    linhas = codigo.splitlines()

    # Dicionário que guarda quais linhas foram identificadas para cada linguagem.
    linhas_por_linguagem = {}

    # Cria uma lista vazia para cada linguagem cadastrada.
    for linguagem in linguagens.keys():
        linhas_por_linguagem[linguagem] = []

    # Também guarda linhas que não foram reconhecidas.
    linhas_por_linguagem["Linguagem não identificada"] = []

    # Analisa cada linha digitada.
    for linha in linhas:

        # Ignora linhas vazias.
        if linha.strip() == "":
            continue

        # Identifica a linguagem mais provável da linha.
        resultado, pontuacao = identificar_linguagem(linha)

        # Se a linha for ambígua, ela será adicionada
        # em todas as linguagens que empataram.
        if resultado.startswith("Ambíguo"):

            linguagens_ambiguas = resultado.replace("Ambíguo: ", "").split(", ")

            for linguagem in linguagens_ambiguas:
                linhas_por_linguagem[linguagem].append(linha)

        # Se não houver ambiguidade, a linha vai somente
        # para a linguagem identificada.
        else:
            linhas_por_linguagem[resultado].append(linha)

    # Limpa os resultados antigos da tabela.
    for item in tabela.get_children():
        tabela.delete(item)

    # Preenche a tabela com itens expansíveis.
    for linguagem, linhas_detectadas in linhas_por_linguagem.items():

        quantidade = len(linhas_detectadas)

        # Item pai: mostra o nome da linguagem e a quantidade de linhas detectadas.
        item_pai = tabela.insert(
            "",
            tk.END,
            values=(linguagem, quantidade),
            open=False
        )

        # Itens filhos: aparecem quando o usuário expande a linguagem.
        # Eles mostram quais linhas foram classificadas naquela linguagem.
        for linha in linhas_detectadas:
            tabela.insert(
                item_pai,
                tk.END,
                values=("   " + linha, "")
            )

    resultado_var.set("> RESULTADO: ANÁLISE CONCLUÍDA")


# Função usada para limpar o campo de entrada e a tabela de resultados.
def limpar():

    entrada_codigo.delete("1.0", tk.END)

    resultado_var.set("> AGUARDANDO ENTRADA...")

    for item in tabela.get_children():
        tabela.delete(item)


# ==================================================
# INTERFACE
# ==================================================

janela = tk.Tk()
janela.title("Code Language Scanner")
janela.geometry("1366x768")
janela.minsize(760, 540)
janela.resizable(True, True)
janela.configure(bg="#0b0f14")


def alternar_tela_cheia(event=None):
    janela.attributes("-fullscreen", not janela.attributes("-fullscreen"))
    janela.after(100, redimensionar_canvas)
    janela.after(200, redimensionar_canvas)


def sair_tela_cheia(event=None):
    janela.attributes("-fullscreen", False)
    janela.after(100, redimensionar_canvas)
    janela.after(200, redimensionar_canvas)

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

MARGEM_X = 100
MARGEM_Y = 20

canvas = tk.Canvas(
    janela,
    bg="#0b0f14",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    janela,
    orient="vertical",
    command=canvas.yview
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

container = tk.Frame(
    canvas,
    bg="#0b0f14",
    padx=MARGEM_X,
    pady=MARGEM_Y
)

canvas_window = canvas.create_window(
    (0, 0),
    window=container,
    anchor="nw"
)


def atualizar_scroll(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))


def redimensionar_canvas(event=None):
    largura_canvas = canvas.winfo_width()

    canvas.coords(canvas_window, 0, 0)
    canvas.itemconfig(canvas_window, width=largura_canvas)

    atualizar_scroll()


def scroll_mouse(event):
    primeiro, ultimo = canvas.yview()

    if event.delta > 0 and primeiro <= 0:
        return

    if event.delta < 0 and ultimo >= 1:
        return

    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


container.bind("<Configure>", atualizar_scroll)
canvas.bind("<Configure>", redimensionar_canvas)
canvas.bind_all("<MouseWheel>", scroll_mouse)

titulo = tk.Label(
    container,
    text="CODE LANGUAGE SCANNER",
    font=("Consolas", 20, "bold"),
    bg="#0b0f14",
    fg="#00ffd5"
)
titulo.pack(pady=(20, 25))

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

frame_tabela = tk.Frame(
    container,
    bg="#111827",
    height=250
)

frame_tabela.pack(
    fill="x",
    padx=100,
    pady=20
)

frame_tabela.pack_propagate(False)


tabela = ttk.Treeview(
    container,
    columns=("Linguagem", "Pontos"),
    show="tree headings",
    height=7
)

tabela.heading("#0", text="")
tabela.heading("Linguagem", text="LINGUAGEM / CÓDIGO")
tabela.heading("Pontos", text="QUANTIDADE")

tabela.column("#0", width=40, anchor="center")
tabela.column("Linguagem", width=550, anchor="w")
tabela.column("Pontos", width=180, anchor="center")

tabela.pack(
    in_=frame_tabela,
    fill="both",
    expand=True
)

rodape = tk.Label(
    container,
    text="STATUS: SISTEMA PRONTO PARA ANÁLISE | F11: TELA CHEIA | ESC: SAIR",
    font=("Consolas", 9),
    bg="#0b0f14",
    fg="#6ee7b7"
)
rodape.pack(pady=(10, 0))

janela.mainloop()
