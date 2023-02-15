import PySimpleGUI as sg

layout1 =[
    [sg.Text('Test Case Name',size=(15,1)), sg.InputText('',key='test_case_name',size=(60,1))],
    [sg.Text('Account Number',size=(15,1)), sg.InputText('',key='account_number',size=(17,1)),
    sg.Text('Tech'), sg.InputText('',key='tech',size=(10,1)),
    sg.Text('Job ID'), sg.InputText('',key='job_id',size=(10,1))],
    [sg.Text('Device Name',size=(15,1)), sg.Combo(['option1','option2','option3','option4','option5'],key='device_name',size=(15,1)),
    sg.Text('MAC'), sg.InputText('',key='mac',size=(15,1)),
    sg.Checkbox('Clean?', key='clean')],
    [sg.Text('Previous Account',size=(15,1)), sg.InputText('',key='previous_account',size=(17,1)),
    sg.Checkbox('Cease complete?', key='cease_complete')],
    [sg.Text('',)],
    [sg.Button('Reset',key='reset',size=(5,1)),
    sg.Button('Save',key='save',size=(5,1))]
]

window = sg.Window('Title',layout1)

while True:
    event, values =window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()    