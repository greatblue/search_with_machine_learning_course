import pandas as pd

label_count = 499 # keep rows whose labels are associated with at least <label_count> products 

def prune_by_label_product_match(label_count)
    df = pd.read_csv('labeled_products.txt', sep='\t', header=None, names=['merged'])
    df = df['merged'].str.split(' ', n=1, expand=True)
    df.columns =['label', 'product']
    df_group_by_count = df.groupby('label').agg({'product': 'count'}).reset_index()
    df_pruned_labels = df_group_by_count[df_group_by_count['product'] > label_count].reset_index()
    df = pd.merge(df, df_pruned_labels, on='label')
    df_pruned_final = df[['label','product_x']]
    # save into a file
    df_pruned_final.to_csv('pruned_labeled_products.txt', header=False, index=False, sep=' ')

prune_by_label_product_match(label_count)




