import PySimpleGUI as sg
import math


##-----Cnfiguraciones estandar de la página----------------------------------##
bw: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F8F8F8")}
bt: dict = {'size':(7,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F1EABC")}
bo: dict = {'size':(30,2), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#ECA527"), 'focus':True}

#Modificación de los elementos presentes en el layout

layout = [  [sg.Text('Introduzca La latitud en Decimales'),sg.Input(key='-IN-')],
           [sg.Text('Introduzca la longitud en decimales'), sg.Input(key='-IN2-')],
           [sg.Text('Introduzca la Altura del punto'), sg.Input(key='-IN3-')],
            [[(sg.Button('Calcular en coordenadas Planas con el datum Bogotá')), sg.Button('Exit'), sg.Text(size=(15,1), key='-OUTPUT-')]],
            [sg.Text('GranNormal'),sg.Text(size=(15,1), key='-OUTPUT1-')],
            [sg.Text('X'),sg.Text(size=(15,1), key='-OUTPUT2-')],
            [sg.Text('Y'),sg.Text(size=(15,1), key='-OUTPUT3-')],
            [sg.Text('Z'),sg.Text(size=(15,1), key='-OUTPUT4-')]
]

var: dict = {'front':[], 'back':[], 'decimal':False, 'x_val':0.0, 'y_val':0.0, 'result':0.0, 'operator':''}


#funciones de permisión de números




# Create the Window
window: object = sg.Window('Calculadora', layout=layout, background_color="#272533", size=(380, 300), return_keyboard_events=True)
# Event Loop to process "events" and get the "values" of the inputs

#Eventos
while True:
  
  while True:
    event, values = window.read()
    print(event, values)
      
    if event in  (None, 'Exit'):
        break
#Calculo de las coordenadas planas

    elif event == 'Calcular en coordenadas Planas con el datum Bogotá':
            
            
        
            a =  6378388000
            e2 = 0.00669438002290
            latitud = float(values['-IN-'])
            LatitudRadianes=math.radians(latitud)
            Longitud =  float(values['-IN2-'])
            LongitudRadianes= math.radians(Longitud)
            Altura =  float(values['-IN3-'])
            GranNormal = (a)/(math.sqrt(1-e2*(math.sin(LatitudRadianes))**2))
            CoordenadaX=(GranNormal+Altura)*math.cos(LatitudRadianes)*math.cos(LongitudRadianes)
            CoordenadaY=(GranNormal+Altura)*math.cos(LatitudRadianes)*math.sin(LongitudRadianes)
            CoordenadaZ=((1-e2)*GranNormal+Altura)*math.sin(LatitudRadianes)
            window['-OUTPUT1-'].Update(GranNormal)
            window['-OUTPUT2-'].Update(CoordenadaX)
            window['-OUTPUT3-'].Update(CoordenadaY)
            window['-OUTPUT4-'].Update(CoordenadaZ)

    
  
     
    
  
     
   


