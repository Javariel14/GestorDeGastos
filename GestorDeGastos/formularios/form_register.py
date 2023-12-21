import tkinter as tk
from tkinter import messagebox

from config import COLOR_CUERPO_PRINCIPAL

class FormRegister():
    def __init__(self, panel_principal, formulario_maestro):
         # Crear paneles: barra superior
        self.barra_superior = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X, expand=False)

        # Crear paneles: barra inferior
        self.ventana_principal = tk.Frame(panel_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.ventana_principal.pack(side=tk.BOTTOM, fill="both", expand=True)

        self.label_title = tk.Label(self.barra_superior, text="Registrar", font=("FontAwesome", 20), bg=COLOR_CUERPO_PRINCIPAL)
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

        etiqueta_password2 = tk.Label(self.ventana_principal, text="Confirmar contraseña:", font=('FontAwesome', 14), bg=COLOR_CUERPO_PRINCIPAL, anchor="w")
        etiqueta_password2.pack(fill=tk.X, padx=20, pady=5)
        self.EntryPassword2 = tk.Entry(self.ventana_principal, font=('FontAwesome', 14))
        self.EntryPassword2.pack(fill=tk.X, padx=20, pady=10)
        self.EntryPassword2.config(show="*")

        inicio = tk.Button(self.ventana_principal, text="Registrar", font=('FontAwesome', 15), bg='#3a7ff6', bd=0, fg="#fff", command=self.validation)
        inicio.pack(fill=tk.X, padx=20, pady=20)

        # Mantén una referencia a la instancia de FormularioMaestroDesign
        self.formulario_maestro = formulario_maestro
    
    def validation(self):
        Usuario = self.EntryUsuario.get()
        Contrasena = self.EntryPassword.get()
        Contrasena2 = self.EntryPassword2.get()

        # Validar si el usuario no ha ingresado nada
        if not Usuario or not Contrasena or not Contrasena2:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        # Validar si la longitud del usuario o contraseña es menor a 3 caracteres
        if len(Usuario) < 3 or len(Contrasena) < 3:
            messagebox.showwarning("Advertencia", "El usuario y la contraseña deben tener al menos 3 caracteres.")
            return

        # Validar si el usuario o contraseña ya existen en el archivo TXT
        with open('./BaseDeDatos/DatosUsuarios.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                existing_user, existing_password = line.strip().split(',')
                if Usuario == existing_user or Contrasena == existing_password:
                    messagebox.showwarning("Advertencia", "El usuario o contraseña ya están registrados.")
                    return

        # Si pasa todas las validaciones, registrar al usuario en el archivo TXT
        with open('./BaseDeDatos/DatosUsuarios.txt', 'a') as file:
            file.write(f"{Usuario}, {Contrasena}\n")
            self.formulario_maestro.abrir_login()
            self.formulario_maestro.ButtonLogin.pack()
            self.formulario_maestro.ButtonRegister.pack_forget()
            messagebox.showinfo("Registro Exitoso", f"Bienvenido, {Usuario}!")
