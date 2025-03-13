import csv
import itertools
import time
import math

start = time.time()
debug = False


class Visit:
    file_path = "";
    txt_file_name = "";
    csv_file_name = "";

    year_pos = 1;
    year_len = 4;
    
    state_pos = 6;
    state_len = 2;

    # house_situ_pos = 32;
    # house_situ_len = 1;

    # area_type_pos = 33;
    # area_type_len = 1;

    # num_people_pos = 88;
    # num_people_len = 2;

    # relationship_HH_pos = 92;
    # relationship_HH_len = 2;

    sex_pos = 94;
    sex_len = 1;
    
    # age_pos = 103;
    # age_len = 3;

    race_pos = 106;
    race_len  = 1;
    
    income_pos = 0;
    income_len = 0;

    education_years_pos = 0;
    education_years_len = 0;

    # worked_hours_pos = 601;
    # worked_hours_len = 3;

    # activity_group_pos = 0;
    # activity_group_len = 0;

    # ocupation_group_pos = 0;
    # ocupation_group_len = 0;

    def __init__(self, file_name, income_pos, income_len, eduy_pos, eduy_len):
        self.txt_file_name = file_name + ".txt"
        self.csv_file_name = file_name + ".csv"
        self.income_pos = income_pos
        self.income_len = income_len
        self.education_years_pos = eduy_pos
        self.education_years_len = eduy_len

# Rendimento mensal efetivo de todos os trabalhos 
# para pessoas de 14 anos ou mais de idade 
# (apenas para pessoas que receberam em dinheiro, 
# produtos ou mercadorias em qualquer trabalho)
visit2019 = Visit("PNADC_2019_visita1", 564, 8, 536, 2)

# Rendimento mensal efetivo de todos os trabalhos 
# para pessoas de 14 anos ou mais de idade 
# (apenas para pessoas que receberam em dinheiro, 
# produtos ou mercadorias em qualquer trabalho)
visit2020 = Visit("PNADC_2020_visita5", 506, 8, 461, 2)

# Rendimento mensal efetivo de todos os trabalhos 
# para pessoas de 14 anos ou mais de idade 
# (apenas para pessoas que receberam em dinheiro, 
# produtos ou mercadorias em qualquer trabalho)
visit2021 = Visit("PNADC_2021_visita5", 489, 8, 461, 2)

# Rendimento mensal efetivo de todos os trabalhos 
# para pessoas de 14 anos ou mais de idade 
# (apenas para pessoas que receberam em dinheiro, 
# produtos ou mercadorias em qualquer trabalho)
visit2022 = Visit("PNADC_2022_visita5", 697, 8, 669,2)

def dummy_code_state(state_code):
    dummy_state_values = {'SDUMMY_RO':0,
                       'SDUMMY_AC':0,
                       'SDUMMY_AM':0,
                       'SDUMMY_RR':0,
                       'SDUMMY_PA':0,
                       'SDUMMY_AP':0,
                       'SDUMMY_TO':0,
                       'SDUMMY_MA':0,
                       'SDUMMY_PI':0,
                       'SDUMMY_CE':0,
                       'SDUMMY_RN':0,
                       'SDUMMY_PB':0,
                       'SDUMMY_PE':0,
                       'SDUMMY_AL':0,
                       'SDUMMY_SE':0,
                       'SDUMMY_BA':0,
                       'SDUMMY_MG':0,
                       'SDUMMY_ES':0,
                       'SDUMMY_RJ':0,
                       'SDUMMY_SP':0,
                       'SDUMMY_PR':0,
                       'SDUMMY_SC':0,
                       'SDUMMY_RS':0,
                       'SDUMMY_MS':0,
                       'SDUMMY_MT':0,
                       'SDUMMY_GO':0,
                       'SDUMMY_DF':0
                       };
    
    dummy_state_code = {'11':'SDUMMY_RO',
                       '12':'SDUMMY_AC',
                       '13':'SDUMMY_AM',
                       '14':'SDUMMY_RR',
                       '15':'SDUMMY_PA',
                       '16':'SDUMMY_AP',
                       '17':'SDUMMY_TO',
                       '21':'SDUMMY_MA',
                       '22':'SDUMMY_PI',
                       '23':'SDUMMY_CE',
                       '24':'SDUMMY_RN',
                       '25':'SDUMMY_PB',
                       '26':'SDUMMY_PE',
                       '27':'SDUMMY_AL',
                       '28':'SDUMMY_SE',
                       '29':'SDUMMY_BA',
                       '31':'SDUMMY_MG',
                       '32':'SDUMMY_ES',
                       '33':'SDUMMY_RJ',
                       '35':'SDUMMY_SP',
                       '41':'SDUMMY_PR',
                       '42':'SDUMMY_SC',
                       '43':'SDUMMY_RS',
                       '50':'SDUMMY_MS',
                       '51':'SDUMMY_MT',
                       '52':'SDUMMY_GO',
                       '53':'SDUMMY_DF'
                       };
    dummy_state_values[dummy_state_code[state_code]] = 1
    if (debug):
        print(dummy_state_values)
    return dummy_state_code[state_code]

def dummy_code_sex(sex_code):
    if (sex_code == 1):
        return 'M'
    else:
        return 'F'

def dummy_color_race(race_code):
    dummy_race_values = {
        'RDUMMY_WHITE':0,
        'RDUMMY_BLACK':0,
        'RDUMMY_ASIAN':0,
        'RDUMMY_MIXED':0, #PARDO
        'RDUMMY_NATIVE':0,
        'RDUMMY_OTHER':0
    };

    dummy_race_code = {
            '1':'RDUMMY_WHITE',
            '2':'RDUMMY_BLACK',
            '3':'RDUMMY_ASIAN',
            '4':'RDUMMY_MIXED', #PARDO
            '5':'RDUMMY_NATIVE',
            '9':'RDUMMY_OTHER'
        };
    dummy_race_values[dummy_race_code[race_code]] = 1
    if (debug):
        print(dummy_race_values)
    return dummy_race_code[race_code]

for visit in [visit2019, visit2020, visit2021, visit2022]:
    print("Visit txt name: "+visit.txt_file_name)
    print("Visit csv name: "+visit.csv_file_name)
    counter = 1
    count_valid = 0

    # https://stackoverflow.com/questions/39642082/convert-txt-to-csv-python-script
    with open(visit.txt_file_name, 'r') as in_file, open(visit.csv_file_name, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        # writer.writerow(('YEAR', 'DUMMY_FEMALE', 'RDUMMY_WHITE', 'RDUMMY_BLACK', 'RDUMMY_ASIAN', 'RDUMMY_MIXED', 'RDUMMY_NATIVE', 'RDUMMY_OTHER', 
        #                  'SDUMMY_RO','SDUMMY_AC','SDUMMY_AM','SDUMMY_RR','SDUMMY_PA','SDUMMY_AP','SDUMMY_TO','SDUMMY_MA','SDUMMY_PI','SDUMMY_CE',
        #                  'SDUMMY_RN','SDUMMY_PB','SDUMMY_PE','SDUMMY_AL','SDUMMY_SE','SDUMMY_BA','SDUMMY_MG','SDUMMY_ES','SDUMMY_RJ','SDUMMY_SP',
        #                  'SDUMMY_PR','SDUMMY_SC','SDUMMY_RS','SDUMMY_MS','SDUMMY_MT','SDUMMY_GO','SDUMMY_DF', 'INCOME'))
        writer.writerow(('YEAR', 'SEX', 'RACE_COLOR', 'STATE', 'YEARS_OF_STUDY','INCOME', 'LOG_INCOME'))
        group = []
        
        lines = in_file.read().splitlines()
        for line in lines:
            # if (count_valid > 30):
            #     break

            income = int(line[visit.income_pos-1:visit.income_pos-1+visit.income_len].strip() or 0)
            if (income <= 0):
                counter = counter + 1
                continue
            
            row = []
            # print(counter)
            count_valid = count_valid + 1
            # print("income is "+str(income))
            
            year = int(line[visit.year_pos-1:visit.year_pos-1+visit.year_len])
            # print("year is "+str(year))
            row.append(year)

            sex_code = int(line[visit.sex_pos-1:visit.sex_pos-1+visit.sex_len])
            # print("sex code is "+str(sex_code))
            # print(dummy_code_sex(sex_code))
            row.append(dummy_code_sex(sex_code))


            race_code = line[visit.race_pos-1:visit.race_pos-1+visit.race_len]
            # print("race code is "+race_code)
            row.append(dummy_color_race(race_code))
            # row.extend(dummy_color_race(race_code))

            
            state_code = line[visit.state_pos-1:visit.state_pos-1+visit.state_len]
            # print("state code is "+state_code)
            row.append(dummy_code_state(state_code))
            # row.extend(list(dummy_code_state(state_code).values()))

            years_of_study = line[visit.education_years_pos-1:visit.education_years_pos-1+visit.education_years_len]
            row.append(years_of_study)
            
            row.append(income)

            log_income = math.log(income)
            row.append(log_income)
            counter = counter + 1

            print(row)
            group.append(row)
            # writer.writerow(row)

            #print(line)

        writer.writerows(group)
        in_file.close()
        out_file.close()
        print("total of lines "+str(counter))
        print("total of valid income "+str(count_valid))
        end = time.time()
        print("Time elapsed:") # last time: 173 seconds
        print(end - start)

    
    # df = pd.read_csv('PNADC_2022_visita5.csv')

    # stripped = [line.replace(","," ").split() for line in lines]
    # grouped = itertools.izip(*[stripped]*1)
    # with open('PNADC_2016_visita1.csv', 'w') as out_file:
    #     writer = csv.writer(out_file)
    #     writer.writerow(('title', 'intro', 'tagline'))
    #     for group in grouped:
    #         writer.writerows(group)
        


