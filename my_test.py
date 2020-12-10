
from tqdm import tqdm
import time
from tqdm.std import trange
from random import random,randint


def tqdm_test():
    # 对tedm的循环嵌套
    for i in tqdm(range(100),desc="100普通循环进度"):
        time.sleep(0.01)

    # 对range的包装
    for i in trange(100):
        time.sleep(0.01)

    # 对list的使用
    l_list = list('chenqinhai')
    l_bar = tqdm(l_list)
    for letter in l_bar:
        time.sleep(0.01)
        l_bar.set_description(f"get {letter}")

    pbar = tqdm(["a", "b", "c", "d"])
    for c in pbar:
        time.sleep(0.01)
        pbar.set_description("Processing %s" % c)

    # 手动控制更新
    with tqdm(total=100) as pbar:
        for i in range(10): # 循环10次
            time.sleep(0.01)
            pbar.update(5) # 以5%的更新

    with trange(100) as t:
        for i in t:
            # 设置进度条左边显示的信息
            t.set_description("GEN %i" % i)
            # 设置进度条右边显示的信息
            t.set_postfix(loss=random(), gen=randint(1, 999), str="h", lst=[1, 2])
            time.sleep(1)



tqdm_test()

