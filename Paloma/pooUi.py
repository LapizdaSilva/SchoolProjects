import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random

class Item:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.id = random.randint(1000, 9999)

    def usar(self):
        return f"Usando {self.nome} ({self.tipo})"

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo

    def get_id(self):
        return self.id

class Arma(Item):
    def __init__(self, nome, dano):
        super().__init__(nome, "Arma")
        self.dano = dano

    def usar(self):
        return f"Atacou com {self.nome} e causou {self.dano} de dano!"

    def get_atributo(self):
        return self.dano

class Pocao(Item):
    def __init__(self, nome, cura):
        super().__init__(nome, "Poção")
        self.cura = cura

    def usar(self):
        return f"Curou {self.cura} pontos de vida com {self.nome}!"

    def get_atributo(self):
        return self.cura

class Armadura(Item):
    def __init__(self, nome, defesa):
        super().__init__(nome, "Armadura")
        self.defesa = defesa

    def usar(self):
        return f"Equipou {self.nome} (+{self.defesa} de defesa)!"

    def get_atributo(self):
        return self.defesa

# Classe Personagem
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = []

    def adicionar_item(self, item):
        self.inventario.append(item)

    def usar_item(self, item_id):
        for item in self.inventario:
            if item.get_id() == item_id:
                return item.usar()
        return "Item não encontrado no inventário."

    def get_item_por_id(self, item_id):
        for item in self.inventario:
            if item.get_id() == item_id:
                return item
        return None

