import tkinter as tk
from tkinter import Image, PhotoImage, ttk
from tkinter import messagebox
import ventana

#Ventana Bienvenida
def ventana_bienvenida():
    #Inicialización, Título, Tamaño, Posición, Ïcono.
    bienvenida = tk.Tk()
    bienvenida.title('Bienvenida')
    bienvenida.geometry('350x350+400+200')
    bienvenida.iconbitmap('iconos/birrete.ico')
    bienvenida.resizable(False, False)

    #Cartel Bienvenida 
    ##Label
    datos = ventana.Label()
    datos.hacer_etiqueta_place(bienvenida,'¡Bienvenido!',73,90,('Helvetica',27),'transparent')
    
    ##Botón
    b_inicia_sesion = ventana.Button()
    b_inicia_sesion.hacer_boton_place(bienvenida,'Inicia sesión',140,180,lambda: ventana.cerrar_ventana(bienvenida,ventana_iniciar_sesion))

    #Ciclo ventana Bienvenida
    bienvenida.mainloop()

    
#Ventana Iniciar Sesión
def ventana_iniciar_sesion(): 
    #Inicialización, Título, Tamaño, Posición, Ïcono.
    iniciar_sesion = tk.Tk()
    iniciar_sesion.title('Iniciar Sesión')
    iniciar_sesion.geometry('300x200+430+250')
    iniciar_sesion.iconbitmap('iconos/birrete.ico')
    iniciar_sesion.resizable(False,False)

    #Datos a Ingresar
    ##Usuario
    ###Label
    datos = ventana.Label()
    datos.hacer_etiqueta_place(iniciar_sesion,'Usuario:',45,50,('Helvetica',11),'transparent')
    ###Entry
    usuario =ventana.Entry()
    usuario.hacer_entrada_place(iniciar_sesion,130,50,'')
    
    ##Contraseña
    ###Label
    datos.hacer_etiqueta_place(iniciar_sesion,'Contraseña:',45,75,('Helvetica',11),'transparent')
    ###Entry
    contraseña = ventana.Entry()
    contraseña.hacer_entrada_place(iniciar_sesion,130,75,'*')
    
    ##Botón 
    b_iniciar_sesion= ventana.Button()
    b_iniciar_sesion.hacer_boton_place(iniciar_sesion,'Iniciar sesión',113,120,lambda:ventana.boton_login(usuario,contraseña,iniciar_sesion,ventana_principal))

    #Ciclo ventana Iniciar Sesión
    iniciar_sesion.mainloop()


#Ventana Principal - Permitirá la gestión de alumnos (Agregar y Eliminar)
def ventana_principal():
    #Inicialización, Título, Tamaño, Posición, Ïcono y Modificación de tamaño
    window = tk.Tk()
    window.title('Sistema de Gestión Educativo')
    window.geometry('700x460')
    window.iconbitmap('iconos/birrete.ico')
    window.resizable(False,False)

    #Etiquetas - Labels
    ##Datos Personales, Nombre, Apellido, DNI, Domicilio, Género, Año Foto y Materias
    datos = ventana.Label()  
    datos.hacer_etiqueta_grid(window,'Datos Personales',0,0,2,0,(5,10))
    datos.hacer_etiqueta_grid(window,'Nombre',1,0,1,0,0)
    datos.hacer_etiqueta_grid(window,'Apellido',2,0,1,0,0)
    datos.hacer_etiqueta_grid(window,'DNI',3,0,1,0,0)
    datos.hacer_etiqueta_grid(window,'Domicilio',4,0,1,0,0)
    datos.hacer_etiqueta_grid(window,'Género',5,0,1,0,0)
    datos.hacer_etiqueta_grid(window,'Año',6,0,1,0,0)
    datos.hacer_etiqueta_grid(window,'Foto',14,0,2,0,(15,0))
    datos.hacer_etiqueta_grid(window,'Materias',8,0,2,0,(15,0))

    #Entradas - Entrys
    ##Nombre, Apellido, DNI, Domicilio
    e_nombre = ventana.Entry()
    e_nombre.hacer_entrada_grid(window,'black',1,1,'key',True)

    e_apellido = ventana.Entry()
    e_apellido.hacer_entrada_grid(window,'black',2,1,'key',True)

    e_dni = ventana.Entry()
    e_dni.hacer_entrada_grid(window,'black',3,1,'key',(window.register(ventana.validar_si_decimal),'%S'))

    e_domicilio = ventana.Entry()
    e_domicilio.hacer_entrada_grid(window,'black',4,1,'key',True)


    #Checkbox
    #Materias: Literatura, Matemática, Inglés, Educación Física, Ciencias, Religión, Artes, Historia, Geografía y Qúimica
    c_materia_literatura = ventana.CheckButton('Literatura')
    c_materia_literatura.hacer_check_button(window,'Literatura',9,0,'W',(10,0))

    c_materia_matematica = ventana.CheckButton('Matemática')    
    c_materia_matematica.hacer_check_button(window,'Matematica',9,1,'E',0)

    c_materia_ingles = ventana.CheckButton('Inglés')
    c_materia_ingles.hacer_check_button(window,'Inglés',10,0,'W',(10,0))

    c_materia_educ_fis = ventana.CheckButton('Educ.Física')
    c_materia_educ_fis.hacer_check_button(window,'Educ. Física',10,1,'E',0)

    c_materia_ciencias = ventana.CheckButton('Ciencias')
    c_materia_ciencias.hacer_check_button(window,'Ciencias',11,0,'W',(10,0))

    c_materia_religion = ventana.CheckButton('Religión')    
    c_materia_religion.hacer_check_button(window,'Religión',11,1,'E',(0,18))

    c_materia_artes = ventana.CheckButton('Artes')
    c_materia_artes.hacer_check_button(window,'Artes',12,0,'W',(10,0))

    c_materia_historia = ventana.CheckButton('Historia')    
    c_materia_historia.hacer_check_button(window,'Historia',12,1,'E',(0,20))

    c_materia_geo = ventana.CheckButton('Geografía')
    c_materia_geo.hacer_check_button(window,'Geografía',13,0,'W',(10,0))

    c_materia_quimica = ventana.CheckButton('Química')    
    c_materia_quimica.hacer_check_button(window,'Química',13,1,'E',(0,17))

    ##Colocación de materias dentro de una Tupla:
    materias_disponibles = (c_materia_literatura,c_materia_matematica,c_materia_ingles,c_materia_educ_fis,c_materia_ciencias,c_materia_religion,c_materia_artes,c_materia_historia,c_materia_geo,c_materia_quimica)


    #Lista Desplegable - ComboBox
    ##Género
    com_genero = ventana.ComboBox()
    com_genero.hacer_lista_desplegable(window,'readonly',('Femenino','Masculino','Otro'),17,5,1,0)
    
    ##Año
    com_anio = ventana.ComboBox()
    com_anio.hacer_lista_desplegable(window,'readonly',('1er','2do','3ro', '4to', '5to'),17,6,1,0)

    
    #Botones
    #Seleccionar foto
    foto = ventana.Button()
    foto.hacer_boton_grid(window, 'Seleccionar foto...', 15,0,2,(10,0),0, '#ffffff','#3F448C',lambda: ventana.boton_seleccionar_foto(window))

    #Añadir Alumno  
    aniadir = ventana.Button()
    aniadir.hacer_boton_grid(window,'Añadir',20,0,1,0,25,'#ffffff','#3F448C',lambda: ventana.boton_aniadir(lbx_estudiantes,e_nombre,e_apellido,e_dni,e_domicilio,com_genero,com_anio,materias_disponibles))
    
    #Limpiar registros
    limpiar = ventana.Button()
    limpiar.hacer_boton_grid(window,'Limpiar',20,1,1,(60,0),0, '#ffffff','#3F448C' ,lambda: ventana.boton_limpiar(materias_disponibles,com_genero,com_anio,e_nombre,e_apellido,e_dni,e_domicilio))

    #LINEA VERTICAL - Separador de Espacios.
    separator = ttk.Separator(window,orient= tk.VERTICAL, style='TSeparator')
    separator.grid(column=2, row=0, rowspan=30, sticky='NS',padx=(15,0))

    #Frame2 - LISTBOX 
    ##Espacio en el que se almacenarán los estudiantes. 
    lbx_estudiantes = tk.Listbox(window, activestyle='none', selectforeground="#ffffff",selectbackground="#3F448C", selectborderwidth=5)
    lbx_estudiantes.grid(row=1,column=3, sticky='NSEW', rowspan=14, columnspan=4, padx=(30,30))
    lbx_estudiantes.bind('<Double-1>',lambda x: ventana.boton_list_box(window,ventana_perfil,lbx_estudiantes))
    ventana.agregar_label_caja_texto(lbx_estudiantes)
    
    #Botón
    ##Eliminar Alumno
    eliminar = tk.Button(window,text='Eliminar', fg='#ffffff', bg='#db3434', font=('Helvetica', 11,'bold'), width=10,command=lambda: ventana.eliminar_estudiante(lbx_estudiantes))
    eliminar.place(x=415,y=380)

    #Configuración de las filas y columnas de la ventana Principal.
    window.columnconfigure(3,weigh=1)
    window.rowconfigure(1, weight=2)
    window.rowconfigure(2, weight=2)
    window.rowconfigure(3, weight=2)
    window.rowconfigure(4, weight=2)
    window.rowconfigure(5, weight=2)
    window.rowconfigure(6, weight=2)
    window.rowconfigure(8, weight=2)
    window.rowconfigure(9, weight=2)
    window.rowconfigure(10, weight=2)
    window.rowconfigure(11, weight=2)
    window.rowconfigure(12, weight=2)
    window.rowconfigure(13, weight=2)
    window.rowconfigure(14, weight=2)
    window.rowconfigure(15, weight=2)

    #Ciclo de la ventana Principal. 
    window.mainloop()

