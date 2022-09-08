from common import file_utils
from multiprocessing import Process, Queue, current_process
import queue
import time


def process(chunk):
    return chunk.describe(percentiles = [.1, .99])


def read(file_path, chunks_to_process):
    print('Reader processor number : ' + current_process().name)
    for chunk in file_utils.get_chunk(file_path, 10, ','):
        chunks_to_process.put(chunk)
    

    print('Read process finished !')
    return True


def work(chunks_to_process, chunks_processed):
    while True:
        try:           
            chunk = chunks_to_process.get_nowait()
            result = process(chunk)
            chunks_processed.put(result[0][0])
            print(' {} - chunk was done by : {} '.format(result[0][0], current_process().name))
        except queue.Empty:
            print(current_process().name + ' Without DATA ')
            break

    return True


def launch_workers(number, file_path):
    chunks_to_process = Queue()
    chunks_processed = Queue()
    reader = Process(target=read, args=(file_path, chunks_to_process))
    reader.start()

    time.sleep(3) # wait for some data
    process_workers = []
    for count in range(number - 1):        
        worker = Process(target=work, args=(chunks_to_process, chunks_processed))
        process_workers.append(worker)
        worker.start()

    for worker in process_workers:
        worker.join()

    reader.join()

    print('Processed {} chunks '.format(str(chunks_processed.qsize())))
    print('Main thread finished ')

    return True


def main():
    print('Starting : 3 Workers ...')
    launch_workers(3, 'small_file.csv')


if __name__ == '__main__':
    main()