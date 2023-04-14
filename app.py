import tkinter as tk
import subprocess
import os

class CustomTkinterGUI:
    def __init__(self, master):
        self.master = master
        master.title("CustomTkinter GUI")

        # create input text area
        self.input_text = tk.Text(master, height=10, width=50)
        self.input_text.pack()

        # create "Run" button
        self.run_button = tk.Button(master, text="Run", command=self.run_code)
        self.run_button.pack()

    def run_code(self):
        # get the input code from the input text area
        code = self.input_text.get("1.0", tk.END)

        # save the code to a text file
        with open("input.txt", "w") as f:
            f.write(code)

        # run the compiled binary file with the text file as input
        # ./miniCompiler<input.txt
        output = subprocess.Popen(["./miniCompiler", "<input.txt"], stdout=subprocess.PIPE).communicate()
        print("entire output: "+ output )
        output= output[0]

        print("ouput variable: "+ output)
      
        # create a new window to display the output
        output_window = tk.Toplevel(self.master)
        output_window.title("Output")
        output_text = tk.Text(output_window, height=10, width=50)
        output_text.pack()
        output_text.insert(tk.END, output)

if __name__ == '__main__':
    root = tk.Tk()
    gui = CustomTkinterGUI(root)
    root.mainloop()
