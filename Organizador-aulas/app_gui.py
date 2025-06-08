import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from agendamento import ler_aulas, obter_grade_formatada

class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Aulas - Tema Escuro")
        self.root.configure(bg="#1e1e1e")

        fonte = ("Segoe UI", 10)
        cor_fundo = "#1e1e1e"
        cor_texto = "#ffffff"
        cor_botoes = "#333333"
        cor_borda = "#444444"

        self.botao_arquivo = tk.Button(
            root, text="📂 Selecionar arquivo de aulas",
            command=self.abrir_arquivo,
            bg=cor_botoes, fg=cor_texto, font=fonte,
            relief="flat", activebackground="#444"
        )
        self.botao_arquivo.pack(pady=10)

        self.botao_processar = tk.Button(
            root, text="▶️ Organizar Grade",
            command=self.processar_grade,
            state="disabled",
            bg=cor_botoes, fg=cor_texto, font=fonte,
            relief="flat", activebackground="#444"
        )
        self.botao_processar.pack(pady=10)

        self.texto_resultado = scrolledtext.ScrolledText(
            root, width=100, height=30,
            font=("Courier New", 10),
            bg=cor_fundo, fg=cor_texto,
            insertbackground=cor_texto,  # Cor do cursor
            borderwidth=1, relief="solid"
        )
        self.texto_resultado.pack(pady=10)

        self.caminho_arquivo = None

    def abrir_arquivo(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
        if caminho:
            self.caminho_arquivo = caminho
            self.botao_processar.config(state="normal")
            messagebox.showinfo("Arquivo selecionado", f"Arquivo carregado: {caminho}")

    def processar_grade(self):
        try:
            aulas = ler_aulas(self.caminho_arquivo)
            resultado = obter_grade_formatada(aulas)
            self.texto_resultado.delete("1.0", tk.END)
            self.texto_resultado.insert(tk.END, resultado)
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao processar o arquivo:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()
