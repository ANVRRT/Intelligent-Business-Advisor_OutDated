import os
class mis_librerias:
    def error(msj):
        
        pausa=input(msj)
        
    def pide_numero(letrero,li,ls,tipo):
        
        while True:
            cad= input(letrero)
            Bandera=True
            try:
                float(cad)
                
            except ValueError:
                Bandera=False
                
            if not Bandera:
                mensaje_error="Error, sólo deben ser dígitos numéricos"
                ml.error(mensaje_error)
                
                
            else:
                if tipo=="int": num=int(cad)
                else: num=float(cad)
                if (ls!=0 and li!=0):
                    if (num<li or num>ls):
                        mensaje_error="Error, el valor debe estar entre "+str(li)+" y "+str(ls)
                        ml.error(mensaje_error)
                        
                    else: return num
                else: return num

            #Termina el ciclo

    def pide_cadena(msj,li,ls):
        bandera_error=True
        while bandera_error:
            bandera_error=False
            print(msj,end="")
            try:   
                x=input()
                if len(x) <li or len(x)>ls:
                    er="ERROR cadena no está entre "+str(li)+" y "+str(ls)+"caracteres"
                    ml.error(er)
                    bandera_error=True
            except:
                ml.error("ERROR, valor vacio o no es numérico")
                bandera_error=True
        return(x)
                

    def validacion(reg,msg):
        print("Indica si lo ingresado es correcto")
        print(msg)
        try:
            blankIndex=[''] * len(reg)
            reg.index=blankIndex
        except:
            pass
        print(reg)
        print("")
        print("1) Si")
        print("2) No")
        op=ml.pide_numero("Ingresa la opción: ",1,2,"int")
        return(op)
        
        
        
                    
        #terminawhile
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def report(reporte):
        blankIndex=[''] * len(reporte)
        reporte.index=blankIndex
        print(reporte)
#PRINCIPAL
ml=mis_librerias

