import pandas as pd


def get_chunk(data_out_file_name, chunksize, delimiter):
    return pd.read_csv(
                data_out_file_name,
                chunksize=chunksize,
                header = None,
                delimiter=delimiter)


def read_content(file_path):
    with open(file_path, "rt") as f: 
        try:
            return f.read()
        except UnicodeDecodeError as e:
            print('Err on {} '.format(e))