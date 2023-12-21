import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import datetime

from config import COLOR_CUERPO_PRINCIPAL

from formularios.form_login import FormLogin as Login

class FormularioFlujoDinero():
    def __init__(self, panel_principal):
        self.Meses = {
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
        self.anios = list(range(2020, 2031))

        self.barra_ingresos = self.crear_barra(panel_principal, COLOR_CUERPO_PRINCIPAL, tk.LEFT)
        self.barra_egresos = self.crear_barra(panel_principal, COLOR_CUERPO_PRINCIPAL, tk.RIGHT)

        self.componentes_ingresos()
        self.componentes_egresos()

    def crear_barra(self, panel, color, side):
        barra = tk.Frame(panel, bg=color)
        barra.pack(side=side, fill=tk.BOTH, expand=True)
        return barra

    def agregar_componente(self, frame, text, side=tk.TOP):
        label = tk.Label(frame, text=text, bg=COLOR_CUERPO_PRINCIPAL)
        label.pack(side=side, fill=tk.NONE)
        entry = tk.Entry(frame, justify="center")
        entry.pack(side=side, fill=tk.NONE)
        entry.insert(0, "0")
        entry.bind("<FocusIn>", self.limpiar_submensaje)
        entry.bind("<FocusOut>", self.restaurar_submensaje)
        return entry

    def limpiar_submensaje(self, event):
        entry = event.widget
        if entry.get() == "0":
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def restaurar_submensaje(self, event):
        entry = event.widget
        if not entry.get():
            entry.delete(0, tk.END)
            entry.insert(0, "0")
            entry.config(fg='black')

    def componentes_ingresos(self):
        self.labelingresos = tk.Label(self.barra_ingresos, text="Ingresos", bg=COLOR_CUERPO_PRINCIPAL, font=('arial black', 20))
        self.labelingresos.pack()
        
        self.EntrySueldo = self.agregar_componente(self.barra_ingresos, "Sueldo")
        self.EntryNegocio = self.agregar_componente(self.barra_ingresos, "Negocios")
        self.EntryInversiones = self.agregar_componente(self.barra_ingresos, "Inversiones")
        self.EntryPensiones = self.agregar_componente(self.barra_ingresos, "Pensiones")

        self.labelmes = tk.Label(self.barra_ingresos, text="Ingrese el mes actual", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelmes.place(relx=0.35, rely=0.5)

        self.ComboBoxMes = Combobox(self.barra_ingresos, value=list(self.Meses.values()), state="readonly")
        self.ComboBoxMes.set(self.traducir_mes(datetime.now().strftime("%B")))
        self.ComboBoxMes.place(relx=0.35, rely=0.55)

        self.labelanio = tk.Label(self.barra_ingresos, text="Ingrese el año a registrar", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelanio.place(relx=0.35, rely=0.60)

        self.ComboBoxAnio = Combobox(self.barra_ingresos, values=self.anios)
        self.ComboBoxAnio.place(relx=0.35, rely=0.65)
        self.ComboBoxAnio.set(datetime.now().year)

        self.buttonregister = tk.Button(self.barra_ingresos, text="Registrar", command=self.validation)
        self.buttonregister.place(relx=0.45, rely=0.70)

    def componentes_egresos(self):
        self.labelegresos = tk.Label(self.barra_egresos, text="Egresos", bg=COLOR_CUERPO_PRINCIPAL, font=('arial black', 16))
        self.labelegresos.pack()
        self.labelalquiler = tk.Label(self.barra_egresos, text="Alquiler / Hipoteca", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelalquiler.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryAlquiler = tk.Entry(self.barra_egresos, justify="center")
        self.EntryAlquiler.pack(side=tk.TOP, fill = tk.NONE)
        self.labelprestamos = tk.Label(self.barra_egresos, text="Préstamos / Créditos", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelprestamos.pack(side=tk.TOP, fill = tk.NONE)
        self.Entryprestamos = tk.Entry(self.barra_egresos, justify="center")
        self.Entryprestamos.pack(side=tk.TOP, fill = tk.NONE)
        self.labeltarjeta = tk.Label(self.barra_egresos, text="Tarjeta de crédito", bg=COLOR_CUERPO_PRINCIPAL)
        self.labeltarjeta.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryTarjetaCredito = tk.Entry(self.barra_egresos, justify="center")
        self.EntryTarjetaCredito.pack(side=tk.TOP, fill = tk.NONE)
        self.labelseguros = tk.Label(self.barra_egresos, text="Seguros", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelseguros.pack(side=tk.TOP, fill = tk.NONE)
        self.EntrySeguro = tk.Entry(self.barra_egresos, justify="center")
        self.EntrySeguro.pack(side=tk.TOP, fill = tk.NONE)
        self.labeltelefonia = tk.Label(self.barra_egresos, text="Telefonía", bg=COLOR_CUERPO_PRINCIPAL)
        self.labeltelefonia.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryCelular = tk.Entry(self.barra_egresos, justify="center")
        self.EntryCelular.pack(side=tk.TOP, fill = tk.NONE)
        self.labeltransporte = tk.Label(self.barra_egresos, text="Transporte / Gasolina", bg=COLOR_CUERPO_PRINCIPAL)
        self.labeltransporte.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryTransporte = tk.Entry(self.barra_egresos, justify="center")
        self.EntryTransporte.pack(side=tk.TOP, fill = tk.NONE)
        self.labelbasicos = tk.Label(self.barra_egresos, text="Servicios básicos", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelbasicos.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryServiciosBasicos = tk.Entry(self.barra_egresos, justify="center")
        self.EntryServiciosBasicos.pack(side=tk.TOP, fill = tk.NONE)
        self.labelropa = tk.Label(self.barra_egresos, text="Vestido y calzado", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelropa.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryRopa = tk.Entry(self.barra_egresos, justify="center")
        self.EntryRopa.pack(side=tk.TOP, fill = tk.NONE)
        self.labelcomida = tk.Label(self.barra_egresos, text="Alimentación", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelcomida.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryComida = tk.Entry(self.barra_egresos, justify="center")
        self.EntryComida.pack(side=tk.TOP, fill = tk.NONE)
        self.labellimpieza = tk.Label(self.barra_egresos, text="Limpieza / Hogar", bg=COLOR_CUERPO_PRINCIPAL)
        self.labellimpieza.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryLimpieza = tk.Entry(self.barra_egresos, justify="center")
        self.EntryLimpieza.pack(side=tk.TOP, fill = tk.NONE)
        self.labelocio = tk.Label(self.barra_egresos, text="Ocio", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelocio.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryOcio = tk.Entry(self.barra_egresos, justify="center")
        self.EntryOcio.pack(side=tk.TOP, fill = tk.NONE)
        self.labelvarios = tk.Label(self.barra_egresos, text="Varios", bg=COLOR_CUERPO_PRINCIPAL)
        self.labelvarios.pack(side=tk.TOP, fill = tk.NONE)
        self.EntryVarios = tk.Entry(self.barra_egresos, justify="center")
        self.EntryVarios.pack(side=tk.TOP, fill = tk.NONE)

        # Asignar 0 por defecto a los Entry de egresos
        self.EntryAlquiler.insert(0, "0")
        self.Entryprestamos.insert(0, "0")
        self.EntryTarjetaCredito.insert(0, "0")
        self.EntrySeguro.insert(0, "0")
        self.EntryCelular.insert(0, "0")
        self.EntryTransporte.insert(0, "0")
        self.EntryServiciosBasicos.insert(0, "0")
        self.EntryRopa.insert(0, "0")
        self.EntryComida.insert(0, "0")
        self.EntryLimpieza.insert(0, "0")
        self.EntryOcio.insert(0, "0")
        self.EntryVarios.insert(0, "0")

        # Asignar eventos a los Entry de egresos
        self.EntryAlquiler.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryAlquiler.bind("<FocusOut>", self.restaurar_submensaje)
        self.Entryprestamos.bind("<FocusIn>", self.limpiar_submensaje)
        self.Entryprestamos.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryTarjetaCredito.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryTarjetaCredito.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntrySeguro.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntrySeguro.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryCelular.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryCelular.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryTransporte.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryTransporte.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryServiciosBasicos.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryServiciosBasicos.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryRopa.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryRopa.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryComida.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryComida.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryLimpieza.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryLimpieza.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryOcio.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryOcio.bind("<FocusOut>", self.restaurar_submensaje)
        self.EntryVarios.bind("<FocusIn>", self.limpiar_submensaje)
        self.EntryVarios.bind("<FocusOut>", self.restaurar_submensaje)

    def validation(self):
        try:
            sueldo = int(self.EntrySueldo.get())
            negocios = int(self.EntryNegocio.get())
            inversiones = int(self.EntryInversiones.get())
            pensiones = int(self.EntryPensiones.get())
            Ingresos = abs(sueldo + negocios + inversiones + pensiones)
        except ValueError:
            messagebox.showwarning("Advertencia", "Ingrese valores numéricos válidos en los ingresos.")
            return

        try:
            egresos_entries = [
                self.EntryAlquiler, self.Entryprestamos, self.EntryTarjetaCredito, self.EntrySeguro,
                self.EntryCelular, self.EntryTransporte, self.EntryServiciosBasicos, self.EntryRopa,
                self.EntryComida, self.EntryLimpieza, self.EntryOcio, self.EntryVarios
            ]

            Egresos = sum([int(entry.get()) for entry in egresos_entries])
        except ValueError:
            messagebox.showwarning("Advertencia", "Ingrese valores numéricos válidos en los egresos.")

        total = Ingresos - Egresos

        mes_select = self.ComboBoxMes.get()
        anio_select = self.ComboBoxAnio.get()

        usuario = Login.get_usuario()

        # Verifica si esta el campo del mes y el año completado
        if not mes_select or not anio_select:
            messagebox.showinfo("Advertencia", "Por favor, complete el mes y el año.")
            return
        
        # Comprobar si ya existe el mes y año en el archivo
        with open("./BaseDeDatos/FlujoEconomico.txt", "r") as fichero:
            lineas = fichero.readlines()
        
        # Comprobar si ya existe el mes y año en el archivo
        with open("./BaseDeDatos/FlujoEconomico.txt", "w") as fichero:
            reemplazado = False  
            for linea in lineas:
                user, mes, anio, _, _, _ = linea.strip().split(', ')
                if mes == mes_select and anio == anio_select and usuario == user:
                    respuesta = messagebox.askyesno("Registro existente", f"Ya existe un registro para {mes_select}, {anio_select}. ¿Desea reemplazarlo?")
                    if respuesta:
                        fichero.write(f"{usuario}, {mes_select}, {anio_select}, {total}, {Ingresos}, {Egresos}\n")
                        reemplazado = True
                    else:
                        fichero.write(linea)
                else:
                    fichero.write(linea)

            # Si no se reemplazó ningún valor, agregar la nueva entrada
            if not reemplazado:
                messagebox.showinfo("Listo", f"Registro de {mes_select} guardado")
                fichero.write(f"{usuario}, {mes_select}, {anio_select}, {total}, {Ingresos}, {Egresos}\n")

    def traducir_mes(self, mes_ingles):
        return self.Meses.get(mes_ingles, mes_ingles)
    