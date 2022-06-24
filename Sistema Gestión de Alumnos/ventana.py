from csv import list_dialects
from fileinput import close
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image,ImageOps
from PIL import ImageTk
import os
import tkinter as tk

#Labels
class Label:
    def __init__(self):
        pass

    def hacer_etiqueta_grid(self,ventana,text,row,column,columnspan,padx,pady):
        etiqueta = tk.Label(ventana,text=text)
        etiqueta.grid(row=row,column=column,columnspan=columnspan,padx=padx,pady=pady)

    def hacer_etiqueta_place(self,ventana,text,x,y,font,bg):
        etiqueta = tk.Label(ventana,text=text,font=font)
        etiqueta.place(x=x,y=y)

#Entradas
class Entry:
    def __init__(self):
        self.dato = tk.StringVar()

    def hacer_entrada_grid(self,ventana,fg,row,column,validate,validatecommand):
        entrada = tk.Entry(ventana, fg=fg,validate=validate,validatecommand=validatecommand,textvariable=self.dato)
        entrada.grid(row=row,column=column)

    def hacer_entrada_place(self,ventana,x,y,show):
        entrada = tk.Entry(ventana,show=show,textvariable=self.dato)
        entrada.place(x=x,y=y)

    def obtener_entrada(self):
        valor = self.dato.get()
        return valor

    def reiniciar_valor(self):
        self.dato.set('')

#Casillas de marcado
class CheckButton():
    def __init__(self,nombre):
        self.dato = tk.BooleanVar()
        self.nombre = nombre 
        
    def hacer_check_button(self,ventana,text,row,column,sticky,padx):
        checkbutton = tk.Checkbutton(ventana,text=text,variable=self.dato)
        checkbutton.grid(row=row,column=column,sticky=sticky,padx=padx)

    def obtener_valor(self):
        valor = self.dato.get()
        return valor

    def reiniciar_valor(self):
        self.dato.set(False)

#Listas desplegables
class ComboBox(Entry):
    def hacer_lista_desplegable(self,ventana,state,values,width,row,column,pady):
        lista = ttk.Combobox(ventana,state=state,values=values, width=width ,textvariable=self.dato)
        lista.grid(row=row,column=column,pady=pady)

    def hacer_entrada_place(self,ventana,state,values,x,y):
        lista = ttk.Combobox(ventana,state=state,values=values)
        lista.place(x=x,y=y)

#Botones
class Button:
    def __init__(self):
        pass

    def hacer_boton_grid(self,ventana,text,row,column,columspan,padx,pady,activeforeground,activebackground,command):
        boton = tk.Button(ventana,text=text, activeforeground=activeforeground,activebackground=activebackground, command=command)
        boton.grid(row=row,column=column,columnspan=columspan,padx=padx,pady=pady)

    def hacer_boton_place(self,ventana,text,x,y,command):
        boton = tk.Button(ventana,text=text,command=command)
        boton.place(x=x,y=y)

#Alerta
class MessageBox:

    def __init__(self,text,mensaje):
        self.text= text
        self.mensaje = mensaje
        messagebox.showwarning(self.text,self.mensaje)

#Estudiante
class Estudiante:

    def __init__(self,nombre,apellido,dni,domicilio,genero,anio,materias):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.domicilio = domicilio
        self.genero = genero
        self.anio = anio
        self.materias = materias


#Funciones
#Iniciar sesión con bóton
def boton_login(usuario, contraseña,ventana,ventana2):
    valor_usuario = usuario.obtener_entrada()
    valor_contraseña = contraseña.obtener_entrada()

    if len(valor_usuario) == 0:
        alerta = MessageBox('Alerta','El campo Usuario es obligatorio.')
    
    if len(valor_contraseña) == 0:
        alerta = MessageBox('Alerta','El campo Contraseña es obligatorio.')

    elif valor_usuario == 'Usuario2022' and valor_contraseña == '@Usuario2022':
        ventana.destroy()
        ventana2()

    else:
        alerta = MessageBox('Alerta','Las credenciales ingresadas son inválidas.')

#Restringir entrada DNI a numeros
def validar_si_decimal(text):
    return text.isdecimal()

#Seleccionar Imagen desde biblioteca
imagen = None 
def boton_seleccionar_foto(ventana_principal):
    global imagen 
    tipos = (('Imágenes', '*.jpg *.png *'), ('Todos los archivos', '*'))

    archivo = fd.askopenfilename(title='Abrir archivo...', initialdir='/imágenes', filetypes=tipos)

    if archivo:
        messagebox.showinfo('Mensaje', archivo)

    if (archivo):
        imagen = tk.PhotoImage(file=archivo)
        lbl_img = tk.Label(ventana_principal,image=imagen)
        lbl_img.place(relx=0.5, rely=0.1,relwidth=0.4,relheight=0.5)

