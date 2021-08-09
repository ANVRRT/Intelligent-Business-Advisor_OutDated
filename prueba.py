import numpy as np
import pandas as pd
i=1
arch=pd.read_csv('./Supuestosgenerales/Generales/Categorias/categorias.csv')
for i in range (1,6):
    
    arch[f"Año {i}"]=""
    arch.loc[0,f'Año {i}']='0'



arch.to_csv("./Supuestosgenerales/Generales/Categorias/categorias2.csv", index=False)
print(arch)
