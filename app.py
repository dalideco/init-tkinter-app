import tkinter as tk
import os

class CustomTkinterGUI:
    def __init__(self, master):
        self.master = master
        master.title("code")

        
        # create input frame
        input_frame = tk.Frame(master)
        input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create line number label for input text area
        self.line_numbers = tk.Label(input_frame, width=5, justify=tk.RIGHT, anchor='nw')
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # create input text area
        self.input_text = tk.Text(input_frame, height=30, width=80)
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.input_text.bind('<Key>', self.update_linenumbers)

        # create scrollbar for input text area
        scrollbar = tk.Scrollbar(input_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=self.input_text.yview)
        self.input_text.config(yscrollcommand=scrollbar.set)

        # create "Run" button
        self.run_button = tk.Button(master, text="▶", command=self.run_code , background="green")
        self.run_button.pack()

    def update_linenumbers(self, event):
        line_numbers = ''
        input_lines = self.input_text.get('1.0', 'end').split('\n')
        for i in range(1, len(input_lines)):
            line_numbers += str(i) + '\n'
        self.line_numbers.config(text=line_numbers)


    def run_code(self):
        # get the input code from the input text area
        code = self.input_text.get("1.0", tk.END)

        # save the code to a text file
        with open("input.txt", "w") as f:
            f.write(code)

        # run the compiled binary file with the text file as input
        # ./miniCompiler<input.txt
        os.system("./miniCompiler < input.txt > output.txt 2>&1 ")

        # read the output from the output file
        with open("output.txt", "r") as f:
            output = f.read()

        # create a new window to display the output
        output_window = tk.Toplevel(self.master)
        output_window.title("Output")
        output_text = tk.Text(output_window, height=30, width=80)
        output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create scrollbar for output text area
        scrollbar = tk.Scrollbar(output_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar.config(command=output_text.yview)
        output_text.config(yscrollcommand=scrollbar.set)

        output_text.insert(tk.END, output)

if __name__ == '__main__':
    root = tk.Tk()
    gui = CustomTkinterGUI(root)
    root.mainloop()
