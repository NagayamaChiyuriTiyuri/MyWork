#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

num = input("何パターンを作成しますか？")

for i in range(0, int(num)):
    angle = random.sample(range(0, 360), 1)[0]
    ratio = random.sample(range(0, 100), 1)[0]
    
    print("楕円：" + str(angle) + "°回転、" + str(ratio) + "％縦横比率")

for i in range(0, int(num)):
    angle2 = random.sample(range(-100, 100), 1)[0]
    ratio2 = random.sample(range(0, 100), 1)[0]
    
    print(str(angle2) + "％カーブ、" + str(ratio2) + "％縮小コピー")
        
for i in range(0, int(num)):
    r_col = random.sample(range(0, 255), 1)[0]
    g_col = random.sample(range(0, 255), 1)[0]
    b_col = random.sample(range(0, 255), 1)[0]
    
    print("R：" + str(r_col) + " G：" + str(g_col) + " B：" + str(b_col))  


# In[ ]:




