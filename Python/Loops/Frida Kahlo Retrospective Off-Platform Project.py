#!/usr/bin/env python
# coding: utf-8

# In[6]:


paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]

dates = [1939, 1933, 1946, 1940]

paintings_and_dates_packed = zip(paintings, dates)

paintings_and_dates = list(paintings_and_dates_packed)

print(paintings_and_dates)


# In[7]:


#I forgot a few paintings I should add

paintings_and_dates.append(["The Broken Column", 1944])

paintings_and_dates.append(["The Wounded Deer", 1946])

paintings_and_dates.append(["Me and My Doll",1937])


# In[13]:


# I am setting up a way to have the paintings with a unique identifier 

identifier = len(paintings_and_dates)
print(identifier)


# In[27]:


audio_tour_number = range(1,8)
print(audio_tour_number)


# In[28]:


master_list_packed = zip(audio_tour_number, paintings_and_dates)

master_list = list(master_list_packed)

print(master_list)


# In[ ]:




