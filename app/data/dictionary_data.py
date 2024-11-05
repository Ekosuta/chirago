import csv

class Dictionary:
    main_dict = 'app\data\dictionary.csv'
    conj_dict = 'app\data\conjugations.csv'

    def get_dictionary(main_dict):
        dictionary = {}
        with open(main_dict, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                english = row['english']
                tenandi = row['tenandi']
                part_of_speech = row['part_of_speech']
                eng_ex = row['english_example']
                ten_ex = row['tenandi_example']
            
            dictionary[tenandi] = {
                'english': english,
                'part_of_speech': part_of_speech,
                'english_example': eng_ex,
                'tenandi_example': ten_ex
            }
            
            dictionary[english] = {
                'tenandi': tenandi,
                'part_of_speech': part_of_speech,
                'english_example': eng_ex,
                'tenandi_example': ten_ex
            }
        return dictionary
    
    def get_conjugations(conj_dict):
        conjugations = {}
        with open(conj_dict, 'r') as f:
            reader =  csv.DictReader(f)
            for row in reader:
                ten_inf = row['infinitiveT']
                eng_inf = row['infinitiveE']
                ten_pres = row['presentT']
                eng_pres = row['presentE']
                ten_pres_par = row['present_particleT']
                eng_pres_par = row['present_particleE']
                ten_past = row['pastT']
                eng_past = row['pastE']
                ten_past_par = row['past_particleT']
                eng_past_par = row['past_particleE']
                ten_future = row['futureT']
                eng_future = row['futureE']
            
            conjugations[ten_inf] = {
                'infinitiveE': eng_inf,
                'presentT': ten_pres,
                'presentE': eng_pres,
                'present_particleT': ten_pres_par,
                'present_particleE': eng_pres_par,
                'pastT': ten_past,
                'pastE': eng_past,
                'past_particleT': ten_past_par,
                'past_particleE': eng_past_par,
                'futureT': ten_future,
                'futureE': eng_future
            }

            conjugations[eng_inf] = {
                'infinitiveT': ten_inf,
                'presentT': ten_pres,
                'presentE': eng_pres,
                'present_particleT': ten_pres_par,
                'present_particleE': eng_pres_par,
                'pastT': ten_past,
                'pastE': eng_past,
                'past_particleT': ten_past_par,
                'past_particleE': eng_past_par,
                'futureT': ten_future,
                'futureE': eng_future
            }
        return conjugations