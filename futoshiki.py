#Importación de modulos

from os import stat
from tkinter import *
from tkinter import messagebox

#Creación de la ventana principal

ventana_principal = Tk()  #Ventana principal
ventana_principal.geometry("800x800") #Dimesiones de la ventana principal
ventana_principal.title("Futoshiki") #Titulo de la ventana principal

#Variables con valor predeterminado / Configuración

valor_nivel = 1
valor_reloj = 4
valor_posicion = 7

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
    global boton_borrar_paso

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

    #Global restricciones parelelo

    global restriccion_0x0
    global restriccion_0x1
    global restriccion_0x2
    global restriccion_0x3

    global restriccion_1x0
    global restriccion_1x1
    global restriccion_1x2
    global restriccion_1x3
 
    global restriccion_2x0
    global restriccion_2x1
    global restriccion_2x2
    global restriccion_2x3

    global restriccion_3x0
    global restriccion_3x1
    global restriccion_3x2
    global restriccion_3x3

    global restriccion_4x0
    global restriccion_4x1
    global restriccion_4x2
    global restriccion_4x3

    #Restricciones verticales global

    global r_vertical_0x0
    global r_vertical_0x1
    global r_vertical_0x2
    global r_vertical_0x3
    global r_vertical_0x4

    global r_vertical_1x0
    global r_vertical_1x1
    global r_vertical_1x2
    global r_vertical_1x3
    global r_vertical_1x4

    global r_vertical_2x0
    global r_vertical_2x1
    global r_vertical_2x2
    global r_vertical_2x3
    global r_vertical_2x4

    global r_vertical_3x0
    global r_vertical_3x1
    global r_vertical_3x2
    global r_vertical_3x3
    global r_vertical_3x4
 

    #Globales timer

    global timer_horas, timer_minutos, timer_segundos, timer

    #Variables

    global seg_reloj,min_reloj,hora_reloj
    global entrada_nombre_jugador
    

    seg_reloj = 0
    min_reloj= 0
    hora_reloj = 0
    

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

    if valor_nivel == 1:

        nivel_juego_actual = Label(ventana_jugar,text="NIVEL FÁCIL",font=("Arial Black",12),fg="#660708",bg="#161a1d")
        nivel_juego_actual.place(x=475,y=85)

    if valor_nivel == 2:

        nivel_juego_actual = Label(ventana_jugar,text="NIVEL INTERMEDIO",font=("Arial Black",12),fg="#660708",bg="#161a1d")
        nivel_juego_actual.place(x=450,y=85)

    if valor_nivel == 3:

        nivel_juego_actual = Label(ventana_jugar,text="NIVEL DIFICIL",font=("Arial Black",12),fg="#660708",bg="#161a1d")
        nivel_juego_actual.place(x=470,y=85)
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

    
    boton_borrar_paso = Button(ventana_jugar,text="BORRAR JUGADA",font=("Arial Black",12), bg="#e5383b",height = 1, width = 15,\
    command=borrar_jugada,state="disabled")
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

    if valor_posicion == 7:

        boton_numero_1 = Button(ventana_jugar,text="1",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton1,\
        state="disabled")
        boton_numero_1.place(x=785,y=200)

        boton_numero_2 = Button(ventana_jugar,text="2",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton2,\
        state="disabled")
        boton_numero_2.place(x=785,y=250)

        boton_numero_3 = Button(ventana_jugar,text="3",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton3,\
        state="disabled")
        boton_numero_3.place(x=785,y=300)

        boton_numero_4 = Button(ventana_jugar,text="4",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton4,\
        state="disabled")
        boton_numero_4.place(x=785,y=350)

        boton_numero_5 = Button(ventana_jugar,text="5",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton5,\
        state="disabled")
        boton_numero_5.place(x=785,y=400)
    
    if valor_posicion == 8:

        boton_numero_1 = Button(ventana_jugar,text="1",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton1)
        boton_numero_1.place(x=175,y=200)

        boton_numero_2 = Button(ventana_jugar,text="2",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton2)
        boton_numero_2.place(x=175,y=250)

        boton_numero_3 = Button(ventana_jugar,text="3",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton3)
        boton_numero_3.place(x=175,y=300)

        boton_numero_4 = Button(ventana_jugar,text="4",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton4)
        boton_numero_4.place(x=175,y=350)

        boton_numero_5 = Button(ventana_jugar,text="5",font=("Arial Black",12),height = 1, width = 3,bg="#a4161a", command=click_boton5)
        boton_numero_5.place(x=175,y=400)

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


    #Restricción 

    #Restriccion / Fila 0

    restriccion_0x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_0x0.place(x=398,y=202)

    restriccion_0x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_0x1.place(x=468,y=202)

    restriccion_0x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_0x2.place(x=538,y=202)

    restriccion_0x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_0x3.place(x=608,y=202)

    #Restriccion / Fila 1

    restriccion_1x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_1x0.place(x=398,y=272)

    restriccion_1x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_1x1.place(x=468,y=272)

    restriccion_1x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_1x2.place(x=538,y=272)

    restriccion_1x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_1x3.place(x=608,y=272)

    #Restriccion / Fila 2

    restriccion_2x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_2x0.place(x=398,y=342)

    restriccion_2x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_2x1.place(x=468,y=342)

    restriccion_2x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_2x2.place(x=538,y=342)

    restriccion_2x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_2x3.place(x=608,y=342)

    #Restriccion / Fila 3

    restriccion_3x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_3x0.place(x=398,y=412)

    restriccion_3x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_3x1.place(x=468,y=412)

    restriccion_3x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_3x2.place(x=538,y=412)

    restriccion_3x3 = Label(ventana_jugar,text="",font=("Bold",12),fg="#660708",bg="#161a1d")
    restriccion_3x3.place(x=608,y=412)

    #Restriccion / Fila 4

    restriccion_4x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_4x0.place(x=398,y=482)

    restriccion_4x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_4x1.place(x=468,y=482)

    restriccion_4x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_4x2.place(x=538,y=482)

    restriccion_4x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    restriccion_4x3.place(x=608,y=482)

    #Restriccion vertical

    r_vertical_0x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d",height=1)
    r_vertical_0x0.place(x=365,y=241)

    r_vertical_0x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_0x1.place(x=435,y=241)

    r_vertical_0x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_0x2.place(x=505,y=241)

    r_vertical_0x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_0x3.place(x=575,y=241)

    r_vertical_0x4 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_0x4.place(x=645,y=241)

    # Botones r_vertical juego / fila 2

    r_vertical_1x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_1x0.place(x=365,y=311)

    r_vertical_1x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_1x1.place(x=435,y=311)

    r_vertical_1x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_1x2.place(x=505,y=311)

    r_vertical_1x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_1x3.place(x=575,y=311)

    r_vertical_1x4 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_1x4.place(x=645,y=311)

    # Botones r_vertical juego / fila 3

    r_vertical_2x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_2x0.place(x=365,y=381)

    r_vertical_2x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_2x1.place(x=435,y=381)

    r_vertical_2x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_2x2.place(x=505,y=381)

    r_vertical_2x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_2x3.place(x=575,y=381)

    r_vertical_2x4 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_2x4.place(x=645,y=381)

    # Botones r_vertical juego / fila 4

    r_vertical_3x0 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_3x0.place(x=365,y=451)

    r_vertical_3x1 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_3x1.place(x=435,y=451)

    r_vertical_3x2 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_3x2.place(x=505,y=451)

    r_vertical_3x3 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_3x3.place(x=575,y=451)

    r_vertical_3x4 = Label(ventana_jugar,text="",font=("Bold",15),fg="#660708",bg="#161a1d")
    r_vertical_3x4.place(x=645,y=451)

    matriz_de_botones()
    archivo_partida_dificultad()

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

    nombre_jugador = str(entrada_nombre_jugador.get())

    if nombre_jugador != "" and len(nombre_jugador) < 20:
        global timer
        global timer_horas, timer_minutos, timer_segundos, timer, felicidades

        #Habilitar botones de cargar y guardar

        boton_iniciar.config(state="disabled")
        boton_cargar_juego.config(state="disabled")

        boton_guardar_juego.config(state="normal")
        boton_borrar_juego.config(state="normal")
        boton_terminar.config(state="normal")
        boton_borrar_paso.config(state="normal")

        boton_numero_1.config(state="normal")
        boton_numero_2.config(state="normal")
        boton_numero_3.config(state="normal")
        boton_numero_4.config(state="normal")
        boton_numero_5.config(state="normal")


        if valor_reloj == 6:

            timer = Label(ventana_jugar,text="Timer",font=("Arial Black",12),fg="#660708",bg="#161a1d")
            timer.place(x=140,y=590)

            timer_horas = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
            timer_horas.place(x=100,y=620)

            timer_minutos = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
            timer_minutos.place(x=150,y=620)

            timer_segundos = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
            timer_segundos.place(x=200,y=620)

            timer.after(1000,timer_funcion)

        if valor_reloj == 4:

            timer = Label(ventana_jugar,text="Reloj",font=("Arial Black",12),fg="#660708",bg="#161a1d")
            timer.place(x=140,y=590)

            timer_horas = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
            timer_horas.place(x=100,y=620)

            timer_minutos = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
            timer_minutos.place(x=150,y=620)

            timer_segundos = Label(ventana_jugar,text="00",font=("Arial Black",12),bg="#161a1d",fg="white")
            timer_segundos.place(x=200,y=620)

            timer.after(1000,reloj)
        if valor_reloj == 5:
            pass
    else:
        messagebox.showinfo(title="Aviso",message= "VALIDE EL NOMBRE DEL JUGADOR, ESTE DEBE SER MAXIMO DE 2O CARACTERES ")

