from PubMedScraper import PubMedScraper
from MeshOnDemand import MeshOnDemand
import os
import numpy as np


if __name__ == '__main__':
    # mash on demand
    print("searching in meshOnDemand")

    mesh = MeshOnDemand(internet_browser='firefox')
    keywords = mesh.get_keywords('60 years old, man, has constant and high pain in the heart, is short of breath, weighs 70 kilos, has diabetes of 130 mg/dl, suffered an acute myocardial infarction and the patient has an ST segment elevation of 2 mm .')

    print(keywords)

    # PubMed
    print("searching in PubMed")
    scraper = PubMedScraper(os.getcwd(), internet_browser='firefox')
    scraper.search_all_keywords(keywords)

    print(scraper.papers_titles)

