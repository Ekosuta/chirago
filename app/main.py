from ui.main_window import MainWindow
import ctypes

def main():
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    app = MainWindow()
    app.mainloop()
    
if __name__ == "__main__":
    main()
