import tkinter as tk
from tkinter import messagebox

# Classes de Item
class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def usa(self):
        return f"Usando {self.nome} ({self.tipo})"

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo


class Arma(Item):
    def __init__(self, nome, dano):
        super().__init__(nome, "arma")
        self.dano = dano

    def usa(self):
        return f"Atacou com {self.nome} e causou {self.dano} de dano!"


class Pocao(Item):
    def __init__(self, nome, cura):
        super().__init__(nome, "poção")
        self.cura = cura

    def usa(self):
        return f"Curou {self.cura} pontos de vida com {self.nome}!"


class Armadura(Item):
    def __init__(self, nome, defesa):
        super().__init__(nome, "armadura")
        self.defesa = defesa

    def usa(self):
        return f"Equipou {self.nome} (+{self.defesa} de defesa)!"


# Classe Personagem
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = []

    def adicionar_item(self, item):
        self.inventario.append(item)

    def listar_itens(self):
        return [(item.get_nome(), item.get_tipo()) for item in self.inventario]

    def usar_item(self, nome_item):
        for item in self.inventario:
            if item.get_nome() == nome_item:
                return item.usa()
        return f"Item {nome_item} não encontrado no inventário."


# Criando personagem e adicionando itens
heroi = Personagem("Aragorn")
heroi.adicionar_item(Arma("Espada Andúril", dano=27))
heroi.adicionar_item(Pocao("Poção de Cura", cura=30))
heroi.adicionar_item(Armadura("Armadura de Mithril", defesa=25))


# ---------------- UI com Tkinter ----------------
def usar_item():
    try:
        indice = lista_itens.curselection()[0]
        nome_item = heroi.inventario[indice].get_nome()
        resultado = heroi.usar_item(nome_item)
        messagebox.showinfo("Ação", resultado)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione um item para usar.")


# Janela principal
janela = tk.Tk()
janela.title("Inventário do Herói")
janela.geometry("300x300")

# Título
titulo = tk.Label(janela, text=f"Inventário de {heroi.nome}", font=("Arial", 14))
titulo.pack(pady=10)

# Lista de Itens
lista_itens = tk.Listbox(janela, height=8)
lista_itens.pack(pady=10, fill=tk.BOTH, expand=True)

# Preenche lista
for nome, tipo in heroi.listar_itens(): x
lista_itens.insert(tk.END, f"{nome} ({tipo})")

# Botão para usar item
botao_usar = tk.Button(janela, text="Usar Item", command=usar_item)
botao_usar.pack(pady=10)

# Rodar janela
janela.mainloop()
