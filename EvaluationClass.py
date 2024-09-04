from PubMedScraper import *
from MedicalDecisionTree import *
import pandas
import numpy
import matplotlib.pyplot as plt


def create_gaussian_distribution(database):
    g_distrib = numpy.random.normal(44, 10, 920)
    passo = numpy.arange(1, 300, 1)
    print(passo)
    print(g_distrib)
    # plt.plot(passo, g_distrib)
    # plt.show()

    #database.assign()
    return database


# pd = pandas.read_csv('/Users/lucaslaheras/Downloads/heart_disease_uci.csv')
#
# print(create_gaussian_distribution(2))
#
# g_distrib = numpy.random.normal(44, 10, 920)
# pd.insert(1, "obesity", g_distrib)
#
# pd.insert(1, "bloodpressure", numpy.random.normal(140, 12, 920))
#
# pd.insert(1, "Diabetes", numpy.random.normal(26, 6, 920))
#
# pd.insert(1, "Respiracao", numpy.random.normal(73, 12, 920))


