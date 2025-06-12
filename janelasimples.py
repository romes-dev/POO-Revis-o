# Eu quero criar uma janela simples com o tkinter que precise clicar em um botão para fechar a janela e outro botão para exibir uma mensagem. A janela deve ter um título, um tamanho específico e uma cor de fundo. Além disso, deve haver um rótulo que exibe a mensagem quando o botão correspondente é clicado.

"""
1-> Janela com título "Minha Janela", tamanho 300x200, cor de fundo colorido.
2-> Botão "Fechar a janela" que fecha a janela ao ser clicado.
3-> Botão "Exibir mensagem" que exibe uma mensagem em um rótulo quando clicado.
4-> Rótulo vazio que será atualizado com a mensagem quando o botão correspondente for clicado.


"""

import tkinter as tk
class JanelaSimples:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Minha Janela")
        self.janela.geometry("300x200")
        self.janela.configure(bg="#b3f4b4")

        self.botao_fechar = tk.Button(self.janela, text="Fechar a janela", command=self.janela.destroy)
        self.botao_exibir_mensagem = tk.Button(self.janela, text="Exibir mensagem", command=self.mostrar_mensagem)

        self.botao_fechar.pack(pady=20)
        self.botao_exibir_mensagem.pack(pady=20)

        self.label = tk.Label(self.janela, text="")
        self.label.pack(pady=10)

        self.janela.mainloop()

    def mostrar_mensagem(self):
        self.label.config(text="Você clicou no botão!")

if __name__ == "__main__":
    JanelaSimples()