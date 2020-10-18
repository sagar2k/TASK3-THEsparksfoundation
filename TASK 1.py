#!/usr/bin/env python
# coding: utf-8

# ## TASK-1
# ## Prediction using Supervised ML
# ## B.Chandra sagar

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


url='https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv'


# In[3]:


data=pd.read_csv(url)


# In[4]:


data


# In[70]:


#plotting the data
plt.plot(data['Hours'],data['Scores'],'o')
plt.xlabel('Hours studied')
plt.ylabel('Percentage score')
plt.title('Hours vs Percentage');


# ## From the graph it is clear that there is a positive linear relationship between percentage score and hours studied

# In[34]:


#preparing data
x=np.array(data['Hours']).reshape(-1,1)
y=data['Scores']


# In[24]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)


# In[25]:


#linear Regression
from sklearn.linear_model import LinearRegression
L=LinearRegression().fit(x_train,y_train)
print('Training complete')


# In[33]:


#plotting regression line
graph=L.coef_*x+L.intercept_
plt.plot(x,y,'o')
plt.plot(x,graph,)
plt.xlabel('Hours studied')
plt.ylabel('Marks Scored')


# In[58]:


#comparing actual and predicted values
y_pred=L.predict(x_test)
pd.DataFrame({'Actual':y_test,'Predicted':y_pred})


# In[71]:


#testing with our own data
x_own=9.25
y_pred1=L.predict(np.array(x_own).reshape(-1,1))
print('Number of Hours {}'.format(x_own))
print('Percentage scored {}'.format(y_pred1))


# In[72]:


#Evaluating the model
from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred))


# In[ ]:




