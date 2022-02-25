import os, argparse
from Bio import SeqIO

def main():
    if 'each_fasta' not in os.listdir(path='./'):
        os.system('mkdir each_fasta')
        
    def get_args():
        parser = argparse.ArgumentParser(description='dkato. November, 2021') 
        parser.add_argument('-f', '--fasta', help='multi-fasta', required=True) 
        return parser.parse_args()
    
    for line in list(SeqIO.parse(get_args().fasta, "fasta")):
        name = line.description
        if " " in name or "/" in name:
            name = name.replace(" ", "_").replace("/", "_")
        SeqIO.write(line, f"./each_fasta/{name}.fasta", "fasta")

if __name__=='__main__':
    main()
