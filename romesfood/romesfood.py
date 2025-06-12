import tkinter as tk
from tkinter import messagebox
import sys
import os

def resource_path(rel_path):
    """Ajusta o caminho para imagens no PyInstaller e no script normal."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)

class Produto:
    def __init__(self, nome, preco, icone):
        self.nome = nome
        self.preco = preco
        self.icone = icone

class Lanchonete:
    def __init__(self):
        self.pedidos = []  # (Produto, qtd)
        self.produtos = []
        self.icones = []   # Lista para manter referências

        self.janela = tk.Tk()
        self.janela.title("Pedidos da Lanchonete")
        self.janela.geometry("540x400")
        self.janela.configure(bg="#ffe0b2")  # laranja claro

        # Ícone principal da janela (opcional)
        try:
            icone_principal = tk.PhotoImage(file=resource_path("imgs/hamburguer.png"))
            icone_principal = icone_principal.subsample(2, 2)  # Reduz para metade
            self.janela.iconphoto(True, icone_principal)
        except Exception:
            pass

        # Título
        tk.Label(self.janela, text="Gerenciador de Pedidos", bg="#ffe0b2", font=("Arial", 20, "bold")).pack(pady=10)

        # Frame de produtos
        frame_prod = tk.Frame(self.janela, bg="#ffe0b2")
        frame_prod.pack()

        # Adicionando produtos
        self.add_produto("Hambúrguer", 15.00, "imgs/hamburguer.png", frame_prod, 0)
        self.add_produto("Batata Frita", 8.00, "imgs/batata.png", frame_prod, 1)
        self.add_produto("Refrigerante", 6.00, "imgs/refrigerante.png", frame_prod, 2)

        # Lista de pedidos
        frame_pedidos = tk.LabelFrame(self.janela, text="Carrinho", bg="#ffe0b2", font=("Arial", 12, "bold"))
        frame_pedidos.pack(pady=20, padx=10, fill="both", expand=True)

        self.lista_pedidos = tk.Listbox(frame_pedidos, font=("Arial", 12), height=7)
        self.lista_pedidos.pack(side="left", fill="both", expand=True, padx=10, pady=5)

        tk.Button(frame_pedidos, text="Remover Selecionado", command=self.remover, bg="#d84315", fg="white", font=("Arial", 10, "bold")).pack(side="left", padx=8)

        # Total e finalizar
        frame_total = tk.Frame(self.janela, bg="#ffe0b2")
        frame_total.pack(pady=5, fill="x")

        self.label_total = tk.Label(frame_total, text="Total: R$ 0.00", bg="#ffe0b2", font=("Arial", 14, "bold"))
        self.label_total.pack(side="left", padx=10)

        tk.Button(frame_total, text="Finalizar Pedido", command=self.finalizar, bg="#388e3c", fg="white", font=("Arial", 12, "bold")).pack(side="right", padx=15)

        self.janela.mainloop()

    def add_produto(self, nome, preco, img_path, frame, coluna):
        try:
            icone = tk.PhotoImage(file=resource_path(img_path))
            icone = icone.subsample(2, 2)  # Reduz o tamanho pela metade
        except Exception:
            icone = tk.PhotoImage()  # Vazio se der erro
        self.icones.append(icone)  # Manter referência viva

        produto = Produto(nome, preco, icone)
        self.produtos.append(produto)

        # Botão com ícone
        botao = tk.Button(
            frame,
            image=icone,
            text=f"\n{nome}\nR$ {preco:.2f}",
            compound="top",
            font=("Arial", 10, "bold"),
            bg="#fff3e0", activebackground="#ffcc80",
            bd=2, relief="raised",
            command=lambda p=produto: self.adicionar(p)
        )
        botao.grid(row=0, column=coluna, padx=18, pady=5)

    def adicionar(self, produto):
        # Procurar no carrinho e somar se já houver
        for idx, (prod, qtd) in enumerate(self.pedidos):
            if prod.nome == produto.nome:
                self.pedidos[idx] = (prod, qtd + 1)
                self.atualizar_lista()
                return
        self.pedidos.append((produto, 1))
        self.atualizar_lista()

    def remover(self):
        selecionado = self.lista_pedidos.curselection()
        if not selecionado:
            messagebox.showinfo("Info", "Selecione um item para remover.")
            return
        idx = selecionado[0]
        del self.pedidos[idx]
        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_pedidos.delete(0, tk.END)
        for prod, qtd in self.pedidos:
            self.lista_pedidos.insert(tk.END, f"{prod.nome} x{qtd} - R$ {prod.preco*qtd:.2f}")
        self.atualizar_total()

    def atualizar_total(self):
        total = sum(prod.preco * qtd for prod, qtd in self.pedidos)
        self.label_total.config(text=f"Total: R$ {total:.2f}")

    def finalizar(self):
        if not self.pedidos:
            messagebox.showinfo("Info", "Carrinho vazio!")
            return
        total = sum(prod.preco * qtd for prod, qtd in self.pedidos)
        resumo = "\n".join([f"- {prod.nome} x{qtd} = R$ {prod.preco*qtd:.2f}" for prod, qtd in self.pedidos])
        mensagem = f"Resumo do Pedido:\n{resumo}\n\nTOTAL: R$ {total:.2f}\n\nObrigado pela preferência!"
        messagebox.showinfo("Pedido Finalizado", mensagem)
        self.pedidos.clear()
        self.atualizar_lista()

if __name__ == "__main__":
    Lanchonete()
