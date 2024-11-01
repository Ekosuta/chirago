import customtkinter as ctk
from data.dictionary_data import load_dict_data

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Chirago')

        # sizing and positioning
        appw = 500 # app width
        apph = 500 # app height
        sw = self.winfo_screenwidth()

        sh = self.winfo_screenheight()
        x = int((sw/2) - (appw*1.5))
        y = int((sh/2) - (apph*1.5))
        self.geometry(f"{appw}x{apph}+{x}+{y}")

        print(sw, sh)

        self.search_service = SearchService(dict_data)
        dict_data = load_dict_data()

        # appearance
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('green')

        self.create_widgets()

    def create_widgets(self):
        # title
        title_label = ctk.CTkLabel(self, text='Chirago')
        title_label.pack(pady=20)
        # search bar
        self.search_bar = ctk.CTkEntry(self, placeholder_text='Search in English or Tenandi', width=300)
        self.search_bar.pack(pady=10)
        # search btn
        self.search_btn = ctk.CTkButton(self, text='Search', command=self.search)
        self.search_btn.pack(pady=10)

    def search():
        pass