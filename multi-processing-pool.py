import multiprocessing
import os
import time


def task_sleep(sleep_duration, task_number):
    time.sleep(sleep_duration)
    print(f"Task {task_number} done (slept for {sleep_duration}s)! "
          f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    time_start = time.time()

    # Create pool of workers
    pool = multiprocessing.Pool(2)

    # Map pool of workers to process
    pool.starmap(func=task_sleep, iterable=[(2, 1)] * 4)

    # Wait until workers complete execution
    pool.close()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")