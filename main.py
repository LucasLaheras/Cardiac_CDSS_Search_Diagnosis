from PubMedScraper import PubMedScraper
from MeshOnDemand import MeshOnDemand
import os
import random
import numpy as np
import MedicalDecisionTree


def swap_random_middle_words(sentence):
    newsentence = list(sentence)

    i, j = random.sample(range(1, len(sentence) - 1), 2)

    newsentence[i], newsentence[j] = newsentence[j], newsentence[i]

    return newsentence
def rewrite(word):
    sentence = word.split(" ")
    random.shuffle(sentence)
    for i in range(int(len(sentence)/2)):
        a = random.randint(0, (len(sentence)-1))
        sentence[a] = ""
    sentence = ' '.join(sentence)
    # sentence = 'Evaluation of ST segment elevation criteria for the prehospital electrocardiographic diagnosis of acute myocardial infarction'

    # self.driver.get('https://pt.semrush.com/goodcontent/paragraph-rewriter/')
    # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH,'//*[@id="srf-skip-to-content"]/section[1]/div[2]/div/div/cmp-paraphrase-generator-form/div/div/div/div/form/div[3]/button'))
    #
    # # insert word
    # self.driver.find_element(By.XPATH, '//*[@id="input"]').send_keys(word)
    # time.sleep(3)
    #
    # # click search button
    # b = self.driver.find_element(By.XPATH, '/html/body/section/div/div[1]/div[2]/button[2]')
    # a = self.driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div[3]/div/section[1]/div[2]/div/div/cmp-paraphrase-generator-form/div/div/div/div/form/div[3]/button')
    # b.click()
    # a.click()
    # time.sleep(10)

    # new_word = self.driver.find_element(By.XPATH, '//*[@id="srf-skip-to-content"]/section[1]/div[2]/div/div/cmp-paraphrase-generator-form/div/div/div/div/div/div[2]/div[2]/p').text

    return sentence

if __name__ == '__main__':
    caracteristics = {'Sex' : 'Men',
                      'years' : 47 ,
                      'weight' : 63,
                      'Acute coronary syndrome (ACS) ST segment elevation' : 0.1 ,
                      'acute instability of atherosclerosis' : True,
                      'pain intensity' : 'médio',
                      'duration of pain per hour of the day' : 1,
                      'shortness of breathe' : False,
                      'The person’s resting blood pressure' : 140,
                      'cholesterol' : 177,
                      'Exercise induced angina' : 0,
                      'slope' : 'downsloping',
                      'desease' : 'myocardial infarction type 2'}

    # caracteristics = {'Sex': 'Woman',
    #                   'years': 34,
    #                   'weight': 71,
    #                   'Acute coronary syndrome (ACS) ST segment elevation': 0.0,
    #                   'acute instability of atherosclerosis': True,
    #                   'pain intensity': 'médio',
    #                   'duration of pain per hour of the day': 1,
    #                   'shortness of breathe': False,
    #                   'The person’s resting blood pressure': 140,
    #                   'cholesterol': 130,
    #                   'Exercise induced angina': 0,
    #                   'slope': 'upsloping'}

    # caracteristics = {'Sex': 'Men',
    #                   'years': 34,
    #                   'weight': 120,
    #                   'Acute coronary syndrome (ACS) ST segment elevation': 0.0,
    #                   'acute instability of atherosclerosis': True,
    #                   'pain intensity': 'médio',
    #                   'duration of pain per hour of the day': 1,
    #                   'shortness of breathe': False,
    #                   'The person’s resting blood pressure': 140,
    #                   'cholesterol': 130,
    #                   'Exercise induced angina': 0,
    #                   'slope': 'downsloping'}


    caracteristicsSearch = ", ".join(str(y) + " " + str(x) for y, x in caracteristics.items())

    print(caracteristicsSearch)

    # size of keyword building minimum 1 and maximum 10
    sizeKeywords = 1

    # define variables
    idexSize = 0
    executedWords = []

    # mash on demand
    print("searching in meshOnDemand")

    mesh = MeshOnDemand(internet_browser='firefox')
    # keywords = mesh.get_keywords('60 years old, man, has constant and high pain in the heart, is short of breath, weighs 70 kilos, has diabetes of 130 mg/dl, suffered an acute myocardial infarction and the patient has an ST segment elevation of 2 mm .')
    keywords = mesh.get_keywords(caracteristicsSearch)

    testid = 0
    for word in keywords:
        if idexSize < sizeKeywords:
            idexSize += 1
            print(word)
            for i in range(5):
                sentence = rewrite(word)
                executedWords.append(sentence)
    print("Palavras chave: ")
    print(executedWords)
    print("\n\n\n")

    # PubMed search
    print("searching in PubMed")
    scraper = PubMedScraper(os.getcwd(), internet_browser='firefox')
    scraper.search_all_keywords(executedWords)

    MedicalDecisionTree.desisionMedicalTree(caracteristics)

    print(scraper.papers_titles)

