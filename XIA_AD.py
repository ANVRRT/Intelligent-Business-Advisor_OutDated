import pandas as pd
import numpy as np
import os
import sys

from p_func import mis_librerias as pf


class multi_ad:
    def categoria_multi(ruta):
        i=1
        arch=pd.read_csv('./Supuestosgenerales/Generales/Categorias/categorias.csv')
        arch.pop("J1")
        arch.pop("J2")
        for i in range (1,6):
            arch[f"Año {i}"]=""
            for j in range (0,len(arch)):
                arch.loc[j,f'Año {i}']='0'    

        arch.to_csv(f"{ruta}", index=False)

    

    def del_row(cat,ruta):
        arch=pd.read_csv(f'{ruta}')
        for i in range (1,6):
            arch.loc[cat-1,f'Año {i}']='0.0'
        arch.to_csv(f"{ruta}", index=False)
    
    def multi_anios(cat,anio,val,ruta):
        #

        arch=pd.read_csv(f'{ruta}')
        arch.loc[cat-1,f'Año {anio}']=val
            
        arch.to_csv(f"{ruta}", index=False)
    
    def multi_sueldos(ruta,titulo,cat,val):
        arch=open(f"{ruta}","a")
        filesize=os.path.getsize(f"{ruta}")
        if (filesize==0):
            reginit=f"{titulo}"+","+"Año 1"+","+"Año 2"+","+"Año 3"+","+"Año 4"+","+"Año 5"+"\n"
            arch.write(reginit)
        reg=f"{cat}"+","+str(val[0])+","+str(val[1])+","+str(val[2])+","+str(val[3])+","+str(val[4])+"\n"
        arch.write(reg)
        arch.close()

        

class categorias_ad:
  
    def grabar_archivo(num,J1,J2):
        
        reg=str(num)+","+J1+","+J2+"\n"
        arch=open("./Supuestosgenerales/Generales/Categorias/categorias.csv","a")
        filesize=os.path.getsize("./Supuestosgenerales/Generales/Categorias/categorias.csv")
        if (filesize==0):
            reginit="CATEGORÍA"+","+"J1"+","+"J2"+"\n"
            arch.write(reginit)
        arch.write(reg)
        arch.close()

    def editar_categoria(num,J1,J2):
        arch=open("./Supuestosgenerales/Generales/Categorias/categorias.csv","r")
      
        
        for reg in arch.readlines():
            ren=reg.split(",")
            
            if ren[0]==str(num):
                arch.close()
                
                arch2=pd.read_csv('./Supuestosgenerales/Generales/Categorias/categorias.csv')
                
                
                arch2.loc[(num-1),'J1']=J1
                arch2.loc[(num-1),'J2']=J2
                
                arch2.to_csv("./Supuestosgenerales/Generales/Categorias/categorias.csv",index=False)
                
                break

class inflacion_ad:

    def categoria_gastos(cat,anio,val):
        arch=open("./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv","a")
        filesize=os.path.getsize("./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv")
        
        if (filesize==0):
            reginit="CATEGORÍA"+","+"Año 1"+","+"Año 2"+","+"Año 3"+","+"Año 4"+","+"Año 5"+"\n"
            reg2="Gastos_Adm"+"\n"
            reg3="Sueldos"+"\n"
            arch.write(reginit)
            arch.write(reg2)
            arch.write(reg3)
            arch.close()
            arch=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
            
            for i in range(1,6):
                arch.loc[:,f'Año {i}']='0'
            arch.to_csv("./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv", index=False)
        
        arch=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
        if (cat=="Gastos_Adm"): ind=0
        if (cat=="Sueldos"): ind=1
        arch.loc[ind,f'Año {anio}']=val
        arch.to_csv("./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv", index=False)

    

    def del_row2(cat):
        arch=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
        if (cat=="Gastos_Adm"): ind=0
        if (cat=="Sueldos"): ind=1
        for i in range (1,6):
            arch.loc[ind,f'Año {i}']='0.0'
        arch.to_csv("./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv", index=False)

class impuestos:
    def categoria_impuestos():
        arch=open("./Supuestosgenerales/Generales/Impuestos/impuestos.csv","a")
        filesize=os.path.getsize("./Supuestosgenerales/Generales/Impuestos/impuestos.csv")
        if (filesize==0):
            reginit="IMPUESTOS"+","+"J1"+"\n"
            arch.write(reginit)
            reg1="ISR"+"\n"
            reg2="PTU"+"\n"
            arch.write(reg1)
            arch.write(reg2)
        arch.close()

    def editar_impuesto(isr,ptu):
        arch=pd.read_csv('./Supuestosgenerales/Generales/Impuestos/impuestos.csv')
        arch.loc[0,'J1']=isr
        arch.loc[1,'J1']=ptu
        arch.to_csv("./Supuestosgenerales/Generales/Impuestos/impuestos.csv", index=False)

