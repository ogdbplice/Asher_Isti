import tkinter as tk

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create the main window
root = tk.Tk()
root.title("Quiz Program")
root.geometry("400x700")

# Configure a grid to make frames stack properly
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create frames for each page
welcome_frame = tk.Frame(root)
selection_frame = tk.Frame(root)


for frame in (welcome_frame, selection_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# Page 1: Welcome Frame
welcome_label = tk.Label(welcome_frame, text="Welcome to My App!", font=("Arial", 18))
welcome_label.pack(pady=20)

start_button = tk.Button(welcome_frame, text="Start", font=("Arial", 14),
                         command=lambda: show_frame(selection_frame))
start_button.pack()

# Page 2: Program Frame
program_label = tk.Label(selection_frame, text="This is the main program!", font=("Arial", 18))
program_label.pack(pady=20)

back_button = tk.Button(selection_frame, text="Back", font=("Arial", 14),
                        command=lambda: show_frame(welcome_frame))
back_button.pack()

# Show the initial frame
show_frame(welcome_frame)

# Run the application
root.mainloop()
