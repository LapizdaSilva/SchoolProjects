import tkinter as tk

root = tk.Tk()
root.title("Calculadora Simples")
root.minsize(300,300)


resultado = tk.Entry(root, width=45, borderwidth=5)
resultado.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def acao(number):
    op = resultado.get()
    resultado.delete(0, tk.END)
    resultado.insert(0, op + str(number))

def limpa():
    resultado.delete(0, tk.END)

def soma():
    numero1 = resultado.get()
    global num1
    global math
    math = "adicao"
    num1 = int(numero1)
    resultado.delete(0, tk.END)

def menos():
    numero1 = resultado.get()
    global num1
    global math
    math = "menos"
    num1 = int(numero1)
    resultado.delete(0, tk.END)
    
def dividido():
    numero1 = resultado.get()
    global num1
    global math
    math = "divisao"
    num1 = int(numero1)
    resultado.delete(0, tk.END)
    
def vezes():
    numero1 = resultado.get()
    global num1
    global math
    math = "vezes"
    num1 = int(numero1)
    resultado.delete(0, tk.END)

def igual():
    numero2 = resultado.get()
    resultado.delete(0, tk.END)
    try:
        if math == "adicao":
            resultado.insert(0, str(num1 + int(numero2)))
        if math == "menos":
            resultado.insert(0, str(num1 - int(numero2)))
        if math == "vezes":
            resultado.insert(0, str(num1 * int(numero2)))
        if math == "divisao":
            resultado.insert(0, str(num1 / int(numero2)))
    except (ZeroDivisionError):
        resultado.insert(0, "Nâo é possível dividir por Zero")
        
# -----------------------------------------------------------------
botao_0 = tk.Button(root, text="0", padx=40, pady=20, command= lambda: acao(0)) # 0
botao_1 = tk.Button(root, text="1", padx=40, pady=20, command= lambda: acao(1)) # 1
botao_2 = tk.Button(root, text="2", padx=40, pady=20, command= lambda: acao(2)) # 2
botao_3 = tk.Button(root, text="3", padx=40, pady=20, command= lambda: acao(3)) # 3
botao_4 = tk.Button(root, text="4", padx=40, pady=20, command= lambda: acao(4)) # 4
botao_5 = tk.Button(root, text="5", padx=40, pady=20, command= lambda: acao(5)) # 5
botao_6 = tk.Button(root, text="6", padx=40, pady=20, command= lambda: acao(6)) # 6
botao_7 = tk.Button(root, text="7", padx=40, pady=20, command= lambda: acao(7)) # 7 
botao_8 = tk.Button(root, text="8", padx=40, pady=20, command= lambda: acao(8)) # 8
botao_9 = tk.Button(root, text="9", padx=40, pady=20, command= lambda: acao(9)) # 9

botao_plus = tk.Button(root, text="+", padx=40, pady=20, command= lambda: soma()) # +
botao_equal = tk.Button(root, text="=", padx=40, pady=20, command= lambda: igual()) # =
botao_clear = tk.Button(root, text="C", padx=40, pady=20, command= lambda: limpa()) # C
botao_divide = tk.Button(root, text="/", padx=40, pady=20, command= lambda: dividido()) # /
botao_times = tk.Button(root, text="*", padx=40, pady=20, command= lambda: vezes()) # *
botao_minus = tk.Button(root, text="-", padx=40, pady=20, command= lambda: menos()) # -
# -----------------------------------------------------------------

# terceira coluna
botao_1.grid(row=3,column=0)
botao_2.grid(row=3,column=1)
botao_3.grid(row=3,column=2)
botao_plus.grid(row=3,column=3)

# segunda coluna1
botao_4.grid(row=2,column=0)
botao_5.grid(row=2,column=1)
botao_6.grid(row=2,column=2)
botao_minus.grid(row=2,column=3)

# primeira coluna
botao_7.grid(row=1,column=0)
botao_8.grid(row=1,column=1) 
botao_9.grid(row=1,column=2)
botao_times.grid(row=1,column=3)

botao_0.grid(row=4, column=0)
botao_clear.grid(row=4,column=1)
botao_equal.grid(row=4,column=2)
botao_divide.grid(row=4,column=3)

# -----------------------------------------------------------------


root.mainloop()