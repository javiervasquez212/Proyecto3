#Importación de modulos

from tkinter import *
from tkinter import messagebox

#Variables globales

seg_reloj = 0
min_reloj= 0
hora_reloj = 0

#Creación de la ventana principal

ventana_principal = Tk()  #Ventana principal
ventana_principal.geometry("800x800") #Dimesiones de la ventana principal
ventana_principal.title("Futoshiki") #Titulo de la ventana principal

#Funciones principales

def func_jugar(): 

    #Variables globales

   #Globales boton número

    global boton_numero_1
    global boton_numero_2
    global boton_numero_3
    global boton_numero_4
    global boton_numero_5
    
    #Global botones principales

    global boton_cargar_juego
    global boton_guardar_juego
    global boton_terminar
    global boton_borrar_juego
    global boton_iniciar

    #Global ventana

    global ventana_jugar

    #Global número

    global poner_numero

    #Globales casillas

    global casilla_0x0
    global casilla_0x1
    global casilla_0x2
    global casilla_0x3
    global casilla_0x4

    global casilla_1x0
    global casilla_1x1
    global casilla_1x2
    global casilla_1x3
    global casilla_1x4

    global casilla_2x0
    global casilla_2x1
    global casilla_2x2
    global casilla_2x3
    global casilla_2x4

    global casilla_3x0
    global casilla_3x1
    global casilla_3x2
    global casilla_3x3
    global casilla_3x4

    global casilla_4x0
    global casilla_4x1
    global casilla_4x2
    global casilla_4x3
    global casilla_4x4

    #Globales timer

    global timer_horas, timer_minutos, timer_segundos, timer
    

    ventana_principal.state(newstate="withdraw")

    #Creación de la ventana

    ventana_jugar = Toplevel()
    ventana_jugar.title("Jugar")
    ventana_jugar.geometry("1000x1000")
    ventana_jugar.configure(bg="#161a1d")

    #Titulo
    
    titulo_futoshiki = Label(ventana_jugar,text="FUTOSHIKI",font=("Arial Black",40),fg="#660708",bg="#161a1d")
    titulo_futoshiki.place(x=350,y=10)

    #Nivel

    nivel_juego_actual = Label(ventana_jugar,text="NIVEL FÁCIL",font=("Arial Black",12),fg="#660708",bg="#161a1d")
    nivel_juego_actual.place(x=475,y=85)

    #Etiquetas

    nombre_del_jugador = Label(ventana_jugar,text="Nombre del jugador:",font=("Arial Black",12),fg="#660708",bg="#161a1d")
    nombre_del_jugador.place(x=200,y=115)

    #Entrada

    entrada_nombre_jugador = Entry(ventana_jugar,width = 35)
    entrada_nombre_jugador.place(x=425,y=120)

    #Botones principales
    
    boton_iniciar = Button(ventana_jugar,text="INICIAR JUEGO",font=("Arial Black",12),bg="#e5383b",height = 1, width = 15,\
    command=iniciar_juego)
    boton_iniciar.place(x=100,y=540)

    
    boton_borrar_paso = Button(ventana_jugar,text="BORRAR JUGADA",font=("Arial Black",12), bg="#e5383b",height = 1, width = 15)
    boton_borrar_paso.place(x=285,y=540)

    boton_terminar = Button(ventana_jugar,text="TERMINAR JUEGO",font=("Arial Black",12),bg="#e5383b",height = 1, width = 15,\
    command=terminar_juego,state="disabled")
    boton_terminar.place(x=470,y=540)

    boton_borrar_juego = Button(ventana_jugar,text="BORRAR JUEGO",font=("Arial Black",12),bg="#e5383b",height = 1, width = 15,\
    state="disabled",command=borrar_juego)
    boton_borrar_juego.place(x=655,y=540)

    boton_top_10 = Button(ventana_jugar,text="TOP 10",font=("Arial Black",12),bg="#e5383b",height = 1, width = 15,command=top_10)
    boton_top_10.place(x=655,y=590)

    boton_cargar_juego = Button(ventana_jugar,text="CARGAR JUEGO",font=("Arial Black",12),bg="#b1a7a6",height = 1, width = 15,\
    state="normal")
    boton_cargar_juego.place(x=470,y=590)

    boton_guardar_juego = Button(ventana_jugar,text="GUARDAR JUEGO",font=("Arial Black",12),bg="#b1a7a6",height = 1, width = 15,\
    state="disabled")
    boton_guardar_juego.place(x=285,y=590)
    
    #Boton regresar menu principal

    boton_salida = Button(ventana_jugar, text = "X", command = lambda: regresar_menu_principal(ventana_jugar))
    boton_salida.place(anchor=NW)

    #Botones para jugar

    boton_numero_1 = Button(ventana_jugar,text="1",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton1)
    boton_numero_1.place(x=785,y=200)

    boton_numero_2 = Button(ventana_jugar,text="2",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton2)
    boton_numero_2.place(x=785,y=250)

    boton_numero_3 = Button(ventana_jugar,text="3",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton3)
    boton_numero_3.place(x=785,y=300)

    boton_numero_4 = Button(ventana_jugar,text="4",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton4)
    boton_numero_4.place(x=785,y=350)

    boton_numero_5 = Button(ventana_jugar,text="5",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton5)
    boton_numero_5.place(x=785,y=400)

    # Timer


    timer = Label(ventana_jugar,text="Timer",font=("Arial Black",12),fg="#660708",bg="#161a1d")
    timer.place(x=140,y=590)

    timer_horas = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
    timer_horas.place(x=100,y=620)

    timer_minutos = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
    timer_minutos.place(x=150,y=620)

    timer_segundos = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
    timer_segundos.place(x=200,y=620)


    # Botones casilla juego / fila 1

    casilla_0x0 = Button(ventana_jugar,height = 2, width = 5,text="", command=cambio_cuadricula_0x0)
    casilla_0x0.place(x=350,y=200)

    casilla_0x1 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_0x1)
    casilla_0x1.place(x=420,y=200)

    casilla_0x2 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_0x2)
    casilla_0x2.place(x=490,y=200)

    casilla_0x3 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_0x3)
    casilla_0x3.place(x=560,y=200)

    casilla_0x4 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_0x4)
    casilla_0x4.place(x=630,y=200)

    # Botones casilla juego / fila 2

    casilla_1x0 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_1x0)
    casilla_1x0.place(x=350,y=270)

    casilla_1x1 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_1x1)
    casilla_1x1.place(x=420,y=270)

    casilla_1x2 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_1x2)
    casilla_1x2.place(x=490,y=270)

    casilla_1x3 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_1x3)
    casilla_1x3.place(x=560,y=270)

    casilla_1x4 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_1x4)
    casilla_1x4.place(x=630,y=270)

    # Botones casilla juego / fila 3

    casilla_2x0 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_2x0)
    casilla_2x0.place(x=350,y=340)

    casilla_2x1 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_2x1)
    casilla_2x1.place(x=420,y=340)

    casilla_2x2 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_2x2)
    casilla_2x2.place(x=490,y=340)

    casilla_2x3 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_2x3)
    casilla_2x3.place(x=560,y=340)

    casilla_2x4 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_2x4)
    casilla_2x4.place(x=630,y=340)

    # Botones casilla juego / fila 4

    casilla_3x0 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_3x0)
    casilla_3x0.place(x=350,y=410)

    casilla_3x1 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_3x1)
    casilla_3x1.place(x=420,y=410)

    casilla_3x2 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_3x2)
    casilla_3x2.place(x=490,y=410)

    casilla_3x3 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_3x3)
    casilla_3x3.place(x=560,y=410)

    casilla_3x4 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_3x4)
    casilla_3x4.place(x=630,y=410)

    # Botones casilla juego / fila 5

    casilla_4x0 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_4x0)
    casilla_4x0.place(x=350,y=480)

    casilla_4x1 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_4x1)
    casilla_4x1.place(x=420,y=480)

    casilla_4x2 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_4x2)
    casilla_4x2.place(x=490,y=480)

    casilla_4x3 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_4x3)
    casilla_4x3.place(x=560,y=480)

    casilla_4x4 = Button(ventana_jugar,height = 2, width = 5, command=cambio_cuadricula_4x4)
    casilla_4x4.place(x=630,y=480)


#Funcion configuración

def func_config(): 
    ventana_principal.state(newstate="withdraw")


    #Variables globales

    global nivel_id
    global reloj_id
    global posicion_id

    global timer_entrada_segundos
    global timer_entrada_minutos
    global timer_entrada_horas

    global ventana_conf

    #Separación de Radiobuttons

    nivel_id = IntVar()
    reloj_id = IntVar()
    posicion_id = IntVar()

    #Creación de la ventana

    ventana_conf = Toplevel()
    ventana_conf.title("Configuración")
    ventana_conf.geometry("500x500")

    #Titulo

    bienvenido = Label(ventana_conf,text="Bienvenido a la configuración del juego!", font=("Arial Black",16),fg="firebrick2")
    bienvenido.place(x=50,y=0)

    #Nivel y Radiobuttons relacionados

    nivel = Label(ventana_conf,text="1. Nivel:", font=("Arial Black",9))
    nivel.place(x=0,y=50)

    opcion_facil = Radiobutton(ventana_conf,text="Fácil",value=1,variable=nivel_id,command=señalar_nivel)
    opcion_facil.place(x=50,y=50)

    opcion_intermedio = Radiobutton(ventana_conf,text="Intermedio",value=2,variable=nivel_id,command=señalar_nivel)
    opcion_intermedio.place(x=50,y=75)

    opcion_dificil = Radiobutton(ventana_conf,text="Difícil",value=3,variable=nivel_id,command=señalar_nivel)
    opcion_dificil.place(x=50,y=100)

    #Reloj y Radiobuttons relacionados

    reloj = Label(ventana_conf,text="2. Reloj", font=("Arial Black",9))
    reloj.place(x=0,y=150)

    opcion_si = Radiobutton(ventana_conf,text="Sí",value=4,variable=reloj_id,command=señalar_reloj)
    opcion_si.place(x=50,y=150)

    opcion_no = Radiobutton(ventana_conf,text="No",value=5,variable=reloj_id,command=señalar_reloj)
    opcion_no.place(x=50,y=175)

    opcion_timer = Radiobutton(ventana_conf,text="Timer",value=6,variable=reloj_id,command=señalar_reloj)
    opcion_timer.place(x=50,y=200)

    #Posicion ventana panel de digitos  y Radiobuttons relacionados

    posicion = Label(ventana_conf,text="3. Posición en la ventana del panel de dígitos:", font=("Arial Black",9))
    posicion.place(x=0,y=250)

    posicion_derecha = Radiobutton(ventana_conf,text="Derecha",value=7,variable=posicion_id,command=señalar_posicion)
    posicion_derecha.place(x=50,y=275)

    posicion_izquierda = Radiobutton(ventana_conf,text="Izquierda",value=8,variable=posicion_id,command=señalar_posicion)
    posicion_izquierda.place(x=50,y=300)

    #Aceptar y Cancelar

    boton_aceptar = Button(ventana_conf,text="Aceptar",command=aceptar_configuracion)
    boton_aceptar.place(x=30,y=350)

    boton_cancelar = Button(ventana_conf,text="Cancelar", command = lambda: regresar_menu_principal(ventana_conf))
    boton_cancelar.place(x=85,y=350)

    #Boton regresar menu principal

    boton_salida = Button(ventana_conf, text = "X", command = lambda: regresar_menu_principal(ventana_conf))
    boton_salida.place(anchor=NW)

    #Entradas timer

    timer_entrada_segundos = Entry(ventana_conf, width = 4)
    timer_entrada_segundos.place(x=440,y=125)

    timer_entrada_minutos = Entry(ventana_conf, width = 4)
    timer_entrada_minutos.place(x=370,y=125)

    timer_entrada_horas = Entry(ventana_conf, width = 4)
    timer_entrada_horas.place(x=300,y=125)

    #Etiquetas timer
    
    
    timer_timer_etiqueta_segundos = Label(ventana_conf,text="Segundos")
    timer_timer_etiqueta_segundos.place(x=425,y=150)

    timer_etiqueta_minutos = Label(ventana_conf,text="Minutos")
    timer_etiqueta_minutos.place(x=360,y=150)

    timer_etiqueta_horas = Label(ventana_conf,text="Horas")
    timer_etiqueta_horas.place(x=295,y=150)

    timer_etiqueta_timer = Label(ventana_conf,text="Timer!",font=("Arial Black",12))
    timer_etiqueta_timer.place(x=355,y=90)

