import tkinter as tk
from tkinter import messagebox
# Importamos a sua função do seu arquivo pessoal
from ferramentas import divisores 

def acao_divisores():
    try:
        # Pega o valor da caixa de entrada
        num = int(entrada_numero.get())
        # Chama sua função matemática
        resultado = divisores(num)
        # Exibe no label de resultado
        label_resultado.config(text=f"Divisores de {num}:\n{resultado}", fg="blue")
    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, digite um número inteiro válido.")

def acao_limpar():
    """Função para o botão 'Voltar ao Início' / Limpar"""
    entrada_numero.delete(0, tk.END)
    label_resultado.config(text="O resultado aparecerá aqui", fg="gray")

# 1. Criar a janela principal
app = tk.Tk()
app.title("Painel Matemático - Prof. Helder")
app.geometry("450x400")
app.configure(bg="#f0f0f0")

# 2. Título e Instruções
tk.Label(app, text="Dashboard de Matemática", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
tk.Label(app, text="Informe um número para calcular:", bg="#f0f0f0").pack()

# 3. Campo de Entrada (Input)
entrada_numero = tk.Entry(app, font=("Arial", 14), justify="center")
entrada_numero.pack(pady=10)

# 4. Área de Botões (Container)
frame_botoes = tk.Frame(app, bg="#f0f0f0")
frame_botoes.pack(pady=10)

# Botão Divisores
btn_div = tk.Button(frame_botoes, text="Ver Divisores", command=acao_divisores, width=15, bg="#e1e1e1")
btn_div.grid(row=0, column=0, padx=5, pady=5)

# Botão para Futura Função (Exemplo: Primos)
btn_futuro = tk.Button(frame_botoes, text="Em breve...", state="disabled", width=15)
btn_futuro.grid(row=0, column=1, padx=5, pady=5)

# 5. Área de Exibição de Resultados
label_resultado = tk.Label(app, text="O resultado aparecerá aqui", font=("Arial", 10), 
                           wraplength=400, bg="white", width=50, height=5, relief="sunken")
label_resultado.pack(pady=20)

# 6. Botão de Reset (Voltar ao início) sempre visível embaixo
btn_reset = tk.Button(app, text="🔄 Limpar / Início", command=acao_limpar, bg="#ffcccb", width=20)
btn_reset.pack(side="bottom", pady=20)

# Iniciar o Loop da Interface (O que mantém a janela aberta)
app.mainloop()