class costos_gastos:
    def calcular(cat,valor):
        arch_inflacion=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_costos.csv')
        arch_costosventas=pd.read_csv('./Supuestosgenerales/Costosygastos/Costos_ventas/costos_ventas.csv')

        arch_costosventas.loc[cat-1,'Año 1']=valor
        for i in range (2,6):
            pinflacion=arch_inflacion.loc[cat-1,f'Año {i}']

            costo=arch_costosventas.loc[cat-1,f'Año {i-1}']
            
            ncosto=costo*(1+pinflacion)
            
            arch_costosventas.loc[cat-1,f'Año {i}']=ncosto
        arch_costosventas.to_csv("./Supuestosgenerales/Costosygastos/Costos_ventas/costos_ventas.csv", index=False)

class sueldos_salarios:
    def categoria_p(cat,val):
        arch=open("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv","a")
        filesize=os.path.getsize("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv")
        if (filesize==0):
            reginit="TIPO PRESTACIÓN"+","+"J1"+"\n"
            arch.write(reginit)
            reg1="Asimilado"+","+"0.0"+"\n"
            reg2="Empleado"+","+"0.0"+"\n"
            arch.write(reg1)
            arch.write(reg2)
            arch.close()
        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv')
        
        if (cat=="Asimilado"): ind=0
        if (cat=="Empleado"): ind=1
        arch.loc[ind,'J1']=val
            
        arch.to_csv("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv", index=False)

    def del_row(cat):
        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv')
        if (cat=="Asimilado"): ind=0
        if (cat=="Empleado"): ind=1
        
        arch.loc[ind,'J1']='0.0'
        arch.to_csv("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv", index=False)
        
    
    
    def categoria_puestos(opig="",presta="",nom=""):
        arch=open("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv","a")
        filesize=os.path.getsize("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv")
        base=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos_base.csv')
        prestaciones=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv')
        if opig!=9:
            ind=opig-1
            nom=base.loc[ind,'J1']
            presta=base.loc[ind,'J2']
        else:
            if presta=="A":
                ind=0
            elif(presta=="E"):
                ind=1
            presta=prestaciones.loc[ind,'J1']

        if (filesize==0):
            reginit="PUESTO"+","+"J1"+","+"J2"+"\n"

            reg="1"+","+str(nom)+","+str(presta)+"\n"
            arch.write(reginit)
            arch.write(reg)
            return(1)
            
        else:
            puestos=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv')
            num=puestos["PUESTO"].iloc[-1]
            num=int(num)+1
            reg=str(num)+","+str(nom)+","+str(presta)+"\n"
            arch.write(reg)
            arch.close()
            return(num)
    


    def del_row2(cat):
        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv')
        arch.drop([cat-1],inplace=True)
        
        arch.to_csv("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv", index=False)
        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv')
        
        for i in range (0,len(arch)):
            arch.loc[i,'PUESTO']=str(i+1)
        arch.to_csv("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv", index=False)
    
    def matrices_sueldos(cat,hc,sueldo):
        valores=[]
        #SUELDO BASE
        valores.append(sueldo)
        arch_inflacion=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
        
        for i in range (1,5):
            pinflacion=arch_inflacion.loc[1,f'Año {i+1}']

            sueldo_ant=valores[i-1]
            
            
            nsueldo=sueldo_ant*(1+pinflacion)
            
            valores.append(nsueldo)
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/sueldos_base.csv","SUELDO_BASE",cat,valores)
        #Termina Sueldo Base

        

        #Empieza Prestaciones
        valores=[]
        arch_sueldobase=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/sueldos_base.csv')
        arch_prestacion=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv')
        prest=arch_prestacion.loc[cat-1,'J2']

        for i in range (0,5):
            
            sueldo=arch_sueldobase.loc[cat-1,f'Año {i+1}']
            valores.append(sueldo*prest)
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/prestaciones.csv","PRESTACIONES",cat,valores)

        #Termina Prestaciones

        #Empieza HEADCOUNT
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/headcount.csv","HEADCOUNT",cat,hc)
        #Termina HEADCOUNT

        #Empieza Sueldo_Mensual
        valores=[]
        arch_prestacion=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/prestaciones.csv')
        for i in range (0,5):
            
            sueldo=arch_sueldobase.loc[cat-1,f'Año {i+1}']
            prestacion=arch_prestacion.loc[cat-1,f'Año {i+1}']
            valores.append((sueldo+prestacion)*hc[i])
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/sueldo_mensual.csv","SUELDO_MENSUAL",cat,valores)

        #Termina Sueldo_Mensual

        #Empieza Nomina
        try:
            os.remove("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Nomina/nomina.csv")
        except:
            pass
        arch_sueldo_mensual=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/sueldo_mensual.csv')
        valores=[]
        sumatoria=0
        for i in range (1,6):
            
            for j in range (0,len(arch_sueldo_mensual)):
                x=arch_sueldo_mensual.loc[j,f'Año {i}']
                sumatoria=sumatoria+x  
            valores.append(sumatoria)
            sumatoria=0

        

        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Nomina/nomina.csv","NOMINA",1,valores)
        valores2=(np.array(valores))*12
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Sueldos_salarios/Nomina/nomina.csv","NOMINA",2,valores2)

        #TERMINA NOMINA

