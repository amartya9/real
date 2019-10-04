
# coding: utf-8

# In[ ]:


import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'id':2, 'groups':2, 'active_lifestyle':3,'age':4,'healthy_eating':5})

print(r.json())

