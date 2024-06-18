# Datos del autor: Juan David Vergara, Santiago Ortiz
# Fecha: 
# Código de los integrantes: 202362484, 202362601
# Descripción: funciones del Sitema de Inventario para una bodega
import json 
from tkinter import messagebox, Toplevel, Label, Entry, Button, ttk

def verificar_acceso(usuarios, usuario, contraseña): # funcion para verificar el acceso al sistema
    for user in usuarios: # recorre la lista de usuarios
        if usuario == user["Usuario"] and contraseña == user["contraseña"]: # si el usuario y la contraseña son iguales a los del usuario y la contraseña del usuario en la lista de usuarios
            return True # retorna True lo que significa que el usuario y la contraseña son correctos
    return False # si no retorna False lo que significa que el usuario y/o la contraseña son incorrectos

def iniciar_sesion(usuarios, entry_usuario, entry_contraseña, ventana_inicio, abrir_ventana_principal):
    usuario = entry_usuario.get() # obtiene el usuario ingresado
    contraseña = entry_contraseña.get() # obtiene la contraseña ingresada
    if usuario == "" or contraseña == "": # si el usuario o la contraseña estan vacios
        messagebox.showerror("Error", "Por favor ingrese usuario y contraseña")
        return
    
    if verificar_acceso(usuarios, usuario, contraseña): # si el usuario y la contraseña son correctos
        messagebox.showinfo("Acceso Concedido", f"Acceso concedido al sistema, Hola {usuario}") # muestra un mensaje de que el acceso fue concedido
        ventana_inicio.destroy() # cierra la ventana de inicio
        abrir_ventana_principal() # abre la ventana principal del sistema
    else:
        messagebox.showerror("Acceso Denegado", "Usuario y/o contraseña incorrectos")


def agregar_producto(inventario, codigo, nombre, cantidad, precio): # funcion para agregar un producto al inventario 
    if codigo in inventario: # si el codigo ya esta en el inventario 
        print("El producto ya existe en el inventario.")
        messagebox.showerror("Sistema de inventario","El producto ya existe en el inventario.")
    else:
        inventario[codigo] = { # si no esta en el inventario lo agrega en la siguente posicion con los datos ingresados y la posicion del codigo
            'nombre': nombre, 
            'cantidad': cantidad,
            'precio': precio
        }
        print(f"Producto {nombre} agregado.") 
        messagebox.showinfo("Sistema de inventario",f"Producto {nombre} agregado con exito.")

def eliminar_producto(inventario, codigo): # funcion para eliminar un producto del inventario 
    if codigo in inventario: # si el codigo esta en el inventario lo elimina
        eliminado = inventario.pop(codigo)  # elimina el producto del inventario con el metodo pop y con el codigo del producto y lo guarda en la variable eliminado 
        print(f"Producto {eliminado['nombre']} eliminado.")
        messagebox.showinfo("Sistema de inventario",f"Producto {eliminado['nombre']} eliminado.")
    else:
        print("El producto no existe en el inventario.")
        messagebox.showerror("Sistema de inventario","El producto no existe en el inventario.")

def actualizar_cantidad(inventario, codigo, cantidad): # funcion para actualizar la cantidad de un producto en el inventario
    if codigo in inventario: # si el codigo esta en el inventario 
        inventario[codigo]['cantidad'] = cantidad # actualiza la cantidad del producto dependiendo del codigo ingresado 
        print(f"Cantidad de {inventario[codigo]['nombre']} actualizada a {cantidad}.") # imprime que la cantidad del producto fue actualizada
        messagebox.showinfo("Sistema de inventario",f"Cantidad de {inventario[codigo]['nombre']} actualizada a {cantidad}.")
    else:
        print("El producto no existe en el inventario.")
        messagebox.showerror("Sistema de inventario","El producto no existe en el inventario.")

