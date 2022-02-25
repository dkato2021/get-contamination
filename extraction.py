import sys, argparse, warnings
import pandas as pd
from tqdm import tqdm

def get_args():
    parser = argparse.ArgumentParser(description='dkato. November, 2021') 
    parser.add_argument('-a' , dest ='annotation', 
                        help = 'specify the path to your annotation file(ex. ~.xlsx) which number of sheet is 1', required=True) 
    parser.add_argument('-c' , dest ='col_name', 
                        help = 'specify the column name you want to search' , required=True) 
    parser.add_argument('-k' , dest ='keywards', nargs='*', 
                        default = ['transport','facilitator','permease', 'antiporter', 'symporter'],
                        help = 'specify the keywords(default:transport facilitator permease antiporter symporter')
    return parser.parse_args()

def main(df = None, col_name = None, keywards = None):
    MyRow = []
    for i in tqdm(range(len(df))):
        if pd.isna(df[col_name][i]):
            df[col_name][i]='Nan'
        if any(map(df[col_name][i].__contains__, keywards)):
            MyRow += [i]
    df.iloc[MyRow, ].to_csv("extracted.csv")
    
if __name__ == "__main__":
    #loading data..
    warnings.filterwarnings('ignore') 
    print('1.loading your annotation file..')
    df = pd.read_excel(get_args().annotation)
    keywards = get_args().keywards
    
    #main
    print(f'2.Extracting rows which contain the keywards:{get_args().keywards} in the specified column')
    main(df = df,
         col_name = get_args().col_name, 
         keywards = keywards); print('3.extracted.csv file has been made.')
