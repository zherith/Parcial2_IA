import numpy as np
import pandas as pd
from sklearn import preprocessing as pre
from sklearn import linear_model as lm
from sklearn.preprocessing import Normalizer as nm
from sklearn.preprocessing import StandardScaler as sc

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


# cargamos el dataset
dato = pd.read_csv("haberman.csv")

aux = np.array(dato[['edad', 'year', 'auxilia']])


norm = nm().fit(X=aux).fit_transform(X=aux)


standar = sc().fit(X=norm).fit_transform(X=norm)


aux2 = np.array(dato[['supervivencia']])
norm2 = nm().fit(X=aux2).fit_transform(X=aux2)



X_train, X_test, y_train, y_test = train_test_split(standar,
                                                    aux2,
                                                    test_size=0.2,
                                                    random_state=0
                                                    )


pipe = Pipeline([('scaler', StandardScaler()),
                 ('svc', LogisticRegression(random_state=42))])
doge = lm.LogisticRegression(random_state=42)
doge.fit(X_train, y_train)
print("Resultados obtenidos con la regresión logistica ",
      doge.score(X_test, y_test))
print("Predición de esperanza de vida de una mujer con cancer usando pipeline, bajo las siguientes caracteristicas\nedad=30\nAño de Operación = 1960 ",
      "\nGanglios cancerosos encontrados = 23 \nResultado = ", doge.predict([[30, 60, 23]]))
pipe.fit(X_train, y_train)
print("Resultados obtenidos con la regresión logistica usando pipeline",
      pipe.score(X_test, y_test))
print("Predición de esperanza de vida de una mujer con cancer usando pipeline, bajo las siguientes caracteristicas\nedad=30\nAño de Operación = 1960 ",
      "\nGanglios cancerosos encontrados = 23 \nResultado = ", pipe.predict([[30, 60, 23]]))
