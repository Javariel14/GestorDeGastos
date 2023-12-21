# import tkinter as tk
# from tkinter import font

# import util.util_ventana as util_ventana
# import util.util_imagenes as util_img

# from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA

# from formularios.form_informacion_Design import FormularioInformacionDesign
# from formularios.form_login import Form_Login
# from formularios.form_register import Form_Register
# from formularios.form_graficas_design import FormularioGraficasDesign
# from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
# from formularios.form_info_design import FormularioInfoDesign
# from formularios.form_FlujoDinero import FormularioFlujoDinero

# class FormularioMaestroDesign(tk.Tk):

#     def __init__(self):
#         super().__init__()
#         self.perfil = util_img.leer_imagen("./imagenes/Perfil.jpg", (100, 100))
#         self.img_sitio_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (200, 200))
#         self.menu_img= util_img.leer_imagen("./imagenes/LineasMenu.ico", (40,40))
        
#         self.config_window()
#         self.paneles()
#         self.controles_barra_superior()        
#         self.controles_menu_lateral()
#         self.controles_cuerpo()
    
#     def config_window(self):
#         # Configuración inicial de la ventana
#         self.title('Gestor de gastos personales')
#         self.iconbitmap("./imagenes/logo.ico")
#         w, h = 1024, 600        
#         util_ventana.centrar_ventana(self, w, h)        

#     def paneles(self):        
#         self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
#         self.barra_superior.pack(side=tk.TOP, fill='both')      

#         self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
#         self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
#         self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
#         self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
#     def controles_barra_superior(self):
#         # Configuración de la barra superior
#         font_awesome = font.Font(family='FontAwesome', size=12)

#         # Etiqueta de título
#         self.labelTitulo = tk.Label(self.barra_superior, text="Menu")
#         self.labelTitulo.config(fg="#fff", font=(
#             "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16, bd=0)
#         self.labelTitulo.pack(side=tk.LEFT)
        
#         # Botón del menú lateral
#         self.buttonMenuLateral = tk.Button(self.barra_superior, image=self.menu_img, font=font_awesome,
#                                            command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")

#         self.buttonMenuLateral.pack(side=tk.LEFT)   
    
#     # Vinculo de botones
#     def controles_menu_lateral(self):
#         # Configuración del menú lateral
#         ancho_menu = 20
#         alto_menu = 2
#         font_awesome = font.Font(family='FontAwesome', size=15)
         
#          # Etiqueta de perfil
#         self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
#         self.labelPerfil.pack(side=tk.TOP, pady=10)

#         # Botones del menú lateral
        
#         self.ButtonInformacion = tk.Button(self.menu_lateral)        
#         self.ButtonLogin = tk.Button(self.menu_lateral)
#         self.ButtonRegister = tk.Button(self.menu_lateral)
#         self.ButtonFlujoDinero = tk.Button(self.menu_lateral)        
#         self.ButtonEstadisticas = tk.Button(self.menu_lateral)        
#         self.ButtonVersion = tk.Button(self.menu_lateral)
#         self.ButtonLogOut = tk.Button(self.menu_lateral)
        
       
#         buttons_info = [
#             ("Informacion", self.ButtonInformacion,self.abrir_informacion_panel),
#             ("Login",self.ButtonLogin,self.abrirlogin),
#             ("Register", self.ButtonRegister, self.abrirregister),
#             ("Flujo de dinero", self.ButtonFlujoDinero,self.abrir_FlujodeDinero),
#             ("Estadistica", self.ButtonEstadisticas,self.abrir_panel_graficas),
#             ("Version", self.ButtonVersion,self.abrir_panel_info),
#             ("Cerrar Sesion", self.ButtonLogOut, self.cerrar_sesion)
#         ]
        
#         for text, button,comando in buttons_info:
#             self.configurar_boton_menu(button, text, font_awesome, ancho_menu, alto_menu,comando)                    
    
#     def controles_cuerpo(self):

#         FormularioInformacionDesign(self.cuerpo_principal)

#     """Eventos interactivos"""

#     def configurar_boton_menu(self, button, text, font_awesome, ancho_menu, alto_menu, comando):
#         button.config(text=f"    {text}", anchor="w", font=font_awesome,
#                       bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
#                       command = comando)
#         button.pack(side=tk.TOP)
#         self.ButtonFlujoDinero.pack_forget()
#         self.ButtonEstadisticas.pack_forget()
#         self.ButtonLogOut.pack_forget()
#         self.ButtonVersion.pack(side=tk.BOTTOM)
#         self.bind_hover_events(button)
        
#     def bind_hover_events(self, button):
#         # Asociar eventos Enter y Leave con la función dinámica
#         button.bind("<Enter>", lambda event: self.on_enter(event, button))
#         button.bind("<Leave>", lambda event: self.on_leave(event, button))

#     def on_enter(self, event, button):
#         # Cambiar estilo al pasar el ratón por encima
#         button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

#     def on_leave(self, event, button):
#         # Restaurar estilo al salir el ratón
#         button.config(bg=COLOR_MENU_LATERAL, fg='white')

#     def toggle_panel(self):
#         # Alternar visibilidad del menú lateral
#         if self.menu_lateral.winfo_ismapped():
#             self.menu_lateral.pack_forget()
#         else:
#             self.menu_lateral.pack(side=tk.LEFT, fill='y')
    
#     """Interaccion de los botones"""

#     def abrirlogin(self):
#         self.limpiar_panel(self.cuerpo_principal)
#         Form_Login(self.cuerpo_principal, self)
    
#     def abrir_informacion_panel(self):
#         self.limpiar_panel(self.cuerpo_principal)
#         FormularioInformacionDesign(self.cuerpo_principal)

