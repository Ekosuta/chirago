import pandas as pd
import os

def load_dict_data():
    file_path = os.path.join(os.path.dirname(__file__), 'data', dictionary_data.xlsx)

    data = pd.read_excel(file_path)

    dict_data = {}
    for ind, row in data.iterrows():
        english = row['English'].strip().lower()
        tenandi = row['Tenandi'].strip().lower()
        part = row['Part of Speech']
        definition = row.get('Definition', '')

        dict_data[english_word] = {
            'tenandi': tenandi,
            'type': part,
            'definition': definition
        }

        dict_data[tenandi_word] = {
            'english': english,
            'type': part,
            'definition': definition
        }
    return dict_data