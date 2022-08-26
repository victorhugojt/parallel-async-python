import pandas as pd


def get_chunk(data_out_file_name, chunksize, delimiter):
    yield pd.read_csv(data_out_file_name, chunksize=chunksize, delimiter=delimiter)


def read_content(file_path):
    with open(file_path, "rt") as f: 
        try:
            return f.read()
        except UnicodeDecodeError as e:
            print('Err on {} '.format(e))