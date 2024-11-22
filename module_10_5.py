import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf8') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not line:
                break


filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start1 = time.time()

# for i in filenames:
#     read_info(i)
#     end1 = time.time()
#     time_of_line_function = end1 - start1
#     print(f'Линейный вызов : {time_of_line_function}')

if __name__ == '__main__':
    start_time_parallel = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time_parallel = time.time()
    time_of_multiprocessing = end_time_parallel - start_time_parallel
    print(f"Многопроцессный : {time_of_multiprocessing:.2f} секунд")
