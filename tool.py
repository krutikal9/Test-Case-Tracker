import gooeypie as gp


app=gp.GooeyPieApp('Test Case Tracker')

path =None
def reset_val(event):
    print(test_case_name_input.text)



def save_val(event):

    file_name = test_case_name_input.text
    data =['Test case Name: ',test_case_name_input.text,'\n','Account Number: ',acc_no_input.text,'\n',
            'Tech: ',tech_input.text,'\n','Job ID: ',job_id_input.text,'\n',
            'Device Name: ',str(device_name_input.selected),'\n','MAC: ',mac_input.text,'\n',
            'Clean: ',str(clean.checked),'\n','Previous Account: ',previous_acc_input.text,'\n',
            'Cease Completed: ',str(cease.checked)]
    with open(path+'/'+file_name, 'w') as file:
        file.writelines(data)
        

def folder_open(event):
    global path
    path =open_folder_window.open()
    path_lbl.text = path

l_count =4

def add_layout(event):

    global l_count

    container_lbl = gp.LabelContainer(app,'Device Info')
    device_name_lbl = gp.Label(container_lbl,'Device Name')
    device_name =['option 1','oprton 2','option 3','option 4','option 5']
    device_name_input =gp.Dropdown(container_lbl,device_name)

    mac_lbl = gp.Label(container_lbl,'MAC')
    mac_input = gp.Input(container_lbl)

    clean = gp.Checkbox(container_lbl,'Clean?')

    previous_acc_lbl = gp.Label(container_lbl,'Previous Account')
    previous_acc_input = gp.Input(container_lbl)

    cease = gp.Checkbox(container_lbl,'Cease completed?')
    container_lbl.set_grid(2,6)
    app.add(container_lbl,l_count,1,row_span=2,column_span=6)

    container_lbl.add(device_name_lbl,1,1,align='right')
    container_lbl.add(device_name_input,1,2,fill='True')
    container_lbl.add(mac_lbl,1,3,align='right')
    container_lbl.add(mac_input,1,4,fill='True')
    container_lbl.add(clean,1,5,fill='True')
   
    container_lbl.add(previous_acc_lbl,2,1,align='right')
    container_lbl.add(previous_acc_input,2,2,fill='True')
    container_lbl.add(cease,2,4,align='right')
    l_count = l_count+2
 

    app.refresh()

select_button = gp.Button(app,'Select',folder_open)
path_lbl = gp.Label(app,'')
open_folder_window = gp.OpenFolderWindow(app, 'select')




test_case_name_lbl = gp.Label(app,'Test Case Name')
test_case_name_input = gp.Input(app)

acc_no_lbl = gp.Label(app,'Account Number')
acc_no_input = gp.Input(app)

tech_lbl = gp.Label(app,'Tech')
tech_input = gp.Input(app)

job_id_lbl = gp.Label(app,'Job ID')
job_id_input = gp.Input(app)



reset_button = gp.Button(app,'Reset',reset_val)
add_button = gp.Button(app,'Add device',add_layout)
save_button = gp.Button(app,'Save',save_val)

app.set_grid(24,6)


# app.set_column_weights()
app.add(select_button,1,1,align='right')
app.add(path_lbl,1,2, column_span=5)

app.add(test_case_name_lbl,2,1,align='right')
app.add(test_case_name_input,2,2, column_span=5, fill='True')

app.add(acc_no_lbl,3,1,align='right')
app.add(acc_no_input,3,2,fill='True')
app.add(tech_lbl,3,3,align='right')
app.add(tech_input,3,4,fill='True')
app.add(job_id_lbl,3,5,align='right')
app.add(job_id_input,3,6,fill='True')




app.add(reset_button,24,1, allign='right')
app.add(save_button,24,2, allign='right')
app.add(add_button,24,3, allign='right')
app.run()