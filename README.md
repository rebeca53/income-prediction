# income-prediction

This project was developed as part of the Erasmus MSc in Geospatial Technologies.

To investigate the factors that might influence the monthly income in Brazil, I trained different machine learnings.

Ensemble learners achieve higher accuracy. However, simple learners like LASSO have better interpretability in understanding and ranking the variables that influence income. You can check the results in this [presentation](https://github.com/rebeca53/income-prediction/blob/main/Income%20Prediction%20on%20Brazil%20data.pdf).

## Data

All the data is freely provided by the IBGE, the Brazilian Institute of Geography and Statistics.

Documents retrieved from
https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/

| Year | Visit | Dictionary                                                                                                                                                                                                                                                      | Data                                                                                                                                                                                                   | Unzipped data size |
| ---- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| 2019 | 1     | [dicionario_PNADC_microdados_2019_visita1_20230811.xls](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2019_visita1_20230811.xls) | [zipped PNADC_2019_Visita1](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2019_visita1_20230511.zip) | 1.53GB             |
| 2020 | 5     | [dicionario_PNADC_microdados_2020_visita5_20220224.xls](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2020_visita5_20220224.xls) | [zipped PNADC_2020_Visita5](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2020_visita5_20220916.zip) | 1.20GB             |
| 2021 | 5     | [dicionario_PNADC_microdados_2021_visita5.xls](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2021_visita5.xls)                   | [zipped PNADC_2021_Visita5](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2021_visita5_20220916.zip) | 1.13GB             |
| 2022 | 5     | [dicionario_PNADC_microdados_2022_visita5_20231220.xls](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2022_visita5_20231220.xls) | [zipped PNADC_2022_Visita5](https://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2022_visita5_20231222.zip) | 1.37GB             |

## Running data preparation scripts

### datapreparation_few_features_encoded.py

This script reads .txt files regarding "Effective monthly income from all work for persons 14 years of age or older (only for persons who received cash, products or goods in any work)".

More specifically:

- PNADC_2019_visita1.txt
- PNADC_2020_visita5.txt
- PNADC_2021_visita5.txt
- PNADC_2022_visita5.txt

The script process the data by encoding the values, and then generates the .csv files with processed data. For instance, each state value represents a column in the resulting data, which can be 0 or 1.
To run the code, make sure you have the aforementioned files in the same path as the script.

### datapreparation_few_uncoded_features.py

This script reads .txt files regarding "Effective monthly income from all work for persons 14 years of age or older (only for persons who received cash, products or goods in any work)".

More specifically:

- PNADC_2019_visita1.txt
- PNADC_2020_visita5.txt
- PNADC_2021_visita5.txt
- PNADC_2022_visita5.txt

The script process the data, and then generates the .csv files with processed data. It doesn't encodes values. For instance, the state is a column with a string value.
To run the code, make sure you have the aforementioned files in the same path as the script.
The resulting files are in the folder few_features.

### datapreparation.py

This script reads .txt files regarding "Effective monthly income from all work for persons 14 years of age or older (only for persons who received cash, products or goods in any work)".

More specifically:

- PNADC_2019_visita1.txt
- PNADC_2020_visita5.txt
- PNADC_2021_visita5.txt
- PNADC_2022_visita5.txt

The script process the data, and then generates the .csv files with processed data. It doesn't encodes values. For instance, the state is a column with a string value.
It differs from **_datapreparation_few_uncoded_features.py_** because it process more features (columns) from the original data.
To run the code, make sure you have the aforementioned files in the same path as the script.
The resulting files are in the folder many_features_text_category_values.

## Prediction model

The models were trained using [Orange](https://orangedatamining.com/). The resulting files are:

- final_text_category_values.ows
- final.ows

The results are summarized as follow:

| Model | MSE | MAE | R2 Coefficient of determination |
|-------|-----|-----|---------------------------------|
| Linear Regression | 0.456 | 0.501 | 0.506 |
| Lasso Linear Regression | 0.509 | 0.526 | 0.45 |
| kNN | 0.447 | 0.486 | 0.516 |
| Random Forest | 0.396 | 0.455 | 0.571 |
| _Gradient Boosting_ | 0.381 | 0.449 | 0.588 |
| AdaBoost | 0.421 | 0.474 | 0.545 |

Regarding the Lasso coeficients, the following table sorts the attributes according to the relationship with the response:
| Name | Coefficient| Category |
| -----|------------|----------|
|SCIENCE_INTELECTUAL | 0.364143| Occupation group |
|DIRECTOR_MANAGER| 0.287265| Occupation group |
|PUBLIC_ADMIN| 0.283835| Activity group |
|SEX=F |-0.232058| Gender |
|RACE_COLOR=RDUMMY_WHITE| 0.167143| Race |
|ELEMENTARY| -0.131037| Occupation group |
|HOME_SITUATION=RURAL| -0.128279| Home situation rural vs urban|
|SERVICE_SALESPEOPLE| -0.120774| Occupation group |
|MA| -0.109275| State |
|SC| 0.101642| State |
|HEAD| 0.0875955| Being the head of the household |
|CE| -0.0866028| State |
|YEARS_OF_STUDY| 0.0832276| Years of study |
|PARTNER_OTHER_SEX| 0.0739007| Being married to the head of the household |
|SP| 0.0604968| State |
|AREA_TYPE=CAPITAL| 0.0510832| Area type |
|QUALIFIED_AGRI_FISH_FORESTRY| -0.0517706| Occupation group |
|AREA_TYPE=NON_METRO_INTEG| -0.0419371| Area type |
|YEAR| 0.0407838| Year of the data collection |
|TECHNICIAN| 0.037846| Occupation group|
|EDUCATION_HEALTH_SOCIAL| 0.0374922| Activity group |
|INFO_COMM_FINANCE_MANAGE| 0.0188843| Activity group |
|WORKED_HOURS| 0.0181856| Worked hours |
|AGRI_FISH_FORESTRY| -0.0169214| Activity group |
|AGE| 0.0119543| Age |
|NUM_PEOPLE| -0.0087971| Number of people in the household |
|PR| 0.00693947| State |

## References

The main reference work for this project is:

Matkowski, M. (2021). Prediction of individual income: A machine learning approach.
