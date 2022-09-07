from common import file_utils
from multiprocessing import Process, Queue, current_process
import queue


def process(chunk):
    return chunk.describe(percentiles = [.1, .99])


def read(file_path, chunks_to_process):
    for chunk in file_utils.get_chunk(file_path, 10, ','):
        chunks_to_process.put(chunk)


def work(chunks_to_process, chunks_processed):
    while True:
        try:           
            chunk = chunks_to_process.get_nowait()
            result = process(chunk)
            print(result)
            print('chunk was done by : ' + current_process().name)
            chunks_processed.put(result)
        except queue.Empty:
            break

    return True


def launch_workers(number, file_path):
    chunks_to_process = Queue()
    chunks_processed = Queue()
    reader = Process(target=read, args=(file_path, chunks_to_process))
    reader.start()
    reader.join()

    process_workers = []
    for count in range(number - 1):
        worker = Process(target=work, args=(chunks_to_process, chunks_processed))
        process_workers.append(worker)
        worker.start()

    for worker in process_workers:
        worker.join()

    while not chunks_processed.empty():
        print(chunks_processed.get())


def main():
    print('Starting : 4 Workers ...')
    launch_workers(4, 'small_csv_file.csv')


if __name__ == '__main__':
    main()