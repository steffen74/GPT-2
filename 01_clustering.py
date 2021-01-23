import pandas as pd
import numpy as np
import json
import os





### code for getting the handles, the journal name and the metadata
# setting your personal path
path = r'C:/Users/steve/PycharmProjects/pythonProject1/json'

# initiating the lists for handles, journal name and metadata

os.chdir(path)

metadata = []
abstracts = []
keywords = []
## setting up the list of keywords to filter out the abstracts related to climate change

# 193 abstracts with this keyword list
keyword_list_climate = ['Sustainability', 'sustainability','sustainable development','Sustainable development','Sustainable Development',
                'globalization', 'Globalization',
                'environment', 'Environment'
                'climate change', 'Climate change', 'Climate Change',
                'energy','Energy', 'sustainable development goals' ]
# (116 + 88 + 55 + 43 + 36 + 35 = 373 ) keywords related to management topics
keyword_list_management = ['innovation', 'Innovation', 'entrepreneurship','Entrepreneurship', 'human capital', 'Human capital','Productivity','productivity',
                  'performance','Performance', 'efficiency','Efficiency']

#count = 100
#j = 0
# here we filter only the abstracts which fit a specific keyword
# change keyword_list_climate to a different keyword_list
for item in keyword_list_climate:
    for i in os.listdir():

        with open(i, "r", encoding='utf-8', errors='ignore') as f:
            data = json.load(f)

            handles.append(data['handle'])
            journal_name.append(data['parentCollection']['name'])
    #for obj in data["metadata"]:
     #   if obj["key"] == "dc.description.abstract":
      #      abstracts.append(obj["value"])

    #keywords = [obj['key'] for obj in data['metadata'] if (obj['key'] == 'dc.subject.keyword' and obj['value'] == 'Journals')]
            for obj in data["metadata"]:
                if obj["key"] == "dc.subject.keyword":
                    if (obj['value'] == ''+ item):
                        for ob in data['metadata']:
                            if ob['key'] == 'dc.description.abstract':
                                abstracts.append(ob["value"])

    #j += 1
    #if j >= count:
     #   break







# put the list into a dataframe to print the abstracts with an index to count the number of abstracts
df = pd.DataFrame(abstracts)

print(df)

#print(df_filtered)