class administrativos:
    def categoria_admin(opig="",detalle="",nom="",ruta="",ruta_base="",titulo=""):
        arch=open(f"{ruta}","a")
        filesize=os.path.getsize(f"{ruta}")
        base=pd.read_csv(f'{ruta_base}')
        if titulo=="CATEGORÍA":
            if opig!=16:
                ind=opig-1
                nom=base.loc[ind,'J1']
                detalle=base.loc[ind,'J2']
        else:
            if opig!=9:
                ind=opig-1
                nom=base.loc[ind,'J1']
                detalle=base.loc[ind,'J2']
        



        if (filesize==0):
            reginit=f"{titulo}"+","+"J1"+","+"J2"+"\n"

            reg="1"+","+nom+","+detalle+"\n"
            arch.write(reginit)
            arch.write(reg)
            return(1)
            
        else:
            puestos=pd.read_csv(f'{ruta}')
            num=puestos[f"{titulo}"].iloc[-1]
            num=int(num)+1
            reg=str(num)+","+str(nom)+","+str(detalle)+"\n"
            arch.write(reg)
            arch.close()
            return(num)
    def del_row(cat):
        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/gastos.csv')
        arch.drop([cat-1],inplace=True)
        
        arch.to_csv("./Supuestosgenerales/Costosygastos/Administrativos/gastos.csv", index=False)
        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/gastos.csv')
        
        for i in range (0,len(arch)):
            arch.loc[i,'CATEGORÍA']=str(i+1)
        arch.to_csv("./Supuestosgenerales/Costosygastos/Administrativos/gastos.csv", index=False)

    def matrices_gastos(cat,costo):
        valores=[]
        #GASTOS ADMIN
        valores.append(costo)
        arch_inflacion=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
        
        for i in range (1,5):
            pinflacion=arch_inflacion.loc[0,f'Año {i+1}']

            sueldo_ant=valores[i-1]
            
            
            nsueldo=sueldo_ant*(1+pinflacion)
            
            valores.append(nsueldo)
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Administrativos/gastos_admin.csv","GASTOS_ADMIN",cat,valores)
        #Termina GASTOS ADMIN

        #Empieza TOTAL ADMIN
        try:
            os.remove("./Supuestosgenerales/Costosygastos/Administrativos/total_admin.csv")
        except:
            pass
        arch_gastos=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/gastos_admin.csv')
        valores=[]
        sumatoria=0
        for i in range (1,6):
            
            for j in range (0,len(arch_gastos)):
                x=arch_gastos.loc[j,f'Año {i}']
                sumatoria=sumatoria+x  
            valores.append(sumatoria)
            sumatoria=0

        

        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Administrativos/total_admin.csv","TOTAL_ADMIN",1,valores)

        valores2=(np.array(valores))*12
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Administrativos/total_admin.csv","TOTAL_ADMIN",2,valores2)

        #TERMINA TOTAL ADMIN
    def matrices_gastos_venta(cat,costo):
        valores=[]
        #GASTOS ADMIN
        valores.append(costo)
        arch_inflacion=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
        
        for i in range (1,5):
            pinflacion=arch_inflacion.loc[0,f'Año {i+1}']

            sueldo_ant=valores[i-1]
            
            
            nsueldo=sueldo_ant*(1+pinflacion)
            
            valores.append(nsueldo)
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Gastos_ventas/gastos_ventas.csv","GASTOS_VENTAS",cat,valores)
        #Termina GASTOS ADMIN

        #Empieza TOTAL ADMIN
        try:
            os.remove("./Supuestosgenerales/Costosygastos/Gastos_ventas/total_ventas.csv")
        except:
            pass
        arch_gastos=pd.read_csv('./Supuestosgenerales/Costosygastos/Gastos_ventas/gastos_ventas.csv')
        valores=[]
        sumatoria=0
        for i in range (1,6):
            
            for j in range (0,len(arch_gastos)):
                x=arch_gastos.loc[j,f'Año {i}']
                sumatoria=sumatoria+x  
            valores.append(sumatoria)
            sumatoria=0

        

        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Gastos_ventas/total_ventas.csv","TOTAL_VENTAS",1,valores)

        valores2=(np.array(valores))*12
        mad.multi_sueldos("./Supuestosgenerales/Costosygastos/Gastos_ventas/total_ventas.csv","TOTAL_VENTAS",2,valores2)

        #TERMINA TOTAL ADMIN




        
        
mad=multi_ad
        
            