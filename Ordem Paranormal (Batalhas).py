import tkinter as tk

class Personagem:
    def __init__(self, nome, vida, sanidade, iniciativa):
        self.nome = nome
        self.vida = vida
        self.vida_inicial = vida
        self.sanidade = sanidade
        self.sanidade_inicial = sanidade
        self.iniciativa = iniciativa

class Jogo:
    def __init__(self):
        self.personagens = {}
        self.root = tk.Tk()
        self.root.title("When the night falls - @jordaozz")
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.label_nome = tk.Label(self.frame, text="Personagem:")
        self.label_nome.grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)
        self.label_vida = tk.Label(self.frame, text="Vida:")
        self.label_vida.grid(row=1, column=0)
        self.vida_entry = tk.Entry(self.frame)
        self.vida_entry.grid(row=1, column=1)
        self.label_sanidade = tk.Label(self.frame, text="Sanidade:")
        self.label_sanidade.grid(row=2, column=0)
        self.sanidade_entry = tk.Entry(self.frame)
        self.sanidade_entry.grid(row=2, column=1)
        self.label_iniciativa = tk.Label(self.frame, text="Iniciativa:")
        self.label_iniciativa.grid(row=3, column=0)
        self.iniciativa_entry = tk.Entry(self.frame)
        self.iniciativa_entry.grid(row=3, column=1)

        self.add_button = tk.Button(self.frame, text="Adicionar Personagem", command=self.adicionar_personagem)
        self.add_button.grid(row=4, columnspan=3)

    def adicionar_personagem(self):
        nome = self.nome_entry.get() 
        vida = int(self.vida_entry.get())
        sanidade = int(self.sanidade_entry.get())
        iniciativa = int(self.iniciativa_entry.get())
        personagem = Personagem(nome, vida, sanidade, iniciativa)
        self.personagens[nome] = personagem
        self.ordenar_personagens_por_iniciativa()
        self.atualizar_interface()

    def ordenar_personagens_por_iniciativa(self):
        self.personagens = dict(sorted(self.personagens.items(), key=lambda x: x[1].iniciativa, reverse=True))

    def atualizar_interface(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for i, personagem in enumerate(self.personagens.values()):
            label_nome = tk.Label(self.frame, text=personagem.nome)
            label_nome.grid(row=i, column=0)
            label_vida = tk.Label(self.frame, text=str(personagem.vida))
            label_vida.grid(row=i, column=1)
            label_sanidade = tk.Label(self.frame, text=str(personagem.sanidade))
            label_sanidade.grid(row=i, column=2)
            label_iniciativa = tk.Label(self.frame, text=str(personagem.iniciativa))
            label_iniciativa.grid(row=i, column=3)

            if personagem.vida == 0:
                label_status = tk.Label(self.frame, text="Morrendo")
                label_status.grid(row=i, column=3)
            elif personagem.vida < 0:  
                label_status = tk.Label(self.frame, text="ERRO")
                label_status.grid(row=i, column=3)
            elif personagem.vida <= personagem.vida_inicial / 2:
                label_status = tk.Label(self.frame, text="Machucado")
                label_status.grid(row=i, column=3)
            elif personagem.vida > personagem.vida_inicial:
                label_status = tk.Label(self.frame, text="Sobrevida")
                label_status.grid(row=i, column=3)
            elif personagem.vida == personagem.vida_inicial:
                label_status = tk.Label(self.frame, text="Full")
                label_status.grid(row=i, column=3)
            else:
                label_status = tk.Label(self.frame, text="--")
                label_status.grid(row=i, column=3)

            if personagem.sanidade == 0:
                label_status = tk.Label(self.frame, text="Louco")
                label_status.grid(row=i, column=4)
            elif personagem.sanidade < 0:
                label_status = tk.Label(self.frame, text="ERRO")
                label_status.grid(row=i, column=4)
            elif personagem.sanidade == personagem.sanidade_inicial:
                label_status = tk.Label(self.frame, text="Full")
                label_status.grid(row=i, column=4)
            elif personagem.sanidade <= personagem.sanidade_inicial / 3:
                label_status = tk.Label(self.frame, text="Enlouquecendo")
                label_status.grid(row=i, column=4)
            else:
                label_status = tk.Label(self.frame, text="--")
                label_status.grid(row=i, column=4)

            botao_menos = tk.Button(self.frame, text="-V", command=lambda p=personagem: self.diminuir_vida(p))
            botao_menos.grid(row=i, column=5)
            botao_mais = tk.Button(self.frame, text="+V", command=lambda p=personagem: self.aumentar_vida(p))
            botao_mais.grid(row=i, column=6)

            botao_menos = tk.Button(self.frame, text="-S", command=lambda p=personagem: self.diminuir_sanidade(p))
            botao_menos.grid(row=i, column=7)
            botao_mais = tk.Button(self.frame, text="+S", command=lambda p=personagem: self.aumentar_sanidade(p))
            botao_mais.grid(row=i, column=8)

        self.label_nome = tk.Label(self.frame, text="Personagem:")
        self.label_nome.grid(row=len(self.personagens), column=0)
        self.nome_entry = tk.Entry(self.frame)
        self.nome_entry.grid(row=len(self.personagens), column=1)
        self.label_vida = tk.Label(self.frame, text="Vida:")
        self.label_vida.grid(row=len(self.personagens) + 1, column=0)
        self.vida_entry = tk.Entry(self.frame)
        self.vida_entry.grid(row=len(self.personagens) + 1, column=1)
        self.label_sanidade = tk.Label(self.frame, text="Sanidade:")
        self.label_sanidade.grid(row=len(self.personagens) + 2, column=0)
        self.sanidade_entry = tk.Entry(self.frame)
        self.sanidade_entry.grid(row=len(self.personagens) + 2, column=1)
        self.label_iniciativa = tk.Label(self.frame, text="Iniciativa:")
        self.label_iniciativa.grid(row=len(self.personagens) + 3, column=0)
        self.iniciativa_entry = tk.Entry(self.frame)
        self.iniciativa_entry.grid(row=len(self.personagens) + 3, column=1)

        self.add_button = tk.Button(self.frame, text="Adicionar Personagem", command=self.adicionar_personagem)
        self.add_button.grid(row=len(self.personagens) + 4, columnspan=3)

    def diminuir_vida(self, personagem):
        personagem.vida -= 1
        self.atualizar_interface()

    def aumentar_vida(self, personagem):
        personagem.vida += 1
        self.atualizar_interface()
    
    def diminuir_sanidade(self, personagem):
        personagem.sanidade -= 1
        self.atualizar_interface()

    def aumentar_sanidade(self, personagem):
        personagem.sanidade += 1
        self.atualizar_interface()

if __name__ == "__main__":
    jogo = Jogo()
    jogo.root.mainloop()