def mostrar_inventario(inventario): # funcion para mostrar el inventario
    if not inventario: # si el inventario esta vacio
        print("El inventario está vacío.")
        messagebox.showerror("Sistema de inventario","El inventario está vacío.")
    else:
        for codigo, detalles in inventario.items(): # recorre el inventario y muestra los detalles del producto 
            print(f"Codigo: {codigo}, Nombre: {detalles['nombre']}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")
            messagebox.showinfo("Sistema de inventario",f"Codigo: {codigo}, Nombre: {detalles['nombre']}, Cantidad: {detalles['cantidad']}, Precio: {detalles['precio']}")

def listado_ventas(inventario): # funcion para mostrar el listado de ventas 
    if not inventario: # si el inventario esta vacio 
        print("El inventario está vacío.")
        messagebox.showerror("Sistema de inventario","El inventario está vacío.")
    else:
        for codigo, detalles in inventario.items(): # recorre el inventario y muestra los detalles del producto 
            precio_mayor = detalles['precio'] * 1.0855 # calcula el precio de venta al mayor
            precio_detal = detalles['precio'] * 1.1215 # calcula el precio de venta al detal
            # print(f"{codigo} {detalles['nombre']} {detalles['cantidad']} {precio_mayor:<15.2f} {precio_detal:<15.2f}") # imprime los detalles del producto, los detalles estan alineados a la izquierda y el :<[numero] es para que haya un espacio entre cada detalle

def guardar_inventario(inventario, filename):
    if not filename.endswith('.json'): # si el archivo no termina en .json
        filename += '.json' # le agrega la extension .json
    try:
        with open(filename, 'w') as file: # abre el archivo en modo escritura 
            json.dump(inventario, file, indent=2) # guarda el inventario en el archivo con el metodo dump y con el formato indentado 
        print(f"Inventario guardado en {filename}.")
        messagebox.showinfo("Sistema de inventario",f"Inventario guardado en {filename}.")
    except Exception as e:
        print(f"Error al guardar el inventario: {e}") # imprime si hay un error al guardar el inventario 
        messagebox.showerror("Sistema de inventario",f"Error al guardar el inventario: {e}") 

def cargar_inventario(filename):
    if not filename.endswith('.json'): # si el archivo no termina en .json 
        print("Error: Solo se permiten archivos con extensión .json") # imprime que solo se permiten archivos con extension .json
        messagebox.showerror("Sistema de inventario","Error: Solo se permiten archivos con extensión .json") 
        return None # retorna None
    
    inventario = {} 
    try:
        with open(filename, 'r') as file: # abre el archivo en modo lectura
            inventario = json.load(file) # carga el archivo en el inventario con el metodo load
        print(f"Inventario cargado desde {filename}.") # imprime que el inventario fue cargado 
        messagebox.showinfo("Sistema de inventario",f"Inventario cargado desde {filename}.") # imprime que el inventario fue cargado 
        return inventario # retorna el inventario
    except FileNotFoundError: # si el archivo no se encuentra, el fileNotFoundError es una excepcion que se lanza cuando un archivo no se encuentra
        print(f"Error: El archivo {filename} no existe.")
        messagebox.showerror("Sistema de inventario",f"Error: El archivo {filename} no existe.")
        return None # retorna None
    except Exception as e: # si hay un error al cargar el inventario
        print(f"Error al cargar el inventario: {e}")
        messagebox.showerror("Sistema de inventario",f"Error al cargar el inventario: {e}")
        return None

# Funciones de la interfaz gráfica las cuales reciben los parametros de la interfaz gráfica y los pasan a las funciones anteriores
def agregar_producto_tk(inventario, entry_codigo, entry_nombre, entry_cantidad, entry_precio):
    codigo = entry_codigo.get() # obtiene el codigo ingresado en la interfaz gráfica con el metodo get
    nombre = entry_nombre.get() # obtiene el nombre ingresado en la interfaz gráfica con el metodo get
    cantidad = int(entry_cantidad.get()) # obtiene la cantidad ingresada en la interfaz gráfica con el metodo get y la convierte a entero
    precio = float(entry_precio.get()) # obtiene el precio ingresado en la interfaz gráfica con el metodo get y lo convierte a flotante
    agregar_producto(inventario, codigo, nombre, cantidad, precio) # llama la funcion agregar_producto con los parametros ingresados en la interfaz gráfica

