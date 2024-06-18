import tkinter as tk #se importa la libreria tkinter con el alias tk
import modulos

usuarios = [
    {"Usuario": "juan", "contraseña": "vergara"},
    {"Usuario": "santiago", "contraseña": "ortiz"},
    {"Usuario": "julian", "contraseña": "castro"},
]

inventario = {}

def abrir_ventana_principal():
    ventana_principal = tk.Tk() # crea la ventana principal 
    ventana_principal.geometry("400x170+600+200") # tamaño de la ventana principal
    ventana_principal.title("Sistema de Inventario") # titulo de la ventana principal
    
    # la siguiente linea de codigo crea un frame en la ventana principal y lo agrega a la ventana principal
    # la funcion pack() se utiliza para agregar el frame a la ventana principal y los parametros padx y pady se utilizan para agregar un espacio entre el frame y la ventana principal
    frame = tk.Frame(ventana_principal) # crea un frame en la ventana principal que es donde se agregaran las opciones del sistema
    frame.pack(padx=10, pady=10) # agrega el frame a la ventana principal

    # la funcion grid() se utiliza para agregar los botones al frame y los parametros row y column se utilizan para indicar la fila y columna en la que se agregara el boton
    # la funcion command se utiliza para indicar la funcion que se ejecutara al hacer click en el boton 
    # la funcion lambda se utiliza para pasar parametros a la funcion que se ejecutara al hacer click en el boton
    # el
    # la siguiente linea de codigo crea botones en el frame de la ventana principal
    tk.Button(frame, text="Agregar Producto", command=lambda: modulos.abrir_ventana_agregar(inventario)).grid(row=0, column=0, padx=5, pady=5) # crea un boton con el texto "Agregar Producto" y llama a la funcion abrir_ventana_agregar del modulo modulos pasandole el parametro inventario
    tk.Button(frame, text="Eliminar Producto", command=lambda: modulos.abrir_ventana_eliminar(inventario)).grid(row=0, column=1, padx=5, pady=5) # crea un boton con el texto "Eliminar Producto" y llama a la funcion abrir_ventana_eliminar del modulo modulos pasandole el parametro inventario
    tk.Button(frame, text="Actualizar Cantidad", command=lambda: modulos.abrir_ventana_actualizar(inventario)).grid(row=1, column=0, padx=5, pady=5) # crea un boton con el texto "Actualizar Cantidad" y llama a la funcion abrir_ventana_actualizar del modulo modulos pasandole el parametro inventario
    tk.Button(frame, text="Mostrar Inventario", command=lambda: modulos.abrir_ventana_mostrar_inventario(inventario)).grid(row=1, column=1, padx=5, pady=5) # crea un boton con el texto "Mostrar Inventario" y llama a la funcion abrir_ventana_mostrar_inventario del modulo modulos pasandole el parametro inventario
    tk.Button(frame, text="Listado de Ventas", command=lambda: modulos.abrir_ventana_listado_ventas(inventario)).grid(row=2, column=0, padx=5, pady=5) # crea un boton con el texto "Listado de Ventas" y llama a la funcion abrir_ventana_listado_ventas del modulo modulos pasandole el parametro inventario
    tk.Button(frame, text="Guardar/Cargar Inventario", command=lambda: modulos.abrir_ventana_guardar_cargar(inventario)).grid(row=2, column=1, padx=5, pady=5) # crea un boton con el texto "Guardar/Cargar Inventario" y llama a la funcion abrir_ventana_guardar_cargar del modulo modulos pasandole el parametro inventario
    tk.Button(frame, text="Cerrar Sesión", command=lambda: modulos.cerrar_sesion(ventana_principal, inventario, iniciar_ventana_inicio)).grid(row=3, column=0, columnspan=2, pady=10) # crea un boton con el texto "Cerrar Sesión" y llama a la funcion cerrar_sesion del modulo modulos pasandole los parametros correspondientes 

    ventana_principal.mainloop()

def iniciar_ventana_inicio():
    # Widgets de la ventana de inicio
    ventana_inicio = tk.Tk()  # crea la ventana de inicio 
    ventana_inicio.geometry("300x250+700+250") # tamaño de la ventana de inicio
    ventana_inicio.title("Inicio de Sesión") # titulo de la ventana de inicio
    ventana_inicio.resizable(False, False) # no se puede cambiar el tamaño de la ventana

    tk.Label(ventana_inicio, text="Usuario").pack(padx=20, pady=10) # crea un label con el texto "Usuario"
    entry_usuario = tk.Entry(ventana_inicio) # crea un entry para ingresar el usuario
    entry_usuario.pack(padx=20, pady=10) # agrega el entry a la ventana de inicio 

    tk.Label(ventana_inicio, text="Contraseña").pack() # crea un label con el texto "Contraseña"
    entry_contraseña = tk.Entry(ventana_inicio, show='*') # crea un entry para ingresar la contraseña
    entry_contraseña.pack() # agrega el entry a la ventana de inicio

    tk.Button(ventana_inicio, text="Iniciar Sesión", command=lambda: modulos.iniciar_sesion(usuarios, entry_usuario, entry_contraseña, ventana_inicio, abrir_ventana_principal)).pack(padx=20, pady=20) # crea un boton para iniciar sesion y llama a la funcion iniciar_sesion del modulo modulos pasandole los parametros correspondientes 
    

    ventana_inicio.mainloop() # se ejecuta la ventana de inicio 

if __name__ == "__main__":
    iniciar_ventana_inicio()
