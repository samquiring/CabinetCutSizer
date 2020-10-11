from tkinter import *
from tkinter import filedialog
from cabinets import *

# created by Sam Quiring
#CabinetCutGUI is the GUI for the cabinet cut calculator
#this allows for non-python experienced users such as my
#father to use this program with relative ease after the
#dependencies are installed

# Function for opening the  
# file explorer window 
input_file = ""
output_file = ""

#this is the first browseFiles which is for the input file
def browseFiles1(): 
    global input_file
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("excel files", 
                                                        ".xlsx"), 
                                                       ("excel files", 
                                                        ".xls")))      
    label_input.configure(text="File Opened: "+filename)
    input_file = str(filename) 

#this is the second browseFiles which is for the output file
def browseFiles2(): 
    global output_file
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Select a File", 
                                          filetypes = (("excel files", 
                                                        ".xlsx"), 
                                                       ("excel files", 
                                                        ".xls")))      
    label_output.configure(text="File Opened: "+filename)
    output_file = str(filename)

#when this function is run it runs the CabinetCutCalculator and then
#prints out "run successful", if it encountered no errors
def run_cabinets():
    csvConverter(input_file, output_file)
    run = Label(text = "run successful, please check your output file")
    run.pack()

#this is the heart of the GUI which was setup using Tkinter
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
