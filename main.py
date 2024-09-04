import multiprocessing
import time

# 第一部分：使用鎖來管理計數器
def increase_num_lock(lock_num, lock):
    for _ in range(20):
        with lock:
            lock_num.value += 10
        time.sleep(0.1)
        
def decrease_num_lock(lock_num, lock):
    for _ in range(20):
        with lock:
            lock_num.value -= 50
        time.sleep(0.3)

# 第二部分：啟動兩個進程來修改同一個 Value
def general(v, num):
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value, end=",")

def lock_and_general_example():
    # 創建 Value 和 Lock
    lock_num = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()

    # 啟動進程來增加和減少 lock_num
    increase_processes = []
    decrease_processes = []

    for _ in range(5):
        p = multiprocessing.Process(target=increase_num_lock, args=(lock_num, lock))
        p.start()
        increase_processes.append(p)

    for _ in range(5):
        p = multiprocessing.Process(target=decrease_num_lock, args=(lock_num, lock))
        p.start()
        decrease_processes.append(p)

    # 創建另外一個 Value 用於 general
    general_value = multiprocessing.Value("i", 0)
    p1 = multiprocessing.Process(target=general, args=(general_value, 1))
    p2 = multiprocessing.Process(target=general, args=(general_value, 3))

    # 開始所有進程
    for p in increase_processes:
        p.join()  # 等待所有增加進程完成

    for p in decrease_processes:
        p.join()  # 等待所有減少進程完成

    # 啟動 general 的進程
    p1.start()
    p2.start()

    # 等待 general 的進程完成
    p1.join()
    p2.join()

    print(f"\nFinal counter value with lock: {lock_num.value}")
    print(f"Final value from general: {general_value.value}")

if __name__ == '__main__':
    lock_and_general_example()