#Función ayuda

def func_ayuda(): 
    ventana_principal.state(newstate="withdraw")

    #Creación de la ventana

    ventana_ayuda = Toplevel()
    ventana_ayuda.title("Ayuda")
    ventana_ayuda.geometry("500x500")

    boton_salida = Button(ventana_ayuda, text = "X", command = lambda: regresar_menu_principal(ventana_ayuda))
    boton_salida.place(anchor=NW)

#Función acerca de

def func_acerca_de(): 
    ventana_principal.state(newstate="withdraw")

    #Creación de la ventana

    ventana_acerca_de = Toplevel()
    ventana_acerca_de.title("Acerca de")
    ventana_acerca_de.geometry("500x500")
    ventana_acerca_de.configure(bg="#b1a7a6")

    #Titulo

    acerca_titulo = Label(ventana_acerca_de,text="Acerca de nuestro programa!",font=("Arial Black",16),fg="Sea green",bg="#b1a7a6")
    acerca_titulo.place(x=50,y=15)

    #Etiquetas

    nombre_programa = Label(ventana_acerca_de,text="Nombre del programa: FUTOSHIKI",bg="#b1a7a6",font=("Arial Black",12))
    nombre_programa.place(x=50,y=50)

    autor = Label(ventana_acerca_de,text="Autor: Javier Vásquez Monsalve",bg="#b1a7a6",font=("Arial Black",12))
    autor.place(x=50,y=75)

    fecha_creación = Label(ventana_acerca_de,text="Fecha de creación: 4 de Junio del 2021",bg="#b1a7a6",font=("Arial Black",12))
    fecha_creación.place(x=50,y=100)

    version = Label(ventana_acerca_de,text="Version: 1.0",bg="#b1a7a6",font=("Arial Black",12))
    version.place(x=50,y=125)

    agradecimiento = Label(ventana_acerca_de,text="Gracias por jugar con nosotros!",bg="#b1a7a6",font=("Arial Black",12))
    agradecimiento.place(x=50,y=150)

    boton_salida = Button(ventana_acerca_de, text = "X", command = lambda: regresar_menu_principal(ventana_acerca_de))
    boton_salida.place(anchor=NW)

#Función para salir del programa

def func_salir(): 
    ventana_principal.destroy()
    
#Funciones jugar / Función Top 10

def top_10():

    #Creación de la ventana

    ventana_top_10 = Toplevel()
    ventana_top_10.title("Top 10")
    ventana_top_10.geometry("500x500")
    ventana_top_10.configure(bg="#b1a7a6")

    #Titulo

    titulo_top = Label(ventana_top_10,text="Top 10", font=("Arial Black",18),fg="red",bg="#b1a7a6")
    titulo_top.place(x=50,y=15)

    #Top nivel dificil

    nivel_dificil = Label(ventana_top_10,text="NIVEL DIFICIL:",font=("Arial Black",12),bg="#b1a7a6")
    nivel_dificil.place(x=50,y=50)

    jugador_dificil = Label(ventana_top_10,text="JUGADOR",font=("Arial Black",12),bg="#b1a7a6")
    jugador_dificil.place(x=350,y=50)

    tiempo_dificil = Label(ventana_top_10,text="TIEMPO",font=("Arial Black",12),bg="#b1a7a6")
    tiempo_dificil.place(x=650,y=50)

    #Top nivel intermedio

    nivel_intermedio = Label(ventana_top_10,text="NIVEL INTERMEDIO:",font=("Arial Black",12),bg="#b1a7a6")
    nivel_intermedio.place(x=50,y=250)

    jugador_intermedio = Label(ventana_top_10,text="JUGADOR",font=("Arial Black",12),bg="#b1a7a6")
    jugador_intermedio.place(x=350,y=250)

    tiempo_intermedio = Label(ventana_top_10,text="TIEMPO",font=("Arial Black",12),bg="#b1a7a6")
    tiempo_intermedio.place(x=650,y=250)

    #Top nivel fácil

    nivel_facil = Label(ventana_top_10,text="NIVEL FÁCIL:",font=("Arial Black",12),bg="#b1a7a6")
    nivel_facil.place(x=50,y=450)

    jugador_facil = Label(ventana_top_10,text="JUGADOR",font=("Arial Black",12),bg="#b1a7a6")
    jugador_facil.place(x=350,y=450)

    tiempo_facil = Label(ventana_top_10,text="TIEMPO",font=("Arial Black",12),bg="#b1a7a6")
    tiempo_facil.place(x=650,y=450)

