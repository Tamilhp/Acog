def transform_uppercase(record:str)->str:
    return record.upper()

def transform_remove_stopwords(record:str)->str:
    record =record.split()
    all_stopwords=["a", "an", "the", "and", "or"]
    tokens_without_sw = [word for word in record if word.lower() not in all_stopwords]
    return ' '.join(tokens_without_sw)

def transform_lowercase(record:str)->str:
    return record.lower()

# def main():
#     file_name=input("Enter the file name:")
#     f1 = open(file_name, "r")
#     for line in f1:
#         print(transform_uppercase(line))
#         print(transform_remove_stopwords(line))
