import fasttext
import csv
import pandas as pd

threshold = 0.8
model = fasttext.load_model('/workspace/datasets/fasttext/title_model.bin')
synonyms = []
with open('/workspace/datasets/fasttext/top_words.txt', 'r') as fd:
    reader = csv.reader(fd)
    for idx, row in enumerate(reader):
        sim_word_array = model.get_nearest_neighbors(row[0])
        sim_word_dict = dict(sim_word_array)
        # filter out by treshold
        synonym_array = [v for k,v in sim_word_dict.items() if k >= threshold]
        if len(synonym_array) > 1:
            # append comma delimited synonyms
            comma_delimited = ','.join(synonym_array)
            synonyms.append(comma_delimited)

df = pd.DataFrame(data={"synonyms": synonyms})
df.to_csv('/workspace/datasets/fasttext/synonyms.csv', index=False, header=False)
