#!/usr/bin/env python
# coding: utf-8

# In[1]:


age = 28
sex = 0 
bmi = 26.2
num_of_children = 3 
smoker = 0


# In[2]:


insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

"""This is to calculate the insurance cost. However I understand that these are no accurate to how health insurance prices are given in America.
In fact some of these citerias would be illegal to use"""


# In[3]:


print("This person's insurance cost is " + str(insurance_cost)+ " dollars.")


# In[4]:


age += 4

new_insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500


# In[5]:


change_in_insurance_cost = new_insurance_cost - insurance_cost


# In[7]:


print("The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")


# In[8]:


age = 28
bmi += 3.1 


# In[9]:


"""bmicic stand for bmi_change insurance cost"""
bmicic = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

"""Now we will do what we did to the lines above"""
"""bmiciic stands for bmi change in insurance cost"""
bmiciic = bmicic - insurance_cost


# In[11]:


print("The change in estimated insurance cost after increasing bmi by 3.1 which makes it " + str(bmi) + " is " + str(bmiciic) + " dollars.")


# In[12]:


bmi = 26.2 
sex = 1


# In[14]:


male_insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500


# In[17]:


males_insured_differnece = male_insurance_cost - insurance_cost


# In[18]:


print("The change in estimated insurance cost for being male instead of female is " + str(males_insured_differnece) + " dollars(USD).")


# In[19]:


"""The information that could be obtained from this analysis is that males could have a lower medical cost compared to females"""


# In[22]:


""" now I will do the same for all of the rest of the varibles for musdcle meomery retention"""
sex = 0 

num_of_children -= 3 

new_insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

insurance_difference = new_insurance_cost - insurance_cost 

print("The change in estimated insurance cost for having 0 children instead of 3 is " + str(insurance_difference) + " dollars(USD).")


# In[23]:


print("This means that having children could effect the average insurance cost and cost more.")


# In[24]:


num_of_children = 3 

smoker = 1

new_insurance_cost = 250 * age -128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

insurance_difference = new_insurance_cost - insurance_cost 


# In[26]:


print("The change in estimated insurance cost for being a smoke is " + str(insurance_difference) + " dollars(USD).")


# In[ ]:




