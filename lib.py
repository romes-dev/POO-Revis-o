import tkinter as tk

class JanelaCustomizada:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Minha Janela Personalizada")
        self.janela.geometry("400x200")               # largura x altura
        self.janela.configure(bg="#e0f7fa")           # cor de fundo (exemplo: azul claro)

        # Rótulo para mensagem
        self.label = tk.Label(self.janela, text="", bg="#e0f7fa", font=("Arial", 14))
        self.label.pack(pady=30)

        # Botão para mostrar mensagem
        self.botao_msg = tk.Button(self.janela, text="Mostrar Mensagem", command=self.mostrar_mensagem)
        self.botao_msg.pack(pady=5)

        # Botão para fechar janela
        self.botao_fechar = tk.Button(self.janela, text="Fechar Janela", command=self.janela.destroy)
        self.botao_fechar.pack(pady=5)

        self.janela.mainloop()

    def mostrar_mensagem(self):
        self.label.config(text="Olá, seja bem-vindo ao Tkinter!")

if __name__ == "__main__":
    JanelaCustomizada()
