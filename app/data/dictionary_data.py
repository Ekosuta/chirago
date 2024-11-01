import csv
dict_path = 'app\data\dictionary_data.csv'

def load_dict_data(dict_path):
    with open(dict_path, 'r') as f:
        data = csv.reader(f)

        dict_data = {}
        for row in data:
            english = row[0].strip().lower()
            tenandi = row[1].strip().lower()
            part = row[2]
            definition = row[3]
            eng_ex = row[4]
            ten_ex = row[5]
            
            dict_data[english] = {
                'tenandi': tenandi,
                'type': part,
                'definition': definition,
                'english example': eng_ex,
                'tenandi example': ten_ex
            }

            dict_data[tenandi] = {
                'english': english,
                'type': part,
                'definition': definition,
                'english example': eng_ex,
                'tenandi example': ten_ex
            }
        return dict_data
    
dictionary_data = load_dict_data(dict_path)
print(load_dict_data(dict_path))