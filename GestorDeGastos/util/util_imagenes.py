# from PIL import ImageTk, Image

# def leer_imagen(path, size): 
#         return ImageTk.PhotoImage(Image.open(path).resize(size,  Image.ADAPTIVE))

from PIL import ImageTk, Image

def leer_imagen(ruta, size):
    try:
        imagen = Image.open(ruta)
        imagen = imagen.resize(size, Image.ADAPTIVE)
        return ImageTk.PhotoImage(imagen)
    except FileNotFoundError:
        print(f"Error: Archivo no encontrado en la ruta: {ruta}")
        return None
