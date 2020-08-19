from tkinter import *
from tkinter import filedialog
from cabinets import *
   
# Function for opening the  
# file explorer window 
input_file = ""
output_file = ""
def browseFiles1(): 
    global input_file
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("excel files", 
                                                        ".xlsx"), 
                                                       ("excel files", 
                                                        ".xls")))      
    # Change label contents 
    label_input.configure(text="File Opened: "+filename)
    input_file = str(filename) 

def browseFiles2(): 
    global output_file
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("excel files", 
                                                        ".xlsx"), 
                                                       ("excel files", 
                                                        ".xls")))      
    # Change label contents 
    label_output.configure(text="File Opened: "+filename)
    output_file = str(filename)

def run_cabinets():
    csvConverter(input_file, output_file)
    run = Label(text = "run successful, please check your output file")
    run.pack()

window = Tk()
window.title("Cabinet Cut Calculator")
title = Label(text = "Sam's Automatic Cabinet Cut Calculator")
title.pack()
label_input = Label(text = "input excel path")
inputExcel = Button(text = "browse files", command = browseFiles1)
label_output = Label(text = "output excel path")
outputExcel = Button(text = "browse files", command = browseFiles2)
execute_button = Button(text = "Run", command = run_cabinets)
label_input.pack()
inputExcel.pack()
label_output.pack()
outputExcel.pack()
execute_button.pack()
window.mainloop() 