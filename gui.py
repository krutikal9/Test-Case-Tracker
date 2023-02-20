import PySimpleGUI as sg

sg.theme('darkblue14')

layout1 =[
    [sg.FolderBrowse('Select',key='-FOLDER-',enable_events=True)],
    [sg.Text('Test Case Name',size=(15,1)), sg.InputText('',key='-NAME-',size=(60,1))],
    [sg.Text('Account Number',size=(15,1)), sg.InputText('',key='-ACC_NO-',size=(17,1)),
    sg.Text('Tech'), sg.InputText('',key='-TECH-',size=(10,1)),
    sg.Text('Job ID'), sg.InputText('',key='-ID-',size=(10,1))],
    [sg.Text('Device Name',size=(15,1)), sg.Combo(['option1','option2','option3','option4','option5'],key='-DEVICE-',size=(15,1)),
    sg.Text('MAC'), sg.InputText('',key='-MAC-',size=(15,1)),
    sg.Checkbox('Clean?', key='-CLEAN-',pad=(15,0))],
    [sg.Text('Previous Account',size=(15,1)), sg.InputText('',key='-PRV_ACC-',size=(17,1)),
    sg.Checkbox('Cease complete?', key='-CEASE-',pad=(42,0))],
    [sg.Text('',)],
    [sg.Button('Reset',key='-RESET-',size=(5,1)),
    sg.Button('Save',key='-SAVE-',size=(5,1))]
]

window = sg.Window('Test case Tracker',layout1)

def write_to_file(values,path):
    data =['Test case name: ',values['-NAME-'],'\n','Account Number: ', values['-ACC_NO-'],'\n','Tech: ', values['-TECH-'],'\n','Job ID: ', values['-ID-'],'\n', 'Device Name: ',values['-DEVICE-'],'\n',"MAC: " ,values['-MAC-'],'\n','Clean: ', str(values['-CLEAN-']),'\n','Previous Account: ',values['-PRV_ACC-'],'\n','Cease compleated: ' ,str(values['-CEASE-'])]
    name_file = values['-NAME-']
    print(values['-NAME-'])
    with open(path+'/'+ name_file+'.txt', 'w') as file:
        file.writelines(data)
   
while True:
    event, values =window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == '-SAVE-':
        write_to_file(values,path)
    if event == '-FOLDER-':
        path = values['-FOLDER-']
 
window.close()    

   
