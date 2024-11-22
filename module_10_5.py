import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)
    return all_data


if __name__ == '__main__':
    filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    total_time = 0

    for i in filenames:
        start1 = time.time()
        read_info(i)
        end1 = time.time()

        time_of_data_function = end1 - start1
        total_time += time_of_data_function

    print(f"Линейный вызов : {total_time:}")

    start_time_parallel = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)

    end_time_parallel = time.time()
    time_of_multiprocessing = end_time_parallel - start_time_parallel
    print(f"Многопроцессный: {time_of_multiprocessing:}")
