from tkinter import *
import  random
import datetime
from tkinter import filedialog, messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# operador almacenara todo el string que se ingrese en la calculadora


def click_boton(numero):
    # Para mostrar en pantalla segun sea el boton que se presione
    global operador
    # Se concatena para que aparezcan todos los botones que se presionen
    # De lo contrario se sustituiria cada vez que se presione
    operador = operador + numero
    # Esto evita que el string concatenado se repita, borrando la posicion anterior
    visor_calculadora.delete(0, END)
    # Y sustituyendola por la siguiente:
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    # Primero se evalua la operacion
    # Posteriormente se convierte a string el resultado
    resultado = str(eval(operador))
    # Se elimina el contenido actual de visor calculadora
    visor_calculadora.delete(0, END)
    # Se inserta el resultado guardado en "resultado"
    visor_calculadora.insert(0, resultado)

    # Operador se "reinicia"
    operador = ''

    # Nota: No se recomienda el uso de eval() en situaciones donde la seguridad del programa sea de interes
    # Existen alternativas mas seguras para eval, por ejemplo safe_eval()


def revisar_check():
    # Contador para saber en que iteracion estamos
    x = 0
    for check in cuadros_comida:
        if variables_comida[x].get() == 1:  # chequear que este activado, 1 = ACTIVO
            # Cuadros comida deja de ser DISABLED
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                # Se elimina el 0 contenido
                cuadros_comida[x].delete(0, END)
            # Aparece un cursor para escribir
            cuadros_comida[x].focus()
        # Cuando el check se desactive:
        else:
            # Vuelve al estado DISABLED
            cuadros_comida[x].config(state=DISABLED)
            # Vuelve a setearse en 0
            texto_comida[x].set("0")
        # Pasamos a la siguiente iteracion, segun sea el caso
        x += 1

    # Se repiten exactamente los mismos pasos
    x = 0
    for check in cuadros_bebida:
        if variables_bebida[x].get() == 1:  # chequear que este activado, 1 = ACTIVO
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                # Se elimina el 0 contenido
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set("0")
        x += 1

    x = 0
    for check in cuadros_postres:
        if variables_postre[x].get() == 1:  # chequear que este activado, 1 = ACTIVO
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                # Se elimina el 0 contenido
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set("0")
        x += 1

        """elif variables_comida[x].get() == 0:
            cuadros_comida[x].config(state=DISABLED)"""


def total():
    # Comida
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        # Sub_total_comida es la variable que tomara el valor de la suma de cantidad y precios_comida
        # p solamente seria el indice para identificar la iteracion
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    # Bebidas
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    # Postres
    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    # Se setean los resultados para mostrarlos en pantalla
    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos)}')
    var_total.set(f'$ {round(total)}')

def recibo():
    # La posicion 1.0 se posicion en el primer caracter de la cadena
    # Se borrara desde el primer caracter hasta el final (END)
    # Esto es para crear otro recibo, borrando lo que hubiese anteriormente
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 60 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 71 + '\n')

    # Variable para realizar iteraciones
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t\t'
                                     f'${int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t\t'
                                     f'${int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t\t'
                                     f'${int(postre.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 71 + '\n')
    texto_recibo.insert(END,f'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-' * 71 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'-' * 71 + '\n')
    texto_recibo.insert(END, '\t   Vuelva pronto!')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', "Archivo Guardado")


def reset():
    texto_recibo.delete(0.1, END)
    visor_calculadora.delete(0, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state = DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state = DISABLED)

    for variable in variables_comida:
        variable.set(0)
    for variable in variables_bebida:
        variable.set(0)
    for variable in variables_postre:
        variable.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

# iniciar tkinter
aplicacion = Tk()

# Tamaño de la ventana
aplicacion.geometry('1300x550+0+0')

# Evitar maximizar
aplicacion.resizable(0, 0)

# Titulo de la centana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# Color de fondo de la ventana
aplicacion.config(bg='burlywood')

# Panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Sistema de Facturacion", fg='azure4',
                        font=('Dosis', 48), bg='burlywood', width=34)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=180)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# Panel Bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# Panel Postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel Derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel Calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Panel Recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel Botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'pizza', 'hamburguesa', 'tacos', 'milanesa']
lista_bebidas = ['agua natural', 'soda de sabor', 'te', 'cafe', 'agua de sabor', 'cola', 'agua mineral', 'batido']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'galletas', 'mousse', 'pastel', 'pay']

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # Crear los chekbuttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=8,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# Generar itemsa bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # Crear los chekbuttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()

    bebida = Checkbutton(panel_bebidas, text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=8,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# Generar items postres
variables_postre = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    # Crear los chekbuttons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postres = Checkbutton(panel_postres, text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postre[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # Crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=8,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)

    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costo y los campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text="Costo Comida",
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos,
                           bd=1,
                           font=('Dosis', 12, 'bold'),
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida
                           )

texto_costo_comida.grid(row=0, column=1, padx=35)

# Etiquetas de costo y los campos de entrada
etiqueta_costo_bebida = Label(panel_costos,
                              text="Costo Bebidas",
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos,
                           bd=1,
                           font=('Dosis', 12, 'bold'),
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida
                           )

texto_costo_bebida.grid(row=1, column=1, padx=35)

# Etiquetas de costo y los campos de entrada
etiqueta_costo_postre = Label(panel_costos,
                              text="Costo Postres",
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos,
                           bd=1,
                           font=('Dosis', 12, 'bold'),
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre
                           )

texto_costo_postre.grid(row=2, column=1, padx=35)

# Etiquetas de costo y los campos de entrada
etiqueta_subtotal = Label(panel_costos,
                          text="Subtotal",
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                       bd=1,
                       font=('Dosis', 12, 'bold'),
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal
                       )

texto_subtotal.grid(row=0, column=3, padx=35)

# Etiquetas de costo y los campos de entrada
etiqueta_impuesto = Label(panel_costos,
                          text="Impuesto",
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(panel_costos,
                       bd=1,
                       font=('Dosis', 12, 'bold'),
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto
                       )

texto_impuesto.grid(row=1, column=3, padx=35)

# Etiquetas de costo y los campos de entrada
etiqueta_total = Label(panel_costos,
                       text="Total",
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,
                    bd=1,
                    font=('Dosis', 12, 'bold'),
                    width=10,
                    state='readonly',
                    textvariable=var_total
                    )

texto_total.grid(row=2, column=3, padx=35)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Reset']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)

    botones_creados.append(boton)

    boton.grid(row=0, column=columnas)

    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=reset)

# Area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=40,
                    height=10)

texto_recibo.grid(row=0, column=0)

# Calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=29,
                          bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'CE', 'Borrar', '0', '/']

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    # se toma la informacion de la iteracion actual y se le da formato
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   bg='azure4',
                   bd=1,
                   width=6)

    botones_guardados.append(boton)

    # Posicionamiento del boton
    boton.grid(row=fila, column=columna)
    # Comprueba si el valor columna, originalmente en 0 ha llegado hasta 3
    # Recuerda que comienza el conteo desde 0
    if columna == 3:
        # Si la condicion se cumple, la fila se incrementa en 1 para avanzar un espacio hacia abajo
        fila += 1
    # La columna se incrementa naturalmente en 1 para pasar al siguiente espacio
    columna += 1
    # Si la columna alcanza un maximo de 4 resetea a 0 para volver a empezar
    if columna == 4:
        columna = 0
        # Columnas -- Filas
        #            0 1 2 3
        #   0 ------ 7 8 9 +
        #   1 ------ 4 5 6 -
        #   2 ------ 1 2 3 x
        #   3 ------ ce b 0 /

# Uso de lambda:
# Funcion simple (o anonima) que llamara la funcion click_button cuando se haga click en el boton
botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# Evitar que la pantalla se cierre
aplicacion.mainloop()
