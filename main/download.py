from sqlalchemy import true
import main, config
import os
import time
import glob
import re
from pathlib import Path
from selenium.webdriver.support.ui import Select

from config import CHROMEDRIVER
from config import FILES2 

TIME_SLEEP = 5

# caso da cemig - dois lançamentos de tafira no ano 
# inconsistencia com a data de aniversario para pucos agentes 
# rename without -D/_D/-DIS
# quem é energisa?
# arquivos que começam com PCAT

#  CRTL + SHIFT + L - Select all
# https://www.npmjs.com/package/python-bridge
# -> 2022
#   -> 2021
#       -> 2020 ...
# change [year_] to iterable

# 

year_2022 = '2022'
year = '2021'
year_2020 = '2020'
file_path = glob.glob(FILES2 + "\\*")
file_name = []

'''

'''

# 2022
URL_2022 = [

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/43%20PCAT%20Celpe%20" + year_2022 + "%20V02.xlsx", # CELPE - 29/04

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/47%20PCAT%20Coelba%20" + year_2022 + "%20V02.xlsx", # COELBA - 22/04

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/40%20PCAT%20Cosern%20" + year_2022 + "%20V02.xlsx", # COSERN - 22/04

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/63%20PCAT%20CPFL%20Paulista%20" + year_2022 + "%20V02.xlsx", # CPFL PAULISTA - 08/40

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6611%20PCAT%20EBO%20" + year_2022 + "%20V02.xlsx", # EBO - 04/02

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/404%20PCAT%20EMS%20%20" + year_2022 + "%20V02.xlsx", # EMS - 16/04

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/405%20PCAT%20EMT%20" + year_2022 + "%20V02.xlsx", # EMT - 16/04

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/39%20PCAT%20Enel%20CE%20" + year_2022 + "%20V02.xlsx", # Enel - CE - 22/04

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/383%20PCAT%20Enel%20RJ%20" + year_2022 + "%20V02.xlsx", # Enel - RJ - 15/03

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/44%20PCAT%20Ceal%20" + year_2022 + "%20V02.xlsx", # EQUATORIAL AL - 03/05

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6587%20PCAT%20ESE%20" + year_2022 + "%20V02.xlsx", # ESE - 22/04

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/382%20PCAT%20Light%20" + year_2022 + "%20V02.xlsx", # LIGHT - 15/03

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_CPFL%20Santa%20Cruz_" + year_2022 + ".xlsx", # CPFL SANTA CRUZ - 22/03
]

# 2021


# 2020 and before
URL_2020 = [

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5160%20PCAT%20CEB-DIS%20" + year_2020 + "%20V021.xlsx", # CEBDIS 22/10

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5351%20PCAT%20Ceral%20Anit%C3%A1polis%20" + year_2020 + "%20V02.xlsx", # CERAL 2 - 30/11

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6610%20PCAT%20CERMC%20" + year_2020 + "%20V02.xlsx", # CERMC 2 - 30/11/2020

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/396%20PCAT%20RGE%20SUL%202019%20V021.xlsx", # RGE - 19/06

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_CERR_2013.xlsx", ### CEER - 01/11

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20174.xlsx", # CFLO - 12/07

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20171.xlsx", # CNEE - 12/07

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/SPARTA_SANTA_CRUZ_2018.xlsx", # CPFL JAGUARI - 22/03

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_NSC_20181.xlsx", # CPFL LESTE PAULISTA - 22/03

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_NSC_20182.xlsx", # CPFL MOOCA - 22/03

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_NSC_20184.xlsx", # CPFL SUL PAULISTA - 22/03

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20172.xlsx", # EDEVP - 12/07

    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20173.xlsx", # EEB - 12/07
]

