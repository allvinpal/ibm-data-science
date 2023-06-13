#!/usr/bin/env python
# coding: utf-8

# Exercise 2 - Create a markdown cell with the title of the notebook.

# # Data Science Tools and Ecosystem

# In[ ]:


Exercise 3 - Create a markdown cell for an introduction.


# ## In this notebook, Data Science Tools and Ecosystem are summarized.
# 
# ### Objectives:
# 
# 1.List popular languages that Data Scientists use.
# 2.List commonly used libraries used by Data Scientists.
# 3.Comment on Data Science tools.

# In[ ]:


Exercise 4 - Create a markdown cell to list data science languages.


# In[ ]:


## Some of the popular languages that Data Scientists use are:

1.Python.
2.R.
3.SQL.
4.Java.
5.Julia.
6.Scala.
7.C/C++.
7.JavaScript.


# In[ ]:


Exercise 5 - Create a markdown cell to list data science libraries.


# ## Some of the commonly used libraries used by Data Scientists include:
# 
# 1.TensorFlow.
# 2.NumPy.
# 3.SciPy.
# 4.Pandas.
# 5.Matplotlib.
# 6.Keras.
# 7.SciKit-Learn.
# 8.PyTorch.
# 9.Scrapy.
# 10.BeautifulSoup.
# 11.LightGBM.
# 12.ELI5.
# 13.Theano.
# 14.NuPIC.
# 15.Ramp.
# 16.Pipenv.
# 17.Bob.
# 18.PyBrain.
# 19.Caffe2.
# 20.Chainer

# In[ ]:


Exercise 6 - Create a markdown cell with a table of Data Science tools.


# ## Data Science Tools
# 
# | Tool           | Description                                         |
# |----------------|-----------------------------------------------------|
# | Jupyter Notebook | Interactive coding environment                     |
# | Anaconda       | Distribution of Python and R for data science       |
# | RStudio        | Integrated development environment for R           |
# | Tableau        | Data visualization and business intelligence       |
# | Apache Spark   | Distributed computing framework for big data       |
# | Hadoop         | Distributed storage and processing of big data     |
# | Docker         | Containerization platform for deploying applications |
# | Git            | Version control system for code collaboration      |
# 
# These tools play a crucial role in various stages of the data science workflow, including data exploration, analysis, visualization, and collaboration. Depending on your specific needs and preferences
# 

# In[ ]:


Exercise 7 - Create a markdown cell introducing arithmetic expression examples.


# # Below are a few examples of evaluating arithmetic expressions in Python

# In[1]:


# Arithmetic operations
code = compile("5 + 4", "<string>", "eval")
eval(code)
# Result: 9


# In[2]:


code1 = compile("(5 + 7) * 2", "<string>", "eval")
eval(code1)
# Result: 24


# In[3]:


import math
# Volume of a sphere
code2 = compile("4 / 3 * math.pi * math.pow(25, 3)", "<string>", "eval")
eval(code2)
# Result: 65449.84694978735


# In[ ]:


Exercise 8 - Create a code cell to multiply and add numbers.


# This a simple arithmetic expression to mutiply then add integers

# In[4]:


(3*4)+5
# Result: 17


# In[ ]:


Exercise 9 - Create a code cell to convert minutes to hours.


# This will convert 200 minutes to hours by diving by 60

# In[5]:


days = 0
hours = 0
mins = 0

time = 200
#days = time / 1440
leftover_minutes = time % 1440
hours = leftover_minutes / 60
#mins = time - (days*1440) - (hours*60)
print(str(days) + " days, " + str(hours) + " hours, " + str(mins) +  " mins. ")

# Result: 3.3333333333333335 hours


# In[ ]:


Exercise 10 -Insert a markdown cell to list Objectives.


# Below the introduction cell created in Exercise 3, insert a new markdown cell to list the objectives that this notebook covered (i.e. some of the key takeaways from the course). In this new cell start with an introductory line titled: Objectives: in bold font. Then using an unordered list (bullets) indicate 3 to 5 items covered in this notebook, such as List popular languages for Data Science.

# In[ ]:


Exercise 11 - Create a markdown cell to indicate the Author’s name.


# # Author:
# Germano Costa
