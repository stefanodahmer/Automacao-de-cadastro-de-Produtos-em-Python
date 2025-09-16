import tkinter as tk
from tkinter import messagebox
import random

# --- Configurações principais ---
LARGURA_JANELA = 520
ALTURA_JANELA = 300
MARGEM = 10              # margem interna para o botão não "escapar" da janela
DISTANCIA_FUGA = 80      # distância mínima do mouse para o botão "Não"

def centralizar_janela(win, w, h):
    win.update_idletasks()
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

def mover_botao_nao(aleatorio=True, mouse_x=None, mouse_y=None):
    root.update_idletasks()
    bw = btn_nao.winfo_width()
    bh = btn_nao.winfo_height()
    cw = root.winfo_width()
    ch = root.winfo_height()

    max_x = max(MARGEM, cw - bw - MARGEM)
    max_y = max(MARGEM, ch - bh - MARGEM)

    if aleatorio or mouse_x is None or mouse_y is None:
        novo_x = random.randint(MARGEM, max_x)
        novo_y = random.randint(MARGEM + 40, max_y)  # +40 para não colidir com o texto
    else:
        # Tenta empurrar para o lado oposto do mouse
        cur_x = btn_nao.winfo_x()
        cur_y = btn_nao.winfo_y()
        dx = cur_x - mouse_x
        dy = cur_y - mouse_y
        # se vetor nulo, joga aleatório
        if dx == 0 and dy == 0:
            novo_x = random.randint(MARGEM, max_x)
            novo_y = random.randint(MARGEM + 40, max_y)
        else:
            passo = 120
            novo_x = cur_x + (passo if dx <= 0 else -passo)
            novo_y = cur_y + (passo if dy <= 0 else -passo)
            # limita nos limites da janela; se bater, joga aleatório
            if not (MARGEM <= novo_x <= max_x and MARGEM + 40 <= novo_y <= max_y):
                novo_x = random.randint(MARGEM, max_x)
                novo_y = random.randint(MARGEM + 40, max_y)

    btn_nao.place(x=novo_x, y=novo_y)

def on_mouse_move(event):
    # faz o botão "Não" fugir quando o mouse chega perto
    bx = btn_nao.winfo_x() + btn_nao.winfo_width() // 2
    by = btn_nao.winfo_y() + btn_nao.winfo_height() // 2
    dist = ((event.x - bx) ** 2 + (event.y - by) ** 2) ** 0.5
    if dist < DISTANCIA_FUGA:
        mover_botao_nao(aleatorio=False, mouse_x=event.x, mouse_y=event.y)

def on_nao_hover(event):
    mover_botao_nao()

def on_nao_click():
    # Se por acaso clicarem, ele foge mesmo assim 😅
    mover_botao_nao()

def on_sim_click():
    messagebox.showinfo("", "Sabia que tu ia dizer sim! ")

# --- UI ---
root = tk.Tk()
root.title("Fica comigo pra sempre?")
root.resizable(False, False)
centralizar_janela(root, LARGURA_JANELA, ALTURA_JANELA)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

label = tk.Label(
    frame,
    text="Fica comigo pra sempre?",
    font=("Segoe UI", 18, "bold"),
    pady=20
)
label.pack()

# Botões
btn_sim = tk.Button(frame, text="Sim 💘", font=("Segoe UI", 12), command=on_sim_click, cursor="hand2")
btn_sim.place(x=150, y=180)

btn_nao = tk.Button(frame, text="Não ", font=("Segoe UI", 12), takefocus=0, cursor="spider")  # cursor engraçado
btn_nao.place(x=300, y=180)

# Eventos para o botão "Não" fugir
btn_nao.bind("<Enter>", on_nao_hover)
btn_nao.bind("<Button-1>", lambda e: on_nao_click())
root.bind("<Motion>", on_mouse_move)

root.mainloop()
