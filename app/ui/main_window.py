import customtkinter as ctk
from services.search_service import search
from data.dictionary_data import Dictionary

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('Chirago')
        self.master.geometry('500x500')

        # appearance
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('green')

        #load the home page
        self.create_main_frame()
        self.search = search()

    def create_main_frame(self):
        # create main frame
        self.main_frame = ctk.CTkFrame(self.master)
        self.main_frame.pack(fill='both', expand=True)

        # title
        title_label = ctk.CTkLabel(self.main_frame, text='Chirago', font=('Arial', 24))
        title_label.pack(pady=20)

        # search bar
        self.search_entry = ctk.CTkEntry(self.main_frame, placeholder_text='Search in English or Tenandi', width=300)
        self.search_entry.pack(pady=10)

        # search btn
        self.search_btn = ctk.CTkButton(self.main_frame, text='Search', command=self.search)
        self.search_btn.pack(pady=10)

        self.verb_result_frame = ctk.CTkFrame(self.master)
        self.result_frame = ctk.CTkFrame(self.master)

    def display_verb_result(self, result):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        result_label = ctk.CTkLabel(self.verb_result_frame, text=result, font=('Arial', 24))
        result_label.pack(pady=10)

        self.tabview = ctk.CTkTabview(self.verb_result_frame)

    def display_word_result(self, result):
        pass

    def route_window(self):
        word = self.search_entry.get()
        result = self.search(word)
        if result['part_of_speech'] == 'verb':
            self.display_verb_result(result)
        else:
            self.display_word_result(result)