from p_func import mis_librerias as pf
import pandas as pd
import numpy as np

from XIA_AD import multi_ad as multi_ad
from XIA_AD import categorias_ad as categorias_ad
from XIA_AD import inflacion_ad as inflacion_ad
from XIA_AD import impuestos as impuestos_ad
from XIA_AD import costos_gastos as costos_gastos_ad
from XIA_AD import sueldos_salarios as sueldos_salarios_ad
from XIA_AD import administrativos as administrativos_ad


class Menu:
    def menu_ximulator():
        print("")
        print("*****************************************************")
        print("BIENVENIDO A XIMULATOR")
        print("")
        print("1) Supuestos generales")
        print("2) Inversión y Financiamiento")
        print("3) Proyección financiera")
        print("4) Salir")
        print("")
        print("*****************************************************")
        op=pf.pide_numero("Ingresa el número correspondiente a las opciones mostradas: ", 1,4,"int")
        print("")
        return (op)

class Generales:
    def menu_supuestos():    

    #AQUI EMPIEZA GENERALES

        def menu_generales():

            def categorias():
                op=0
                cont_cat=0
                while op!=5:
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ CATEGORÍAS")
                    print("")
                    print("1) Agregar")
                    print("2) Reporte")
                    print("3) Siguiente")
                    print("4) Editar categoría")
                    print("5) Atrás")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                    pf.clear()
                    if op==1:
                        opc=0
                        while cont_cat<=10 and opc!=5:
                            
                            cont_cat=cont_cat+1 
                            print("")
                            print("*****************************************************")
                            print("MENÚ DEFINICIÓN DE CATEGORÍA")
                            print("")
                            print("1) Activo")
                            print("2) Suscripción")
                            print("3) Publicidad")
                            print("4) PPV")
                            print("5) Salir")   
                            print("")
                            print("*****************************************************")
                            opc=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                            if opc!=5:
                                if opc==1: J1="ACTIVO"
                                if opc==2: J1="SUSCRIPCION"
                                if opc==3: J1="PUBLICIDAD"
                                if opc==4: J1="PPV"                           
                                J2=pf.pide_cadena("Ingresa el nombre de tu categoría :",1,15)
                                J2=J2.upper()
                                reg=J1+(" "*(12-len(J1)))+J2
                                val=pf.validacion(reg,"Tipo        Nombre")
                                if val==1: categorias_ad.grabar_archivo(cont_cat,J1,J2)
                                if val==2: pf.error("Tu categoría ha sido exitosamente eliminada, ingresala nuevamente")
                        if cont_cat>10:
                            pf.error("Se ha llegado al límite de categorías registradas")
                    else:
                        if op==2:
                            try:
                                reporte = pd.read_csv('./Supuestosgenerales/Generales/Categorias/categorias.csv')
                                pf.report(reporte)
                                pf.error("Enter para continuar")
                            except:
                                pf.error("No existe reporte para mostrar")
                        if op==3:
                            
                            return(2)
                        if op==4:
                            num_edit=pf.pide_numero("Escribe el número de categoría que deseas editar: ",1,10,"int")
                            print("*****************************************************")
                            print("ELIGE TIPO DE CATEGORÍA")
                            print("")
                            print("1) Activo")
                            print("2) Suscripción")
                            print("3) Publicidad")
                            print("4) PPV")
                            print("")
                            print("*****************************************************")
                            opc=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                            if opc==1: J1="ACTIVO"
                            if opc==2: J1="SUSCRIPCION"
                            if opc==3: J1="PUBLICIDAD"
                            if opc==4: J1="PPV"
                            J2=pf.pide_cadena("Ingresa el nombre de tu categoría :",1,15)
                            J2=J2.upper()
                            
                            categorias_ad.editar_categoria(num_edit,J1,J2)        
                if op==5:
                    return(1)        
            def inflacion():
                op=0
                while op!=5: 
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ INFLACIÓN")
                    print("")
                    print("1) Costos")
                    print("2) Gastos")
                    print("3) Reporte")
                    print("4) Siguiente")
                    print("5) Atras")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                    pf.clear()
                    if op==1:
                        try:
                            reporte = pd.read_csv('./Supuestosgenerales/Generales/Categorias/categorias.csv')
                            pf.report(reporte)
                            try:
                                veri=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_costos.csv')
                                print("Existe")
                            except:
                                print("No existe")
                                multi_ad.categoria_multi("./Supuestosgenerales/Generales/Inflacion/inflacion_costos.csv")
                        except:
                            pf.error("No existe reporte para mostrar")
                        num_costo=pf.pide_numero("Escribe el número de categoría que deseas agregar costo: ",1,10,"int")
                        for h in range (2,6):
                            anio=pf.pide_numero(f"Ingresa el valor de inflación del año {h} (Ejemplo 0.03) : ",0.0001,1.0,"")
                            multi_ad.multi_anios(num_costo,h,anio,"./Supuestosgenerales/Generales/Inflacion/inflacion_costos.csv")
                        veri=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_costos.csv')
                        val=pf.validacion(veri,"")
                        if val==1: pass
                        if val==2:
                            multi_ad.del_row(num_costo,"./Supuestosgenerales/Generales/Inflacion/inflacion_costos.csv")
                            pf.error(f"Tus costos de la categoría {num_costo} han sido exitosamente eliminados, ingresalos nuevamente")
                    if op==2:
                        
                        opig=0
                        while (opig!=3):
                            pf.clear()
                            print("")
                            print("*****************************************************")
                            print("MENÚ INFLACIÓN GASTOS")
                            print("")
                            print("1) Gastos Administrativos")
                            print("2) Sueldos")
                            print("3) Atras")
                            print("")
                            print("*****************************************************")
                            opig=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,3,"int")
                            pf.clear()
                            if opig==1:
                                print("Ingresa los valores de inflación de los Gastos Administrativos")
                                for h in range (2,6):
                                    anio=pf.pide_numero(f"Ingresa el valor de inflación del año {h} (Ejemplo 0.03) : ",0.0001,1.0,"")
                                    inflacion_ad.categoria_gastos("Gastos_Adm",h,anio)
                                    
                                veri=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
                                val=pf.validacion(veri,"")
                                if val==1: pass
                                if val==2:
                                    inflacion_ad.del_row2("Gastos_Adm")
                                    pf.error(f"Tus Gastos_Administrativos han sido exitosamente eliminados, ingresalos nuevamente")    
                            if opig==2:
                                print("Ingresa los valores de inflación de los Sueldos")
                                for h in range (2,6):
                                    anio=pf.pide_numero(f"Ingresa el valor de inflación del año {h} (Ejemplo 0.03) : ",0.0001,1.0,"")
                                    inflacion_ad.categoria_gastos("Sueldos",h,anio)
                                    
                                veri=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
                                val=pf.validacion(veri,"")
                                if val==1: pass
                                if val==2:
                                    inflacion_ad.del_row2("Sueldos")
                                    pf.error(f"Tus Sueldos han sido exitosamente eliminados, ingresalos nuevamente")
                    if op==3:
                        try:
                            reporte1=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_costos.csv')
                            reporte2=pd.read_csv('./Supuestosgenerales/Generales/Inflacion/inflacion_gastos.csv')
                            print("*****************************************************")
                            print("REPORTE INFLACIÓN COSTOS")
                            print("")
                            pf.report(reporte1)
                            print("*****************************************************") 
                            print("REPORTE INFLACIÓN GASTOS")
                            print("")
                            pf.report(reporte2)
                            print("*****************************************************")
                            pf.error("Enter para continuar")
                        except:
                            pf.error("No existe reporte para mostrar")
                    if op==4: 
                        return(3)
            def incremento_ventas():
                op=0
                while op!=4:
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ CRECIMIENTO VENTAS")
                    print("")
                    print("1) Agregar")
                    print("2) Reporte")
                    print("3) Siguiente")
                    print("4) Atras")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,4,"int")
                    pf.clear()
                    if op==1:
                        try:
                            reporte = pd.read_csv('./Supuestosgenerales/Generales/Categorias/categorias.csv')
                            pf.report(reporte)
                            try:
                                veri=pd.read_csv('./Supuestosgenerales/Generales/Incrementoventas/tasas_ventas.csv')
                                print("Existe")
                            except:
                                print("No existe")
                                multi_ad.categoria_multi("./Supuestosgenerales/Generales/Incrementoventas/tasas_ventas.csv")
                        except:
                            pf.error("No existe reporte para mostrar")
                        num_costo=pf.pide_numero("Escribe el número de categoría que deseas agregar tasa de crecimiento: ",1,10,"int")
                        for h in range (2,6):
                            anio=pf.pide_numero(f"Ingresa el valor de inflación del año {h} (Ejemplo 0.03) : ",0.0001,1.0,"")
                            multi_ad.multi_anios(num_costo,h,anio,"./Supuestosgenerales/Generales/Incrementoventas/tasas_ventas.csv")
                        veri=pd.read_csv('./Supuestosgenerales/Generales/Incrementoventas/tasas_ventas.csv')
                        val=pf.validacion(veri,"")
                        if val==1: pass
                        if val==2:
                            multi_ad.del_row(num_costo,"./Supuestosgenerales/Generales/Incrementoventas/tasas_ventas.csv")
                            pf.error(f"Tus costos de la categoría {num_costo} han sido exitosamente eliminados, ingresalos nuevamente")
                    if op==2:
                        try:
                            reporte = pd.read_csv('./Supuestosgenerales/Generales/Incrementoventas/tasas_ventas.csv')
                            pf.report(reporte)
                            pf.error("Enter para continuar")
                        except:
                            pf.error("No existe reporte para mostrar")
                    if op==3:
                        return(4)
            def impuestos():
                op=0
                while op!=5:
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ IMPUESTOS")
                    print("")
                    print("1) Impuestos y PTU")
                    print("2) Tasa de Cambio")
                    print("3) Dividendos")
                    print("4) Reporte")
                    print("5) Atras")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                    pf.clear()
                    if op==1:
                        try:
                            reporte = pd.read_csv('./Supuestosgenerales/Generales/Impuestos/impuestos.csv')
                            pf.report(reporte)
                        except:
                            impuestos_ad.categoria_impuestos()
                        ISR=pf.pide_numero(f"Ingresa el valor del impueso ISR :",0.0001,1.0,"")

                        PTU=pf.pide_numero(f"Ingresa el valor del impueso PTU :",0.0001,1.0,"")
                        impuestos_ad.editar_impuesto(ISR,PTU)
                    if op==4:
                        try:
                            reporte = pd.read_csv('./Supuestosgenerales/Generales/Impuestos/impuestos.csv')
                            pf.report(reporte)
                            pf.error("Enter para continuar")
                        except:
                            pf.error("No existe reporte para mostrar")
            op=0
            while op!=5:
                pf.clear()
                print("")
                print("*****************************************************")
                print("MENÚ GENERALES")
                print("")
                print("1) Categorías")
                print("2) Inflación de costos y gastos")
                print("3) Incremento de ventas")
                print("4) Impuestos/Dividendos/TC")
                print("5) Regresar")
                print("")
                print("*****************************************************")
                op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                pf.clear()
                if op==1:
                    op=categorias()
                    
                    if op==2:
                        pf.error("Enter para continuar a inflación de costos y gastos")
                    
                if op==2:
                    op=inflacion()
                    if op==3:
                        pf.error("Enter para continuar a incremento de ventas")
                    
                if op==3:
                    op=incremento_ventas()
                    if op==4:
                        pf.error("Enter para continuar a impuestos/Dividendos/TC")
                    
                if op==4:
                    impuestos()
                    print("Usted ha terminado la sección de 'Generales' ")
                    pf.error("Enter para continuar")
                    
        def costos_gastos():
            def costos_ventas():
                try:
                    reporte = pd.read_csv('./Supuestosgenerales/Costosygastos/Costos_ventas/costos_ventas.csv')
                    
                except:
                    multi_ad.categoria_multi("./Supuestosgenerales/Costosygastos/Costos_ventas/costos_ventas.csv")
                op=0
                while op!=4:
                    print("")
                    print("*****************************************************")
                    print("MENÚ COSTOS DE VENTAS")
                    print("")
                    print("1) Agregar costos")
                    print("2) Reporte")
                    print("3) Siguiente")
                    print("4) Atras")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,4,"int")
                    if op==1:
                        reporte = pd.read_csv('./Supuestosgenerales/Costosygastos/Costos_ventas/costos_ventas.csv')
                        pf.report(reporte)
                        num_costo=pf.pide_numero("Escribe el número de categoría que deseas agregar costo: ",1,10,"int")
                        precio=pf.pide_numero(f"Escribe el costo inicial de la categoría {num_costo} :",0,0,"")
                        costos_gastos_ad.calcular(num_costo,precio)
                    if op==2:
                        try:
                            reporte = pd.read_csv('./Supuestosgenerales/Costosygastos/Costos_ventas/costos_ventas.csv')
                            pf.report(reporte)
                            pf.error("Enter para continuar")
                        except:
                            pf.error("No existe reporte para mostrar")
                    if op==3:
                        return(2)

            def sueldos_salarios():

                def asimil_empleados():

                    def tasas(cat):
                        

                        tasa=pf.pide_numero(f"Ingresa la tasa de {cat} (Ejemplo 0.03) : ",0.0001,1.0,"")
                        sueldos_salarios_ad.categoria_p(cat,tasa)
                        veri=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/tasa_prestacion.csv')
                        val=pf.validacion(veri,"")
                        if val==1: pass
                        if val==2:
                            sueldos_salarios_ad.del_row(cat)
                            pf.error(f"Tus tasa de {cat} han sido exitosamente reestablecida a 0, ingresala nuevamente")
                       

                    opg=0
                    while opg!=4:
                        pf.clear()
                        print("")
                        print("*****************************************************")
                        print("MENÚ TASAS ASIMILADOS Y EMPLEADOS")
                        print("")
                        print("1) Editar tasa asimilados")
                        print("2) Editar tasa empleados")
                        print("3) Siguiente")
                        print("4) Atras")
                        print("")
                        print("*****************************************************")
                        opg=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,4,"int")
                        pf.clear()

                        if opg==1:
                            tasas("Asimilado")

                        if opg==2:
                            tasas("Empleado")
                            
                        if opg==3:
                            return(2)
                def empleos():
                    #AQUI ME QUEDÉ
                    def agregar_puesto():
                        presta="X"
                        nom="X"
                        bases=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos_base.csv')
                        pf.report(bases)
                        print("")
                        opig=pf.pide_numero("Ingresa el número del puesto que deseas agregar: ",1,9,"int")
                        if opig==9: 
                            nom=pf.pide_cadena("Ingresa el nombre de tu puesto :",1,15)
                            nom=nom.upper()
                            presta=pf.pide_cadena("Indica la letra 'A' si es Asimilado, si es Empleado indica 'E' :",1,1)
                            presta= presta.upper()
                        cat=sueldos_salarios_ad.categoria_puestos(opig=opig,presta=presta,nom=nom)
                        sueldo=pf.pide_numero("Ingresa el sueldo del puesto ingresado: ",0,0,"")
                        hc=[]
                        for n in range(1,6):
                            num=pf.pide_numero(f"Ingresa el número de personas en el puesto seleccionado del año {n} : ",0,0,"int")
                            hc.append(num)
                        sueldos_salarios_ad.matrices_sueldos(cat,hc,sueldo)
                    opg=0
                    
                    while opg!=5:
                        pf.clear()
                        print("")
                        print("*****************************************************")
                        print("MENÚ PUESTOS EMPLEOS")
                        print("")
                        print("1) Agregar nuevo puesto")
                        print("2) Eliminar puesto")
                        print("3) Reporte")
                        print("4) Siguiente")
                        print("5) Atras")
                        print("")
                        print("*****************************************************")
                        opg=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                        pf.clear()
                        if opg==1:
                            agregar_puesto()

                        if opg==2:
                            arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv')
                            pf.report(arch)
                            cat=pf.pide_numero("Ingresa el número del puesto que deseas eliminar: ",1,30,"int")
                            sueldos_salarios_ad.del_row2(cat)
                            pf.error("Tu puesto se ha eliminado exitosamente")
                            
                        if opg==3:
                            try:
                                print("*****************************************************")
                                print("Reporte puestos")
                                print("")
                                reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/puestos.csv')
                                pf.report(reporte)
                                print("")
                                print("*****************************************************")
                                print("")
                                print("Reporte Sueldos Base")
                                print("")
                                reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/sueldos_base.csv')
                                pf.report(reporte)
                                print("")
                                print("*****************************************************")
                                print("")
                                print("Reporte Prestaciones")
                                print("")
                                reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Prestaciones/prestaciones.csv')
                                pf.report(reporte)
                                print("")
                                print("*****************************************************")
                                print("")
                                print("Reporte Headcount")
                                print("")
                                reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/headcount.csv')
                                pf.report(reporte)
                                print("")
                                print("*****************************************************")
                                print("")
                                print("Reporte Sueldo Mensual")
                                print("")
                                reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Sueldos/sueldo_mensual.csv')
                                pf.report(reporte)
                                print("")
                                print("*****************************************************")
                                print("")
                                print("Reporte Nomina")
                                print("")
                                reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Sueldos_salarios/Nomina/nomina.csv')
                                pf.report(reporte)
                                print("")
                                print("*****************************************************")
                                pf.error("Enter para continuar")
                            except:
                                pf.error("No existe reporte para mostrar")


                        if opg==4:
                            return(3)
                    

                op=0
                while op!=4:
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ Sueldos_Salarios")
                    print("")
                    print("1) Tasas Asimilados y Empleados")
                    print("2) Puestos empleos")
                    print("3) Siguiente")
                    print("4) Atras")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,4,"int")
                    pf.clear()
                    if op==1:
                        op=asimil_empleados()
                    if op==2:
                        op=empleos()
                        
                    if op==3:
                        return(3)

            def administrativos():
                def agregar_gasto():
                        detalle="X"
                        nom="X"
                        bases=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/gastos_base.csv')
                        pf.report(bases)
                        print("")
                        opig=pf.pide_numero("Ingresa el número del puesto que deseas agregar: ",1,16,"int")
                        if opig==16: 
                            nom=pf.pide_cadena("Ingresa el nombre de tu gasto :",1,15)
                            nom=nom.upper()
                            detalle=pf.pide_cadena("Indica el detalle de tu gasto (MAX 30 CHAR):",1,30)
                            detalle= detalle.upper()
                        cat=administrativos_ad.categoria_admin(opig=opig,detalle=detalle,nom=nom,ruta="./Supuestosgenerales/Costosygastos/Administrativos/gastos.csv",
                                                                ruta_base="./Supuestosgenerales/Costosygastos/Administrativos/gastos_base.csv",titulo="CATEGORÍA")
                        costo=pf.pide_numero("Ingresa el costo del gasto ingresado (MENSUAL): ",0,0,"")
                        
                        
                        administrativos_ad.matrices_gastos(cat,costo)
                op=0
                while op!=5:
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ GASTOS ADMINISTRATIVOS")
                    print("")
                    print("1) Agregar nuevo gasto")
                    print("2) Eliminar gasto")
                    print("3) Reporte")
                    print("4) Siguiente")
                    print("5) Atras")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                    pf.clear()

                    if op==1:
                        op=agregar_gasto()

                    if op==2:
                        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/gastos.csv')
                        pf.report(arch)
                        cat=pf.pide_numero("Ingresa el número del gasto que deseas eliminar: ",1,30,"int")
                        administrativos_ad.del_row(cat)
                        pf.error("Tu puesto se ha eliminado exitosamente")

                    if op==3:
                        try:    
                            print("*****************************************************")
                            print("Reporte gastos")
                            print("")
                            reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/gastos.csv')
                            pf.report(reporte)
                            print("")
                            print("*****************************************************")
                            print("")
                            print("Reporte Gastos Admin")
                            print("")
                            reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/gastos_admin.csv')
                            pf.report(reporte)
                            print("")
                            print("*****************************************************")
                            print("")
                            print("Reporte Total Admin")
                            print("")
                            reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Administrativos/total_admin.csv')
                            pf.report(reporte)
                            print("")
                            pf.error("Enter para continuar")
                        except:
                            pf.error("No existe reporte para mostrar")
                    if op==4:
                        return(4)
            def gastos_ventas():
                def agregar_gasto():
                        detalle="X"
                        nom="X"
                        bases=pd.read_csv('./Supuestosgenerales/Costosygastos/Gastos_ventas/descr_ventas_base.csv')
                        pf.report(bases)
                        print("")
                        opig=pf.pide_numero("Ingresa el número del gasto de venta que deseas agregar: ",1,9,"int")
                        if opig==9: 
                            print("")
                            print("1) VENTAS")
                            print("2) MARKETING")
                            print("3) OTRO")
                            gv=pf.pide_numero("Ingresa el número correspondientes a tu selección de gasto venta: ",1,3,"int")
                            if gv==1: nom="VENTAS"
                            if gv==2: nom="MARKETING"
                            if gv==3: nom=pf.pide_cadena("Ingresa el nombre de tu gasto de venta:",1,15)
                            nom=nom.upper()
                            detalle=pf.pide_cadena("Indica el detalle de tu gasto (MAX 30 CHAR):",1,30)
                            detalle= detalle.upper()
                        cat=administrativos_ad.categoria_admin(opig=opig,detalle=detalle,nom=nom,ruta="./Supuestosgenerales/Costosygastos/Gastos_ventas/descr_ventas.csv",
                                                                ruta_base="./Supuestosgenerales/Costosygastos/Gastos_ventas/descr_ventas_base.csv",titulo="DESCR_VENTAS")
                        costo=pf.pide_numero("Ingresa el costo del gasto de venta ingresado (MENSUAL): ",0,0,"")
                        
                        
                        administrativos_ad.matrices_gastos_venta(cat,costo)
                op=0
                while op!=5:
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ GASTOS ADMINISTRATIVOS")
                    print("")
                    print("1) Agregar nuevo gasto")
                    print("2) Eliminar gasto")
                    print("3) Reporte")
                    print("4) Siguiente")
                    print("5) Atras")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                    pf.clear()

                    if op==1:
                        op=agregar_gasto()

                    if op==2:
                        arch=pd.read_csv('./Supuestosgenerales/Costosygastos/Gastos_ventas/descr_ventas.csv')
                        pf.report(arch)
                        cat=pf.pide_numero("Ingresa el número del gasto de venta que deseas eliminar: ",1,30,"int")
                        administrativos_ad.del_row(cat)
                        pf.error("Tu puesto se ha eliminado exitosamente")

                    if op==3:
                        try:    
                            print("*****************************************************")
                            print("Reporte gastos de venta")
                            print("")
                            reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Gastos_ventas/descr_ventas.csv')
                            pf.report(reporte)
                            print("")
                            print("*****************************************************")
                            print("")
                            print("Reporte Gastos Ventas")
                            print("")
                            reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Gastos_ventas/gastos_ventas.csv')
                            pf.report(reporte)
                            print("")
                            print("*****************************************************")
                            print("")
                            print("Reporte Total Ventas")
                            print("")
                            reporte=pd.read_csv('./Supuestosgenerales/Costosygastos/Gastos_ventas/total_ventas.csv')
                            pf.report(reporte)
                            print("")
                            pf.error("Enter para continuar")
                        except:
                            pf.error("No existe reporte para mostrar")
                    if op==4:
                        return(5)



            op=0
            while op!=5:
                pf.clear()
                print("")
                print("*****************************************************")
                print("MENÚ COSTOS GASTOS")
                print("")
                print("1) Costos de ventas")
                print("2) Sueldos y salarios")
                print("3) Administrativos")
                print("4) Gastos de ventas")
                print("5) Regresar")
                print("")
                print("*****************************************************")
                op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                pf.clear()
  
                if op==1:
                    op=costos_ventas()
                if op==2:
                    op=sueldos_salarios()
                if op==3:
                    op=administrativos()
                if op==4:
                    op=gastos_ventas()
        def ingresos():

            def precios(): 

                def precios_unidadesventa(accion):
                    try:
                        reporte = pd.read_csv('./Supuestosgenerales/Generales/Categorias/categorias.csv')
                        pf.report(reporte)
                        try:
                            veri=pd.read_csv('./Supuestosgenerales/Ingresos/precios_unitarios.csv')
                        except:
                            multi_ad.categoria_multi("./Supuestosgenerales/Ingresos/precios_unitarios.csv")
                            multi_ad.categoria_multi("./Supuestosgenerales/Ingresos/unidades_vendidas.csv")
                    except:
                        pf.error("No existen categorias para agregar")
                    num_cat=pf.pide_numero(f"Escribe el número de categoría que deseas {accion} el precio y unidades: ",1,10,"int")
                    anio=pf.pide_numero(f"Ingresa el valor de las unidades a vender para el año 1 (Ejemplo 500) : ",0,0,"int")
                    for h in range (1,5):
                        anio=pf.pide_numero(f"Ingresa el valor del precio para el año {h} (Ejemplo 500) : ",0,0,"")
                        multi_ad.multi_anios(num_cat,h,anio,"./Supuestosgenerales/Ingresos/precios_unitarios.csv")

                    veri=pd.read_csv('./Supuestosgenerales/Ingresos/precios_unitarios.csv')
                    val=pf.validacion(veri,"")
                    if val==1: pass
                    if val==2:
                        multi_ad.del_row(num_cat,"./Supuestosgenerales/Ingresos/precios_unitarios.csv")
                        pf.error(f"Tus precios de la categoría {num_cat} han sido exitosamente eliminados, ingresalos nuevamente")



                op=0
                while op!=5:
                    pf.clear()
                    print("")
                    print("*****************************************************")
                    print("MENÚ PRECIOS Y UNIDADES DE VENTA")
                    print("")
                    print("1) Agregar a categoría")
                    print("2) Editar categoría")
                    print("3) Eliminar en categoría")
                    print("4) Reporte")
                    print("5) Regresar")
                    print("")
                    print("*****************************************************")
                    op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,5,"int")
                    pf.clear()
    
                    if op==1:
                        precios_unidadesventa("agregar")
                        






            op=0
            while op!=16:
                pf.clear()
                print("*****************************************************")
                print("MENÚ INGRESOS")
                print("")
                print("1)Precios y Unidades de Venta")
                print("2)Descuentos y comisiones")

                
                op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,3,"int")
                pf.clear()
                if op==1: op= registrar_precios()
                

            

                


        #MENU SUPUESTOS GENERALES
        op=0
        while op!=4:
            pf.clear()
            print("")
            print("*****************************************************")
            print("MENÚ SUPUESTOS GENERALES")
            print("")
            print("1) Generales")
            print("2) Costos y gastos")
            print("3) Ingresos")
            print("4) Regresar")
            print("")
            print("*****************************************************")
            op=pf.pide_numero("Ingresa el número correspondientes a tu selección: ",1,4,"int")
            print("")
            pf.clear()
            if op==1:
                menu_generales()
            if op==2:
                costos_gastos()
            if op==3:
                ingresos()
                
        
        

    


class Inversion:
    def menu_inversion():
        print("")
        print("*****************************************************")
        print("MENÚ INVERSIÓN Y FINANCIAMIENTO")
        print("")
        print("1) Recursos")
        print("2) Depreciación y amortización")
        print("3) Fuentes de financiamiento")
        print("4) Costos financieros")
        print("5) Regresar")
        print("")
        print("*****************************************************")
        op=pf.pide_numero("Ingresa el número correspondientes a tu selección",1,5,"int")
        print("")
        return(op)

class Proyeccion:
    def menu_proyeccion():
        print("")
        print("*****************************************************")
        print("MENÚ PROYECCIÓN FINANCIERA")
        print("")
        print("1) Utilidad bruta")
        print("2) Estado de resultados")
        print("3) Fuentes de efectivo")
        print("4) Indicadores")
        print("5) Regresar")
        print("")
        print("*****************************************************")
        op=pf.pide_numero("Ingresa el número correspondientes a tu selección",1,5,"int")
        print("")
        return(op)

