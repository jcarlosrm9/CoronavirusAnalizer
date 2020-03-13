#CORONAVIRUS ANALIZER VERSION 0.1                   12-03-2020
#DESARROLLADO COMO LABORATORIO PARA DEMOSTRACION DE SCRAPER WEB
#EXTRACCION Y REPRESENTACION DE LOS DATOS VIA SELENIUM
#########################################################################
#SOLO PARA FINES ACADEMICOS Y PRACTICOS
#########################################################################
# CARACTERISTICAS ADICIONALES DEL CODIGO:
#    - UTILIZA Options desde Selenium para trabajar con el browser oculto
#    - Despliega el diccionario con los datos hacia Consola y pyplot
#    - Ventana grafica maximizada
#
#
#    Desarrollado por 
#    Marco Arevalo Zambrano - marevaloz@gmail.com 
#    Linkedin: https://www.linkedin.com/in/marevaloz/

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import matplotlib.pyplot as plt

# Clase Coronavirus
class Coronavirus():
    
    #constructor
    #parametro pais: pais que se desea revisar, String, primera letra en mayuscula, ejemplo: China
    def __init__(self,pais):
        self._pais=pais
        WINDOW_SIZE = "1366,768"
        CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        path_webdriver="c:/chromedriver_win32/chromedriver.exe"
        
        chrome_options = Options()  
        chrome_options.add_argument("--headless")  
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.binary_location = CHROME_PATH

        self.driver = webdriver.Chrome(executable_path=path_webdriver,
                              options=chrome_options)

    #Metodo row_data:
    # Utilizado para obtener fila en forma de array
    #
    #parametro paisFind: pais que se desea extraer desde filas, String, primera letra en mayuscula, ejemplo: China
    #parametro trs: listado de filas (TR) extraidas desde una tabla HTML
    def row_data(self, paisFind,trs):
        rData = []
        for row in trs:
            pais=row.text.split(" ")[0]
            if pais==paisFind:
                rData=row.text.split(" ")
            
        return rData

    #metodo getData:
    #metodo que realiza el proceso de scrapper , y muestra la salida de los datos
    #
    #parametros: ninguno
    def getData(self):

        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries"]/tbody[1]')
        trs=table.find_elements_by_tag_name("tr")
        rData=self.row_data(self._pais,trs)
        listado=[]

        info={}
        info.setdefault("casos_totales",int(rData[1].replace(",","").replace("+","")))
        info.setdefault("nuevos_casos",int(rData[2].replace(",","").replace("+","")))
        info.setdefault("total_fallecidos",int(rData[3].replace(",","").replace("+","")))
        info.setdefault("nuevos_fallecidos",int(rData[4].replace(",","").replace("+","")))
        info.setdefault("casos_activos",int(rData[5].replace(",","").replace("+","")))
        info.setdefault("total_recuperados",int(rData[6].replace(",","").replace("+","")))
        info.setdefault("estado_critico",int(rData[7].replace(",","").replace("+","")))

        print(info)
        fig, ax = plt.subplots()
        ax.set_ylabel('Casos')
        ax.set_title('Estadistica CoVid-19 en '+self._pais)
        plt.bar(range(len(info)), list(info.values()), align='center')
        plt.xticks(range(len(info)), list(info.keys()))
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        self.driver.quit()

        plt.show()


#######################################
#################main##################
#######################################
#
#informacion=Coronavirus("China")
#informacion.getData()
informacion=Coronavirus("China")
informacion.getData()
#informacion=Coronavirus("Chile")
#informacion.getData()