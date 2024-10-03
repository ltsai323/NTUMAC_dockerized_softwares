import tkinter as tk
from tkinter import ttk
import yaml

yaml_pool = {
        'Sensor':'data/subtype_sensor.yaml',
        'Bare Hexaboard': 'data/subtype_barehexaboard.yaml',
        'Hexaboard': 'data/subtype_hexaboard.yaml',
        'Baseplate': 'data/subtype_baseplate.yaml',
        'Silicon Module': 'data/subtype_simodule.yaml',
        }
# Sample YAML data as a string (this would typically be loaded from a file)
yaml_data = '''
code_structure:
  - 320: CMS
  - SH: HD Sensors
    SL: LD Sensors
  - Thickness:
        1: 120um
        2: 200um
        3: 300um
    Shape:
        # S: a whole sensor # allowed value but disabled
        # M: half-moons or test structure # allowed value but disabled
        F: Full
        T: Top
        B: Bottom
        L: Left
        R: Right
        5: Five
    Further code:
        XX: default
        # TP: top half-moon
        # BT: bottom half-moon
        # TL: top-left half-moon
        # TR: top-right half-moon
        # BL: bottom-left half-moon
        # BR: bottom-right half-moon
Digits:
    options: # if the previous code in the list, show this number
        1: # 300um and Full
          - 3FXX
        2: # 200um and Full
          - 2FXX
        3: # 120um and Full
          - 1FXX
        4: # 300um and Partial
          - 3TXX
          - 3BXX
          - 3LXX
          - 3RXX
          - 35XX
        5: # 200um and Partial
          - 2TXX
          - 2BXX
          - 2LXX
          - 2RXX
          - 25XX
        6: # 120um and Partial
          - 1TXX
          - 1BXX
          - 1LXX
          - 1RXX
          - 15XX
    Ndigit: 5 # 6-1. The first digit is meaningful
'''
# Load YAML content based on the selected file

# Function to update the GUI based on YAML content
def update_options(yamlFILE):
    # Clear existing options
    for widget in subtype_frame.winfo_children():
        widget.destroy()

    ### reset used variables
    selected_values.clear()  # List to store all selected values (StringVars). The content should be StringVars or a list of StringVars
    digits_before_id_value.clear()
    post_func_checking.clear()
    irow = 0 # start from 1. row 0 is the result row
    main_option_menu(yamlFILE)

# Event handler when a YAML file is selected
def on_yaml_selection():
    selected_file = selected_yaml.get()
    update_options(selected_file)


def update_textbox():
    """Update the textbox with selected values from the radio buttons."""
    global text_box
    text_box.delete(1.0, tk.END)  # Clear the textbox
    selected_text = ""
    sel_vals = []
    for sel_val in selected_values:
        if isinstance(sel_val, tk.StringVar):
            sel_vals.append(sel_val.get())
        if isinstance(sel_val, list):
            sel_vals.append( ''.join(sec_val.get() for sec_val in sel_val) )
    
    #selected_text = '-'.join( sel_val.get() for sel_val in sel_vals )
    selected_text = '-'.join( sel_vals )

    global post_func_checking
    digits_before_id = ''.join( postfunc(sel_vals) for postfunc in post_func_checking )
    #print(f'[digits_before_id] {digits_before_id}. [len of postfunc] {len(post_func_checking)}')
    #digits_before_id = ''.join( digit_before_id_value.get() for digit_before_id_value in digits_before_id_value )

    try:
        intval = int(id_digit_value.get())
    except:
        intval = 0 # if somethinig else happened, got 0
    overall_digits = digits_before_id + f'{intval:0{number_of_digits}d}'
    selected_text += f'-{overall_digits}'  # Add integer value
    #print(f'[selected_text] {selected_text}')
    text_box.insert(tk.END, selected_text)  # Insert the text into the textbox


def copy_to_clipboard():
    """Copy the contents of the textbox to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(text_box.get(1.0, tk.END))  # Copy text to clipboard
    print(f'[CopiedID] {text_box.get(1.0,tk.END)}')


def assembly_code(codeDICT:dict):
    global root, irow

    sel_vals = []
    for subtitle, subopt in codeDICT.items():
        # Add a horizontal separator before the label
        separator = ttk.Separator(subtype_frame, orient='horizontal')
        separator.grid(row=irow, column=0, columnspan=max_column, sticky="ew", pady=10)  # Spans 5 columns and adds vertical padding
        irow += 1  # Move to the next row for the label

        # Label with padding before it
        label = ttk.Label(subtype_frame, text=subtitle)
        label.grid(row=irow, column=0, padx=5, sticky="w")  # Add padding and align label to the left
        label.config(font=font_subtitle)
        irow += 1  # Move to the next row for the Radiobuttons

        # Radiobuttons in the next row
        selected_value = tk.StringVar()
        #selected_values.append(selected_value)  # Add the StringVar to the list
        sel_vals.append(selected_value)  # Add the StringVar to the list
        icol = 0
        for code, illustration in subopt.items():
            #radio = tk.Radiobutton(root, text=f'{illustration}', variable=selected_value, value=f'{code}',
            #                       command=update_textbox)
            radio = tk.Radiobutton(subtype_frame, text=f'{illustration}', variable=selected_value, value=f'{code}', wrap=150, command=update_textbox)
            radio.grid(row=irow, column=icol, padx=20, sticky='w')  # Add small padding between Radiobuttons
            radio.config(font=font_options)
            if icol == 0: radio.select()
            icol += 1
        irow += 1  # Move to the next row for the next set of options
    selected_values.append(sel_vals)


def single_code(codeDICT:dict):
    global root, irow
    # Add a horizontal separator before the label
    #separator = ttk.Separator(subtype_frame, orient='horizontal')
    #separator.grid(row=irow, column=0, columnspan=max_column, sticky="ew", pady=10)  # Spans 5 columns and adds vertical padding
    #irow += 1  # Move to the next row for the label

    # Label with padding before it
    selected_value = tk.StringVar()
    selected_values.append(selected_value)  # Add the StringVar to the list
    #label = ttk.Label(subtype_frame, text="Options:")
    #label.grid(row=irow, column=0, padx=5, sticky="w")  # Add padding and align label to the left
    #label.config(font=font_subtitle)
    irow += 1  # Move to the next row for the Radiobuttons

    # Radiobuttons in the next row
    icol = 0
    for code, illustration in codeDICT.items():
        radio = tk.Radiobutton(subtype_frame, text=f'{illustration}', variable=selected_value, value=f'{code}',
                               command=update_textbox)
        radio.grid(row=irow, column=icol, padx=20, sticky='w')  # Add small padding between Radiobuttons
        radio.config(font=font_options)
        if icol == 0: radio.select() # select first column as the default value
        icol += 1
    irow += 1

def ID_on_entry_click(event):
    """Clear the default text when the entry field is clicked."""
    if ID_entry.get() == "ID":
        ID_entry.delete(0, tk.END)  # Clear the content of the entry

def ID_on_focusout(event):
    """Restore the default text if the entry is left empty."""
    if ID_entry.get() == "":
        ID_entry.insert(0, "ID")  # Restore the default text

def ID_validate_input(value_if_allowed):
    """Validate that the input is an integer or empty (for restoring 'ID')."""
    if value_if_allowed == "" or value_if_allowed == "ID":
        return True  # Allow empty (for placeholder) or 'ID'
    try:
        val = int(value_if_allowed)
        if val > 10**number_of_digits: return False
        return True  # Allow valid integer values
    except ValueError:
        return False  # Disallow non-integer values
def ID_on_enter(event):
    update_textbox()

def main_option_menu(yamlFILE):
########## Row 1~N-1 selected options from yaml file ##########
# Load YAML data
    f = open(yamlFILE)
    data = yaml.safe_load(f)
    def check_yaml_content(data):
        for key,val in data.items():
            print(f'[primary key] {key}')
            if isinstance(val, list):
                for item in val:
                    print(f'    {item}')
            if isinstance(val, dict):
                for k,item in val.items():
                    print(f'    [{k}] {item}')
#check_yaml_content(data)
#exit(0)



    code_structure = data.get('code_structure', [])

    for code_dict in code_structure:
        #opt = a.get('options')
        #first_item = code_dict[ code_dict.keys()[0] ]
        first_item = next(iter(code_dict.values()))
        
        if isinstance(first_item, dict):
            assembly_code(code_dict)
        else:
            single_code(code_dict)
########## Row 1~N-1 selected options from yaml file ##########

########## Row N: Result message box and copy button ########## 
    global text_box
    text_box = tk.Text(subtype_frame, height=5, width=50)
    text_box.grid(row=irow, column=1, columnspan=max_column-1, padx=10, pady=10, sticky="ew")
    text_box.delete(1.0, tk.END)  # Clear the textbox

# Button to copy the text in the TextBox to clipboard
    copy_button = tk.Button(subtype_frame, text="Copy to Clipboard", command=copy_to_clipboard, wrap=100)
    copy_button.grid(row=irow, column=0, padx=10, pady=10)
########## Row N: Result message box and copy button end ########## 


########## Row0: Handling Digits part ##########
### Modify configurations of ID entry
    '''
Digits:
    options: # if the previous code in the list, show this number
        1:
          - 3FXX
        2:
          - 2FXX
        3:
          - 1FXX
        4:
          - 3TXX
          - 3BXX
          - 35XX
        5:
          - 2TXX
        6:
          - 1TXX
          - 1BXX
    Ndigit: 5 # 6-1. The first digit is meaningful
    '''
    digits_info = data.get('Digits', {})
    for opt_title, options2 in digits_info.items():
        if opt_title == 'options':
            def post_func(selVALs:list, options2 = options2):
                val = selVALs[-1]
                for code, avail_list in options2.items():
                    if val in avail_list: return str(code)
                return 'INVALID'
            post_func_checking.append(post_func)
        if opt_title == 'Ndigit':
            global number_of_digits
            number_of_digits = options2
########## Row0: Handling Digits part end ##########

if __name__ == "__main__":
    font_subtitle = ('Arial', 20)
    font_options = ('Arial', 10)
    max_column = 20

    root = tk.Tk()
    root.title('HGCal ID Generator')
    yaml_frame = ttk.Frame(root)
    yaml_frame.pack(padx=10, pady=10)

    ttk.Label(yaml_frame, text="Select a YAML file:").pack(anchor=tk.W)

####### Load list_of_sources.yaml choose generator type. Baseplate / Hexaboard / Module ... etc ####### 
    file_all_sources = 'data/list_of_sources.yaml'
    with open(file_all_sources, 'r') as f:
        yaml_pool_=yaml.safe_load(f)

    selected_yaml = tk.StringVar()
    for name, yaml_file in yaml_pool_.items():
        ttk.Radiobutton(yaml_frame, text=name, value=yaml_file, variable=selected_yaml, command=on_yaml_selection).pack(anchor=tk.W, fill=tk.Y, side=tk.LEFT)
# Frame for dynamic options based on YAML content
####### Load list_of_sources.yaml choose generator type. Baseplate / Hexaboard / Module ... etc END ####### 

####### ID Entry #######
# Create a validation function for the Entry widget
    ID_vcmd = (root.register(ID_validate_input), "%P")

# Create an Entry widget with default text "ID"
    id_digit_value = tk.StringVar(value='ID')  # Variable to store the integer value # global var
    number_of_digits = 3 # global var
    ID_entry = ttk.Entry(root, validate="key", validatecommand=ID_vcmd, textvariable=id_digit_value)

# Bind the entry to clear the default text on focus
    ID_entry.bind("<FocusIn>", ID_on_entry_click)

# Bind the entry to restore the default text if focus is lost and the field is empty
    ID_entry.bind("<FocusOut>", ID_on_focusout)
    ID_entry.bind("<Return>", ID_on_enter)


    ID_entry.pack()
####### ID Entry end #######

####### Loaded options #######
    subtype_frame = ttk.Frame(root)
    subtype_frame.pack(padx=10, pady=10)


### used variables
    selected_values = []  # List to store all selected values (StringVars). The content should be StringVars or a list of StringVars

    digits_before_id_value = []
    post_func_checking = []
    irow = 0 # start from 1. row 0 is the result row
    text_box = None
    #subtype_frame.columnconfigure(8, weight=1)
    root.mainloop()
