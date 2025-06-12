import tkinter as tk

class MinhaJanela:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Minha Janela")
        self.botao = tk.Button(self.janela, text="Fechar a janela", command=self.janela.destroy)
        self.botoademensagem = tk.Button(self.janela, text="Exibir mensagem", command=self.mostrar_mensagem)
        self.botao.pack(pady=20)
        self.botoademensagem.pack(pady=20)
        self.label = tk.Label(self.janela, text="")
        self.label.pack(pady=10)
        self.janela.geometry("300x200")
        self.janela.configure(bg="#f0f0f0")
        self.janela.mainloop()
    
    def mostrar_mensagem(self):
        self.label.config(text="Você clicou no botão!")


if __name__ == "__main__":
    MinhaJanela()




