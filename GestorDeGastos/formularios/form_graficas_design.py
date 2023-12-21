import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from config import COLOR_CUERPO_PRINCIPAL
from formularios.form_login import FormLogin as Login

class FormularioGraficasDesign():

    def __init__(self, panel_principal):
        # Crear dos subgráficos usando Matplotlib
        figura = Figure(figsize=(8, 6), dpi=100)
        self.ax1 = figura.add_subplot(211)
        
        # Ajustar la distribución para agregar espacio de separación en el eje Y
        figura.subplots_adjust(hspace=0.4)

        # Variable de control para almacenar la selección del usuario
        self.año_seleccionado = tk.StringVar()

        # Interfaz de usuario para seleccionar el año
        self.label_año = tk.Label(panel_principal, text="Seleccione el año:", bg= COLOR_CUERPO_PRINCIPAL)
        self.label_año.pack()

        # Obtener la lista de años desde la función obtener_datos_flujo_economico
        años = list(range(2020, 2031))

        # Menú desplegable para seleccionar el año
        self.combo_año = ttk.Combobox(panel_principal, values=años, textvariable=self.año_seleccionado)
        self.combo_año.pack()

        # Establecer el año actual como valor predeterminado
        self.año_seleccionado.set(datetime.now().year)

        # Botón para actualizar las estadísticas
        self.boton_actualizar = tk.Button(panel_principal, text="Actualizar Estadísticas", command=self.actualizar_estadisticas)
        self.boton_actualizar.pack()

        # Graficar en los subgráficos
        self.grafico1(self.ax1)

        # Agregar los gráficos a la ventana de Tkinter
        canvas = FigureCanvasTkAgg(figura, master=panel_principal)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def obtener_datos_flujo_economico(self, año=None):
        # Leer el archivo de flujo económico y obtener los datos
        datos = {'Enero': 0, 'Febrero': 0, 'Marzo': 0, 'Abril': 0, 'Mayo': 0, 'Junio': 0, 'Julio': 0, 'Agosto': 0, 'Septiembre': 0, 'Octubre': 0, 'Noviembre': 0, 'Diciembre': 0}
        try:
            with open("./BaseDeDatos/FlujoEconomico.txt", "r") as fichero:
                for linea in fichero:
                    usuario, mes, año_registro, total, _, _, = linea.strip().split(', ')
                    mes = self.traducir_mes(mes)
                    if (año is None or año_registro == año) and usuario == Login.get_usuario():
                        datos[mes] += int(total)
        except FileNotFoundError:
            # Manejar el caso en que el archivo no existe
            print("El archivo de flujo económico no existe.")
        return datos

    def grafico1(self, ax):
        datos = self.obtener_datos_flujo_economico(año=self.año_seleccionado.get())
        x = list(datos.keys())
        y = list(datos.values())
        x_posiciones = range(len(x))
        ax.bar(x_posiciones, y, label='Ganancias mensuales', color='blue', alpha=0.7)
        ax.set_title(f'Estadistica del año {self.año_seleccionado.get()}')
        ax.set_xlabel('Mes')
        ax.set_ylabel('Total')
        ax.legend()

        # Añadir etiquetas a cada barra
        for i, v in enumerate(y):
            ax.text(x_posiciones[i] - 0.1, v + 0.1, str(v), color='black')

        # Añadir etiquetas de mes en el eje x
        ax.set_xticks(x_posiciones)
        ax.set_xticklabels(x, rotation=45, ha='right')

        # Añadir cuadrícula
        ax.grid(axis='y', linestyle='--', alpha=0.7)

    def traducir_mes(self, mes_ingles):
        Meses = {
            "January": "Enero", 
            "February": "Febrero", 
            "March": "Marzo", 
            "April": "Abril",
            "May": "Mayo", 
            "June": "Junio", 
            "July": "Julio", 
            "August": "Agosto",
            "September": "Septiembre", 
            "October": "Octubre", 
            "November": "Noviembre", 
            "December": "Diciembre"
        }
        return Meses.get(mes_ingles, mes_ingles)

    def actualizar_estadisticas(self):
        año_seleccionado = self.año_seleccionado.get()
        entrada_encontrada = False
        with open("./BaseDeDatos/FlujoEconomico.txt", "r") as fichero:
            for linea in fichero:
                usuario, _, año_registro, _, _, _ = linea.strip().split(', ')
                if usuario == Login.get_usuario() and año_registro == año_seleccionado:
                    entrada_encontrada = True
                    break

        if entrada_encontrada:
            self.ax1.clear()
            self.grafico1(self.ax1)
            canvas = self.ax1.figure.canvas
            canvas.draw()
        else:
            # Si no se encuentra una entrada, mostrar un mensaje
            messagebox.showinfo("Sin datos", f"No hay datos registrados para el usuario en el año {año_seleccionado}.")
