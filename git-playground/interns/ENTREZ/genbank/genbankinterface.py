import os, csv, pandas as pd
from Bio import Entrez, SeqIO


class Genbank():
    def __init__(self):
        self.email = "abinash@aganitha.ai"
        self.db = "nucleotide"
        self.rettype = "fasta"
        Entrez.email = self.email
 
    def info():
        info = Entrez.einfo()
        dblist = Entrez.read(info)
        for key in dblist.keys():
            print(key, " : ", dblist[key])
 
    def search(self, keyword: str, max: int):
        info = Entrez.esearch(db=self.db, term=keyword, retmax=max)
        idlist = Entrez.read(info)
        return idlist
 
    def fetch(self, keyword: str, file: str, max: int):
        idlist = self.search(keyword, max)
        records = []
        ids = idlist['IdList']
        for id in ids:
            handle = Entrez.efetch(db=self.db, id=id, rettype=self.rettype)
            record = SeqIO.read(handle, self.rettype)
            records.append(record)
        keys = ['Id', 'SeqId', 'Name', 'Description', 'SeqLength', 'Seqeunce']
        values = []
        for i in range(len(ids)):
            values.append([ids[i], records[i].id, records[i].name, records[i].description, len(records[i].seq), records[i].seq])
        with open(file, 'w') as csvfile:
            csvwriter= csv.writer(csvfile)
            csvwriter.writerow(keys)
            for value in values:
                csvwriter.writerow(value)
            csvfile.close()
        
        return idlist, records

# if __name__ == "__main__":
#     app()
    # keyword = input("Enter the keyword to search: ")
    # max = input("Enter the max amount to fetch: ")
    # file_name = input("Enter the file name to write the sequence: ")
    # if max:
    #     max = int(max)
    # else:
    #     max = 5
    # file= f'{os.getcwd()+"/"+file_name}'
    # gb = Genbank()
    # idlist, records = gb.fetch(keyword, file, max)
    # if idlist['Count'] != 0:
    #     print("idCount: ", idlist['Count'])
    #     print("idRetrieved: ", idlist['RetMax'])
    #     print("recordCount: ", len(records))
    #     ids = idlist['IdList']
    #     for i in range(len(ids)):
    #         print("id: ", ids[i])
    #         print("Sequence: ", records[i])
    #         print("< ","===="*25," >")
    # else:
    #     print("The DB is empty on the keyword.")