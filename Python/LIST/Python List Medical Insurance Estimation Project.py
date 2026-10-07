#!/usr/bin/env python
# coding: utf-8

# In[20]:


def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)


name = ["Maria", "Rohan", "Valentina"]

insurance_costs = [4105.0, 5320.0, 35210]

insurance_rawdata = zip(name, insurance_costs)

insurance_data = list(insurance_rawdata)

estimated_insurance_data = []

estimated_insurance_data.extend([maria_insurance_cost, rohan_insurance_cost,valentina_insurance_cost])
print(estimated_insurance_data)



# In[21]:


print("Here is the actual insurance cost data: " + str(insurance_data))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))


# In[24]:


akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)

insurance_data = ["Akira", 2930.0]

estimated_insurance_data.append(akira_insurance_cost)

print("Here is the actual insurance cost data: " + str(insurance_data))
print("Here is the estimated insurance cost data: " + str(estimated_insurance_data))

