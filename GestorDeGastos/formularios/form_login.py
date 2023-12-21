import tkinter as tk
from tkinter import messagebox

from config import COLOR_CUERPO_PRINCIPAL

class FormLogin():
    def __init__(self, panel_principal, formulario_maestro):

         # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.ventana_principal = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.ventana_principal.pack(side=tk.BOTTOM, fill="both", expand=True)

        self.label_title = tk.Label(self.barra_superior, text="Iniciar sesión", font=("FontAwesome", 20), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_title.pack(side=tk.TOP, fill="both", expand=True)
       
        etiqueta_usuario = tk.Label(self.ventana_principal, text="Usuario:", font=('FontAwesome', 14), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.EntryUsuario = tk.Entry(self.ventana_principal, font=('FontAwesome', 14))
        self.EntryUsuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(self.ventana_principal, text="Contraseña:", font=('FontAwesome', 14), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.EntryPassword = tk.Entry(self.ventana_principal, font=('FontAwesome', 14))
        self.EntryPassword.pack(fill=tk.X, padx=20, pady=10)
        self.EntryPassword.config(show="*")

        inicio = tk.Button(self.ventana_principal, text="Iniciar sesión", font=('FontAwesome', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.verificar)
        inicio.pack(fill=tk.X, padx=20, pady=20)
            
        # Mantén una referencia a la instancia de FormularioMaestroDesign
        self.formulario_maestro = formulario_maestro
            
    """Validación de login"""

    def verificar(self):
        global usuario
        try:
            usuario = self.EntryUsuario.get()
            password = self.EntryPassword.get()
            found = False
        except ValueError:
            messagebox.showerror("ERROR", "Ingrese los datos de manera correcta")

        with open("./BaseDeDatos/DatosUsuarios.txt", "r") as fichero:
            for linea in fichero:
                elementos = linea.strip().split(',')
                user_real = elementos[0] 
                password_real = elementos[1]
                user_real = user_real.replace(" ","")
                password_real = password_real.replace(" ","")
                if usuario == user_real and password == password_real:
                    found = True
                    break
                
        if found:
            messagebox.showinfo("Correcto", f"Bienvenido {usuario}")
            self.formulario_maestro.abrir_FlujodeDinero()
            self.formulario_maestro.ButtonFlujoDinero.pack()
            self.formulario_maestro.ButtonEstadisticas.pack()
            self.formulario_maestro.ButtonLogOut.pack(side=tk.BOTTOM)
            self.formulario_maestro.ButtonLogin.pack_forget()
            self.formulario_maestro.ButtonRegister.pack_forget()
        else:
            self.EntryUsuario.delete(0, "end")
            self.EntryPassword.delete(0, "end")
            messagebox.showerror("Incorrecto", "Usuario o contraseña incorrectos")
    
    @staticmethod
    def get_usuario():
        return usuario