#     def abrir_panel_graficas(self):   
#         self.limpiar_panel(self.cuerpo_principal)     
#         FormularioGraficasDesign(self.cuerpo_principal)   
    
#     def abrirregister(self):
#         self.limpiar_panel(self.cuerpo_principal)
#         Form_Register(self.cuerpo_principal, self) 
        
#     def abrir_panel_en_construccion(self):   
#         self.limpiar_panel(self.cuerpo_principal)     
#         FormularioSitioConstruccionDesign(self.cuerpo_principal,self.img_sitio_construccion) 

#     def abrir_panel_info(self):           
#         FormularioInfoDesign()    

#     def abrir_FlujodeDinero(self):
#         self.limpiar_panel(self.cuerpo_principal)
#         FormularioFlujoDinero(self.cuerpo_principal) 
    
#     def cerrar_sesion(self):
#         self.ButtonFlujoDinero.pack_forget()
#         self.ButtonEstadisticas.pack_forget()
#         self.ButtonLogOut.pack_forget()
#         self.ButtonLogin.pack()
#         self.ButtonRegister.pack()
#         self.limpiar_panel(self.cuerpo_principal)
#         Form_Login(self.cuerpo_principal, self)

#     """Limpia panel"""

#     def limpiar_panel(self,panel):
#         # Función para limpiar el contenido del panel
#             for widget in panel.winfo_children():
#                 widget.destroy()
import tkinter as tk
from tkinter import font

import util.util_ventana as util_ventana
import util.util_imagenes as util_img

from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA

from formularios.form_informacion_Design import FormularioInformacionDesign
from formularios.form_login import FormLogin
from formularios.form_register import FormRegister
from formularios.form_graficas_design import FormularioGraficasDesign
from formularios.form_sitio_construccion import FormularioSitioConstruccionDesign
from formularios.form_info_design import FormularioInfoDesign
from formularios.form_FlujoDinero import FormularioFlujoDinero

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.perfil = util_img.leer_imagen("./imagenes/Perfil.jpg", (100, 100))
        self.img_sitio_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (200, 200))
        self.menu_img = util_img.leer_imagen("./imagenes/LineasMenu.ico", (40, 40))
        
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Gestor de gastos personales')
        self.iconbitmap("./imagenes/logo.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Menú")
        self.labelTitulo.config(fg="#fff", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16, bd=0)
        self.labelTitulo.pack(side=tk.LEFT)
        
        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, image=self.menu_img, font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")

        self.buttonMenuLateral.pack(side=tk.LEFT)   
    
    # Vinculo de botones
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de perfil
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        
        self.ButtonInformacion = tk.Button(self.menu_lateral)        
        self.ButtonLogin = tk.Button(self.menu_lateral)
        self.ButtonRegister = tk.Button(self.menu_lateral)
        self.ButtonFlujoDinero = tk.Button(self.menu_lateral)        
        self.ButtonEstadisticas = tk.Button(self.menu_lateral)        
        self.ButtonVersion = tk.Button(self.menu_lateral)
        self.ButtonLogOut = tk.Button(self.menu_lateral)
        
       
        buttons_info = [
            ("Información", self.ButtonInformacion,self.abrir_informacion_panel),
            ("Iniciar sesión",self.ButtonLogin,self.abrir_login),
            ("Registrar", self.ButtonRegister, self.abrir_register),
            ("Flujo de dinero", self.ButtonFlujoDinero,self.abrir_FlujodeDinero),
            ("Estadística", self.ButtonEstadisticas,self.abrir_panel_graficas),
            ("Versión", self.ButtonVersion,self.abrir_panel_info),
            ("Cerrar Sesión", self.ButtonLogOut, self.cerrar_sesion)
        ]
        
        for text, button,comando in buttons_info:
            self.configurar_boton_menu(button, text, font_awesome, ancho_menu, alto_menu,comando)                    
    
    def controles_cuerpo(self):
        FormularioInformacionDesign(self.cuerpo_principal)

    """Eventos interactivos"""

    def configurar_boton_menu(self, button, text, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu,
                      command=comando)
        button.pack(side=tk.TOP)
        self.ButtonFlujoDinero.pack_forget()
        self.ButtonEstadisticas.pack_forget()
        self.ButtonLogOut.pack_forget()
        self.ButtonVersion.pack(side=tk.BOTTOM)
        self.bind_hover_events(button)
        
    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
    
    """Interacción de los botones"""

    def abrir_login(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormLogin(self.cuerpo_principal, self)
    
    def abrir_informacion_panel(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioInformacionDesign(self.cuerpo_principal)

    def abrir_panel_graficas(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        FormularioGraficasDesign(self.cuerpo_principal)   
    
    def abrir_register(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormRegister(self.cuerpo_principal, self) 
        
    def abrir_panel_en_construccion(self):   
        self.limpiar_panel(self.cuerpo_principal)     
        FormularioSitioConstruccionDesign(self.cuerpo_principal, self.img_sitio_construccion) 

    def abrir_panel_info(self):           
        FormularioInfoDesign()    

    def abrir_FlujodeDinero(self):
        self.limpiar_panel(self.cuerpo_principal)
        FormularioFlujoDinero(self.cuerpo_principal) 
    
    def cerrar_sesion(self):
        self.ButtonFlujoDinero.pack_forget()
        self.ButtonEstadisticas.pack_forget()
        self.ButtonLogOut.pack_forget()
        self.ButtonLogin.pack()
        self.ButtonRegister.pack()
        self.limpiar_panel(self.cuerpo_principal)
        FormLogin(self.cuerpo_principal, self)

    """Limpia panel"""

    def limpiar_panel(self, panel):
        # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()
