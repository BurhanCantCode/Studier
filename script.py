import tkinter as tk
import webbrowser

def open_links(subject):
    if subject == "oop":
        # Open OOP link
        oop_link = "https://classroom.google.com/u/0/c/NjU2NzU5Nzg1NDM0"
        webbrowser.open(oop_link)

        # Open YouTube in the second page
        youtube_link = "https://www.youtube.com"
        webbrowser.open_new_tab(youtube_link)

    elif subject == "mvc":
        # Open instructions for MVC
        mvc_instructions = "https://youtube.com/"
        webbrowser.open(mvc_instructions)

        # Open Calculus PDF
        calculus_pdf = "C:/Users/Lenovo/Downloads/Calculus-late-transcendental (Anton 11-e).pdf"
        webbrowser.open(calculus_pdf)

        # Open MVC Classroom link
        mvc_classroom = "https://classroom.google.com/u/0/c/NjU3MjY5MTg4Mjc0"
        webbrowser.open(mvc_classroom)

        # Open YouTube
        webbrowser.open_new_tab(youtube_link)

    elif subject == "dld":
        # Open DLD Classroom link
        dld_classroom = "https://classroom.google.com/u/0/c/NjU3MjY4NDQ2NjIy"
        webbrowser.open(dld_classroom)

        # Open DLD PDF
        dld_pdf = "C:/Users/Lenovo/Desktop/pdfs/dld_book.pdf"
        webbrowser.open(dld_pdf)

        # Open YouTube channel
        youtube_channel = "https://www.youtube.com"
        webbrowser.open_new_tab(youtube_channel)

    else:
        print("Invalid subject entered.")

root = tk.Tk()
root.title("Subject Links")
root.geometry("300x200")

frame = tk.Frame(root, bg="lightgrey")
frame.place(relwidth=1, relheight=1)

oop_button = tk.Button(frame, text="OOP", command=lambda: open_links("oop"), font=("Arial", 14), bg="white", width=20, height=2)
oop_button.pack(pady=10)

mvc_button = tk.Button(frame, text="MVC", command=lambda: open_links("mvc"), font=("Arial", 14), bg="white", width=20, height=2)
mvc_button.pack(pady=10)

dld_button = tk.Button(frame, text="DLD", command=lambda: open_links("dld"), font=("Arial", 14), bg="white", width=20, height=2)
dld_button.pack(pady=10)

root.mainloop()