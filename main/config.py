import os

FILES = os.getcwd() + "\\files"
CHROMEDRIVER = os.path.dirname(os.getcwd()) + "\\Tarifas\\chromedriver\\chromedriver.exe" # fix

'''
URL = [
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7019%20PCAT%20AmE%20" + year + "%20V02.xlsx", # AME - 01/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/370%20PCAT%20Roraima%20Energia%20" + year + "%20V02.xlsx", # Boa Vista - 01/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/11825 PCAT Castro-DIS 2021 V02.xlsx", ## Castro-DIS - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/31 PCAT CEA 2021 V02.xlsx", ## CEA - 13/12
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5160%20PCAT%20CEB-DIS%202020%20V021.xlsx", # CEBDIS 22/10
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5381%20PCAT%20Cedrap%202021%20V02.xlsx", # CEDRAP - 30/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5366%20PCAT%20Cedri%202021.xlsx", # CEDRI - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5707%20PCAT%20CEEE-D%202021%20V02.xlsx", # CEE-D - 22/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5356%20PCAT%20Cegero%202021.xlsx", # CECEGRO - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5372%20PCAT%20Cejama%202021.xlsx", # CEJAMA - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5697%20PCAT%20Celesc_D%20%20RTP%202021.xlsx", # CELESC-DIS - 22/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5343%20PCAT%20CELETRO%202021%20V02.xlsx", # CELETRO - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6072%20PCAT%20Enel%20GO%202021%20V02.xlsx", # CELG-D -> Enel - GO - 22/10
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/43%20PCAT%20Celpe%202022%20V02.xlsx", # CELPE - 29/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/4950%20PCAT%20Cemig-D%202021%20V021.xlsx", # CEMIG-D - 29/05
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7467%20PCAT%20Cemirim%202021%20V02%20.xlsx", # CEMIRIM - 29/05
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_Ceprag_2021.xls", ## CEPRAG - 22/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6897%20PCAT%20Cera%C3%A7a%202021.xlsx", # CERAÇA - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5351%20PCAT%20Ceral%20Anit%C3%A1polis%202018%20V02.xlsx", # CERAL 1 - 30/10
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5351%20PCAT%20Ceral%20Anit%C3%A1polis%202020%20V02.xlsx", # CERAL 2 - 30/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5351%20PCAT%20Ceral%20Anit%C3%A1polis%202021%20V02.xlsx", # CERAL-DIS - 30/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6898%20PCAT%20Cerbranorte%202021%20V02.xlsx", # CERBRANORTE - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5279%20PCAT%20CERCI%202021%20V02.xlsx", # CERCI - 29/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5377%20PCAT%20Cercos%202021%20V02.xlsx", # CERCOS - 29/05
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5352%20PCAT%20Cerej%202021.xlsx", # CEREJ - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5274%20PCAT%20Ceres%202021%20V02.xlsx", # CERES - 29/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/504%20PCAT%20Cerfox%202021%20V02.xlsx", # CERFOX - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5353%20PCAT%20Cergal%202021%20V02.xlsx", # CERGAL - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5355%20PCAT%20Cergapa%202021%20V02.xlsx", # CERGAPA - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5363%20PCAT%20Cergral%202021%20V02.xlsx", # CERGRAL - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2763%20PCAT%20Ceriluz%202021%20V02.xlsx", # CERILUZ - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5386%20PCAT%20Cerim%202021%20V02.xlsx", # CERIM - 30/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5378%20PCAT%20Ceripa%202021%20V02.xlsx", # CERIPA - 29/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5382%20PCAT%20Ceris%202021%20V02.xlsx", # CERIS - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6610%20PCAT%20CERMC%202021%20V02.xlsx", # CERMC 1 - 30/11/2021
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6610%20PCAT%20CERMC%202020%20V02.xlsx", # CERMC 2 - 30/11/2020
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2381%20PCAT%20Cermiss%C3%B5es%202021%20V02.xlsx", # CERMISSÕES - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5364%20PCAT%20Cermoful%202021%20V02.xlsx", # CERMOFUL - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6609%20PCAT%20Cernhe%202021%20V02.xlsx", # CERNHE - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/369%20PCAT%20Ceron%202021%20V02.xlsx", # CERON - 13/12
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5365%20PCAT%20Cerpalo%202021.xlsx", # CERPALO - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5384%20PCAT%20Cerpro%202021%20V02.xlsx", # CERPRO - 29/05
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_CERR_2013.xlsx", ### CEER - 01/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5385%20PCAT%20CERRP%202021%20V02.xlsx", # CERRP - 29/05
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7883%20PCAT%20Cersad%202021%20V02.xlsx", # CERSAD DISTRIBUIDORA - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5368%20PCAT%20Cersul%202021%20V02.xlsx", # CERSUL - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/3223%20PCAT%20Certaja%202021%20V02.xlsx", # CERTAJA - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7371%20PCAT%20Certel%202021%20V02.xlsx", # CERTEL - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/527%20PCAT%20Certhil%202021%20V02.xlsx", # CERTHIL - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5369%20PCAT%20Certrel%202021.xlsx", # CERTREL - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5375%20PCAT%20Cervam%202021.xlsx", # CERVAM - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5379%20PCAT%20Cetril%202021%20V02.xlsx", # CETRIL - 30/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20174.xlsx", # CFLO - 12/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/103%20PCAT%20Chesp%202021%20V02.xlsx", # CHESP - 22/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20171.xlsx", # CNEE - 12/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/82%20PCAT%20Cocel%202021%20V02.xlsx", # COCEL - 29/06
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/11763%20PCAT%20Codesam%202021%20V02.xlsx", # CODESAM - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/47%20PCAT%20Coelba%202022%20V02.xlsx", # COELBA - 22/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5370%20PCAT%20Coopera%202021%20V02.xlsx", # COOPERA - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2904%20PCAT%20Cooperalian%C3%A7a%202021%20V02.xlsx", # COOPERALIANÇA - 29/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5371%20PCAT%20Coopercocal%202021%20V02.xlsx", # COOPERCOCAL - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/3627%20PCAT%20Cooperluz%202021%20V02.xlsx", # COOPERLUZ - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5373%20PCAT%20Coopermila%202021.xlsx", # COOPERMILA - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_Coopernorte_2021.xlsx", # COOPERNORTE - 22/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_Coopersul_2021.xlsx", # COOPERSUL - 22/12
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/5374%20PCAT%20Cooperzem%202021%20V02.xlsx", # COOPERZEM - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/7016%20PCAT%20Coorsel%202021%20V02.xlsx", # COORSEL - 30/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2866%20PCAT%20Copel-DIS%202021%20V02.xlsx", # COPEL-DIS - 24/06
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2351%20PCAT%20Coprel%202021%20V02.xlsx", # COPREL - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/40%20PCAT%20Cosern%202022%20V02.xlsx", # COSERN - 22/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/SPARTA_SANTA_CRUZ_2018.xlsx", # CPFL JAGUARI - 22/03
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_NSC_20181.xlsx", # CPFL LESTE PAULISTA - 22/03
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_NSC_20182.xlsx", # CPFL MOOCA - 22/03
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2937%20PCAT%20CPFL%20Piratininga%202021%20V02.xlsx", # CPFL PIRATININGA - 23/10
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_CPFL%20Santa%20Cruz_2022.xlsx", # CPFL SANTA CRUZ - 22/03
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_NSC_20184.xlsx", # CPFL SUL PAULISTA - 22/03
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/63%20PCAT%20CPFL%20Paulista%202022%20V02.xlsx", # CPFL PAULISTA - 08/40
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/598%20PCAT%20Creluz-D%202021%20V02.xlsx", # CRELUZ-D - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/2783%20PCAT%20Creral%202021%20V02.xlsx", # CRERAL - 30/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/87%20PCAT%20Ienergia%202021%20V02.xlsx", # DCELT - 29/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/95%20PCAT%20Demei%202021%20V02.xlsx", # DEMEI - 22/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/51%20PCAT%20DMED%202021%20V02.xlsx", # DMED - 22/11
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6611%20PCAT%20EBO%202022%20V02.xlsx", # EBO - 04/02
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20172.xlsx", # EDEVP - 12/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/380%20PCAT%20EDP%20ES%202021%20V02.xlsx", # EDP ES - 07/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/391%20PCAT%20EDP%20SP%202021%20V02.xlsx", # EDP SP - 23/10
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/PCAT_SuperEner_20173.xlsx", # EEB - 12/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/88%20PCAT%20EFLJC%202021%20V02.xlsx", # EFLJC - 29/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/86%20PCAT%20Eflul%202021%20V02.xlsx", # EFLUL - 29/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/385%20PCAT%20Elektro%202021%20V02.xlsx", # ELEKTRO - 27/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/26%20PCAT%20Eletroacre%202021%20V02.xlsx", # ELETROACRE - 13/12
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/398%20PCAT%20Eletrocar%202021%20V02.xlsx", # ELETROCAR - 22/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/390%20PCAT%20Enel%20SP%202021%20V02.xlsx", # ELETROPAULO - 04/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/381%20PCAT%20ELFSM%202021%20V02.xlsx", # ELFSM - 22/09
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6585%20PCAT%20EMG%202021%20V02.xlsx", # EMG - 22/06
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/404%20PCAT%20EMS%20%202022%20V02.xlsx", # EMS - 16/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/405%20PCAT%20EMT%202022%20V02.xlsx", # EMT - 16/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/39%20PCAT%20Enel%20CE%202022%20V02.xlsx", # Enel - CE - 22/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/383%20PCAT%20Enel%20RJ%202022%20V02.xlsx", # Enel - RJ - 15/03
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6612%20PCAT%20ENF%202021%20V02.xlsx", # ENF - 22/06
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6600%20PCAT%20EPB%202021%20V02.xlsx", # EPB - 28/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/44%20PCAT%20Ceal%202022%20V02.xlsx", # EQUATORIAL AL - 03/05
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/37%20PCAT%20Cemar%202021%20V02.xlsx", # EQUATORIAL MA - 28/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/371%20PCAT%20Celpa%202021%20V02.xlsx", # EQUATORIAL PA - 07/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/38%20PCAT%20Cepisa%202021%20V02.xlsx", # EQUATORIAL PI - 02/12
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/6587%20PCAT%20ESE%202022%20V02.xlsx", # ESE - 22/04
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/1000040%20PCAT%20ESS%20(agrupada)%202021%20V02.xlsx", # ESS - 12/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/32%20PCAT%20ETO%202021%20V02.xlsx", # ETO - 04/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/83%20PCAT%20Forcel%202021%20V02.xlsx", # FORCEL - 26/08
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/399%20PCAT%20Hidropan%202021%20V02.xlsx", # HIDROPAN - 22/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/382%20PCAT%20Light%202022%20V02.xlsx", # LIGHT - 15/03
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/401%20PCAT%20MuxEnergia%202021%20V02.xlsx", # MUXENERGIA - 22/07
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/396%20PCAT%20RGE%20SUL%202019%20V021.xlsx", # RGE - 19/06
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/1000042%20PCAT%20RGE%20(agrupada)%202021%20V02.xlsx", # RGE SUL - 19/06
    "https://www2.aneel.gov.br/aplicacoes/tarifa/arquivo/46%20PCAT%20Sulgipe%202021%20V02.xlsx", # SULGIPE - 22/05
]

'''