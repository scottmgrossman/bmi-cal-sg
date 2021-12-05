#!/usr/bin/env python
# coding: utf-8

# In[4]:


from pywebio.input import *
from pywebio.output import *


def bmicalculator():
    height=input('Please enter your height inches ',type=FLOAT)
    weight=input('Please enter your weight in pounds',type=FLOAT)
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16,'Severely underweight'), (18.5, 'Underwight'),
                      (25,'Normal'),(30,'Overweight'),
                      (35,'Moderately obese'),(float('inf'),'Severely obese')]
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('The BMI is: %.1f and the person is: %s' %(bmi,tuple2))
            break

if __name__=='__main__':
    bmicalculator()
    

