import tkinter as tk
from tkinter import messagebox, simpledialog

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class CaixaSupermercado:
    def __init__(self):
        self.produtos = []         # Lista de todos produtos cadastrados
        self.carrinho = []         # Lista de tuplas: (produto, quantidade)

        
        self.janela = tk.Tk()
        self.janela.title("Caixa de Supermercado")
        self.janela.geometry("600x500")
        self.janela.configure(bg="#f5f5f5")
        icone = tk.PhotoImage(file="icons/shopping-cart.png") 
        self.janela.iconphoto(True, icone) 

        # -------- CADASTRO DE PRODUTO --------
        frame_cadastro = tk.LabelFrame(self.janela, text="Cadastro de Produto", bg="#f5f5f5", padx=10, pady=10)
        frame_cadastro.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_cadastro, text="Nome:", bg="#f5f5f5").grid(row=0, column=0)
        self.nome_entry = tk.Entry(frame_cadastro)
        self.nome_entry.grid(row=0, column=1)

        tk.Label(frame_cadastro, text="Preço (R$):", bg="#f5f5f5").grid(row=0, column=2)
        self.preco_entry = tk.Entry(frame_cadastro)
        self.preco_entry.grid(row=0, column=3)

        tk.Button(frame_cadastro, text="Cadastrar Produto", command=self.cadastrar_produto, bg="#1976d2", fg="white").grid(row=0, column=4, padx=10)

        # -------- LISTA DE PRODUTOS CADASTRADOS --------
        frame_lista = tk.LabelFrame(self.janela, text="Produtos Disponíveis", bg="#f5f5f5", padx=10, pady=10)
        frame_lista.pack(padx=10, pady=5, fill="x")

        self.lista_produtos = tk.Listbox(frame_lista, height=5)
        self.lista_produtos.pack(side="left", fill="x", expand=True)
        tk.Button(frame_lista, text="Adicionar ao Carrinho", command=self.adicionar_carrinho, bg="#388e3c", fg="white").pack(side="left", padx=10)

        # -------- CARRINHO DE COMPRAS --------
        frame_carrinho = tk.LabelFrame(self.janela, text="Carrinho de Compras", bg="#f5f5f5", padx=10, pady=10)
        frame_carrinho.pack(padx=10, pady=10, fill="x")

        self.lista_carrinho = tk.Listbox(frame_carrinho, height=8)
        self.lista_carrinho.pack(side="left", fill="both", expand=True)
        tk.Button(frame_carrinho, text="Remover Selecionado", command=self.remover_item, bg="#d32f2f", fg="white").pack(side="left", padx=10)

        # -------- TOTAL E FINALIZAR --------
        frame_total = tk.Frame(self.janela, bg="#f5f5f5")
        frame_total.pack(fill="x", padx=10, pady=10)

        self.label_total = tk.Label(frame_total, text="Total: R$ 0.00", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#1976d2")
        self.label_total.pack(side="left", padx=10)

        tk.Button(frame_total, text="Finalizar Venda", command=self.finalizar_venda, bg="#ffb300", fg="black", font=("Arial", 12, "bold")).pack(side="right", padx=10)

        self.janela.mainloop()

    def cadastrar_produto(self):
        nome = self.nome_entry.get().strip()
        try:
            preco = float(self.preco_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido.")
            return
        if not nome or preco <= 0:
            messagebox.showerror("Erro", "Preencha os campos corretamente.")
            return
        produto = Produto(nome, preco)
        self.produtos.append(produto)
        self.atualizar_lista_produtos()
        self.nome_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)

    def atualizar_lista_produtos(self):
        self.lista_produtos.delete(0, tk.END)
        for idx, prod in enumerate(self.produtos):
            self.lista_produtos.insert(tk.END, f"{prod.nome} - R$ {prod.preco:.2f}")

    def adicionar_carrinho(self):
        selecionado = self.lista_produtos.curselection()
        if not selecionado:
            messagebox.showinfo("Info", "Selecione um produto para adicionar.")
            return
        idx = selecionado[0]
        produto = self.produtos[idx]
        # Perguntar quantidade
        qtd = simpledialog.askinteger("Quantidade", f"Quantos '{produto.nome}'?", minvalue=1, initialvalue=1)
        if qtd:
            # Se já está no carrinho, só aumenta a quantidade
            for i, (prod, quantidade) in enumerate(self.carrinho):
                if prod == produto:
                    self.carrinho[i] = (prod, quantidade + qtd)
                    break
            else:
                self.carrinho.append((produto, qtd))
            self.atualizar_carrinho()
            self.atualizar_total()

    def atualizar_carrinho(self):
        self.lista_carrinho.delete(0, tk.END)
        for prod, qtd in self.carrinho:
            self.lista_carrinho.insert(tk.END, f"{prod.nome} x{qtd} - R$ {prod.preco*qtd:.2f}")

    def remover_item(self):
        selecionado = self.lista_carrinho.curselection()
        if not selecionado:
            messagebox.showinfo("Info", "Selecione um item para remover.")
            return
        idx = selecionado[0]
        del self.carrinho[idx]
        self.atualizar_carrinho()
        self.atualizar_total()

    def atualizar_total(self):
        total = sum(prod.preco * qtd for prod, qtd in self.carrinho)
        self.label_total.config(text=f"Total: R$ {total:.2f}")

    def finalizar_venda(self):
        if not self.carrinho:
            messagebox.showinfo("Info", "Carrinho vazio!")
            return
        total = sum(prod.preco * qtd for prod, qtd in self.carrinho)
        mensagem = "Itens da compra:\n"
        for prod, qtd in self.carrinho:
            mensagem += f"- {prod.nome} x{qtd} = R$ {prod.preco*qtd:.2f}\n"
        mensagem += f"\nTOTAL: R$ {total:.2f}\n\nVenda finalizada com sucesso!"
        messagebox.showinfo("Venda Finalizada", mensagem)
        self.carrinho.clear()
        self.atualizar_carrinho()
        self.atualizar_total()

if __name__ == "__main__":
    CaixaSupermercado()