#Función boton iniciar juego

def iniciar_juego():
    
    #Variable global

    global repetidor_timer

    #Habilitar botones de cargar y guardar

    boton_iniciar.config(state="disabled")

    boton_cargar_juego.config(state="disabled")
    boton_guardar_juego.config(state="normal")

    boton_borrar_juego.config(state="normal")
    boton_terminar.config(state="normal")

    repetidor_timer = Label(ventana_jugar,text="",font=("Arial Black",12),bg="#b1a7a6")
    repetidor_timer.place(x=800,y=800)

    repetidor_timer.after(1000,timer_funcion)

#Función borrar jugada

def borrar_jugada():
    pass

#Funcion terminar juego

def terminar_juego():

    respuesta = messagebox.askyesno("Terminar juego","¿ESTÁ SEGURO DE TERMINAR EL JUEGO?")
    
    if respuesta == True:
        ventana_jugar.state(newstate="withdraw")
        func_jugar()
    else:
        pass

#Funcion borrar juego

def borrar_juego():
    
    respuesta = messagebox.askyesno("Terminar juego","¿ESTÁ SEGURO DE BORRAR EL JUEGO")
    

#Funcion guardar juego

def guardar_juego():
    pass

#Funcion cargar_juego

def cargar_juego():
    pass

#Funciones para cambiar el color del boton seleccionado

def click_boton1():
    
    global poner_numero

    poner_numero = 1

    boton_numero_1.config(bg="chartreuse4")

    boton_numero_2.config(bg="#a4161a")
    boton_numero_3.config(bg="#a4161a")
    boton_numero_4.config(bg="#a4161a")
    boton_numero_5.config(bg="#a4161a")

def click_boton2():

    global poner_numero

    poner_numero = 2

    boton_numero_2.config(bg="chartreuse4")

    boton_numero_1.config(bg="#a4161a")
    boton_numero_3.config(bg="#a4161a")
    boton_numero_4.config(bg="#a4161a")
    boton_numero_5.config(bg="#a4161a")

def click_boton3():

    global poner_numero

    poner_numero = 3

    boton_numero_3.config(bg="chartreuse4")

    boton_numero_1.config(bg="#a4161a")
    boton_numero_2.config(bg="#a4161a")
    boton_numero_4.config(bg="#a4161a")
    boton_numero_5.config(bg="#a4161a")

def click_boton4():

    global poner_numero

    poner_numero = 4

    boton_numero_4.config(bg="chartreuse4")

    boton_numero_1.config(bg="#a4161a")
    boton_numero_3.config(bg="#a4161a")
    boton_numero_2.config(bg="#a4161a")
    boton_numero_5.config(bg="#a4161a")

def click_boton5():

    global poner_numero

    poner_numero = 5

    boton_numero_5.config(bg="chartreuse4")

    boton_numero_1.config(bg="#a4161a")
    boton_numero_3.config(bg="#a4161a")
    boton_numero_4.config(bg="#a4161a")
    boton_numero_2.config(bg="#a4161a")

# Boton X para regresar el menú principal

def regresar_menu_principal(opcion_menu): 
    opcion_menu.state(newstate="withdraw")
    ventana_principal.state(newstate="normal")


#Funciones auxiliares

def señalar_nivel():
    global valor_nivel

    valor_nivel = nivel_id.get()
    print(valor_nivel)
    

def señalar_reloj():
    global valor_reloj

    valor_reloj = reloj_id.get()
    print(valor_reloj)
    

def señalar_posicion():
    global señalar_posicion

    valor_posicion = posicion_id.get()
    print(valor_posicion)
    

# Funciones cuadriculas juego:

# Fila 0

def cambio_cuadricula_0x0():
    try:
        casilla_0x0.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")


def cambio_cuadricula_0x1():
    try:
        casilla_0x1.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_0x2():
    try:
        casilla_0x2.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_0x3():
    try:
        casilla_0x3.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_0x4():
    try:
        casilla_0x4.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

#Fila 1

def cambio_cuadricula_1x0():

    try:
        casilla_1x0.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_1x1():
    try:
        casilla_1x1.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_1x2():
    try:
        casilla_1x2.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_1x3():
    try:
        casilla_1x3.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_1x4():
    try:
        casilla_1x4.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

# Fila 2

def cambio_cuadricula_2x0():
    try:
        casilla_2x0.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_2x1():
    try:
        casilla_2x1.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_2x2():
    try:
        casilla_2x2.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_2x3():
    try:
        casilla_2x3.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_2x4():
    try:
        casilla_2x4.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

#Fila 3

def cambio_cuadricula_3x0():
    try:
        casilla_3x0.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_3x1():
    try:
        casilla_3x1.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_3x2():
    try:
        casilla_3x2.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_3x3():
    try:
        casilla_3x3.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_3x4():
    try:
        casilla_3x4.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

#Fila 4

def cambio_cuadricula_4x0():
    try:
        casilla_4x0.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_4x1():
    try:
        casilla_4x1.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_4x2():
    try:
        casilla_4x2.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_4x3():
    try:
        casilla_4x3.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

def cambio_cuadricula_4x4():
    try:
        casilla_4x4.config(text=poner_numero)
    except:
        messagebox.showinfo(title="Casilla",message= "Seleccione un número primero")

# Función Timer

def aceptar_configuracion():

    global seg_timer
    global min_timer
    global hora_timer

    try:
        seg_timer = int(timer_entrada_segundos.get())
        min_timer = int(timer_entrada_minutos.get())
        hora_timer = int(timer_entrada_horas.get())

        ventana_conf.state(newstate="withdraw")
        ventana_principal.state(newstate="normal")


    except:
        messagebox.showinfo(title="Timer",message="Verifique los valores del timer esten completos")


def reloj():
    global seg_reloj,min_reloj,hora_reloj

    seg_reloj += 1

    if seg_reloj == 60:
        seg_reloj = 0
        min_reloj +=1
        if min_reloj == 60:
            min_reloj = 0
            hora_reloj +=1
    
    timer_horas.config(text=hora_reloj)
    timer_minutos.config(text=min_reloj)
    timer_segundos.config(text=seg_reloj)


def timer_funcion():
    global seg_timer,min_timer,hora_timer

    seg_timer -= 1

    if seg_timer == 0:
        if min_timer!=0:
            seg_timer = 59
            min_timer -= 1
        else:
            min_timer = 0
            seg_timer = 0
            if min_timer == 0:
                if hora_timer !=0:
                    min_timer = 59
                    hora_timer = 0
                else:
                    min_timer = 0
                    hora_timer = 0
                    if seg_timer == 0 and min_timer == 0 and hora_timer == 0:
                        respuesta = messagebox.askyesno("TIEMPO EXPIRADO", "¿DESEA CONTINUAR EL MISMO JUEGO")

                        if respuesta == True:
                            pass
                        else:
                            ventana_jugar.state(newstate="withdraw")
                            func_jugar()

    if seg_timer >= 0:
        timer_segundos.config(text=seg_timer)
    timer_horas.config(text=hora_timer)
    timer_minutos.config(text=min_timer)
   

    repetidor_timer.after(1000,timer_funcion)
