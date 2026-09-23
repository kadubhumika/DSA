import multiprocessing
import os
def compute_square(number):
    result = number * number
    print(f"Process {os.getpid()} calculated square: {result}")
if __name__ == '__main__':
    processes = []
    numbers = [10, 20, 30]
    for num in numbers:
        process = multiprocessing.Process(target=compute_square, args=(num,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
