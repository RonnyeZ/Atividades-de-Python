import tkinter as tk

def verificar():
    entrada = entry.get().strip()
    resultado_texto.set("")
    log_texto.set("")

    # 👉 Validação de campo vazio
    if entrada == "":
        resultado_texto.set("⚠ ERRO: Digite uma cadeia antes de verificar!")
        resultado_label.config(fg="#f59e0b")  # amarelo
        return

    mensagens = []
    tem_invalido = False

    for caracter in entrada:
        if caracter in ["0", "1"]:
            mensagens.append(f"✔ {caracter} válido")
        else:
            mensagens.append(f"✖ {caracter} inválido")
            tem_invalido = True

    log_texto.set("\n".join(mensagens))

    # 👉 Se tiver caractere inválido
    if tem_invalido:
        resultado_texto.set("⚠ ERRO: Cadeia contém caractere inválido!")
        resultado_label.config(fg="#f59e0b")
        return

    # 👉 Se tudo válido
    q0 = entrada[-1]

    if q0 == "1":
        resultado_texto.set("✅ SUCESSO: Terminou em 1")
        resultado_label.config(fg="#22c55e")
    else:
        resultado_texto.set("❌ FRACASSO: Terminou em 0")
        resultado_label.config(fg="#ef4444")


# Janela
janela = tk.Tk()
janela.title("Verificador Binário")
janela.geometry("420x350")
janela.configure(bg="#0f172a")

frame = tk.Frame(janela, bg="#1e293b", padx=20, pady=20)
frame.pack(pady=20)

titulo = tk.Label(
    frame,
    text="🔍 Verificador de Cadeia Binária",
    font=("Segoe UI", 14, "bold"),
    fg="#e2e8f0",
    bg="#1e293b"
)
titulo.pack(pady=(0, 15))

entry = tk.Entry(
    frame,
    font=("Segoe UI", 12),
    width=25,
    justify="center",
    bd=0,
    bg="#334155",
    fg="white",
    insertbackground="white"
)
entry.pack(pady=5, ipady=6)

botao = tk.Button(
    frame,
    text="Verificar",
    command=verificar,
    font=("Segoe UI", 11, "bold"),
    bg="#3b82f6",
    fg="white",
    activebackground="#2563eb",
    bd=0,
    padx=10,
    pady=5,
    cursor="hand2"
)
botao.pack(pady=15)

resultado_texto = tk.StringVar()
resultado_label = tk.Label(
    frame,
    textvariable=resultado_texto,
    font=("Segoe UI", 12, "bold"),
    bg="#1e293b"
)
resultado_label.pack(pady=5)

log_texto = tk.StringVar()
log = tk.Label(
    frame,
    textvariable=log_texto,
    font=("Consolas", 10),
    justify="left",
    bg="#1e293b",
    fg="#cbd5f5"
)
log.pack(pady=10)

janela.mainloop()