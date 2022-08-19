def read_content(file_path):
    with open(file_path, "rt") as f: 
        try:
            return f.read()
        except UnicodeDecodeError as e:
            print('Err on {} '.format(e))