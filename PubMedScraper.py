import copy
import shutil
import selenium.webdriver.firefox.options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
import platform
import sys
import urllib.request
import random
import time
import zipfile



class PubMedScraper:
    def __init__(self, root_directory, internet_browser='google_chrome'):
        # increase the recursion limit to handle very large searches
        sys.setrecursionlimit(5000)

        # saves current directory in a string
        self.root_directory = root_directory

        # saves current platform in a string
        self.current_platform = platform.system()

        self.directory_driver = ''

        self.driver = []

        self.select_browser(internet_browser)

        self.papers_titles = []
        self.papers_num_search = 0

        self.index_progress_bar = 1

    def select_browser(self, internet_browser):
        if internet_browser == 'google_chrome':
            # options handler for chrome to run Headless
            self.options = selenium.webdriver.chrome.options.Options()
            # self.options.headless = True

            self.driver = webdriver.Chrome(options=self.options)

        elif internet_browser == 'firefox':
            # options handler for Firefox to run Headless
            self.options = selenium.webdriver.firefox.options.Options()
            # self.options.headless = True

            self.driver = webdriver.Firefox(options=self.options)

        elif internet_browser == 'safari':
            self.options = selenium.webdriver.safari.options.Options()
            self.options.headless = True

            self.driver = selenium.webdriver.Safari(options=self.options)

        elif internet_browser == 'edge':
            self.options = selenium.webdriver.edge.options.Options()
            self.options.headless = True

            self.driver = selenium.webdriver.Edge(options=self.options)

    def search_pubmed(self, search_keyword, pages):
        getTitles = True

        self.driver.get('https://pubmed.ncbi.nlm.nih.gov/')
        WebDriverWait(self.driver, 60).until(lambda x: x.find_element(By.XPATH, '//*[@id="search-form"]/div/div[1]/div/button'))
        # print("achou")
        # insert keywords
        self.driver.find_element(By.XPATH, '//*[@id="id_term"]').send_keys(search_keyword)

        # click search button
        try:
            self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[1]/div/button').click()
        except:
            print("erro")
            pass

        try:
            WebDriverWait(self.driver, 30).until(lambda x: x.find_element(By.XPATH, '//*[@id="search-results"]/section/div[2]/div/article[1]/div[2]/div[1]'))
        except:
            getTitles = False
            # try:
            #     WebDriverWait(self.driver, 30).until(lambda x: x.find_element(By.XPATH, '//*[@id="full-view-heading"]/div[2]/div'))
            # except:
            #     pass
            pass


        # print("carregou")

        for it_page in range(1, pages + 1, 1):
            print('seraching page ' + str(it_page))

            for it_article in range(1, 11, 1):
                try:
                    item = self.driver.find_element(By.XPATH, '//*[@id="search-results"]/section/div[2]/div/article[' + str(it_article) + ']/div[2]/div[1]').text
                    self.papers_titles[self.papers_num_search].append(copy.copy(item).split("\n"))

                except:
                    pass

            try:
                self.driver.find_element(By.XPATH, '//*[@id="search-results"]/div[6]/button[3]').click()
                WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="search-results"]'))

            except:
                pass

        #time.sleep(1000000)

    def rewrite(self, word):
        sentence = word.split(" ")
        random.shuffle(sentence)
        for i in range(int(len(sentence)/2)):
            a = random.randint(0, (len(sentence)-1))
            sentence[a] = ""
        sentence = ' '.join(sentence)
        # print(sentence)
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

    def search_all_keywords(self, vet_keywords):
        for keyword in vet_keywords:
            self.papers_titles.append([])
            self.search_pubmed(keyword, 2)
            self.papers_num_search += 1

        # delete duplicates

    # download url items to temp directory
    def download_url_files(self):
        # print("Downloading files")
        name = None

        try:
            # for name, url in self.name2url.items():
            type_file = url[url.rfind('.'):]
            urllib.request.urlretrieve(url, os.path.join(self.temp_directory, name + type_file))
        except:
            # print(name)
            pass

        # time.sleep(100000)