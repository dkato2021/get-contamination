import argparse
import pandas as pd

def main():
    def get_args():
        parser = argparse.ArgumentParser(description='dkato. November, 2021') 
        parser.add_argument('-f', '--features', help = 'features.tsv from DFAST', required=True) 
        return parser.parse_args()
    
    _df = pd.read_table(get_args().features)

    start, end = [], []
    for i, df_i in enumerate(_df.location):
        if df_i[0] != 'c':
            start += [df_i.split('..')[0]]
            end += [df_i.split('..')[1]]
        else:
            start += [df_i.split('..')[1][:-1]]
            end += [df_i.split('..')[0][len('complement('):]]
    df = pd.DataFrame(columns = ['start', 'end'])
    df.start, df.end = start, end

    pd.concat([df, _df], axis = 1).to_csv("new_feature.csv")
    
if __name__=='__main__':
    main()