# Archivos

def archivo_partida_dificultad():
    partidas = open("futoshiki2021partidas.dat","w")
        
    partidas.write("\nFacil = [((\"5\",0,0),(\"5\",0,1),(\"2\",0,3)\
                            \n(\"2\",2,1),(\"5\",2,3),(\"3\",2,4),\
                            \n(\"1\",3,1),(\"2\",3,3),\
                            \n(\"5\",4,4)),\
                            \n((\"2\",0,3),\
                            \n(\"2\",1,0),(\"1\",1,2),(\"3\",1,3),\
                            \n(\"3\",2,2),(\"1\",2,3),\
                            \n(\"1\",4,0),(\"5\",4,4),\
                            \n(\"5\",0,2),\
                            \n(\"1\",1,0),(\"3\",1,1),(\"2\",1,4),\
                            \n(\"3\",3,0),(\"1\",3,4),\
                            \n(\"1\",4,3),(\"5\",4,4))],\
                    \nIntermedio = [((\"5\",0,0),(\"3\",0,4),(\"^\",0,2),\
                            \n(\">\",1,1),\
                            \n(\"v\",2,0),\
                            \n(\">\",3,0),(\"^\",3,2),\
                            \n(\">\",4,1),\
                            \n(\"<\",0,0),(\"v\",0,0),(\"^\",0,1),\
                            \n(\"v\",1,3),(\"^\",1,4),\
                            \n(\">\",2,3),(\"v\",2,4),\
                            \n(\">\",4,0),(\"4\",4,4),\
                            \n(\"5\",0,0),(\"<\",0,1),(\"<\",0,2),\
                            \n(\"^\",1,0),(\"v\",1,3),\
                            \n(\"^\",3,1),(\"^\",3,3),\
                            \n(\"<\",4,0),(\"3\",4,1)(\">\",4,2),(\"1\",4,4))],\
                    \nDificil = [((\"v\",0,0),(\"v\",0,4),\
                            \n(\"v\",1,0),(\"<\",1,1),\
                            \n(\"^\",2,1),(\"<\",2,3),\
                            \n(\">\",3,0),(\"v\",3,3),\
                            \n(\"<\",4,2),(\"1\",4,4),\
                            \n(\">\",0,0),(\">\",0,1),(\"<\",0,3),(\"^\",0,3),\
                            \n(\">\",1,0),(\"4\",1,4),\
                            \n(\"<\",2,0),(\"^\",2,1),(\"^\",2,0),\
                            \n(\"1\",3,3)),\
                            \n(\"^\",0,0),(\"<\",0,3),\
                            \n(\"^\"1,0),(\">\",0,1),(\"^\",1,3),\
                            \n(\"v\",2,1),(\"v\",2,4),\
                            \n(\">\",3,0),(\"^\",3,0),(\"<\",3,3),\
                            \n(\"<\",4,0),(\">\",4,1))]")
    partidas.close()
    partidas = open("futoshiki2021partidas.dat","r")
    print(partidas.readlines())
    partidas.close()

#Creación de la barra menú

Menu_principal = Menu(ventana_principal)
ventana_principal.config(menu = Menu_principal)

A_jugar_menu = Menu(ventana_principal)
Menu_principal.add_cascade(label = "Jugar", command=func_jugar)

Configuracion_menu = Menu(ventana_principal)
Menu_principal.add_cascade(label = "Configuración", command=func_config)
                      
Ayuda_menu = Menu(ventana_principal)
Menu_principal.add_cascade(label = "Ayuda", command=func_ayuda)

Acerca_de_menu = Menu(ventana_principal)
Menu_principal.add_cascade(label = "Acerca de",command=func_acerca_de)

Salir_menu = Menu(ventana_principal)
Menu_principal.add_cascade(label = "Salir",command=func_salir)


ventana_principal.mainloop() 