def checkear_materia(materias):
    materias_cursadas = []
    for materia in materias:
        if (materia.obtener_valor() == True):
            materias_cursadas.append(materia.nombre)
    return tuple(materias_cursadas)

#1.Añadir entradas a archivo y listbox ventana principal
def boton_aniadir(ventana,*entradas):
    nombre = entradas[0].obtener_entrada()
    apellido = entradas[1].obtener_entrada()
    dni = entradas[2].obtener_entrada()
    domicilio = entradas[3].obtener_entrada()
    genero = entradas[4].obtener_entrada()
    anio = entradas[5].obtener_entrada()
    materias = checkear_materia(entradas[6])
    estudiante = Estudiante(nombre,apellido,dni,domicilio,genero,anio,materias)
    gestionar_archivo(nombre,apellido,dni,domicilio,genero,anio,materias)
    agregar_label_caja_texto(ventana)
    boton_limpiar(entradas[6],entradas[0],entradas[1],entradas[2],entradas[3],entradas[4],entradas[5])

#1.5Limpiar entradas de la ventana principal
def boton_limpiar(materias,*entradas):
    for entrada in entradas:
        entrada.reiniciar_valor()
    for materia in materias:
        materia.reiniciar_valor()

#Eliminar estudiante de archivo de texto y listbox ventana principal
def eliminar_estudiante(lista):
    indice = lista.curselection()
    lista.delete(indice[0])
    archivo = open('alumnos/estudiantes.txt','r',encoding='utf-8')
    lineas = archivo.readlines()
    archivo.close()

    archivo = open('alumnos/estudiantes.txt','w',encoding='utf-8')
    pos = indice[0]
    linea = lineas[pos]
    lineas.remove(linea)
    for linea in lineas:
        archivo.write(linea)
    archivo.close()
#1.4Comprobar si una materia es seleccionada

#1.2Añadir entradas a archivo txt
def gestionar_archivo(nombre,apellido,dni,domicilio,genero,anio,materias):
    if (os.path.exists('alumnos/estudiantes.txt')):
        archivo = open('alumnos/estudiantes.txt','at',encoding='utf-8')
        archivo.write('N:{} A:{} D:{} DO:{} GE:{} AÑ:{}!{}\n'.format(nombre,apellido,dni,domicilio,genero,anio,materias))
        archivo.close
    else:
        archivo = open('alumnos/estudiantes.txt','w+',encoding='utf-8')
        archivo.write('N:{} A:{} D:{} DO:{} GE:{} AÑ:{}!{}\n'.format(nombre,apellido,dni,domicilio,genero,anio,materias))
        archivo.close

#1.3Agregar entradas a listbox ventana principal
def agregar_label_caja_texto(ventana):
    archivo = open('alumnos/estudiantes.txt','r',encoding='utf-8')
    ventana.delete(0,tk.END)
    tamaño_linea = 0
    for linea in archivo:
        cadena = ''
        tamaño_linea += len(linea)
        for word in range(0,tamaño_linea):
            if ((linea[word] == 'N' and linea[word+1] == ':')or(linea[word] == ':')):
                continue
            elif ((linea[word] == 'A' and linea[word+1] == ':')or(linea[word] == ':')):
                continue
            elif ((linea[word] == 'D' and linea[word+1] == ':')or(linea[word] == ':')):
                continue
            elif ((linea[word] == 'D' and linea[word+1] == 'O' and linea[word+2] == ':')or(linea[word] == 'O' and linea[word+1] == ':')):
                continue
            elif ((linea[word] == 'G' and linea[word+1] == 'E' and linea[word+2] == ':')or(linea[word] == 'E' and linea[word+1] == ':')):
                continue
            elif ((linea[word] == 'A' and linea[word+1] == 'Ñ' and linea[word+2] == ':')or(linea[word] == 'Ñ' and linea[word+1] == ':')):
                continue
            elif (linea[word] == '!'):
                break
            else:
                cadena += linea[word]
        ventana.insert(tk.END,cadena)

def cerrar_ventana(ventana_cerrar,ventana_abrir):
    ventana_cerrar.destroy()
    ventana_abrir()

