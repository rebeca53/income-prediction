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

    home_situation_pos = 32;
    home_situation_len = 1;

    area_type_pos = 33;
    area_type_len = 1;

    num_people_pos = 88;
    num_people_len = 2;

    relationship_HH_pos = 92;
    relationship_HH_len = 2;

    sex_pos = 94;
    sex_len = 1;
    
    age_pos = 103;
    age_len = 3;

    race_pos = 106;
    race_len  = 1;
    
    # Rendimento mensal efetivo de todos os trabalhos 
    # para pessoas de 14 anos ou mais de idade 
    # (apenas para pessoas que receberam em dinheiro, 
    # produtos ou mercadorias em qualquer trabalho)
    income_pos = 0;
    income_len = 8;

    education_years_pos = 0;
    education_years_len = 2;

    worked_hours_pos = 0;
    worked_hours_len = 3;

    activity_group_pos = 0;
    activity_group_len = 2;

    ocupation_group_pos = 0;
    ocupation_group_len = 2;

    def __init__(self, file_name, income_pos, eduy_pos, workh_pos, activity_pos, ocupation_pos):
        self.txt_file_name = file_name + ".txt"
        self.csv_file_name = file_name + ".csv"
        self.income_pos = income_pos
        self.education_years_pos = eduy_pos
        self.worked_hours_pos = workh_pos
        self.activity_group_pos = activity_pos
        self.ocupation_group_pos = ocupation_pos

visit2019 = Visit("PNADC_2019_visita1", income_pos=564, eduy_pos=536, workh_pos=601,
                  activity_pos=548, ocupation_pos=550)

visit2020 = Visit("PNADC_2020_visita5", 506, 461, workh_pos=526,
                  activity_pos=473, ocupation_pos=475)

visit2021 = Visit("PNADC_2021_visita5", 489, 461, workh_pos=526,
                  activity_pos=473, ocupation_pos=475)

visit2022 = Visit("PNADC_2022_visita5", 697, 669, workh_pos=734,
                  activity_pos=681, ocupation_pos=683)

def dummy_code_state(state_code):
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
    return dummy_state_code[state_code]

def dummy_code_sex(sex_code):
    if (sex_code == 1):
        return 'M'
    else:
        return 'F'

def decode_home_situation(home_situation_code):
    if (home_situation_code == 1):
        return 'URBAN'
    else:
        return 'RURAL'

def decode_area_type(area_type_code):
    area_type = {
        '1':'CAPITAL',
        '2':'METROPOLITAN',
        '3':'INTEGRATED',
        '4':'NON_METRO_INTEG'
    }

    return area_type[area_type_code]

def decode_relationship_HH(relation_code):
    relation_HH = {
        '01':'HEAD',
        '02':'PARTNER_OTHER_SEX',
        '03':'PARTNER_SAME_SEX',
        '04':'CHILD_BOTH',
        '05':'CHILD_HEAD',
        '06':'STEPCHILD',
        '07':'SON_DAUGTHER_IN_LAW',
        '08':'PARENT',
        '09':'PARENT_IN_LAW',
        '10':'GRANDCHILD',
        '11':'GREATGRANDCHILD',
        '12':'SIBLING',
        '13':'GRANDPARENT',
        '14':'RELATIVE',
        '15':'FREE_NON_RELATIVE',
        '16':'PAYING_NON_RELATIVE',
        '17':'PENSIONER',
        '18':'DOMESTIC_EMPLOYEE',
        '19':'DOMESTRIC_EMPLOYEE_RELATIVE'
    }

    return relation_HH[relation_code]

def dummy_color_race(race_code):
    dummy_race_code = {
            '1':'RDUMMY_WHITE',
            '2':'RDUMMY_BLACK',
            '3':'RDUMMY_ASIAN',
            '4':'RDUMMY_MIXED', #PARDO
            '5':'RDUMMY_NATIVE',
            '9':'RDUMMY_OTHER'
        };

    return dummy_race_code[race_code]

def decode_activity(activity_code):
    activity_sector_code = {
        '01':'AGRI_FISH_FORESTRY',
        '02':'INDUSTRY',
        '03':'CONSTRUCTION',
        '04':'VEIHICLES_SELL_MAINTENANCE',
        '05':'TRANSPORTATION_WAREHOUSE',
        '06':'HOUSING_FOOD',
        '07':'INFO_COMM_FINANCE_MANAGE',
        '08':'PUBLIC_ADMIN',
        '09':'EDUCATION_HEALTH_SOCIAL',
        '10':'OTHER',
        '11':'DOMESTIC_LABOR',
        '12':'POORLY_DEFINED'
    }
    return activity_sector_code[activity_code]

def decode_ocupation(ocupation_code):
    ocupation_group_code = {
        '01':'DIRECTOR_MANAGER',
        '02':'SCIENCE_INTELECTUAL',
        '03':'TECHNICIAN',
        '04':'MANAGEMENT_SUPPORT',
        '05':'SERVICE_SALESPEOPLE',
        '06':'QUALIFIED_AGRI_FISH_FORESTRY',
        '07':'QUALIFIED_CONSTRUCTION_MECH',
        '08':'MACHINERY_OPERATOR',
        '09':'ELEMENTARY',
        '10':'ARMY',
        '11':'POORLY_DEFINED'
    }
    return ocupation_group_code[ocupation_code]

for visit in [visit2019, visit2020, visit2021, visit2022]:
    print("Visit txt name: "+visit.txt_file_name)
    print("Visit csv name: "+visit.csv_file_name)
    counter = 1
    count_valid = 0

    # https://stackoverflow.com/questions/39642082/convert-txt-to-csv-python-script
    with open(visit.txt_file_name, 'r') as in_file, open(visit.csv_file_name, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('YEAR', 'AGE', 'SEX', 'RACE_COLOR', 'STATE', 'HOME_SITUATION', 'AREA_TYPE', 
                         'NUM_PEOPLE', 'RELATION_HEAD', 'YEARS_OF_STUDY','WORKED_HOURS' , 'ACTIVITY_GROUP' , 
                         'OCUPATION_GROUP' ,'INCOME', 'LOG_INCOME'))
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

            age = int(line[visit.age_pos-1:visit.age_pos-1+visit.age_len])
            row.append(age)

            sex_code = int(line[visit.sex_pos-1:visit.sex_pos-1+visit.sex_len])
            # print("sex code is "+str(sex_code))
            # print(dummy_code_sex(sex_code))
            # row.append(dummy_code_sex(sex_code))
            row.append(sex_code)

            race_code = line[visit.race_pos-1:visit.race_pos-1+visit.race_len]
            # print("race code is "+race_code)
            # row.append(dummy_color_race(race_code))
            row.append(int(race_code))
            
            state_code = line[visit.state_pos-1:visit.state_pos-1+visit.state_len]
            # print("state code is "+state_code)
            # row.append(dummy_code_state(state_code))
            row.append(int(state_code))

            home_situ_code = int(line[visit.home_situation_pos-1:visit.home_situation_pos-1+visit.home_situation_len])
            # row.append(decode_home_situation(home_situ_code))
            row.append(home_situ_code)

            area_type_code = line[visit.area_type_pos-1:visit.area_type_pos-1+visit.area_type_len]
            # row.append(decode_area_type(area_type_code))
            row.append(int(area_type_code))

            number_people_house = int(line[visit.num_people_pos-1:visit.num_people_pos-1+visit.num_people_len])
            row.append(number_people_house)

            relation_head_code = line[visit.relationship_HH_pos-1:visit.relationship_HH_pos-1+visit.relationship_HH_len]
            row.append(decode_relationship_HH(relation_head_code))

            years_of_study = line[visit.education_years_pos-1:visit.education_years_pos-1+visit.education_years_len]
            row.append(years_of_study)

            worked_hours = int(line[visit.worked_hours_pos-1:visit.worked_hours_pos-1+visit.worked_hours_len])
            row.append(worked_hours)
            
            activity_code = line[visit.activity_group_pos-1:
                                 visit.activity_group_pos-1+visit.activity_group_len]
            row.append(decode_activity(activity_code))

            ocupation_code = line[visit.ocupation_group_pos-1:
                                  visit.ocupation_group_pos-1+visit.ocupation_group_len]
            row.append(decode_ocupation(ocupation_code))

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
        


