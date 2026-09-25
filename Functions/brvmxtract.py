! python3 -m pip install -r requirements.txt

import brvmfinance as bf           #On importe brvmfinance pour accéder aux données financières de la BRVM
import matplotlib.pyplot as plt    #On importe matplotlib.pyplot pour visualiser les données financières de la BRVM
import pandas as pd                #On importe pandas pour gerer les data-frames des données financières
import seaborn as sns              #On importe seaborn pour visualiser nos données de manière plus esthétique

def download_tickers(tickers : list[str], time : int, pct : bool = True, OHLC : str = "Close") -> pd.DataFrame :
  
    # On crée une liste vide pour stocker les dataframes de chaque ticker
  names = []
    # La boucle for télécharge le dataframe de chaque ticker et l'ajoute à la liste names avec le nom du ticker comme nom de colonne 
  for ticker in tickers :
      tick = bf.Ticker(ticker)

      if pct == True :
        dfi = tick.history(length = time)[OHLC].pct_change()
      else :
         dfi = tick.history(length = time)[OHLC]

      dfi.columns = [ticker]
      names.append(dfi)

    # On concatène les dataframes de chaque ticker en un seul dataframe avec les noms des tickers comme noms de colonnes
  df = pd.concat(names, axis=1)
  df.columns = tickers
    # La sortie sera un dataframe composé formé à partir de l'historique de chaque ticker
  return df

 