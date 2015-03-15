import Tkinter as tk

def pressed():
	print "This is a button"
	lab.config(text="You did it!")

root = tk.Tk()

button = tk.Button(root,text="Press", command = pressed)
lab = tk.Label(root, text="Press the button")
button.pack(pady=20,padx=20)
lab.pack()
root.mainloop()