import tkinter as tk

from config import COLOR_CUERPO_PRINCIPAL

class FormularioInformacionDesign():
    def __init__(self, panel_principal):
        # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.ventana_principal = tk.Frame(panel_principal)
        self.ventana_principal.pack(side=tk.BOTTOM, fill="both", expand=True)

        self.labelTitulo = tk.Label(self.barra_superior, text=f"Gestor de gastos personales")
        self.labelTitulo.config(fg="#222d33", font=("Roboto", 30), bg=COLOR_CUERPO_PRINCIPAL)
        self.labelTitulo.pack(side=tk.TOP, fill="both", expand=True)

        self.labelExplicativo = tk.Label(self.ventana_principal, text="Bienvenido a este gestor. Aquí puedes gestionar tus gastos personales y mantener una contabilidad de los gastos registrados.")
        self.labelExplicativo.config(fg="#222d33", font=("Roboto", 16), bg=COLOR_CUERPO_PRINCIPAL, wraplength=(500))
        self.labelExplicativo.pack(side=tk.TOP, fill="both", expand=True)