#Función borrar jugada

def borrar_jugada():
    if len(matriz_pila) > 0:

        ultima_jugada = matriz_pila.pop()
        matriz_botones[ultima_jugada[0]][ultima_jugada[1]].config(text="")

        valores_botones[ultima_jugada[0]][ultima_jugada[1]] = 0
        valores_botones_vertical[ultima_jugada[1]][ultima_jugada[0]] = 0

    else:
        messagebox.showinfo(title="Aviso",message= "NO HAY MÁS JUGADAS PARA BORRAR")

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

    if respuesta == False:
        pass
    else:
        while len(matriz_pila) > 0:
            ultima_jugada = matriz_pila.pop()
            matriz_botones[ultima_jugada[0]][ultima_jugada[1]].config(text="")

            valores_botones[ultima_jugada[0]][ultima_jugada[1]] = 0
            valores_botones_vertical[ultima_jugada[1]][ultima_jugada[0]] = 0
            
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
    opcion_menu.destroy()
    ventana_principal.state(newstate="normal")

#Funciones auxiliares

def señalar_nivel():
    global valor_nivel
    valor_nivel = nivel_id.get()

def señalar_reloj():
    global valor_reloj
    valor_reloj = reloj_id.get()

def señalar_posicion():
    global valor_posicion
    valor_posicion = posicion_id.get()