'''
#rename_file('2937 PCAT CPFL Piratininga " + year + " V02.xlsx', 'CPFL- PIRATININGA." + year + "-10-23.xlsx') # [code], name

#2937 PCAT CPFL Piratininga " + year + " V02

TIME_SLEEP = 5

# PATHS

CHROMEDRIVER = os.path.dirname(os.getcwd()) + '\\chromedriver\\chromedriver.exe'
FILES = os.path.dirname(os.getcwd()) + '\\files\\'

def rename_file(old_file, new_file):
    old_file = os.path.join(config.FILES, old_file)
    new_file = os.path.join(config.FILES, new_file)
    return os.rename(old_file, new_file)

'''
def tarifas(driver):

    files = glob.glob(FILES2 + '\\*')
    for f in files:
        os.remove(f)

    year_21 = 2021

    # change 2022 to current year
    while year_21 <= 2022:
        year = str(year_21)

        URL_2021 = [

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7019%20PCAT%20AmE%20" + year + "%20V02.xlsx", # AME - 01/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/370%20PCAT%20Roraima%20Energia%20" + year + "%20V02.xlsx", # Boa Vista - 01/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/11825 PCAT Castro-DIS " + year + " V02.xlsx", ## Castro-DIS - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/31 PCAT CEA " + year + " V02.xlsx", ## CEA - 13/12

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5381%20PCAT%20Cedrap%20" + year + "%20V02.xlsx", # CEDRAP - 30/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5366%20PCAT%20Cedri%20" + year + ".xlsx", # CEDRI - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5707%20PCAT%20CEEE-D%20" + year + "%20V02.xlsx", # CEE-D - 22/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5356%20PCAT%20Cegero%20" + year + ".xlsx", # CECEGRO - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5372%20PCAT%20Cejama%20" + year + ".xlsx", # CEJAMA - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5697%20PCAT%20Celesc_D%20%20RTP%20" + year + ".xlsx", # CELESC-DIS - 22/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5343%20PCAT%20CELETRO%20" + year + "%20V02.xlsx", # CELETRO - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6072%20PCAT%20Enel%20GO%20" + year + "%20V02.xlsx", # CELG-D -> Enel - GO - 22/10

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/4950%20PCAT%20Cemig-D%20" + year + "%20V021.xlsx", # CEMIG-D - 29/05

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7467%20PCAT%20Cemirim%20" + year + "%20V02%20.xlsx", # CEMIRIM - 29/05

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_Ceprag_" + year + ".xls", ## CEPRAG - 22/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6897%20PCAT%20Cera%C3%A7a%20" + year + ".xlsx", # CERAÇA - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5351%20PCAT%20Ceral%20Anit%C3%A1polis%20" + year + "%20V02.xlsx", # CERAL-DIS - 30/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6898%20PCAT%20Cerbranorte%20" + year + "%20V02.xlsx", # CERBRANORTE - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5279%20PCAT%20CERCI%20" + year + "%20V02.xlsx", # CERCI - 29/04

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5377%20PCAT%20Cercos%20" + year + "%20V02.xlsx", # CERCOS - 29/05

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5352%20PCAT%20Cerej%20" + year + ".xlsx", # CEREJ - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5274%20PCAT%20Ceres%20" + year + "%20V02.xlsx", # CERES - 29/04

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/504%20PCAT%20Cerfox%20" + year + "%20V02.xlsx", # CERFOX - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5353%20PCAT%20Cergal%20" + year + "%20V02.xlsx", # CERGAL - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5355%20PCAT%20Cergapa%20" + year + "%20V02.xlsx", # CERGAPA - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5363%20PCAT%20Cergral%20" + year + "%20V02.xlsx", # CERGRAL - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2763%20PCAT%20Ceriluz%20" + year + "%20V02.xlsx", # CERILUZ - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5386%20PCAT%20Cerim%20" + year + "%20V02.xlsx", # CERIM - 30/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5378%20PCAT%20Ceripa%20" + year + "%20V02.xlsx", # CERIPA - 29/04

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5382%20PCAT%20Ceris%20" + year + "%20V02.xlsx", # CERIS - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6610%20PCAT%20CERMC%20" + year + "%20V02.xlsx", # CERMC 1 - 30/11/" + year + "

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2381%20PCAT%20Cermiss%C3%B5es%20" + year + "%20V02.xlsx", # CERMISSÕES - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5364%20PCAT%20Cermoful%20" + year + "%20V02.xlsx", # CERMOFUL - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6609%20PCAT%20Cernhe%20" + year + "%20V02.xlsx", # CERNHE - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/369%20PCAT%20Ceron%20" + year + "%20V02.xlsx", # CERON - 13/12

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5365%20PCAT%20Cerpalo%20" + year + ".xlsx", # CERPALO - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5384%20PCAT%20Cerpro%20" + year + "%20V02.xlsx", # CERPRO - 29/05

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5385%20PCAT%20CERRP%20" + year + "%20V02.xlsx", # CERRP - 29/05

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7883%20PCAT%20Cersad%20" + year + "%20V02.xlsx", # CERSAD DISTRIBUIDORA - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5368%20PCAT%20Cersul%20" + year + "%20V02.xlsx", # CERSUL - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/3223%20PCAT%20Certaja%20" + year + "%20V02.xlsx", # CERTAJA - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7371%20PCAT%20Certel%20" + year + "%20V02.xlsx", # CERTEL - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/527%20PCAT%20Certhil%20" + year + "%20V02.xlsx", # CERTHIL - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5369%20PCAT%20Certrel%20" + year + ".xlsx", # CERTREL - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5375%20PCAT%20Cervam%20" + year + ".xlsx", # CERVAM - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5379%20PCAT%20Cetril%20" + year + "%20V02.xlsx", # CETRIL - 30/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/103%20PCAT%20Chesp%20" + year + "%20V02.xlsx", # CHESP - 22/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/82%20PCAT%20Cocel%20" + year + "%20V02.xlsx", # COCEL - 29/06

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/11763%20PCAT%20Codesam%20" + year + "%20V02.xlsx", # CODESAM - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5370%20PCAT%20Coopera%20" + year + "%20V02.xlsx", # COOPERA - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2904%20PCAT%20Cooperalian%C3%A7a%20" + year + "%20V02.xlsx", # COOPERALIANÇA - 29/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5371%20PCAT%20Coopercocal%20" + year + "%20V02.xlsx", # COOPERCOCAL - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/3627%20PCAT%20Cooperluz%20" + year + "%20V02.xlsx", # COOPERLUZ - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5373%20PCAT%20Coopermila%20" + year + ".xlsx", # COOPERMILA - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_Coopernorte_" + year + ".xlsx", # COOPERNORTE - 22/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_Coopersul_" + year + ".xlsx", # COOPERSUL - 22/12

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5374%20PCAT%20Cooperzem%20" + year + "%20V02.xlsx", # COOPERZEM - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7016%20PCAT%20Coorsel%20" + year + "%20V02.xlsx", # COORSEL - 30/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2866%20PCAT%20Copel-DIS%20" + year + "%20V02.xlsx", # COPEL-DIS - 24/06

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2351%20PCAT%20Coprel%20" + year + "%20V02.xlsx", # COPREL - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2937%20PCAT%20CPFL%20Piratininga%20" + year + "%20V02.xlsx", # CPFL PIRATININGA - 23/10

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/598%20PCAT%20Creluz-D%20" + year + "%20V02.xlsx", # CRELUZ-D - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2783%20PCAT%20Creral%20" + year + "%20V02.xlsx", # CRERAL - 30/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/87%20PCAT%20Ienergia%20" + year + "%20V02.xlsx", # DCELT - 29/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/95%20PCAT%20Demei%20" + year + "%20V02.xlsx", # DEMEI - 22/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/51%20PCAT%20DMED%20" + year + "%20V02.xlsx", # DMED - 22/11

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/380%20PCAT%20EDP%20ES%20" + year + "%20V02.xlsx", # EDP ES - 07/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/391%20PCAT%20EDP%20SP%20" + year + "%20V02.xlsx", # EDP SP - 23/10

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/88%20PCAT%20EFLJC%20" + year + "%20V02.xlsx", # EFLJC - 29/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/86%20PCAT%20Eflul%20" + year + "%20V02.xlsx", # EFLUL - 29/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/385%20PCAT%20Elektro%20" + year + "%20V02.xlsx", # ELEKTRO - 27/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/26%20PCAT%20Eletroacre%20" + year + "%20V02.xlsx", # ELETROACRE - 13/12

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/398%20PCAT%20Eletrocar%20" + year + "%20V02.xlsx", # ELETROCAR - 22/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/390%20PCAT%20Enel%20SP%20" + year + "%20V02.xlsx", # ELETROPAULO - 04/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/381%20PCAT%20ELFSM%20" + year + "%20V02.xlsx", # ELFSM - 22/09

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6585%20PCAT%20EMG%20" + year + "%20V02.xlsx", # EMG - 22/06

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6612%20PCAT%20ENF%20" + year + "%20V02.xlsx", # ENF - 22/06

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6600%20PCAT%20EPB%20" + year + "%20V02.xlsx", # EPB - 28/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/37%20PCAT%20Cemar%20" + year + "%20V02.xlsx", # EQUATORIAL MA - 28/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/371%20PCAT%20Celpa%20" + year + "%20V02.xlsx", # EQUATORIAL PA - 07/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/38%20PCAT%20Cepisa%20" + year + "%20V02.xlsx", # EQUATORIAL PI - 02/12

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/1000040%20PCAT%20ESS%20(agrupada)%20" + year + "%20V02.xlsx", # ESS - 12/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/32%20PCAT%20ETO%20" + year + "%20V02.xlsx", # ETO - 04/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/83%20PCAT%20Forcel%20" + year + "%20V02.xlsx", # FORCEL - 26/08

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/399%20PCAT%20Hidropan%20" + year + "%20V02.xlsx", # HIDROPAN - 22/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/401%20PCAT%20MuxEnergia%20" + year + "%20V02.xlsx", # MUXENERGIA - 22/07

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/1000042%20PCAT%20RGE%20(agrupada)%20" + year + "%20V02.xlsx", # RGE SUL - 19/06

        "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/46%20PCAT%20Sulgipe%20" + year + "%20V02.xlsx", # SULGIPE - 22/05
    
    ] 

        for url in URL_2021:
                driver.get(url)
        year_21 += 1
        # handle new files

    time.sleep(TIME_SLEEP)
    driver.close();

