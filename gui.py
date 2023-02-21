import PySimpleGUI as sg

sg.theme('darkblue14')

def write_to_file(values,path):
    data =['Test case name: ',values['-NAME-'],'\n','Account Number: ', values['-ACC_NO-'],'\n','Tech: ', values['-TECH-'],'\n','Job ID: ', values['-ID-'],'\n', 'Device Name: ',values[f'-DEVICE{counter}-'],'\n',"MAC: " ,values[f'-MAC{counter}-'],'\n','Clean: ', str(values[f'-CLEAN{counter}-']),'\n','Previous Account: ',values[f'-PRV_ACC{counter}-'],'\n','Cease compleated: ' ,str(values['-CEASEpip install gooeypie-'])]
    name_file = values['-NAME-']
    print(values['-NAME-'])
    with open(path+'/'+ name_file+'.txt', 'w') as file:
        file.writelines(data)

counter = 0

def add_layout(counter):

    device_layout=[sg.pin(sg.Column([
        [sg.Text('Device Name',size=(15,1)), sg.Combo(['option1','option2','option3','option4','option5'],key=f'-DEVICE{counter}-',size=(15,1)),
        sg.Text('MAC'), sg.InputText('',key=f'-MAC{counter}-',size=(15,1)),
        sg.Checkbox('Clean?', key=f'-CLEAN{counter}-',pad=(15,0))],
        [sg.Text('Previous Account',size=(15,1)), sg.InputText('',key=f'-PRV_ACC{counter}-',size=(17,1)),
        sg.Checkbox('Cease complete?', key=f'-CEASE{counter}-',pad=(42,0)),
        sg.Button('-', key=f'-DELETE{counter}-')]
    ],pad=(0,0),key=f'-COL{counter}-'))]
    return device_layout

layout1 =[
    [sg.FolderBrowse('Select',key='-FOLDER-',enable_events=True)],
    [sg.Text('Test Case Name',size=(15,1)), sg.InputText('',key='-NAME-',size=(60,1))],
    [sg.Text('Account Number',size=(15,1)), sg.InputText('',key='-ACC_NO-',size=(17,1)),
    sg.Text('Tech'), sg.InputText('',key='-TECH-',size=(10,1)),
    sg.Text('Job ID'), sg.InputText('',key='-ID-',size=(10,1))],
    [sg.Column([add_layout(counter)],key='-D_COL-',pad=(0,0))],
    [sg.Text('',)],
    [sg.Button('Reset',key='+',size=(5,1)),
    sg.Button('Save',key='-SAVE-',size=(5,1))]
]

window = sg.Window('Test case Tracker',layout1)

 
while True:
    event, values =window.read()
    print(event,values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-SAVE-':
        write_to_file(values,path)
    if event == '-FOLDER-':
        path = values['-FOLDER-']
    if event == '+':
        counter = counter +1
        window.extend_layout(window["-D_COL-"], [add_layout(counter)])
    if event.startswith('-DELETE'):
        # print(event)
        hide = event[7:-1]
        # print(hide)
        window[f'-COL{hide}-'].update(visible =False)
window.close()    
  