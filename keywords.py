#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def tag():
    tag = ["amazing", "amusement park", "architecture", "aurora", "autumn", "autumn leaves", "beautiful",
           "bird", "bread", "brick", "cafe", "candle", "castle", "christmas", "city", "cloud", "color", "colored pencil",
           "dandelion", "dynamics", "evening", "experiment", "festival", "fireworks", "flower", "flower garden", "forest",
           "fruit", "halloween", "hiking", "home", "hydrangea", "ice", "illumination", "ink", "large tree", "lifestyle",
           "light", "lily", "meadow", "moon", "mountain", "nature", "neon", "night view", "palm", "park", "rainbow", "rainy season",
           "room", "rose", "sakura", "science", "sea", "ship", "sky", "snack", "snow", "spectral", "starry sky", "summer", "sunrise",
           "trip", "tulip", "urban", "vegetable", "walking", "water", "waterfall", "work", "world"]
    return random.choice(tag)
title = tag()

print(title + "が今回のキーワードです。")

# In[ ]:




