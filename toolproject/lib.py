from datetime import datetime as dt
import pandas

def zodiak_sign():
    print("Veuillez entrer votre date de naissance (type = YYYY-MM-DD) : ")
    birth_str = input()
    birth_date = dt.fromisoformat(birth_str)
    annee = str(birth_date.year)

    if birth_date in pandas.date_range(f'{annee}-03-21', f'{annee}-04-20', freq='D'):
        return print("Tu es un Bélier! Attention t'es un peu tétu")
    elif birth_date in pandas.date_range(f'{annee}-04-21',f"{annee}-05-20", freq='D'):
        return print("Tu es un Taureau!")
    elif birth_date in pandas.date_range(f'{annee}-05-21',f"{annee}-06-21",freq='D'):
        return print("Tu es un Gémeaux!")
    elif birth_date in pandas.date_range(f'{annee}-06-22',f"{annee}-07-23",freq='D'):
        return print("Tu es un Cancer!")
    elif birth_date in pandas.date_range(f'{annee}-07-24',f"{annee}-08-23",freq='D'):
        return print("Tu es un Lion!")
    elif birth_date in pandas.date_range(f'{annee}-08-24',f"{annee}-09-23",freq='D'):
        return print("Tu es un Vierge!")
    elif birth_date in pandas.date_range(f'{annee}-09-24',f"{annee}-10-23",freq='D'):
        return print("Tu es un Balance!")
    elif birth_date in pandas.date_range(f'{annee}-10-24',f"{annee}-11-22",freq='D'):
        return print("Tu es un Scorpion!")
    elif birth_date in pandas.date_range(f'{annee}-11-23',f"{annee}-12-20",freq='D'):
        return print("Tu es un Sagittaire!")
    elif birth_date in pandas.date_range(f'{annee}-12-21',f"{annee}-01-20",freq='D'):
        return print("Tu es un Capricorne!")
    elif birth_date in pandas.date_range(f'{annee}-01-21',f"{annee}-02-19",freq='D'):
        return print("Tu es un Verseau!")
    else:
        return print("Tu es un Poissons!")


zodiak_sign()
