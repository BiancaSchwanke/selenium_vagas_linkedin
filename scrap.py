# -*- coding: utf-8 -*-
## 1. Todos as importacoes
from selenium import webdriver
from time import sleep


## 2. Todos os parametros
URL_LINKEDIN_DS = 'https://www.linkedin.com/jobs/data-scientist-vagas/?originalSubdomain=br'


## 3. Execucao do codigo
if __name__ == '__main__':
    
    # Criar uma instancia do Google Chrome pelo Selenium.
    driver = webdriver.Chrome()
    
    # Acessou o link do Linkedin
    driver.get(URL_LINKEDIN_DS)
    
    # Pegar lista de vagas de DS
    resultados = driver.find_elements_by_class_name('result-card')
    
    lista_descricoes = []
    
    #Iniciar um While Loop em cima de todos os resultados.
    while True:
        #For loop para pegar descricao.
        for r in resultados[len(lista_descricoes):]:
            r.click()
            sleep(2)
            descricao = driver.find_element_by_class_name('description')
            lista_descricoes.append(descricao.text)
        
        resultados = driver.find_elements_by_class_name('result-card')
    
        if len(lista_descricoes) == len(resultados):
            break
        
    # Salvar os dados.
    print(lista_descricoes)
    descricao_salvar = '\n'.join(lista_descricoes)
    with open('descricao_vagas.txt', 'w') as f:
        f.write(descricao_salvar)
    
    driver.quit()
    
    
    
    
        
  

            
