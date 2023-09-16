from PubMedScraper import PubMedScraper
import os
import numpy as np

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scraper = PubMedScraper(os.getcwd(), 'firefox')

    # l = [['a', '2'], ['c', '2'], ['a', '2'], ['c', '1']]
    #
    #
    # new_l = np.unique(l).tolist()
    #
    # print(l)
    # print(new_l)

    scraper.search_all_keywords(['cardiac', 'cardiac disease'])

    print(scraper.papers_titles)