# Funciones cuadriculas juego:

# Fila 0

def cambio_cuadricula_0x0():
    try:
        if poner_numero in valores_botones_vertical[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[0] and poner_numero not in valores_botones_vertical[0]:
            valores_botones[0][0] = poner_numero
            valores_botones_vertical[0][0] = poner_numero
            casilla_0x0.config(text=poner_numero)
            matriz_pila.append((0,0))

        if valores_botones[1][0] != 0 and poner_numero > valores_botones[1][0] and signo_restricciones_verticales[0][0] == '˄':
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_0x0.config(text="")
            if matriz_pila[-1] == (0,0):
                valores_botones[0][0] = 0
                valores_botones_vertical[0][0] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_0x1():

    try:
        if poner_numero in valores_botones_vertical[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[0] and poner_numero not in valores_botones_vertical[1]:
            valores_botones[0][1] = poner_numero
            valores_botones_vertical[1][0] = poner_numero
            casilla_0x1.config(text=poner_numero)
            matriz_pila.append((0,1))

        if valores_botones[0][2] != 0 and poner_numero < valores_botones[0][2] and signo_restricciones_paralelas[0][1] == ">": 
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_0x1.config(text="")
            if matriz_pila[-1] == (0,1):
                valores_botones[0][1] = 0
                valores_botones_vertical[1][0] = 0
                matriz_pila.pop()

        if valores_botones[0][2] != 0 and poner_numero > valores_botones[0][2] and signo_restricciones_paralelas[0][1] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_0x1.config(text="")
            if matriz_pila[-1] == (0,1):
                valores_botones[0][1] = 0
                valores_botones_vertical[1][0] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")


def cambio_cuadricula_0x2():
    try:
         
        if poner_numero in valores_botones_vertical[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[0]and poner_numero not in valores_botones_vertical[2]:
            valores_botones[0][2] = poner_numero
            valores_botones_vertical[2][0] = poner_numero
            casilla_0x2.config(text=poner_numero)
            matriz_pila.append((0,2))

        if valores_botones[0][3] != 0 and poner_numero < valores_botones[0][3] and signo_restricciones_paralelas[0][2] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_0x2.config(text="")
            if matriz_pila[-1] == (0,2):
                valores_botones[0][2] = 0
                valores_botones_vertical[2][0] = 0
                matriz_pila.pop()
        
        if valores_botones[0][1] != 0 and poner_numero > valores_botones[0][1] and signo_restricciones_paralelas[0][1] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_0x2.config(text="")
            if matriz_pila[-1] == (0,2):
                valores_botones[0][2] = 0
                valores_botones_vertical[2][0] = 0
                matriz_pila.pop()
        
        if valores_botones[0][1] != 0 and poner_numero < valores_botones[0][1] and signo_restricciones_paralelas[0][1] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_0x2.config(text="")
            if matriz_pila[-1] == (0,2):
                valores_botones[0][2] = 0
                valores_botones_vertical[2][0] = 0
                matriz_pila.pop()
 
        
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_0x3():
    try:
        if poner_numero in valores_botones_vertical[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[0]and poner_numero not in valores_botones_vertical[3]:
            valores_botones[0][3] = poner_numero
            valores_botones_vertical[3][0] = poner_numero
            casilla_0x3.config(text=poner_numero)
            matriz_pila.append((0,3))
        
        if valores_botones[0][2] != 0 and poner_numero > valores_botones[0][2] and signo_restricciones_paralelas[0][2] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_0x3.config(text="")
            if matriz_pila[-1] == (0,3):
                valores_botones[0][3] = 0
                valores_botones_vertical[3][0] = 0
                matriz_pila.pop()
        
        if valores_botones[0][4] != 0 and poner_numero > valores_botones[0][4] and signo_restricciones_paralelas[0][3] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_0x3.config(text="")
            if matriz_pila[-1] == (0,3):
                valores_botones[0][3] = 0
                valores_botones_vertical[3][0] = 0
                matriz_pila.pop()
        
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_0x4():
    try:
        if poner_numero in valores_botones_vertical[4]:
            print(valores_botones_vertical[4])
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[0]:
            print(valores_botones[0])
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[0]and poner_numero not in valores_botones_vertical[4]:
            valores_botones[0][4] = poner_numero
            valores_botones_vertical[4][0] = poner_numero
            casilla_0x4.config(text=poner_numero)
            matriz_pila.append((0,4))
        
        if valores_botones[0][3] != 0 and poner_numero < valores_botones[0][3] and signo_restricciones_paralelas[0][3] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_0x4.config(text="")
            if matriz_pila[-1] == (0,4):
                valores_botones[0][4] = 0
                valores_botones_vertical[4][0] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

#Fila 1

def cambio_cuadricula_1x0():

    try:
        if poner_numero in valores_botones_vertical[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[1]and poner_numero not in valores_botones_vertical[0]:
            valores_botones[1][0] = poner_numero
            valores_botones_vertical[0][1] = poner_numero
            casilla_1x0.config(text=poner_numero)
            matriz_pila.append((1,0))
        
        if valores_botones[1][1] != 0 and poner_numero < valores_botones[1][1] and signo_restricciones_paralelas[1][0] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_1x0.config(text="")
            if matriz_pila[-1] == (1,0):
                valores_botones[1][0] = 0
                valores_botones_vertical[0][1] = 0
                matriz_pila.pop()
        
        if valores_botones[0][0] != 0 and poner_numero < valores_botones[0][0] and signo_restricciones_verticales[0][0] == '˄':
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_1x0.config(text="")
            if matriz_pila[-1] == (1,0):
                valores_botones[1][0] = 0
                valores_botones_vertical[0][1] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_1x1():
    try:
        if poner_numero in valores_botones_vertical[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[1]and poner_numero not in valores_botones_vertical[1]:
            valores_botones[1][1] = poner_numero
            valores_botones_vertical[1][1] = poner_numero
            casilla_1x1.config(text=poner_numero)
            matriz_pila.append((1,1))
        
        if valores_botones[1][0] != 0 and poner_numero > valores_botones[1][0] and signo_restricciones_paralelas[1][0] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_1x1.config(text="")
            if matriz_pila[-1] == (1,1):
                valores_botones[1][1] = 0
                valores_botones_vertical[1][1] = 0
                matriz_pila.pop()
        
        if valores_botones[1][2] != 0 and poner_numero > valores_botones[1][2] and signo_restricciones_paralelas[1][1] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_1x1.config(text="")
            if matriz_pila[-1] == (1,1):
                valores_botones[1][1] = 0
                valores_botones_vertical[1][1] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_1x2():
    try:
        if poner_numero in valores_botones_vertical[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[1]and poner_numero not in valores_botones_vertical[2]:
            valores_botones[1][2] = poner_numero
            valores_botones_vertical[2][1] = poner_numero
            casilla_1x2.config(text=poner_numero)
            matriz_pila.append((1,2))
        
        if valores_botones[1][1] != 0 and poner_numero < valores_botones[1][1] and signo_restricciones_paralelas[1][1] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_1x2.config(text="")
            if matriz_pila[-1] == (1,2):
                valores_botones[1][2] = 0
                valores_botones_vertical[2][1] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_1x3():
    try:
        if poner_numero in valores_botones_vertical[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[1]and poner_numero not in valores_botones_vertical[3]:
            valores_botones[1][3] = poner_numero
            valores_botones_vertical[3][1] = poner_numero
            casilla_1x3.config(text=poner_numero)
            matriz_pila.append((1,3))
        
        if valores_botones[2][3] != 0 and poner_numero > valores_botones[2][3] and signo_restricciones_verticales[1][3] == '˄':
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_1x3.config(text="")
            if matriz_pila[-1] == (1,3):
                valores_botones[1][3] = 0
                valores_botones_vertical[3][1] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_1x4():
    try:
        if poner_numero in valores_botones_vertical[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[1]and poner_numero not in valores_botones_vertical[4]:
            valores_botones[1][4] = poner_numero
            valores_botones_vertical[4][1] = poner_numero
            casilla_1x4.config(text=poner_numero)
            matriz_pila.append((1,4))
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

# Fila 2

def cambio_cuadricula_2x0():
    try:
        if poner_numero in valores_botones_vertical[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[2]and poner_numero not in valores_botones_vertical[0]:
            valores_botones[2][0] = poner_numero
            valores_botones_vertical[0][2] = poner_numero
            casilla_2x0.config(text=poner_numero)
            matriz_pila.append((2,0))
        
        if valores_botones[2][1] != 0 and poner_numero > valores_botones[2][1] and signo_restricciones_paralelas[2][0] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_2x0.config(text="")
            if matriz_pila[-1] == (2,0):
                valores_botones[2][0] = 0
                valores_botones_vertical[0][2] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_2x1():
    try:
        if poner_numero in valores_botones_vertical[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[2]and poner_numero not in valores_botones_vertical[1]:
            valores_botones[2][1] = poner_numero
            valores_botones_vertical[1][2] = poner_numero
            casilla_2x1.config(text=poner_numero)
            matriz_pila.append((2,1))
        
        if valores_botones[2][0] != 0 and poner_numero < valores_botones[2][0] and signo_restricciones_paralelas[2][0] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_2x1.config(text="")
            if matriz_pila[-1] == (2,1):
                valores_botones[2][1] = 0
                valores_botones_vertical[1][2] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_2x2():
    try:
        if poner_numero in valores_botones_vertical[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[2]and poner_numero not in valores_botones_vertical[2]:
            valores_botones[2][2] = poner_numero
            valores_botones_vertical[2][2] = poner_numero
            casilla_2x2.config(text=poner_numero)
            matriz_pila.append((2,2))

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_2x3():
    try:
        if poner_numero in valores_botones_vertical[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[2]and poner_numero not in valores_botones_vertical[3]:
            valores_botones[2][3] = poner_numero
            valores_botones_vertical[3][2] = poner_numero
            casilla_2x3.config(text=poner_numero)
            matriz_pila.append((2,3))
        
        if valores_botones[2][4] != 0 and poner_numero < valores_botones[2][4] and signo_restricciones_paralelas[2][3] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_2x3.config(text="")
            if matriz_pila[-1] == (2,3):
                valores_botones[2][3] = 0
                valores_botones_vertical[3][2] = 0
                matriz_pila.pop()
        
        if valores_botones[2][4] != 0 and poner_numero > valores_botones[2][4] and signo_restricciones_paralelas[2][3] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_2x3.config(text="")
            if matriz_pila[-1] == (2,3):
                valores_botones[2][3] = 0
                valores_botones_vertical[3][2] = 0
                matriz_pila.pop()

        if valores_botones[1][3] != 0 and poner_numero < valores_botones[1][3] and signo_restricciones_verticales[1][3] == '˄':
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_2x3.config(text="")
            if matriz_pila[-1] == (2,3):
                valores_botones[2][3] = 0
                valores_botones_vertical[3][2] = 0
                matriz_pila.pop()


    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_2x4():
    try:
        if poner_numero in valores_botones_vertical[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[2]and poner_numero not in valores_botones_vertical[4]:
            valores_botones[2][4] = poner_numero
            valores_botones_vertical[4][2] = poner_numero
            casilla_2x4.config(text=poner_numero)
            matriz_pila.append((2,4))
        
        if valores_botones[2][3] != 0 and poner_numero > valores_botones[2][3] and signo_restricciones_paralelas[2][3] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_2x4.config(text="")
            if matriz_pila[-1] == (2,4):
                valores_botones[2][4] = 0
                valores_botones_vertical[4][2] = 0
                matriz_pila.pop()

        if valores_botones[2][3] != 0 and poner_numero < valores_botones[2][3] and signo_restricciones_paralelas[2][3] == "<":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_2x4.config(text="")
            if matriz_pila[-1] == (2,4):
                valores_botones[2][4] = 0
                valores_botones_vertical[4][2] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

#Fila 3

def cambio_cuadricula_3x0():
    try:
        if poner_numero in valores_botones_vertical[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[3]and poner_numero not in valores_botones_vertical[0]:
            valores_botones[3][0] = poner_numero
            valores_botones_vertical[0][3] = poner_numero
            casilla_3x0.config(text=poner_numero)
            matriz_pila.append((3,0))
        
        if valores_botones[3][1] != 0 and poner_numero < valores_botones[3][1] and signo_restricciones_paralelas[3][0] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_3x0.config(text="")
            if matriz_pila[-1] == (3,0):
                valores_botones[3][0] = 0
                valores_botones_vertical[0][3] = 0
                matriz_pila.pop()
        
        if valores_botones[4][0] != 0 and poner_numero > valores_botones[4][0] and signo_restricciones_verticales[3][0] == '˄':
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_3x0.config(text="")
            if matriz_pila[-1] == (3,0):
                valores_botones[3][0] = 0
                valores_botones_vertical[0][3] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_3x1():
    try:
        if poner_numero in valores_botones_vertical[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[3]and poner_numero not in valores_botones_vertical[1]:
            valores_botones[3][1] = poner_numero
            valores_botones_vertical[1][3] = poner_numero
            casilla_3x1.config(text=poner_numero)
            matriz_pila.append((3,1))
        
        if valores_botones[3][0] != 0 and poner_numero > valores_botones[3][0] and signo_restricciones_paralelas[3][0] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_3x1.config(text="")
            if matriz_pila[-1] == (3,1):
                valores_botones[3][1] = 0
                valores_botones_vertical[1][3] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_3x2():
    try:
        if poner_numero in valores_botones_vertical[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[3]and poner_numero not in valores_botones_vertical[2]:
            valores_botones[3][2] = poner_numero
            valores_botones_vertical[2][3] = poner_numero
            casilla_3x2.config(text=poner_numero)
            matriz_pila.append((3,2))
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_3x3():
    try:
        if poner_numero in valores_botones_vertical[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[3]and poner_numero not in valores_botones_vertical[3]:
            valores_botones[3][3] = poner_numero
            valores_botones_vertical[3][3] = poner_numero
            casilla_3x3.config(text=poner_numero)
            matriz_pila.append((3,3))

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_3x4():
    try:
        if poner_numero in valores_botones_vertical[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[3]and poner_numero not in valores_botones_vertical[4]:
            valores_botones[3][4] = poner_numero
            valores_botones_vertical[4][3] = poner_numero
            casilla_3x4.config(text=poner_numero)
            matriz_pila.append((3,4))

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

#Fila 4

def cambio_cuadricula_4x0():
    try:
        if poner_numero in valores_botones_vertical[0]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[4]and poner_numero not in valores_botones_vertical[0]:
            valores_botones[4][0] = poner_numero
            valores_botones_vertical[0][4] = poner_numero
            casilla_4x0.config(text=poner_numero)
            matriz_pila.append((4,0))
        
        if valores_botones[3][0] != 0 and poner_numero < valores_botones[3][0] and signo_restricciones_verticales[3][0] == '˄':
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_4x0.config(text="")
            if matriz_pila[-1] == (4,0):
                valores_botones[4][0] = 0
                valores_botones_vertical[0][4] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_4x1():
    try:
        if poner_numero in valores_botones_vertical[1]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[4]and poner_numero not in valores_botones_vertical[1]:
            valores_botones[4][1] = poner_numero
            valores_botones_vertical[1][4] = poner_numero
            casilla_4x1.config(text=poner_numero)
            matriz_pila.append((4,1))

        if valores_botones[4][2] != 0 and poner_numero < valores_botones[4][2] and signo_restricciones_paralelas[4][1] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_4x1.config(text="")
            if matriz_pila[-1] == (4,1):
                valores_botones[4][1] = 0
                valores_botones_vertical[1][4] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_4x2():
    try:
        if poner_numero in valores_botones_vertical[2]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[4]and poner_numero not in valores_botones_vertical[2]:
            valores_botones[4][2] = poner_numero
            valores_botones_vertical[2][4] = poner_numero
            casilla_4x2.config(text=poner_numero)
            matriz_pila.append((4,2))

        if valores_botones[4][1] != 0 and poner_numero > valores_botones[4][1] and signo_restricciones_paralelas[4][1] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_4x2.config(text="")
            if matriz_pila[-1] == (4,2):
                valores_botones[4][2] = 0
                valores_botones_vertical[2][4] = 0
                matriz_pila.pop()

        if valores_botones[4][3] != 0 and poner_numero < valores_botones[4][3] and signo_restricciones_paralelas[4][2] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_4x2.config(text="")
            if matriz_pila[-1] == (4,2):
                valores_botones[4][2] = 0
                valores_botones_vertical[2][4] = 0
                matriz_pila.pop()
    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_4x3():
    try:
        if poner_numero in valores_botones_vertical[3]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[4]and poner_numero not in valores_botones_vertical[3]:
            valores_botones[4][3] = poner_numero
            valores_botones_vertical[3][4] = poner_numero
            casilla_4x3.config(text=poner_numero)
            matriz_pila.append((4,3))
        
        if valores_botones[4][4] != 0 and poner_numero < valores_botones[4][4] and signo_restricciones_paralelas[4][3] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MAYOR")
            casilla_4x3.config(text="")
            if matriz_pila[-1] == (4,3):
                valores_botones[4][3] = 0
                valores_botones_vertical[3][4] = 0
                matriz_pila.pop()
        
        if valores_botones[4][2] != 0 and poner_numero > valores_botones[4][2] and signo_restricciones_paralelas[4][2] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_4x3.config(text="")
            if matriz_pila[-1] == (4,3):
                valores_botones[4][3] = 0
                valores_botones_vertical[3][4] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

def cambio_cuadricula_4x4():
    try:
        if poner_numero in valores_botones_vertical[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA COLUMNA")

        if poner_numero in valores_botones[4]:
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE EL ELEMENTO YA ESTÁ EN LA FILA")

        if poner_numero not in valores_botones[4]and poner_numero not in valores_botones_vertical[4]:
            valores_botones[4][4] = poner_numero
            valores_botones_vertical[4][4] = poner_numero
            casilla_4x4.config(text=poner_numero)
            matriz_pila.append((4,4))
        
        if valores_botones[4][3] != 0 and poner_numero > valores_botones[4][3] and signo_restricciones_paralelas[4][3] == ">":
            messagebox.showinfo(title="Casilla",message= "JUGADA NO ES VÁLIDA PORQUE NO CUMPLE CON LA RESTRICCIÓN DE MENOR")
            casilla_3x0.config(text="")
            if matriz_pila[-1] == (4,4):
                valores_botones[4][4] = 0
                valores_botones_vertical[4][4] = 0
                matriz_pila.pop()

    except:
        messagebox.showinfo(title="Casilla",message= "FALTA QUE SELECCIONE UN DÍGITO")

# Función Timer

def aceptar_configuracion():

    global seg_timer
    global min_timer 
    global hora_timer

    global seg_aux
    global min_aux
    global hora_aux

    if valor_reloj == 6:
        try:
                seg_timer = int(timer_entrada_segundos.get())
                min_timer = int(timer_entrada_minutos.get())
                hora_timer = int(timer_entrada_horas.get())

                seg_aux = int(timer_entrada_segundos.get())
                min_aux = int(timer_entrada_minutos.get())
                hora_aux = int(timer_entrada_horas.get())

            
                if seg_timer > 0 or min_timer > 0 or hora_timer > 0:
                    ventana_conf.state(newstate="withdraw")
                    ventana_principal.state(newstate="normal")
                else:
                    messagebox.showinfo(title="Timer",message="Para el uso del timer alguna de sus partes debe ser mayor a cero")
        except:
            messagebox.showinfo(title="Timer",message="Verifique los valores del timer esten completos")
    else:
        ventana_conf.state(newstate="withdraw")
        ventana_principal.state(newstate="normal")
        
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
    timer.after(1000,reloj)

def timer_funcion():
    global seg_timer,min_timer,hora_timer
    global seg_aux,min_aux,hora_aux

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

                            seg_aux += 1
                            if seg_aux == 60:
                                seg_aux = 0
                                min_aux +=1
                                if min_aux == 60:
                                    min_aux = 0
                                    hora_aux +=1
                        else:
                            ventana_jugar.state(newstate="withdraw")
                            func_jugar()
    if seg_timer >= 0:
        timer_segundos.config(text=seg_timer)
    timer_horas.config(text=hora_timer)
    timer_minutos.config(text=min_timer)
    timer.after(1000,timer_funcion)
# Archivos

def archivo_partida_dificultad():
    import pickle
    import random

    global matriz_botones, valores_botones, indice, subindice

    f = open("prueba.dat","wb")
    pickle.dump([
                [(("4",0,1),("1",0,3),("2",2,1),("5",2,3),("3",2,4),("1",3,1),("2",3,3),("5",4,4)),
                (("2",0,3),("2",1,0),("1",1,2),("3",1,3),("3",2,2),("1",2,3),("1",4,0),("5",4,4)),
                (("5",0,2),("1",1,0),("3",1,1),("2",1,4),("3",3,0),("1",3,4),("1",4,3),("5",4,4))
                ],

                [
                (("5",0,0),("3",0,4),(">",0,2),("2",1,1),("˅",2,0),(">",3,0),("˄",3,2),(">",4,1)),
                (("2",0,0),("˅",0,0),("4",0,1),("˅",1,3),("˄",1,4),(">",2,3),("2",2,4),(">",4,3)),
                (("5",0,0),("<",0,1),("˄",1,0),("3",1,3),("˄",3,1),("˄",3,3),("3",4,1),(">",4,2))
                ],

                [
                (("2",0,0),("˅",0,4),("˅",1,0),("<",1,1),("5",2,1),("<",2,3),(">",3,0),("˅",3,3),("1",4,2)),
                ((">",0,1),("4",0,3),("˄",0,3),(">",1,0),("4",1,4),("<",2,0),("˄",2,1),("˄",2,0),("1",3,3)),
                (("˄",0,0),("<",0,3),("5",1,0),(">",0,1),("˄",1,3),("4",2,1),("˅",2,4),(">",3,0),("˄",3,0))
                ]
                ],f)
    f.close()

    f = open("prueba.dat","rb")
    while True:
        try:
            x = pickle.load(f)
            a = x
        except EOFError:
            break
    f.close()

    indice = valor_nivel - 1
    subindice = random.randint(0,2)

    for elemento in a[2][2]:
        if elemento[0] == "<" or elemento[0] == ">":

            restricciones_paralelas[elemento[1]][elemento[2]].config(text=elemento[0])
            signo_restricciones_paralelas[elemento[1]][elemento[2]] = elemento[0]


        elif elemento[0] == "˄" or elemento[0] == "˅":

            restricciones_verticales[elemento[1]][elemento[2]].config(text=elemento[0])
            signo_restricciones_verticales[elemento[1]][elemento[2]] = elemento[0]

        else:

            matriz_botones[elemento[1]][elemento[2]].config(text=elemento[0])
            matriz_botones[elemento[1]][elemento[2]].config(command=casilla_fija)

            valores_botones[elemento[1]][elemento[2]] = int(elemento[0])
            valores_botones_vertical[elemento[2]][elemento[1]]= int(elemento[0])

    print(signo_restricciones_verticales)

def casilla_fija():
    messagebox.showinfo(title="Timer",message="JUGADA NO ES VÁLIDA PORQUE ESTE ES UN DÍGITO FIJO")

def matriz_de_botones():

    global matriz_botones, valores_botones, restricciones_paralelas, restricciones_verticales, valores_botones_vertical, matriz_pila
    global signo_restricciones_paralelas, signo_restricciones_verticales

    global valor_0x0
    global valor_0x1
    global valor_0x2
    global valor_0x3
    global valor_0x4

    global valor_1x0
    global valor_1x1
    global valor_1x2
    global valor_1x3
    global valor_1x4

    global valor_2x0
    global valor_2x1
    global valor_2x2
    global valor_2x3
    global valor_2x4

    global valor_3x0
    global valor_3x1
    global valor_3x2
    global valor_3x3
    global valor_3x4

    global valor_4x0
    global valor_4x1
    global valor_4x2
    global valor_4x3
    global valor_4x4

    valor_0x0 = 0
    valor_0x1 = 0
    valor_0x2 = 0
    valor_0x3 = 0
    valor_0x4 = 0

    valor_1x0 = 0
    valor_1x1 = 0
    valor_1x2 = 0
    valor_1x3 = 0
    valor_1x4 = 0

    valor_2x0 = 0
    valor_2x1 = 0
    valor_2x2 = 0
    valor_2x3 = 0
    valor_2x4 = 0

    valor_3x0 = 0
    valor_3x1 = 0
    valor_3x2 = 0
    valor_3x3 = 0
    valor_3x4 = 0

    valor_4x0 = 0
    valor_4x1 = 0
    valor_4x2 = 0
    valor_4x3 = 0
    valor_4x4 = 0

    matriz_botones = [[casilla_0x0,casilla_0x1,casilla_0x2,casilla_0x3,casilla_0x4],\
                      [casilla_1x0,casilla_1x1,casilla_1x2,casilla_1x3,casilla_1x4],\
                      [casilla_2x0,casilla_2x1,casilla_2x2,casilla_2x3,casilla_2x4],\
                      [casilla_3x0,casilla_3x1,casilla_3x2,casilla_3x3,casilla_3x4],\
                      [casilla_4x0,casilla_4x1,casilla_4x2,casilla_4x3,casilla_4x4]]
    
    valores_botones = [[valor_0x0,valor_0x1,valor_0x2,valor_0x3,valor_0x4],\
                      [valor_1x0,valor_1x1,valor_1x2,valor_1x3,valor_1x4],\
                      [valor_2x0,valor_2x1,valor_2x2,valor_2x3,valor_2x4],\
                      [valor_3x0,valor_3x1,valor_3x2,valor_3x3,valor_3x4],\
                      [valor_4x0,valor_4x1,valor_4x2,valor_4x3,valor_4x4]]

    valores_botones_vertical = [[valor_0x0,valor_1x0,valor_2x0,valor_3x0,valor_4x0],\
                                [valor_0x1,valor_1x1,valor_2x1,valor_3x1,valor_4x1],\
                                [valor_0x2,valor_1x2,valor_2x2,valor_3x2,valor_4x2],\
                                [valor_0x3,valor_1x3,valor_2x3,valor_3x3,valor_4x3],\
                                [valor_0x4,valor_1x4,valor_2x4,valor_3x4,valor_4x4]]

    restricciones_paralelas = [[restriccion_0x0,restriccion_0x1,restriccion_0x2,restriccion_0x3],\
                               [restriccion_1x0,restriccion_1x1,restriccion_1x2,restriccion_1x3],\
                               [restriccion_2x0,restriccion_2x1,restriccion_2x2,restriccion_2x3],\
                               [restriccion_3x0,restriccion_3x1,restriccion_3x2,restriccion_3x3],\
                               [restriccion_4x0,restriccion_4x1,restriccion_4x2,restriccion_4x3,]]
 
    restricciones_verticales = [[r_vertical_0x0,r_vertical_0x1,r_vertical_0x2,r_vertical_0x3,r_vertical_0x4],\
                                [r_vertical_1x0,r_vertical_1x1,r_vertical_1x2,r_vertical_1x3,r_vertical_1x4],\
                                [r_vertical_2x0,r_vertical_2x1,r_vertical_2x2,r_vertical_2x3,r_vertical_2x4],\
                                [r_vertical_3x0,r_vertical_3x1,r_vertical_3x2,r_vertical_3x3,r_vertical_3x4]]

    signo_restricciones_paralelas = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
    signo_restricciones_verticales = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    
    matriz_pila = []
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
                    