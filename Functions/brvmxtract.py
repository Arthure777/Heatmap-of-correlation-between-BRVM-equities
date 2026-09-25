import brvmfinance as bf           #On importe brvmfinance afin d'accéder aux données financières de la BRVM
import matplotlib.pyplot as plt    #On importe matplotlib.pyplot afin de visualiser les données financières de la BRVM
import pandas as pd                #On importe pandas afin de gérer les Data Frames des données financières
import seaborn as sns              #On importe seaborn afin de visualiser nos données de manière plus esthétique

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



def mtr_corr(tickers : list[str], time : int, OHLC : str = "Close", map : bool = True) -> pd.DataFrame :

    # On télécharge l'historique des tickers et on le stocke dans un dataframe
    df = download_tickers(tickers, time, OHLC = OHLC)

    if map == True :
        heatmap = sns.heatmap(df.corr(), annot=True, cmap="coolwarm", center=0, vmin = -1, vmax = 1)
        heatmap.set_title("Matrice de corrélation :")
        return heatmap
    else :
        return df.corr()