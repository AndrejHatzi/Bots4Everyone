import PySimpleGUI as sg
import time
from selenium import webdriver

#in -> dentro da localidade
#near -> perto da localidade
class getValueFromLocations():
    def __init__(self,localizacao, near_or_in, estabelecimento):
        self.localizacao = localizacao;
        self.near_or_in = near_or_in;
        self.estabelecimento = estabelecimento;
    def StartSearch(self):
        driver= webdriver.Firefox()
        driver.get("https://www.google.pt/search?tbm=lcl&q={}+{}+{}".format(self.estabelecimento, self.near_or_in, self.localizacao))
        restos : list = [];
        while True:
            rests=driver.find_elements_by_class_name("dbg0pd")
            print(len(rests))
            i : str;
            #div.QqG1Sd:nth-child(2) > a:nth-child(1)
            for i in rests:
                i.click()
                time.sleep(1)
                try:
                    telefone = driver.find_element_by_class_name("LrzXr.zdqRlf.kno-fv");
                except:
                    continue;
                try:
                    nome = driver.find_element_by_class_name("SPZz6b");
                except:
                    continue;
                '''
                try:
                    #UbRuwe
                    #UbRuwe
                    direct = driver.find_element_by_css_selector('div.QqG1Sd:nth-child(2) > a:nth-child(1)');
                    direct.click()
                    time.sleep(5)
                    link : str = driver.current_url
                    print(link)
                    driver.back()
                except:
                    print("Erro 0")
                '''
                
                restos.append([nome.text,telefone.text, link])
            try:
                btn = driver.find_element_by_css_selector('#pnnext > span:nth-child(2)');
                btn.click();
                time.sleep(3);
            except:
                break;
            print('@a_')
        return restos;
        

layout = [   
          [sg.Text('Localização', size=(15, 1)), sg.InputText('')],      
          [sg.Text('Metodo de Procura'), sg.InputCombo(('near', 'in'), key="procura", size=(20, 1),pad=(15, 0))],
          [sg.Text('Estabelecimento'), sg.InputCombo(('Shops', 'Places', 'DrugStore', 'Restaurants', 'Barber Shop', 'Bicycle Store', 'Car Dealer', 'Movie Theater', 'Museum', 'Music Store', 'Gas Station', 'High School'), key="minecraft", size=(20, 1), pad=(28, 0))],
          [sg.Submit(), sg.Cancel()]      
         ]


window = sg.Window('Descobrir Portugal à Meia Noite').Layout(layout)
while True:
    button, values = window.Read();
    x = getValueFromLocations(values[0], values["procura"], values["minecraft"]).StartSearch()
    print(x);
