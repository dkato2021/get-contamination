
import sys, os, argparse, shutil

def get_args():
    parser = argparse.ArgumentParser(description='dkato. November, 2021')
    parser.add_argument('-in' , dest ='dir_in', required=True, 
                       help='The directory containing the files you want to rename')  
    parser.add_argument('-stats' , dest ='stats_dir', required=True, 
                       help='The directory containing the assembly statistcs reports')
    parser.add_argument('-ex' , dest ='extension', required=True, 
                       help='extension of output file(ex. fna.gz)')    
    return parser.parse_args()

def main():
    if 'out' not in os.listdir(path='./'):
        print('1.making output directory..')
        shutil.copytree(os.path.abspath(get_args().dir_in), "./out/")

    print('2.reneming..')
    stats_dir = get_args().stats_dir
    stats_dir_list = os.listdir(path = stats_dir)
    extension = get_args().extension
    for file_in in os.listdir(path=get_args().dir_in):
        if file_in[0]!='.':
            #get the path to the assembly statistcs reports #13 = len('GCF_000024905')
            stats_in = [stats_path for stats_path in stats_dir_list  if file_in[:13] in stats_path][0]
            
            #get output name # 18 = len('# Organism name:  ')
            #_ = file_in[:13]
            _ = open(os.path.join(stats_dir , stats_in), 'r').readlines()[2][18:-1].replace(' ', '_').replace('.', '_').replace('/', '_').replace(')', '_').replace('(', '_').replace('=', '_')
            filename_out  = _ + '.' + extension
            
            
            #rename
            os.rename(os.path.join("./out" , file_in),
                      os.path.join("./out" , filename_out)) 
            print(file_in, '-->', filename_out)
            
if __name__ == "__main__":
    main()
