
from XIA_UI import Menu as ui_menu
from XIA_UI import Generales as ui_generales
from p_func import mis_librerias as pf

op=0
pf.clear()
while op!=4:

    op=ui_menu.menu_ximulator()
    pf.clear()

    if op==1:
        ui_generales.menu_supuestos()
        pf.clear()
       
    if op==2:
        ui.menu_inversion()
    if op==3:
        ui.menu_proyeccion()