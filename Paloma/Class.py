class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def usa(self):
        print(f"Usando {self.nome} ({self.tipo})")

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo


class Arma(Item):
    def __init__(self, nome, dano):
        super().__init__(nome, "arma")
        self.dano = dano

    def usa(self):
        print(f"Atacou com {self.nome} e causou {self.dano} de dano!")


class Pocao(Item):
    def __init__(self, nome, cura):
        super().__init__(nome, "poção")
        self.cura = cura

    def usa(self):
        print(f"Curou {self.cura} pontos de vida com {self.nome}!")


class Armadura(Item):
    def __init__(self, nome, defesa):
        super().__init__(nome, "armadura")
        self.defesa = defesa

    def usa(self):
        print(f"Equipou {self.nome} (+{self.defesa} de defesa)!")


class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = []

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"Item {item.get_nome()} adicionado ao inventário.")

    def listar_itens(self):
        if not self.inventario:
            print("O inventário está vazio.")
            return
        print("Itens no inventário:")
        for item in self.inventario:
            print(f"- {item.get_nome()} ({item.get_tipo()})")


    def usar_item(self, nome_item):
        for item in self.inventario:
            if item.get_nome() == nome_item:
                item.usa()
                return
        print(f"Item {nome_item} não encontrado no inventário.")


heroi = Personagem("Aragorn")
heroi.adicionar_item(Arma("Espada Andúril", dano=27))
heroi.adicionar_item(Pocao("Poção de Cura", cura=30))
heroi.adicionar_item(Armadura("Armadura de Mithril", defesa=25))
heroi.listar_itens()

print("\nEm sua jornada:")
heroi.usar_item("Espada Andúril")
heroi.usar_item("Poção de Cura")
heroi.usar_item("Armadura de Mithril")
heroi.usar_item("Pões") 