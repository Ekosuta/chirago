import customtkinter as ctk
from services.search_service import SearchService
from data.dictionary_data import load_dict_data

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__
        self.title('Chirago')
        self.geometry("1500x1700")

        self.search_service = SearchService(dict_data)
        dict_data = load_dict_data()

        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('green')

        def create_widgets(self):
            # title
            title_label = ctk.CTkLabel(self, text='Chirago')
            title_label.pack(pady=20)
            # search bar
            self.search_bar = ctk.CTkEntry(self, placeholder_text='Search in English or Tenandi', width=300)
            self.search_bar.pack(pady=10)
            # search btn
            search_btn = ctk.CTkButton(self, text='Search', command=self.search)