class SistemaRPG:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema RPG")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.configurar_estilos()
        
        self.personagem = None
        self.item_selecionado = None
        
        self.criar_interface()

    def configurar_estilos(self):
        self.style.configure('Title.TLabel', 
                           font=('Arial', 24, 'bold'),
                           foreground='#ecf0f1',
                           background='#2c3e50')
        
        self.style.configure('Subtitle.TLabel',
                           font=('Arial', 12),
                           foreground='#bdc3c7',
                           background='#2c3e50')
        
        self.style.configure('Modern.TFrame',
                           background='#34495e',
                           relief='flat',
                           borderwidth=2)
        
        self.style.configure('Card.TFrame',
                           background='#ecf0f1',
                           relief='raised',
                           borderwidth=1)
        
        self.style.configure('Modern.TButton',
                           font=('Arial', 10, 'bold'),
                           foreground='white',
                           background='#3498db',
                           borderwidth=0,
                           focuscolor='none')
        
        self.style.map('Modern.TButton',
                      background=[('active', '#2980b9'),
                                ('pressed', '#21618c')])
        
        self.style.configure('Success.TButton',
                           font=('Arial', 10, 'bold'),
                           foreground='white',
                           background='#27ae60',
                           borderwidth=0)
        
        self.style.map('Success.TButton',
                      background=[('active', '#229954'),
                                ('pressed', '#1e8449')])
        
        self.style.configure('Warning.TButton',
                           font=('Arial', 10, 'bold'),
                           foreground='white',
                           background='#e67e22',
                           borderwidth=0)
        
        self.style.map('Warning.TButton',
                      background=[('active', '#d35400'),
                                ('pressed', '#ba4a00')])

    def criar_interface(self):
        main_frame = ttk.Frame(self.root, style='Modern.TFrame')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        title_frame = ttk.Frame(main_frame, style='Modern.TFrame')
        title_frame.pack(fill='x', pady=(0, 20))
        
        title_label = ttk.Label(title_frame, text="Sistema RPG", style='Title.TLabel')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, text="Gerencie seus personagens e inventários", style='Subtitle.TLabel')
        subtitle_label.pack()
        
        container = ttk.Frame(main_frame, style='Modern.TFrame')
        container.pack(fill='both', expand=True)
        
        left_column = ttk.Frame(container, style='Modern.TFrame')
        left_column.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        right_column = ttk.Frame(container, style='Modern.TFrame')
        right_column.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        self.criar_secao_personagem(left_column)
        
        self.criar_secao_itens(left_column)
        
        self.criar_secao_inventario(right_column)
        
        self.criar_secao_mensagens(right_column)

    def criar_secao_personagem(self, parent):
        frame = ttk.LabelFrame(parent, text="Criar Personagem", style='Card.TFrame')
        frame.pack(fill='x', pady=(0, 15))
        
        nome_frame = ttk.Frame(frame)
        nome_frame.pack(fill='x', padx=15, pady=15)
        
        ttk.Label(nome_frame, text="Nome do Personagem:", font=('Arial', 10, 'bold')).pack(anchor='w')
        
        self.entry_nome = ttk.Entry(nome_frame, font=('Arial', 11), width=30)
        self.entry_nome.pack(fill='x', pady=(5, 10))
        self.entry_nome.bind('<Return>', lambda e: self.criar_personagem())
        
        btn_criar = ttk.Button(nome_frame, text="Criar Personagem", 
                              command=self.criar_personagem, style='Modern.TButton')
        btn_criar.pack()
        
        self.label_personagem = ttk.Label(nome_frame, text="Nenhum personagem criado", 
                                         font=('Arial', 9), foreground='#7f8c8d')
        self.label_personagem.pack(pady=(10, 0))

    def criar_secao_itens(self, parent):
        frame = ttk.LabelFrame(parent, text="Adicionar Item", style='Card.TFrame')
        frame.pack(fill='x', pady=(0, 15))
        
        content_frame = ttk.Frame(frame)
        content_frame.pack(fill='x', padx=15, pady=15)
        
        ttk.Label(content_frame, text="Tipo de Item:", font=('Arial', 10, 'bold')).pack(anchor='w')
        self.combo_tipo = ttk.Combobox(content_frame, values=["Arma", "Poção", "Armadura"], 
                                      state="readonly", font=('Arial', 11))
        self.combo_tipo.pack(fill='x', pady=(5, 10))
        self.combo_tipo.bind('<<ComboboxSelected>>', self.atualizar_label_atributo)
        
        ttk.Label(content_frame, text="Nome do Item:", font=('Arial', 10, 'bold')).pack(anchor='w')
        self.entry_nome_item = ttk.Entry(content_frame, font=('Arial', 11))
        self.entry_nome_item.pack(fill='x', pady=(5, 10))
        
        self.label_atributo = ttk.Label(content_frame, text="Atributo:", font=('Arial', 10, 'bold'))
        self.label_atributo.pack(anchor='w')
        self.entry_atributo = ttk.Entry(content_frame, font=('Arial', 11))
        self.entry_atributo.pack(fill='x', pady=(5, 10))
        
        btn_adicionar = ttk.Button(content_frame, text="➕ Adicionar Item", 
                                  command=self.adicionar_item, style='Success.TButton')
        btn_adicionar.pack()

    def criar_secao_inventario(self, parent):
        frame = ttk.LabelFrame(parent, text=" Inventário", style='Card.TFrame')
        frame.pack(fill='both', expand=True, pady=(0, 15))
        
        content_frame = ttk.Frame(frame)
        content_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        list_frame = ttk.Frame(content_frame)
        list_frame.pack(fill='both', expand=True, pady=(0, 10))
        
        columns = ('Nome', 'Tipo', 'Atributo')
        self.tree_inventario = ttk.Treeview(list_frame, columns=columns, show='headings', height=8)
        
        self.tree_inventario.heading('Nome', text='Nome do Item')
        self.tree_inventario.heading('Tipo', text='Tipo')
        self.tree_inventario.heading('Atributo', text='Valor')
        
        self.tree_inventario.column('Nome', width=200)
        self.tree_inventario.column('Tipo', width=100)
        self.tree_inventario.column('Atributo', width=80)
        
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.tree_inventario.yview)
        self.tree_inventario.configure(yscrollcommand=scrollbar.set)
        
        self.tree_inventario.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.tree_inventario.bind('<<TreeviewSelect>>', self.selecionar_item)
        
        btn_usar = ttk.Button(content_frame, text="Usar Item Selecionado", 
                             command=self.usar_item, style='Warning.TButton')
        btn_usar.pack()

    def criar_secao_mensagens(self, parent):
        frame = ttk.LabelFrame(parent, text="Log de Ações", style='Card.TFrame')
        frame.pack(fill='both', expand=True)
        
        content_frame = ttk.Frame(frame)
        content_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        self.text_mensagens = scrolledtext.ScrolledText(content_frame, height=10, 
                                                       font=('Consolas', 10),
                                                       bg='#2c3e50', fg='#ecf0f1',
                                                       insertbackground='#ecf0f1')
        self.text_mensagens.pack(fill='both', expand=True)
        
        self.adicionar_mensagem("Crie um personagem para começar.")

    def atualizar_label_atributo(self, event=None):
        tipo = self.combo_tipo.get()
        if tipo == "Arma":
            self.label_atributo.config(text="Dano:")
        elif tipo == "Poção":
            self.label_atributo.config(text="Cura:")
        elif tipo == "Armadura":
            self.label_atributo.config(text="Defesa:")

    def criar_personagem(self):
        nome = self.entry_nome.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "Digite um nome para o personagem!")
            return
        
        self.personagem = Personagem(nome)
        self.label_personagem.config(text=f"Personagem atual: {nome}", foreground='#27ae60')
        self.entry_nome.delete(0, tk.END)
        self.adicionar_mensagem(f"Personagem '{nome}' foi criado com sucesso!")
        self.atualizar_inventario()

    def adicionar_item(self):
        if not self.personagem:
            messagebox.showwarning("Aviso", "Crie um personagem primeiro!")
            return
        
        tipo = self.combo_tipo.get()
        nome = self.entry_nome_item.get().strip()
        atributo_str = self.entry_atributo.get().strip()
        
        if not tipo or not nome or not atributo_str:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        
        try:
            atributo = int(atributo_str)
            if atributo <= 0:
                raise ValueError()
        except ValueError:
            messagebox.showerror("Erro", "O atributo deve ser um número positivo!")
            return
        
        if tipo == "Arma":
            item = Arma(nome, atributo)
        elif tipo == "Poção":
            item = Pocao(nome, atributo)
        elif tipo == "Armadura":
            item = Armadura(nome, atributo)
        
        self.personagem.adicionar_item(item)
        self.adicionar_mensagem(f"{nome} ({tipo}) foi adicionado ao inventário!")
        
        self.entry_nome_item.delete(0, tk.END)
        self.entry_atributo.delete(0, tk.END)
        self.combo_tipo.set('')
        self.label_atributo.config(text="Atributo:")
        
        self.atualizar_inventario()

    def atualizar_inventario(self):
        for item in self.tree_inventario.get_children():
            self.tree_inventario.delete(item)
        
        if not self.personagem:
            return
        
        for item in self.personagem.inventario:
            emoji = "⚔️" if item.get_tipo() == "Arma" else "💚" if item.get_tipo() == "Poção" else "🛡️"
            nome_com_emoji = f"{emoji} {item.get_nome()}"
            self.tree_inventario.insert('', 'end', values=(nome_com_emoji, item.get_tipo(), item.get_atributo()))

    def selecionar_item(self, event=None):
        selection = self.tree_inventario.selection()
        if selection:
            item_index = self.tree_inventario.index(selection[0])
            if self.personagem and item_index < len(self.personagem.inventario):
                self.item_selecionado = self.personagem.inventario[item_index]

    def usar_item(self):
        if not self.personagem:
            messagebox.showwarning("Aviso", "Crie um personagem primeiro!")
            return
        
        if not self.item_selecionado:
            messagebox.showwarning("Aviso", "Selecione um item para usar!")
            return
        
        resultado = self.item_selecionado.usar()
        self.adicionar_mensagem(resultado)
        
        messagebox.showinfo("Item Usado", resultado)

    def adicionar_mensagem(self, mensagem):
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        mensagem_completa = f"[{timestamp}] {mensagem}\n"
        
        self.text_mensagens.insert(tk.END, mensagem_completa)
        self.text_mensagens.see(tk.END)

    def executar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = SistemaRPG()
    app.executar()