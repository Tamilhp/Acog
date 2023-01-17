# Entrez wrapper

## Assumptions
` Python3 `

` pip `

`python-virtualenv`

## Genbank
```
$ cd git-playground/interns/ENTREZ/genbank
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python genbank.py --help -> to fetch details about genbank.py
$ python genbank.py {command} --help -> to fetch details about commands of genbank.py
$ python genbank.py search {keyword} [max]
$ python genbank.py fetch {keyword} {output_file} [max]
```

### For e.g.
```
$ python genbank.py search --help
$ python search ppf-1 [5]
$ python genbank.py fetch --help
$ python genbank.py ppf-1 result.csv [5]
```

` N.B.: Default max here is 5 to decrease the computation issue though the library provides default value of max to retrive as 20 `





## PubMed 

### Code to Search or Fetch the results from PubMed db using Entrez: 

- Run the `pubmed.py` file. 

- To `Search` from Pubmed db :<br />
  - Type `search` in the terminal window.<br />
  - Enter the `Keyword` to search from the db.<br />
  - Enter the `Number of records` to search.  <br />


- To `Fetch` from the PUBMED DB:<br />
  - Type `fetch` in the terminal window.<br />
  - Enter the `Keyword` to fetch from the db.<br />
  - Enter the `File_Name` to store the output results.<br />
  - Enter the `Number of records` to fetch.  <br />
  
  
