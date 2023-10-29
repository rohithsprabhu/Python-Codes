import csv
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use("fivethirtyeight")
# csv file link :  https://github.com/User-zwj/Pandas-Practice/blob/master/survey_results_public.csv
#with open("survey_results_public.csv") as csv_file:
	#csv_reader = csv.DictReader(csv_file)
data = pd.read_csv('survey_results_public.csv')
ids = data['Respondent']
lang_responses = data['HaveWorkedLanguage']


language_counter = Counter()

for response in lang_responses:
	language_counter.update(str(response).split(';'))
#print(row['HaveWorkedLanguage'])
#row = next(csv_reader)
#using pandas it would be more efficient than matplotlib
languages = []
popularity = []
for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])
languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)

plt.title("Most popular programming languages")
#plt.ylabel("programming languages")
plt.xlabel("Number of people have worked with")
plt.tight_layout()
plt.show()
#print(languages)
#print(popularity)
#print(language_counter)
#print(language_counter.most_common(15))