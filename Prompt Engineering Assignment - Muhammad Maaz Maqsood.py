#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install -q -U google-generativeai


# In[7]:


import google.generativeai as genai
GOOGLE_API_KEY = 'AIzaSyC13aEFB4mVTWqVzBHJS2O5QAwuC7eFew4'
genai.configure(api_key=GOOGLE_API_KEY)


# In[8]:


for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)


# In[11]:


import textwrap
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# In[12]:


model = genai.GenerativeModel('gemini-pro')


# # Ideal Career Visualization Prompt:

# Develop a prompt to help individuals envision their ideal career path, including job responsibilities, work environment, and fulfillment.

# In[22]:


response = model.generate_content("I want you to act as a career counselor. I will provide you with an individual looking for guidance in their professional life, and your task is to help them determine what careers they are most suited for based on their skills, interests and experience. You should also conduct research into the various options available, explain the job market trends in different industries and advice on which qualifications would be beneficial for pursuing particular fields. My first request is [I want to advise someone who wants to pursue a potential career in Business Analytics].")


# In[23]:


to_markdown(response.text)


# In[24]:


response = model.generate_content("I want you to act as a career counselor. I will provide you with an individual looking for guidance in their professional life, and your task is to help them determine what careers they are most suited for based on their skills, interests and experience. You should also conduct research into the various options available, explain the job market trends in different industries and advice on which qualifications would be beneficial for pursuing particular fields. Then conduct research on the likely job titles and the respective job responsibilities the individual would have to perform while pursing a career in that particular field. My first request is [I want to advise someone who wants to pursue a potential career in Business Analytics].")


# In[25]:


to_markdown(response.text)


# In[26]:


response = model.generate_content("I want you to act as a career counselor. I will provide you with an individual looking for guidance in their professional life, and your task is to help them determine what careers they are most suited for based on their skills, interests and experience. You should also conduct research into the various options available, explain the job market trends in different industries and advice on which qualifications would be beneficial for pursuing particular fields. Then conduct research on the likely job titles and the respective job responsibilities the individual would have to perform while pursing a career in that particular field.  Next you must compare the job market of Pakistan, Middle East, USA, Canada, Europe and Australia for that field. Finally, explain the work environment in each region. My first request is [I want to advise someone who wants to pursue a potential career in Business Analytics].")


# In[27]:


to_markdown(response.text)


# In[28]:


response = model.generate_content("I want you to act as a career counselor. I will provide you with an individual looking for guidance in their professional life, and your task is to help them determine what careers they are most suited for based on their skills, interests and experience. You should also conduct research into the various options available, explain the job market trends in different industries and advice on which qualifications would be beneficial for pursuing particular fields. Then conduct research on the likely job titles and the respective job responsibilities the individual would have to perform while pursing a career in that particular field.  Next you must compare the job market of Pakistan, Middle East, USA, Canada, Europe and Australia for that field. Then explain the work environment in each region. Lastly, advice which sector to target in each region. My first request is [I want to advise someone who wants to pursue a potential career in Business Analytics].")


# In[29]:


to_markdown(response.text)


# In[ ]:




