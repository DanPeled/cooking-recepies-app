import tkinter as tk
import tkinter.font as tkFont
import os
import glob
import json

root = tk.Tk()
# setting title
root.title("Recepie Book")
# setting window size
width = 613
height = 594
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)


def recepie_window(recepie: str = "NONE", recepie_dict: dict = {}):
    change_window()
    Title_Lable = tk.Label(root)
    ft = tkFont.Font(family='Times', size=18)
    Title_Lable["font"] = ft
    Title_Lable["fg"] = "#333333"
    Title_Lable["justify"] = "center"
    Title_Lable["text"] = f"{recepie.capitalize()}"
    Title_Lable.place(x=0, y=0, width=588, height=34)

    Description_Label = tk.Label(root)
    ft = tkFont.Font(family="Times", size=15)
    Description_Label["font"] = ft
    Description_Label["fg"] = "#333333"
    Description_Label["justify"] = "left"
    Description_Label["text"] = f"{recepie_dict.get('description','')}"
    Description_Label.place(x=-200, y=100, width=588, height=34)

    CANCEL_BTN = tk.Button(root, cursor="hand2")
    CANCEL_BTN["activebackground"] = "#bcbcbc"
    CANCEL_BTN["activeforeground"] = "#e3e3e3"
    CANCEL_BTN["bg"] = "#7b7b7b"
    ft = tkFont.Font(family='Times', size=10)
    CANCEL_BTN["font"] = ft
    CANCEL_BTN["fg"] = "#000000"
    CANCEL_BTN["justify"] = "center"
    CANCEL_BTN["text"] = "Back"
    CANCEL_BTN["relief"] = "flat"
    CANCEL_BTN.place(x=20, y=560, width=70, height=25)
    CANCEL_BTN["command"] = recepie_list_window


def recepie_list_window():
    change_window()

    def generate_buttons(names: list[str]):
        def recepie_window_cmd(name, recepie_dict):
            """Makes a command to handle the command attribute correctly
            Args:
                name (list of strings) : handles the names of the recepies
            """
            def cmd():
                recepie_window(name, recepie_dict)
            return cmd
        y_pos = 50
        x_pos = 250
        buttons: list[tk.Button] = []
        # Makes a button for each recepie that exists
        for i, name in enumerate(names):
            recepie_dict = {}
            with open(f"recepies/{name}.recepie") as f:
                recepie_dict = f.read()
                print(recepie_dict)
            f.close()
            buttons.append(tk.Button(root, cursor="hand2"))
            buttons[i]["activebackground"] = "#bcbcbc"
            buttons[i]["activeforeground"] = "#e3e3e3"
            buttons[i]["bg"] = "#7b7b7b"
            ft = tkFont.Font(family='Times', size=13)
            buttons[i]["font"] = ft
            buttons[i]["fg"] = "#000000"
            buttons[i]["justify"] = "center"
            buttons[i]["text"] = name.capitalize()
            buttons[i]["relief"] = "flat"
            buttons[i].place(x=x_pos, y=y_pos, width=len(name)
                             * 10 + 20, height=40)
            buttons[i]["command"] = recepie_window_cmd(
                name, eval(recepie_dict))
            y_pos += 50
    Title_Lable = tk.Label(root)
    ft = tkFont.Font(family='Times', size=18, weight='bold')
    Title_Lable["font"] = ft
    Title_Lable["fg"] = "#333333"
    Title_Lable["justify"] = "center"
    Title_Lable["text"] = "Recepie List"
    Title_Lable.place(x=0, y=0, width=588, height=34)

    CANCEL_BTN = tk.Button(root, cursor="hand2")
    CANCEL_BTN["activebackground"] = "#bcbcbc"
    CANCEL_BTN["activeforeground"] = "#e3e3e3"
    CANCEL_BTN["bg"] = "#7b7b7b"
    ft = tkFont.Font(family='Times', size=10)
    CANCEL_BTN["font"] = ft
    CANCEL_BTN["fg"] = "#000000"
    CANCEL_BTN["justify"] = "center"
    CANCEL_BTN["text"] = "Back"
    CANCEL_BTN["relief"] = "flat"
    CANCEL_BTN.place(x=20, y=560, width=70, height=25)
    CANCEL_BTN["command"] = main
    if not os.path.exists('recepies/'):
        # Checks wheter the recepies dir exists, and if doesn't creates it
        os.makedirs('recepies/')
    # Gets all the existing recepie files in the recepies dir
    recepies_files = glob.glob("recepies/*.recepie")
    recepies_files = [
        recepie.replace("recepies\\", "").replace(".recepie", "") for recepie in recepies_files
    ]  # Removes "recepies\\" and file extension from the recepie name
    generate_buttons(recepies_files)


def change_window():
    """
    Goes through each widget in the current window and destroys it
    """
    for widgets in root.winfo_children():
        widgets.destroy()


def main():
    def GButton_547_command():
        change_window()
        create_recepie()

    def recpie_list():
        change_window()
        recepie_list_window()
    change_window()
    # A Label widget to show in toplevel
    tk.Label(root,
             text="This is a new window").pack()
    # setting title
    root.title("Recepie Book")

    GLabel_222 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=18, weight="bold")
    GLabel_222["font"] = ft
    GLabel_222["fg"] = "#333333"
    GLabel_222["justify"] = "center"
    GLabel_222["text"] = "Recepie Book"
    GLabel_222.place(x=0, y=0, width=588, height=34)

    GButton_547 = tk.Button(root, cursor="hand2")
    GButton_547["bg"] = "#7b7b7b"
    ft = tkFont.Font(family='Times', size=10)
    GButton_547["font"] = ft
    GButton_547["fg"] = "#000000"
    GButton_547["justify"] = "center"
    GButton_547["text"] = "NEW RECEPIE"
    GButton_547["relief"] = "flat"
    GButton_547.place(x=240, y=200, width=100, height=37)
    GButton_547["command"] = GButton_547_command

    GButton_857 = tk.Button(root, cursor="hand2")
    GButton_857["bg"] = "#7b7b7b"
    ft = tkFont.Font(family='Times', size=10)
    GButton_857["font"] = ft
    GButton_857["fg"] = "#000000"
    GButton_857["justify"] = "center"
    GButton_857["text"] = "RECEPIE LIST"
    GButton_857["relief"] = "flat"
    GButton_857.place(x=240, y=100, width=101, height=49)
    GButton_857["command"] = recpie_list


def create_recepie():
    title = ""
    description = ""
    preperation = ""
    servings = ""
    ingridients = ""
    directions = ""
    notes = ""

    def get_and_save_values():
        global title, description, preperation, servings, ingridients, directions, notes
        title = TITLE_INPUT.get()
        description = DESCRIPTION_INPUT.get()
        preperation = PREPERATION_INPUT.get()
        servings = SERVING_INPUT.get()
        ingridients = INGRIDIENTS_INPUT.get()
        directions = DIRECTIONS_INPUT.get()
        notes = NOTES_INPUT.get()
        print(notes)
        recepie = {"title": title, "description": description, "preperation": preperation,
                   "servings": servings, "ingridients": ingridients, "directions": directions,
                   "notes": notes}
        recepie_str = json.dumps(recepie, indent=1)
        if not os.path.exists(f"recepies/{title}.recepie"):
            open(f"recepies/{title}.recepie", "w").close()
        with open(f"recepies/{title}.recepie", "w+") as file:
            file.write(recepie_str)
        change_window()
        main()
        # Toplevel object which will
        # be treated as a new window

    TITLE_TEXT = tk.Label(root)
    ft = tkFont.Font(family='Times', size=18, weight="bold")
    TITLE_TEXT["font"] = ft
    TITLE_TEXT["fg"] = "#333333"
    TITLE_TEXT["justify"] = "center"
    TITLE_TEXT["text"] = "Recepie Maker"
    TITLE_TEXT.place(x=0, y=0, width=588, height=34)
    GLabel_631 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=13)
    GLabel_631["font"] = ft
    GLabel_631["fg"] = "#333333"
    GLabel_631["justify"] = "center"
    GLabel_631["text"] = "Title : "
    GLabel_631.place(x=0, y=40, width=612, height=30)

    TITLE_INPUT = tk.Entry(root)
    TITLE_INPUT["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=13)
    TITLE_INPUT["font"] = ft
    TITLE_INPUT["fg"] = "#333333"
    TITLE_INPUT["justify"] = "left"
    TITLE_INPUT["text"] = "title"
    TITLE_INPUT["relief"] = "flat"
    TITLE_INPUT.place(x=0, y=70, width=612, height=32)

    GLabel_700 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=13)
    GLabel_700["font"] = ft
    GLabel_700["fg"] = "#333333"
    GLabel_700["justify"] = "center"
    GLabel_700["text"] = "Description : "
    GLabel_700.place(x=0, y=100, width=615, height=34)

    DESCRIPTION_INPUT = tk.Entry(root)
    DESCRIPTION_INPUT["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=13)
    DESCRIPTION_INPUT["font"] = ft
    DESCRIPTION_INPUT["fg"] = "#333333"
    DESCRIPTION_INPUT["justify"] = "left"
    DESCRIPTION_INPUT["text"] = "description"
    DESCRIPTION_INPUT["relief"] = "flat"
    DESCRIPTION_INPUT.place(x=0, y=130, width=612, height=36)

    GLabel_449 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=13)
    GLabel_449["font"] = ft
    GLabel_449["fg"] = "#333333"
    GLabel_449["justify"] = "center"
    GLabel_449["text"] = "Preperation and cooking time : "
    GLabel_449["relief"] = "flat"
    GLabel_449.place(x=0, y=170, width=612, height=30)

    PREPERATION_INPUT = tk.Entry(root)
    PREPERATION_INPUT["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=13)
    PREPERATION_INPUT["font"] = ft
    PREPERATION_INPUT["fg"] = "#333333"
    PREPERATION_INPUT["justify"] = "left"
    PREPERATION_INPUT["text"] = "preperation and cooking time"
    PREPERATION_INPUT["relief"] = "flat"
    PREPERATION_INPUT.place(x=0, y=200, width=612, height=41)

    GLabel_445 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=13)
    GLabel_445["font"] = ft
    GLabel_445["fg"] = "#333333"
    GLabel_445["justify"] = "center"
    GLabel_445["text"] = "Number of servings and serving size : "
    GLabel_445["relief"] = "flat"
    GLabel_445.place(x=0, y=240, width=613, height=35)

    SERVING_INPUT = tk.Entry(root)
    SERVING_INPUT["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    SERVING_INPUT["font"] = ft
    SERVING_INPUT["fg"] = "#333333"
    SERVING_INPUT["justify"] = "left"
    SERVING_INPUT["text"] = "number of servings and serving size"
    SERVING_INPUT["relief"] = "flat"
    SERVING_INPUT.place(x=0, y=270, width=612, height=39)

    GLabel_444 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=13)
    GLabel_444["font"] = ft
    GLabel_444["fg"] = "#333333"
    GLabel_444["justify"] = "center"
    GLabel_444["text"] = "Ingredients : "
    GLabel_444.place(x=0, y=310, width=612, height=30)

    INGRIDIENTS_INPUT = tk.Entry(root)
    INGRIDIENTS_INPUT["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    INGRIDIENTS_INPUT["font"] = ft
    INGRIDIENTS_INPUT["fg"] = "#333333"
    INGRIDIENTS_INPUT["justify"] = "left"
    INGRIDIENTS_INPUT["text"] = "ingredients"
    INGRIDIENTS_INPUT["relief"] = "flat"
    INGRIDIENTS_INPUT.place(x=0, y=350, width=612, height=36)

    GLabel_293 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=13)
    GLabel_293["font"] = ft
    GLabel_293["fg"] = "#333333"
    GLabel_293["justify"] = "center"
    GLabel_293["text"] = "Directions"
    GLabel_293.place(x=0, y=400, width=613, height=39)

    DIRECTIONS_INPUT = tk.Entry(root)
    DIRECTIONS_INPUT["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    DIRECTIONS_INPUT["font"] = ft
    DIRECTIONS_INPUT["fg"] = "#333333"
    DIRECTIONS_INPUT["justify"] = "left"
    DIRECTIONS_INPUT["text"] = "Directions"
    DIRECTIONS_INPUT["relief"] = "flat"
    DIRECTIONS_INPUT.place(x=0, y=450, width=614, height=33)

    GLabel_621 = tk.Label(root)
    ft = tkFont.Font(family='Times', size=13)
    GLabel_621["font"] = ft
    GLabel_621["fg"] = "#333333"
    GLabel_621["justify"] = "center"
    GLabel_621["text"] = "Notes and FAQ"
    GLabel_621.place(x=0, y=490, width=613, height=36)

    NOTES_INPUT = tk.Entry(root)
    NOTES_INPUT["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=10)
    NOTES_INPUT["font"] = ft
    NOTES_INPUT["fg"] = "#333333"
    NOTES_INPUT["justify"] = "left"
    NOTES_INPUT["text"] = "Notes And FAQ"
    NOTES_INPUT["relief"] = "flat"
    NOTES_INPUT.place(x=0, y=530, width=613, height=30)

    GButton_33 = tk.Button(root, cursor="hand2")
    GButton_33["activebackground"] = "#bcbcbc"
    GButton_33["activeforeground"] = "#e3e3e3"
    GButton_33["bg"] = "#7b7b7b"
    ft = tkFont.Font(family='Times', size=10)
    GButton_33["font"] = ft
    GButton_33["fg"] = "#000000"
    GButton_33["justify"] = "center"
    GButton_33["text"] = "Done"
    GButton_33["relief"] = "flat"
    GButton_33.place(x=0, y=560, width=70, height=25)
    GButton_33["command"] = get_and_save_values

    CANCEL_BTN = tk.Button(root, cursor="hand2")
    CANCEL_BTN["activebackground"] = "#bcbcbc"
    CANCEL_BTN["activeforeground"] = "#e3e3e3"
    CANCEL_BTN["bg"] = "#7b7b7b"
    ft = tkFont.Font(family='Times', size=10)
    CANCEL_BTN["font"] = ft
    CANCEL_BTN["fg"] = "#000000"
    CANCEL_BTN["justify"] = "center"
    CANCEL_BTN["text"] = "Cancel"
    CANCEL_BTN["relief"] = "flat"
    CANCEL_BTN.place(x=100, y=560, width=70, height=25)
    CANCEL_BTN["command"] = main


main()
root.mainloop()
