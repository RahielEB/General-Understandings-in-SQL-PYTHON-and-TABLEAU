# Medical Insurance Project


```python
import csv
```

## To do list:
- I must from the csv into two dictionaries based on rows and columns
- Understand the avgerage cost of insurance for every person
- Make insights on which sex(Females or Males) pays more for insurance on average
- Discover the average cost per person in each region
- Make insights on which sex pays more on average per region 


```python
# I must make an empty list for each variable in the insurance csv
ages = []
sex = []
bmi = []
children = []
smoker = []
region = []
cost = []
```

My next plan of action in to appends the information with all of the list. To do this I will open the csv using "with open" then iterating the information based which part of the list it fits. For instance cost(empty list = chargers in the csv file)


```python
with open("insurance.csv") as us_medical_insurance:
    us_medical_insurance_dict = csv.DictReader(us_medical_insurance)
    for info in us_medical_insurance_dict:
        ages.append(info["age"])
        sex.append(info["sex"])
        bmi.append(info["bmi"])
        children.append(info["children"])
        smoker.append(info["smoker"])
        region.append(info['region'])
        cost.append(info["charges"])
```

Next plan of action is to define a function to put this information into a dictionary


```python
def us_insurance_dict(ages, sex, bmi, children, smoker, region, cost):
    insurance_data = {}
    for i in range(0,len(ages)):
        insurance_data['age'] = ages
        insurance_data['sex'] = sex
        insurance_data['bmi'] = bmi
        insurance_data['children'] = children
        insurance_data['smoker'] = smoker
        insurance_data['region'] = region
        insurance_data['charges'] = cost
    return insurance_data

insurance_data = us_insurance_dict(ages, sex, bmi, children, smoker, region, cost)
#print(insurance_data)

```

i'm opening insurance.csv then skipping the header row, and storing each patient as a dictionary of {column: value} pairs, all held together in one big insurance_records dictionary keyed by row


```python
with open("insurance.csv") as insurance_file:
    file_reader = csv.reader(insurance_file)
    column_name = next(file_reader)

    insurance_records = {}
    row_number = 1
    
    for row in file_reader:
        row_dict = {name: value for name, value in zip(column_name, row)}
        insurance_records[row_number] = row_dict
        row_number += 1
#print(insurance_records)
```

## Insights on the count of females and males.


```python
print("There are a total of " + str(len(sex)) + " female and male candidates in the US Medical Insurance file.")
```

    There are a total of 1338 female and male candidates in the US Medical Insurance file.
    


```python
def count_sex(sex):
    females = sum(1 for s in sex if s == 'female')
# taking the sum of the iteration if it fits female
    males   = sum(1 for s in sex if s == 'male')
# taking the sum of the iteration if it fits male
    print(f"There are {females} females, and {males} males.")
# formatting female and male intergers into strings
count_sex(sex)
```

    There are 662 females, and 676 males.
    

## Insights on the average cost per person


```python
# We are going to iterate all cost and divide it by the amount of people to get the average
def average_cost(cost):
    total_cost = 0
# total_cost is where the results will be put into
    for avg in cost:
        total_cost += float(avg)
# this loop adds all costs
    avg_cost = total_cost/(len(cost))
#finally we divide the total by the number into account
    return avg_cost

print("The Average cost of US medical insurance is: " + str(round(average_cost(cost),2)) + " dollars(USD.)")
# I had to round the number because it was showing many deciamls. It was a float so I had to makje it an integer.
```

    The Average cost of US medical insurance is: 13270.42 dollars(USD.)
    

## Now the total cost via sex
After I will find the average for bothe female and males and compare the values to the combined average


```python
female_cost = []

male_cost = []

for amount in insurance_records.values():
    sex = amount['sex']
    charges = amount['charges']
# I'm taking the values from the insurance records
    if sex == 'female':
        female_cost.append(charges)
    elif sex == 'male':
        male_cost.append(charges)
#print(f" All of the female cost {female_cost}")
# THe print is just a check up
```

Now the total for each group


```python
female_total = 0

male_total = 0

for i in female_cost:
    female_total += float(i)
for i in male_cost:
    male_total += float(i)

print(f"The total cost of all female insurance is {round(female_total,2)} dollars(USD) and for the males it is {round(male_total,2)} dollars(USD).")
```

    The total cost of all female insurance is 8321061.19 dollars(USD) and for the males it is 9434763.8 dollars(USD).
    


```python
def find_avg(total, count):
    return float((total/count))
female_avg = find_avg(female_total,662) 

male_avg = find_avg(male_total,676)

avg_diff_in_sex = round(male_avg,2) - round(female_avg,2)

print(f"The average cost for females surveyed in the US Medical Insurance is: {round(female_avg,2)} dollars(USD).")

print(f"The average cost for males surveyed in the US Medical Insurance is: {round(male_avg,2)} dollars(USD).")

print(f"This is a {avg_diff_in_sex} dollar difference with females paying less on average.")
```

    The average cost for females surveyed in the US Medical Insurance is: 12569.58 dollars(USD).
    The average cost for males surveyed in the US Medical Insurance is: 13956.75 dollars(USD).
    This is a 1387.17 dollar difference with females paying less on average.
    

# Now we focus on the difference in price with region


```python
northwest = []
northeast = []
southwest = []
southeast = []

nw_total = 0
ne_total = 0
sw_total = 0
se_total = 0
for i in insurance_records.values():
    region = i['region']
    charges = float(i['charges'])   # convert to number

    if region == "northeast":
        northeast.append(charges)
    elif region == "northwest":
        northwest.append(charges)
    elif region == "southwest":
        southwest.append(charges)
    elif region == "southeast":
        southeast.append(charges)
nw_total += round(sum(northwest),2)
ne_total += round(sum(northwest),2)
sw_total += round(sum(southwest),2)
se_total += round(sum(southeast),2)
print(len(northwest))
print(len(northeast))
print(len(southwest))
print(len(southeast))
print(nw_total)
print(sum(northwest))
# Just checking my code
```

    325
    324
    325
    364
    4035712.0
    4035711.99654
    


```python
def avg(num,total):
    avg_per_person = num / (len(total))
    on_avg = round(avg_per_person,2)
    return on_avg

print(f"The average cost of Medical Insurance for someone in the North West of the US is {avg(nw_total,northwest)} dollars(USD).")
print(f"The average cost of Medical Insurance for someone in the North East of the US is {avg(ne_total,northeast)} dollars(USD).")
print(f"The average cost of Medical Insurance for someone in the South West of the US is {avg(sw_total,southwest)} dollars(USD).")
print(f"The average cost of Medical Insurance for someone in the South East of the US is {avg(se_total,southeast)} dollars(USD).")

```

    The average cost of Medical Insurance for someone in the North West of the US is 12417.58 dollars(USD).
    The average cost of Medical Insurance for someone in the North East of the US is 12455.9 dollars(USD).
    The average cost of Medical Insurance for someone in the South West of the US is 12346.94 dollars(USD).
    The average cost of Medical Insurance for someone in the South East of the US is 14735.41 dollars(USD).
    

# In Conclusion
## On average scale Medical Insurance is greater in price in the South Easr region of the US and Cheapest on average in the South West region


```python

```
