


# multi thread with pbar 
from time import sleep
from multiprocessing.pool import ThreadPool
from itertools import repeat
from tqdm import tqdm 

loop_list = range(18)
results = ThreadPool(3).imap(lambda x: foo(*x), zip(loop_list,    ))  # 8 threads


def foo(x):
    sleep(1)
    return  x

gb=0
pbar = tqdm(enumerate(results),total = len(loop_list) )
for i, x in pbar:
    gb += x
    pbar.desc = f' Caching images ({gb / 1E9:.1f}GB)'
pbar.close()