def eliminar_producto_tk(inventario, entry_codigo):
    codigo = entry_codigo.get() # obtiene el codigo ingresado en la interfaz gráfica con el metodo get
    eliminar_producto(inventario, codigo) # llama la funcion eliminar_producto con el codigo ingresado en la interfaz gráfica

def actualizar_cantidad_tk(inventario, entry_codigo, entry_cantidad):
    codigo = entry_codigo.get()
    cantidad = int(entry_cantidad.get())
    actualizar_cantidad(inventario, codigo, cantidad)

def guardar_inventario_tk(inventario, entry_archivo):
    nombreArchivo = entry_archivo.get()
    guardar_inventario(inventario, nombreArchivo)

def cargar_inventario_tk(inventario, entry_archivo):
    nombreArchivo = entry_archivo.get() # obtiene el nombre del archivo ingresado en la interfaz gráfica con el metodo get
    inventario.update(cargar_inventario(nombreArchivo)) # llama la funcion cargar_inventario con el nombre del archivo ingresado en la interfaz gráfica y lo guarda en el inventario con el metodo update el cual sirve para agregar un diccionario a otro diccionario ya existente y no sobreescribirlo 


# Funciones de la interfaz gráfica que le dan funcionalidad a los botones de la interfaz gráfica 
def cerrar_sesion(ventana_principal, inventario, abrir_ventana_inicio):
    inventario.clear()  # limpia el inventario
    ventana_principal.destroy() # cierra la ventana principal
    abrir_ventana_inicio() # abre la ventana de inicio

def abrir_ventana_agregar(inventario):
    ventana_agregar = Toplevel() # crea una ventana emergente la cual es una ventana secundaria
    ventana_agregar.geometry("270x170+700+450") # le da un tamaño a la ventana emergente
    ventana_agregar.resizable(False, False) # hace que la ventana no se pueda redimensionar en ancho y alto
    ventana_agregar.title("Agregar Producto") # le pone un titulo a la ventana emergente

    Label(ventana_agregar, text="Código").grid(row=0, column=0,padx=30, pady=5) # crea una etiqueta en la ventana emergente con el texto "Código" y la posiciona en la fila 0 y columna 0 con un padding de 30 en x y 5 en y
    entry_codigo = Entry(ventana_agregar) # crea un campo de entrada en la ventana emergente y lo guarda en la variable entry_codigo que es un campo de entrada 
    entry_codigo.grid(row=0, column=1,padx=5, pady=5) # posiciona el campo de entrada en la fila 0 y columna 1 con un padding de 5 en x y 5 en y 

    Label(ventana_agregar, text="Nombre").grid(row=1, column=0,padx=30, pady=5) # crea una etiqueta en la ventana emergente con el texto "Nombre" y la posiciona en la fila 1 y columna 0 con un padding de 30 en x y 5 en y
    entry_nombre = Entry(ventana_agregar) # crea un campo de entrada en la ventana emergente y lo guarda en la variable entry_nombre que es un campo de entrada
    entry_nombre.grid(row=1, column=1,padx=5, pady=5) # posiciona el campo de entrada en la fila 1 y columna 1 con un padding de 5 en x y 5 en y

    Label(ventana_agregar, text="Cantidad").grid(row=2, column=0,padx=30, pady=5) # crea una etiqueta en la ventana emergente con el texto "Cantidad" y la posiciona en la fila 2 y columna 0 con un padding de 30 en x y 5 en y
    entry_cantidad = Entry(ventana_agregar) # crea un campo de entrada en la ventana emergente y lo guarda en la variable entry_cantidad que es un campo de entrada
    entry_cantidad.grid(row=2, column=1,padx=5, pady=5) # posiciona el campo de entrada en la fila 2 y columna 1 con un padding de 5 en x y 5 en y

    Label(ventana_agregar, text="Precio").grid(row=3, column=0,padx=30, pady=5)
    entry_precio = Entry(ventana_agregar)
    entry_precio.grid(row=3, column=1,padx=5, pady=5)

    Button(ventana_agregar, text="Agregar", command=lambda: agregar_producto_tk(inventario, entry_codigo, entry_nombre, entry_cantidad, entry_precio)).grid(row=4, column=1) # crea un boton en la ventana emergente con el texto "Agregar" y le da la funcionalidad de llamar la funcion agregar_producto_tk con los parametros ingresados en la interfaz gráfica y la posiciona en la fila 4 y columna 1

def abrir_ventana_eliminar(inventario):
    ventana_eliminar = Toplevel() # crea una ventana emergente 
    ventana_eliminar.geometry("270x120+700+450") # le da un tamaño a la ventana emergente
    ventana_eliminar.resizable(False, False) # hace que la ventana no se pueda redimensionar en ancho y alto
    ventana_eliminar.title("Eliminar Producto") # le pone un titulo a la ventana emergente

    Label(ventana_eliminar, text="Código").grid(row=0, column=0) # crea una etiqueta en la ventana emergente con el texto "Código" y la posiciona en la fila 0 y columna 0
    entry_codigo = Entry(ventana_eliminar) # crea un campo de entrada en la ventana emergente y lo guarda en la variable entry_codigo
    entry_codigo.grid(row=0, column=1) # posiciona el campo de entrada en la fila 0 y columna 1

    Button(ventana_eliminar, text="Eliminar", command=lambda: eliminar_producto_tk(inventario, entry_codigo)).grid(row=1, column=1) # crea un boton en la ventana emergente con el texto "Eliminar" y le da la funcionalidad de llamar la funcion eliminar_producto_tk con los parametros ingresados en la interfaz gráfica y la posiciona en la fila 1 y columna 1

def abrir_ventana_actualizar(inventario):
    ventana_actualizar = Toplevel() # crea una ventana emergente
    ventana_actualizar.geometry("270x120+700+450")  # le da un tamaño a la ventana emergente
    ventana_actualizar.resizable(False, False) # hace que la ventana no se pueda redimensionar en ancho y alto
    ventana_actualizar.title("Actualizar Cantidad") # le pone un titulo a la ventana emergente

    Label(ventana_actualizar, text="Código").grid(row=0, column=0) # crea una etiqueta en la ventana emergente con el texto "Código" y la posiciona en la fila 0 y columna 0
    entry_codigo = Entry(ventana_actualizar)  # crea un campo de entrada en la ventana emergente y lo guarda en la variable entry_codigo
    entry_codigo.grid(row=0, column=1) # posiciona el campo de entrada en la fila 0 y columna 1

    Label(ventana_actualizar, text="Cantidad").grid(row=1, column=0)
    entry_cantidad = Entry(ventana_actualizar)
    entry_cantidad.grid(row=1, column=1)

    Button(ventana_actualizar, text="Actualizar", command=lambda: actualizar_cantidad_tk(inventario, entry_codigo, entry_cantidad)).grid(row=2, column=1) # crea un boton en la ventana emergente con el texto "Actualizar" y le da la funcionalidad de llamar la funcion actualizar_cantidad_tk con los parametros ingresados en la interfaz gráfica y la posiciona en la fila 2 y columna 1

def abrir_ventana_mostrar_inventario(inventario):
    ventana_mostrar = Toplevel()  # crea una ventana emergente
    ventana_mostrar.resizable(False, False) # hace que la ventana no se pueda redimensionar en ancho y alto
    ventana_mostrar.title("Mostrar Inventario") # le pone un titulo a la ventana emergente

    if not inventario: # si el inventario esta vacio
        messagebox.showerror("Error", "El inventario está vacío.") # muestra un mensaje de error
        ventana_mostrar.destroy() # cierra la ventana emergente que muestra el inventario y es la que se abre cuando se presiona el boton de mostrar inventario
        return

    tree = ttk.Treeview(ventana_mostrar, columns=("codigo", "nombre", "cantidad", "precio"), show='headings') # crea un arbol en la ventana emergente con las columnas codigo, nombre, cantidad y precio y le da la funcionalidad de solo mostrar las cabeceras el cual es el parametro show='headings'
    tree.heading("codigo", text="Código") # le pone un texto a la cabecera del arbol con el nombre "codigo"
    tree.heading("nombre", text="Nombre") # le pone un texto a la cabecera del arbol con el nombre "nombre"
    tree.heading("cantidad", text="Cantidad")
    tree.heading("precio", text="Precio")
    tree.pack() # empaqueta el arbol en la ventana emergente

    for codigo, detalles in inventario.items(): # recorre el inventario y muestra los detalles del producto en el arbol
        tree.insert("", "end", values=(codigo, detalles['nombre'], detalles['cantidad'], detalles['precio'])) # inserta los valores del producto en el arbol

