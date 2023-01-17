from class_cli import CLI
from Bio import Entrez
from Bio import SeqIO
from Bio import Medline
import pandas as pd
import os, csv


cli = CLI()

@cli.Program()
class Pubmed():
    def __init__(self):
        self.email = "crohit@aganitha.ai"
        self.db = "pubmed"
        self.rettype="medline"
        self.retmode = "text"
        Entrez.email = self.email

    @cli.Operation()
    def search(self, keyword, max):
    # functio to search in pubmed db    
        """

        :param keyword: Enter the Keyword to search from PubMed db
        :param max: Enter the maximum results you want to search

        """
        info = Entrez.esearch(db=self.db, term=keyword, retmax=max)
        idlist = Entrez.read(info)
        return idlist

    @cli.Operation()
    def fetch(self, keyword, file, max):
    # function to fetch from Pubmed db

        """

        :param keyword: Enter the Keyword to fetch from Pubmed db
        :param file: Enter the name of the output file where the results will be stored
        :param max: Enter the maximum number of results you want to fetch from the Pubmed db

        """


        idlist = self.search(keyword, max)
        records = []
        ids = idlist['IdList']
        for id in ids:

            handle = Entrez.esummary(db=self.db, id=id)
            record = Entrez.read(handle)
            records.append(record[0])
            print(id)
            print(record)
            print('-'*25)

        keys = ['Id', 'Source', 'Title', 'DOI', 'FullJournalName', 'SO']
        values = []
        for i in range(len(ids)):
            values.append(
                [ids[i], records[i]['Source'], records[i]['Title'], records[i]['DOI'], records[i]['FullJournalName'], records[i]['SO']])
        with open(file, 'w') as csvfile:
        # write output in CSV format
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(keys)
            for value in values:
                csvwriter.writerow(value)
            csvfile.close()

        return idlist, records

if __name__ == "__main__":
    Pubmed().CLI.main()