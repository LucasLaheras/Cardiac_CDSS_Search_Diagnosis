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

        self.index_progress_bar = 1

    def select_browser(self, internet_browser):
        if internet_browser == 'google_chrome':
            # options handler for chrome to run Headless
            self.options = selenium.webdriver.chrome.options.Options()
            self.options.headless = True

            self.driver = webdriver.Chrome(options=self.options)

        elif internet_browser == 'firefox':
            # options handler for Firefox to run Headless
            self.options = selenium.webdriver.firefox.options.Options()
            self.options.headless = True

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

        self.driver.get('https://pubmed.ncbi.nlm.nih.gov/')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="search-form"]/div/div[1]/div/button'))

        # insert keywords
        self.driver.find_element(By.XPATH, '//*[@id="id_term"]').send_keys(search_keyword)

        # click search button
        self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[1]/div/button').click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="search-results"]'))

        for it_page in range(pages):
            print(it_page)

            for it_article in range(11):
                try:
                    item = self.driver.find_element(By.XPATH, '//*[@id="search-results"]/section[1]/div[1]/div/article[' + str(it_article + 1) + ']/div[2]/div[1]').text
                    self.papers_titles.append(copy.copy(item).split("\n"))

                except:
                    pass

            self.driver.find_element(By.XPATH, '//*[@id="search-results"]/div[6]/button[3]').click()
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="search-results"]'))

    def search_all_keywords(self, vet_keywords):
        for keyword in vet_keywords:
            self.search_pubmed(keyword, 2)

        print(self.papers_titles[0])
        # delete duplicates

    # download url items to temp directory
    def download_url_files(self):
        print("Downloading files")
        name = None

        try:
            for name, url in self.name2url.items():
                type_file = url[url.rfind('.'):]
                urllib.request.urlretrieve(url, os.path.join(self.temp_directory, name + type_file))
        except:
            print(name)