def abrir_ventana_listado_ventas(inventario):
    ventana_listado = Toplevel() # crea una ventana emergente
    ventana_listado.resizable(False, False) # hace que la ventana no se pueda redimensionar en ancho y alto 
    ventana_listado.title("Listado de Ventas") # le pone un titulo a la ventana emergente

    if not inventario:
        messagebox.showerror("Error", "El inventario está vacío.") # muestra un mensaje de error
        ventana_listado.destroy() # cierra la ventana emergente que muestra el listado de ventas y es la que se abre cuando se presiona el boton de listado de ventas
        return

    tree = ttk.Treeview(ventana_listado, columns=("codigo", "nombre", "cantidad", "precio_mayor", "precio_detal"), show='headings') # crea un arbol en la ventana emergente con las columnas codigo, nombre, cantidad, precio_mayor y precio_detal y le da la funcionalidad de solo mostrar las cabeceras el cual es el parametro show='headings'
    tree.heading("codigo", text="Código") # le pone un texto a la cabecera del arbol con el nombre "codigo"
    tree.heading("nombre", text="Nombre") # le pone un texto a la cabecera del arbol con el nombre "nombre"
    tree.heading("cantidad", text="Cantidad") # le pone un texto a la cabecera del arbol con el nombre "cantidad"
    tree.heading("precio_mayor", text="Venta Mayor")
    tree.heading("precio_detal", text="Venta Detal")
    tree.pack() # empaqueta el arbol en la ventana emergente

    for codigo, detalles in inventario.items(): # recorre el inventario y muestra los detalles del producto en el arbol
        precio_mayor = detalles['precio'] * 1.0855 # calcula el precio de venta al mayor
        precio_detal = detalles['precio'] * 1.1215 # calcula el precio de venta al detal
        tree.insert("", "end", values=(codigo, detalles['nombre'], detalles['cantidad'], precio_mayor, precio_detal)) # inserta los valores del producto en el arbol

def abrir_ventana_guardar_cargar(inventario):
    ventana_gc = Toplevel() # crea una ventana emergente
    ventana_gc.geometry("330x75+700+450") # le da un tamaño a la ventana emergente
    ventana_gc.resizable(False, False) # hace que la ventana no se pueda redimensionar en ancho y alto
    ventana_gc.title("Guardar/Cargar Inventario")

    Label(ventana_gc, text="Nombre del Archivo").grid(row=0, column=0,padx=30, pady=5)  # crea una etiqueta en la ventana emergente con el texto "Nombre del Archivo" y la posiciona en la fila 0 y columna 0 con un padding de 30 en x y 5 en y
    entry_archivo = Entry(ventana_gc) # crea un campo de entrada en la ventana emergente y lo guarda en la variable entry_archivo
    entry_archivo.grid(row=0, column=1,padx=5, pady=5) # posiciona el campo de entrada en la fila 0 y columna 1 con un padding de 5 en x y 5 en y

    Button(ventana_gc, text="Guardar", command=lambda: guardar_inventario_tk(inventario, entry_archivo)).grid(row=1, column=0) # crea un boton en la ventana emergente con el texto "Guardar" y le da la funcionalidad de llamar la funcion guardar_inventario_tk con los parametros ingresados en la interfaz gráfica y la posiciona en la fila 1 y columna 0
    Button(ventana_gc, text="Cargar", command=lambda: cargar_inventario_tk(inventario, entry_archivo)).grid(row=1, column=1) # crea un boton en la ventana emergente con el texto "Cargar" y le da la funcionalidad de llamar la funcion cargar_inventario_tk con los parametros ingresados en la interfaz gráfica y la posiciona en la fila 1 y columna 1
