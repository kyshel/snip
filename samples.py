

# .csv to list 
# v1 
import csv

with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


# multi-thread tiny

gb=0
ids = range(n)
results = ThreadPool(workers).imap(self.load_pix,  ids  )  
pbar = tqdm(enumerate(results), total=n, mininterval=1,)
for i, x in pbar:
    self.pixs[i] = x  
    # gb += self.pixs[i].nbytes # sys.getsizeof(b.storage())
    gb +=  sys.getsizeof(self.pixs[i].storage())
    pbar.desc = f'{prefix}Caching images ({gb / 1E9:.1f}GB)'
pbar.close()






# multi-thread with tqdm template

from tqdm import tqdm 
from itertools import repeat
import multiprocessing.dummy as mp 
from time import sleep

workers = 4


def foo(a,b,pbar = None):
    if 'HALT' in vars() or 'HALT' in globals(): # stop multi-threads
        if HALT: return 

    sleep(1)

    print(a,b)


    if pbar:
        pbar.update(1)
    
    return a+b


# make pies
a_list = range(16)
b_list = range(16)
c_list = []

pbar = tqdm(total=len(a_list), position=0, leave=True,
            desc = f"aa: ", )
p=mp.Pool(workers)
c_list = p.starmap(foo, zip(a_list,b_list,repeat(pbar)))
p.close()
pbar.close()
p.join()

print(c_list)





# PIL read 

# https://pillow.readthedocs.io/en/stable/reference/Image.html
from PIL import Image
import numpy as np
im = Image.open('hopper.jpg')
a = np.asarray(im) # im > np

im = Image.fromarray(a) # np > im 














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
