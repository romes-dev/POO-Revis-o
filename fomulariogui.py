# Criar uma janela simples com o tkinter que tenha um formulário com campos de entrada para nome, email e mensagem. Deve haver um botão para enviar os dados e outro para limpar os campos. A janela deve ter um título, um tamanho específico e uma cor de fundo. Além disso, deve haver um rótulo que exibe uma mensagem de confirmação quando o botão de enviar é clicado.

import tkinter as tk
class FormularioContato:
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Formulário de Contato")
        self.janela.geometry("400x300")
        self.janela.configure(bg="#e4f5f7")

        # Nome
        tk.Label(self.janela, text="Nome:", bg="#e4f5f7", anchor='w').pack(fill="x", padx=20, pady=(20,2))
        self.nome_entry = tk.Entry(self.janela)
        self.nome_entry.pack(fill="x", padx=20, pady=2)

        # Email
        tk.Label(self.janela, text="Email:", bg="#e4f5f7", anchor='w').pack(fill="x", padx=20, pady=(20,2))
        self.email_entry = tk.Entry(self.janela)
        self.email_entry.pack(fill="x", padx=20, pady=2)

        # Mensagem
        tk.Label(self.janela, text="Mensagem:", bg="#e4f5f7", anchor='w').pack(fill="x", padx=20, pady=(20,2))
        self.mensagem_text = tk.Text(self.janela, height=5)
        self.mensagem_text.pack(fill="x", padx=20, pady=2)

        # Botão Enviar e limpar
        self.enviar_button = tk.Button(self.janela, text="Enviar", command=self.enviar)
        self.enviar_button.pack(side="left", padx=20, pady=20)
        self.limpar_button = tk.Button(self.janela, text="Limpar", command=self.limpar)
        self.limpar_button.pack(side="right", padx=20, pady=20)

        # Janela de confirmação
        self.confirmacao = tk.Label(self.janela, text="", bg="#e4f5f7", fg="green")
        self.confirmacao.pack(pady=(10, 0))

        self.janela.mainloop()

    def enviar(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        mensagem = self.mensagem_text.get("1.0", tk.END).strip()

        if nome and email and mensagem:
            self.confirmacao.config(text="Dados enviados com sucesso!", fg="green")
        else:
            self.confirmacao.config(text="Por favor, preencha todos os campos.", fg="red")
    
    def limpar(self):
        self.nome_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.mensagem_text.delete("1.0", tk.END)
        self.confirmacao.config(text="")


if __name__ == "__main__":
    formulario = FormularioContato()
    