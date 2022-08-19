import multiprocessing
import os
import time


def task_sleep(sleep_duration, task_number):
    time.sleep(sleep_duration)
    print(f"Task {task_number} done (slept for {sleep_duration}s)! "
          f"Process ID: {os.getpid()}")


if __name__ == "__main__":
    time_start = time.time()

    # Create process
    p1 = multiprocessing.Process(target=task_sleep, args=(4, 1))
    p2 = multiprocessing.Process(target=task_sleep, args=(2, 2))

    # Start task execution
    p1.start()
    p2.start()

    # Wait for process to complete execution
    p1.join()
    p2.join()

    time_end = time.time()
    print(f"Time elapsed: {round(time_end - time_start, 2)}s")