#Ventana Perfil: se accede haciendo doble click en el estudiante (almacenado en el listbox)
def ventana_perfil():
    #Inicialización, Título, Tamaño, Posición, Ïcono y Modificación de tamaño
    ventana_alumno = tk.Tk()
    ventana_alumno.title('Perfil')
    ventana_alumno.geometry('580x550+270+50')
    ventana_alumno.iconbitmap('iconos/birrete.ico')
    ventana_alumno.resizable(False,False)

    #FRAMES
    #FRAME 1 - NOTAS (ABAJO)
    frame_notas = tk.Frame(ventana_alumno)
    frame_notas.pack(side='bottom', fill='x', ipady=130)

    #FRAME 2 - FOTO (IZQUIERDA)
    frame_foto = tk.Frame(ventana_alumno)
    frame_foto.pack(side='left', fill='y')

    #FRAME 3 - DATOS (DERECHA)
    frame_datos = tk.Frame(ventana_alumno)
    frame_datos.pack(side='right', fill='y')

    #BOTÓN ATRÁS
    b_atras = tk.Button(frame_foto, text='←' , activeforeground='#ffffff',activebackground='#3F448C',font=('Helvetica',13),command=lambda: ventana.cerrar_ventana(ventana_alumno,ventana_principal))
    b_atras.place(y=10,x=25)

    #FOTO
    imagen = PhotoImage(file='iconos/user.png',width=256,height=256)
    l_imagen_perfil = tk.Label(frame_foto,image=imagen,bg='white',bd=1, relief='solid',width=200,height=500, anchor='center')
    l_imagen_perfil.pack(side='top',pady=(50,50), padx=(50,50))

    #DATOS: 
    ##NOMBRE Y APELLIDO
    l_nombre_apellido = tk.Label(frame_datos,text='',width=50,height=1,font=('Helvetica',14, 'bold'))
    l_nombre_apellido.pack(side='top',pady=(60,0), padx=(0,20), fill='x')

    ##DNI
    l_dni = tk.Label(frame_datos,text='',width=50,height=1,font=('Helvetica',11,))
    l_dni.pack(side='top', padx=(0,20), fill='x')

    ##DOMICILIO
    l_domicilio = tk.Label(frame_datos,text='',width=50,height=1, anchor='center',font=('Helvetica',11))
    l_domicilio.pack(side='top', padx=(0,20))

    #MATERIAS LABEL
    l_materias = tk.Label(frame_datos,text='Materia',width=50,height=1, anchor='center',font=('Helvetica',11, 'bold'))
    l_materias.pack(side='top', padx=(0,20), pady=(20,0))
    
    #MATERIAS LISTA DESPLEGABLE - COMBOBOX
    c_materias= ttk.Combobox(frame_datos, state='readonly')
    c_materias.bind("<<ComboboxSelected>>", lambda x: ventana.cambiar_seleccion(c_materias,l_promedio,l_estado,e_nota1,e_nota2,e_nota3))
    c_materias.pack(side='top',padx=(0,20), pady=(8,0))
    
    ventana.modificar_ventana(l_nombre_apellido,l_dni,l_domicilio,c_materias)

    #LABELS (EXAMEN)
    l_examen1 = tk.Label(frame_notas,text='EXAMEN I',width=10,height=1, anchor='n',font=('Helvetica',11, 'bold'))
    l_examen1.pack(side='left', fill='y', padx=(10,10))
    
    l_examen2 = tk.Label(frame_notas,text='EXAMEN II',width=10,height=1, anchor='n',font=('Helvetica',11, 'bold'))
    l_examen2.pack(side='left', fill='y', padx=(10,10))

    l_examen3 = tk.Label(frame_notas,text='EXAMEN III',width=10,height=1, anchor='n',font=('Helvetica',11, 'bold'))
    l_examen3.pack(side='left', fill='y', padx=(10,10))

    l_promedio = tk.Label(frame_notas,text='PROMEDIO',width=10,height=1, anchor='n',font=('Helvetica',11, 'bold'))
    l_promedio.pack(side='left', fill='y', padx=(10,10))

    l_estado = tk.Label(frame_notas,text='ESTADO',width=10,height=1, anchor='n',font=('Helvetica',11, 'bold'))
    l_estado.pack(side='left', fill='y', padx=(10,10))

    #Entradas - Notas
    e_nota1 = tk.Entry(frame_notas,validate='key',validatecommand=True)
    e_nota1.config(width=15, fg="#3F448C",justify=tk.CENTER)
    e_nota1.place(y=35, x=10)

    e_nota2 = tk.Entry(frame_notas,validate='key',validatecommand=True)
    e_nota2.config(width=15, fg="#3F448C",justify=tk.CENTER)
    e_nota2.place(y=35, x=130,)

    e_nota3 = tk.Entry(frame_notas,validate='key',validatecommand=True)
    e_nota3.config(width=15, fg="#3F448C",justify=tk.CENTER)
    e_nota3.place(y=35, x=245,)

    l_promedio = tk.Label(frame_notas)
    l_promedio.config(width=14, fg="#3F448C",justify=tk.CENTER, bg='white', borderwidth = 1,relief="sunken")
    l_promedio.place(y=35, x=355)

    l_estado = tk.Label(frame_notas)
    l_estado.config(width=13, fg="#3F448C",justify=tk.CENTER, bg='white', borderwidth = 1,relief="sunken")
    l_estado.place(y=35, x=475)

    #Boton - Agregar nota(s)
    b_agregar_nota = tk.Button(frame_notas, text='Agregar Notas' , activeforeground='#ffffff',activebackground='#3F448C',command=lambda: ventana.calcular_promedio(l_promedio,l_estado,e_nota1,e_nota2,e_nota3))
    b_agregar_nota.place(y=130,x=245)

    ventana_alumno.mainloop()

ventana_bienvenida()
    

