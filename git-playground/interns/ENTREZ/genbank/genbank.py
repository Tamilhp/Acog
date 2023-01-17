from numpy import identity
from typer import Typer, Argument
# import typer
from genbankinterface import Genbank as gi


app = Typer()
query = gi()

@app.command()
def search(keyword : str = Argument(..., help = "Keyword to search in genbank/nucleotide DB"),
            max: int = Argument(5, help = "Maximum IDs to fetch")):
            
    idlist = query.search(keyword, max)
    if idlist['Count'] != 0:
        print("idCount: ", idlist['Count'])
        print("idRetrieved: ", idlist['RetMax'])
        for id in idlist['IdList']:
            print("id:", id)


@app.command()
def fetch(keyword : str = Argument(..., help = "Keyword to search in genbank/nucleotide DB"),
            file: str = Argument(..., help = "File to store output"),
            max: int = Argument(5, help = "Maximum IDs to fetch")):
    print(keyword, file, max)
    query.fetch(keyword, file, max)




if __name__ == '__main__':
    app()