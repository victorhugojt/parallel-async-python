from common import file_utils


def process(chunk):
    return chunk.describe(percentiles = [.1, .99])


def process_file(file_path, chunk_size, delimiter):
    processed_count = 0
    for chunk in file_utils.get_chunk(file_path, chunk_size, delimiter):
        processed_count += 1
        stats = process(chunk)
        print(stats)
        print(stats[0][0])
        if processed_count == 2:
            break


def main():
    print('Starting ...... ')
    process_file('csv_file.csv', 10, ',')


if __name__ == '__main__':
    main()