#Presionar nombre de Listbox de ventana principal para entrar a ventana perfil
nombre_estudiante = ''
apellido_estudiante = ''
dni_estudiante = ''
domicilio_estudiante = ''
materias_estudiante = ''
lista_materias_estudiante = []
def boton_list_box(ventana_cerrar,ventana_abrir,lista):
    global nombre_estudiante
    global apellido_estudiante
    global dni_estudiante
    global domicilio_estudiante
    global materias_estudiante
    global lista_materias_estudiante
    indice = lista.curselection()
    nombre_estudiante = ''
    apellido_estudiante = ''
    dni_estudiante = ''
    domicilio_estudiante = ''
    materias_estudiante = ''
    lista_materias_estudiante = []
    archivo_txt = open("alumnos/estudiantes.txt","r",encoding='utf-8')
    lista_archivo = archivo_txt.readlines()
    archivo_txt.close()
    tamaño_elemento = len(lista_archivo[indice[0]])
    for word in range(0,tamaño_elemento):
        if ((lista_archivo[indice[0]][word] == 'N' and lista_archivo[indice[0]][word+1] == ':')):
            word += 2
            while(not(lista_archivo[indice[0]][word] == 'A' and lista_archivo[indice[0]][word+1] == ':')):
                nombre_estudiante += lista_archivo[indice[0]][word]
                word += 1
        elif ((lista_archivo[indice[0]][word] == 'A' and lista_archivo[indice[0]][word+1] == ':')):
            word += 2
            while(not(lista_archivo[indice[0]][word] == 'D' and lista_archivo[indice[0]][word+1] == ':')):
                apellido_estudiante += lista_archivo[indice[0]][word]
                word += 1
        elif ((lista_archivo[indice[0]][word] == 'D' and lista_archivo[indice[0]][word+1] == ':')):
            word += 2
            while(not(lista_archivo[indice[0]][word] == 'D' and lista_archivo[indice[0]][word+1] == 'O'and lista_archivo[indice[0]][word+2] == ':')):
                dni_estudiante += lista_archivo[indice[0]][word]
                word += 1      
        elif ((lista_archivo[indice[0]][word] == 'D' and lista_archivo[indice[0]][word+1] == 'O' and lista_archivo[indice[0]][word+2] == ':')):
            word += 3
            while(not(lista_archivo[indice[0]][word] == 'G' and lista_archivo[indice[0]][word+1] == 'E'and lista_archivo[indice[0]][word+2] == ':')):
                domicilio_estudiante += lista_archivo[indice[0]][word]
                word += 1 
        elif (lista_archivo[indice[0]][word] == '!'):
            word += 2
            while(not(lista_archivo[indice[0]][word] == ')')):
                if (lista_archivo[indice[0]][word] != "'" and lista_archivo[indice[0]][word] != " "):
                    materias_estudiante += lista_archivo[indice[0]][word]
                word += 1
        elif (lista_archivo[indice[0]][word] == ')'):
            break
    archivo_txt.close()
    lista_materias_estudiante = materias_estudiante.split(',')
    print(lista_materias_estudiante)
    cerrar_ventana(ventana_cerrar,ventana_abrir)

#Modificar ventana perfil para llevar datos desde archivo de texto
def modificar_ventana(*entradas):
    entradas[0]['text'] = '{} {}'.format(nombre_estudiante,apellido_estudiante)
    entradas[1]['text'] = dni_estudiante
    entradas[2]['text'] = domicilio_estudiante
    entradas[3]['values'] = lista_materias_estudiante

#Limpiar notas al cambiar materia
def limpiar_notas(label_promedio,label_estado,*notas):
    label_promedio['text'] = ''
    label_estado['text'] = ''
    notas[0].delete(0, 'end')
    notas[1].delete(0, 'end')
    notas[2].delete(0, 'end')

#cambiar materia
def cambiar_seleccion(selector,label_promedio,label_estado,*notas):
    selection = selector.get()
    limpiar_notas(label_promedio,label_estado,*notas)
    messagebox.showinfo(
        title="Materia Seleccionada",
        message= f' Has seleccionado {selection}'
    )

#Calcular promedio de una materia
def calcular_promedio(promedio,label_estado,*notas):
    try:
        numero_notas = len(notas)
        nota_uno = notas[0].get()
        nota_dos = notas[1].get()
        nota_tres = notas[2].get()
        suma = float(nota_uno) + float(nota_dos) + float(nota_tres)
        resultado = suma/numero_notas
        promedio['text'] = ('{:.2}'.format(resultado))
        comprobar_estado_estudiante(label_estado,promedio)
    except:
        messagebox.showwarning(title='Error en entrada',message='Debes llenar todos los campos con números')

#Comprobar si el estudiante aprobó o reprobó una materia 
def comprobar_estado_estudiante(label_promedio,promedio):
    if (float(promedio['text']) >= 3 and float(promedio['text']) <= 5):
        label_promedio['text'] = ('Aprobado')
        label_promedio['fg'] = ('green')
    else:
        label_promedio['text'] = ('Reprobado')
        label_promedio['fg'] = ('red')



