import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def verificador(vetores):
    matriz = np.array(vetores).T
    posto = np.linalg.matrix_rank(matriz)
    if posto == len(vetores):
        return "LI → Linearmente Independentes"
    else:
        return "LD → Linearmente Dependentes"


def mostrar_vetores(vetores):
    cores = ['blue', 'green', 'orange']
    dim = len(vetores[0])

    if dim == 2:
        origem = [0, 0]
        for i, v in enumerate(vetores):
            plt.quiver(
                origem[0], origem[1], v[0], v[1],
                angles='xy', scale_units='xy', scale=1,
                color=cores[i % len(cores)]
            )
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.grid(True)
        plt.axhline(0, color='red')
        plt.axvline(0, color='red')
        plt.gca().set_aspect('equal')
        plt.title("Vetores no plano 2D")
        plt.show()

    elif dim == 3:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        origem = [0, 0, 0]
        for i, v in enumerate(vetores):
            ax.quiver(
                origem[0], origem[1], origem[2],
                v[0], v[1], v[2],
                color=cores[i % len(cores)]
            )
        ax.set_xlim([-10, 10])
        ax.set_ylim([-10, 10])
        ax.set_zlim([-10, 10])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title("Vetores no espaço 3D")
        plt.show()


class VetorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Verificador de Vetores")

        self.frame_tipo = tk.Frame(root)
        self.frame_tipo.pack(pady=10)

        self.label = tk.Label(self.frame_tipo, text="Escolha o espaço vetorial:")
        self.label.pack(side=tk.LEFT)

        self.botao_r2 = tk.Button(self.frame_tipo, text="R²", command=self.set_r2)
        self.botao_r2.pack(side=tk.LEFT, padx=5)

        self.botao_r3 = tk.Button(self.frame_tipo, text="R³", command=self.set_r3)
        self.botao_r3.pack(side=tk.LEFT, padx=5)

        self.entrada_frame = tk.Frame(root)
        self.entrada_frame.pack(pady=10)

        self.entradas = []
        self.vetores = []
        self.dim = 2

        self.botao_verificar = tk.Button(root, text="Verificar e Plotar", command=self.processar)
        self.botao_verificar.pack(pady=10)

        self.resultado_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.resultado_label.pack()

        self.set_r2()

    def limpar_entradas(self):
        for widget in self.entrada_frame.winfo_children():
            widget.destroy()
        self.entradas.clear()

    def set_r2(self):
        self.dim = 2
        self.limpar_entradas()
        for i in range(2):
            label = tk.Label(self.entrada_frame, text=f"Vetor {i+1} (x,y):")
            label.grid(row=i, column=0)
            entrada = tk.Entry(self.entrada_frame, width=20)
            entrada.grid(row=i, column=1)
            self.entradas.append(entrada)

    def set_r3(self):
        self.dim = 3
        self.limpar_entradas()
        for i in range(3):
            label = tk.Label(self.entrada_frame, text=f"Vetor {i+1} (x,y,z):")
            label.grid(row=i, column=0)
            entrada = tk.Entry(self.entrada_frame, width=25)
            entrada.grid(row=i, column=1)
            self.entradas.append(entrada)

    def processar(self):
        self.vetores.clear()
        try:
            for entrada in self.entradas:
                texto = entrada.get().strip()
                valores = list(map(float, texto.split(",")))
                if len(valores) != self.dim:
                    raise ValueError("Número de componentes inválido.")
                self.vetores.append(valores)

            resultado = verificador(self.vetores)
            self.resultado_label.config(text=f"Resultado: {resultado}")
            mostrar_vetores(self.vetores)

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = VetorApp(root)
    root.mainloop()
