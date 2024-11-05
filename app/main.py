from ui.main_window import MainWindow
import customtkinter as ctk

def main():
    root = ctk.CTk()
    MainWindow(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
