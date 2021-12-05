#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pywebio.input import *
from pywebio.output import *


def bmicalculator():
    feet=input('Please enter how many feet tall you are',type=FLOAT)
    inches=input('Now add inches',type=FLOAT)
    weight=input('Please enter your weight in pounds',type=FLOAT)
    
    bmi=(weight/(feet*12+inches)**2)*703
    
    bmi_output=[(16,'Severely Underweight'), (18.5, 'Underwight'),
                      (25,'Normal'),(30,'Overweight'),
                      (35,'Moderately Obese'),(float('inf'),'Severely Obese')]
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('Your BMI is: %.1f and the person is: %s' %(bmi,tuple2))
            break

if __name__=='__main__':
    bmicalculator()
    