def replace_file():
    # get file ID at begining of file's name
    for file in file_path:
        file_name.append(Path(file).stem.split('.')[0].rstrip())
    file_id = [file.split()[0] for file in file_name]

    fileid = []
    dups = []
    #matches = []
    for id in file_id:
        if not id.startswith('PCAT'):
            id_int = int(id)
            fileid.append(id_int)
        dups = set([x for x in file_id if file_id.count(x) > 1])

    # create a dictionary to hold the original idx
    idx_dict = dict((k,i) for i,k in enumerate(fileid)) 
    # try to find for duplicated ID's
    # find corresponding idx for intersection of the two lists
    # buils set of matches
    matches = set(dups).intersection(file_id)
    list(matches)
    num_match = []
    for match in matches:
        num_match.append(int(match))
    # get list of idx
    idx = [idx_dict[id] for id in num_match]
    for indice in idx:
        os.remove(FILES2 + '\\' + file_name[indice - 1] + '.xlsx')

def rename():    
    for file in file_path:
        file_name.append(Path(file).stem.split('.')[0].rstrip()) # rstrip() - ignore last white spaces
    
    year = []
    name = []
    file_count = []
    year_count = []
    # condition: ID is 5697 - Celesc_D
    for tarifa in file_name:
        # str ends with 'V02'
        if tarifa.endswith('V02'):
            # str backwards
            str = tarifa[::-1]
            # [start_position, stop_position]
            year.append(str[4:8][::-1]) # reverse str from backwards
            print(year)
            name.append(re.search(r'(?<=PCAT )\w+', tarifa).group(0))
            #file_count.append(tarifa)
            #year_count.append(year)
        # str starts with 'PCAT'
        elif tarifa.startswith('PCAT'):
            year.append(tarifa[-4:])
            print(year)
            file_count.append(tarifa)
            # handle [name]_2021
            name_year = re.search(r'(?<=PCAT_)\w+', tarifa).group(0)
            only_name = name_year[:-5] # get all but the last 5 char
            name.append(only_name)
            
        # condition: str don't end with 'V02'
        else:
            year.append(tarifa[-4:])
            print(year)
            file_count.append(tarifa)
            name.append(re.search(r'(?<=PCAT )\w+', tarifa).group(0))
        # [file_name] and [year] must match
    print('a')
        # date - associate year to full date
# list of dates ordered by [file_name]

## final file name [Name].[yyyy]-[mm]-[dd]
'''date = []
full_date = []
for y in year'''

date = ['07-12', '06-19', '11-22', '09-30', '07-30', '07-30', '07-30', '12-13', '07-30', '07-30', '06-24', '08-29', '10-23', '12/13', '07-04', '07-30', '07-30', '12-13',
'08-28', '11-01', '08-07', '12-02', '08-07', '07-22', '07-22', '07-22', '05-22', '05-29', '07-30', '11-22', '07-30', '04-29', '04-29', '07-30', '11-30', '09-30', '09-30',
'09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '09-30', '05-29', '04-29', '11-30', '05-29', '11-30',
'08-22', '11-22', '07-30', '10-22', '06-22', '08-28', '07-30', '11-30', '06-22', '09-30', '09-30', '09-30', '11-01', '07-30', '05-29', '09-30', '06-29', '08-26', '08-29',
'08-29', '08-29', '07-22', '11-22', '11-22', '12-22']
