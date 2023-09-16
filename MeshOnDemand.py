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


class MeshOnDemand:
    def __init__(self, internet_browser='firefox'):
        # increase the recursion limit to handle very large searches
        sys.setrecursionlimit(5000)

        # saves current platform in a string
        self.current_platform = platform.system()

        self.directory_driver = ''

        self.driver = []

        self.select_browser(internet_browser)

        self.keywords = []

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

    def get_keywords(self, input):
        self.driver.get('https://meshb.nlm.nih.gov/MeSHonDemand?_gl=1*1xwt0c4*_ga*MTU4MzAwNDAyNi4xNjk0NjY2MTg4*_ga_7147EPK006*MTY5NDg4NzQ0My4zLjEuMTY5NDg4NzQ2Mi4wLjAuMA..*_ga_P1FPTH9PL4*MTY5NDg4NzQ0My4zLjEuMTY5NDg4NzQ2Mi4wLjAuMA..')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(By.XPATH, '//*[@id="MODEntry"]'))

        # insert the input
        self.driver.find_element(By.XPATH, '//*[@id="MODEntry"]').send_keys(input)

        # click search button
        self.driver.find_element(By.XPATH, '//*[@id="runMOD"]').click()
        WebDriverWait(self.driver, 120).until(lambda x: x.find_element(By.XPATH, '//*[@id="defaultArticleList"]/li[1]'))

        for i in range(1, 11, 1):

            try:
                item = self.driver.find_element(By.XPATH, '//*[@id="defaultArticleList"]/li[' + str(i) + ']').text
                self.keywords.append(item[:item.rfind('. PMID')])
                # self.keywords.append(item[:20])

            except:
                pass

        self.driver.close()

        return self.keywords

