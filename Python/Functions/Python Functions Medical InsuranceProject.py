#!/usr/bin/env python
# coding: utf-8

# In[3]:


def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
 
    print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars(USD).")
    
    return estimated_cost
# Initial variables for Maria 
# age = 28
# sex = 0  
# bmi = 26.2
# num_of_children = 3
# smoker = 0  

# Estimate Maria's insurance cost
Maria_insurance_cost = calculate_insurance_cost(28,0,26.2,3,0, name = "Maria")

# Initial variables for Omar
#age = 35
#sex = 1 
#bmi = 22.2
#num_of_children = 0
#smoker = 1  

#Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost(35,1,22.2,0,1, name = "Omar")

emmanuel_insurance_cost = calculate_insurance_cost(23,1,22.4,0,0, name = "Emmanuel Rahiel Beaucicot")


# In[9]:


def diff_between_others(first_person, second_person, name1, name2):
    insurance_difference = first_person - second_person
    
    print("The difference between " + name1 + " and " + name2 + " is " + str(insurance_difference))
    return insurance_difference
maria_insurance = 5469
omar_insurance = 28336
emmanuel_insurance = 1410


# In[10]:


diff_between_others(maria_insurance, omar_insurance, name1 = "Maria", name2 = "Omar")


# In[11]:


diff_between_others(omar_insurance, maria_insurance, name1 = "Omar", name2 = "Maria")


# In[ ]:




