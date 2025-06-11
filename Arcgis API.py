#!/usr/bin/env python
# coding: utf-8

# In[22]:


from arcgis.gis import GIS

# Replace with your ArcGIS Online credentials
gis = GIS("https://www.arcgis.com", username="vjanga", password="xxxxxxxx")

# Confirm connection
print(f"Logged in as: {gis.users.me.username}")


# In[28]:


story_item = gis.content.get("f731becca7b54f7491f71e477e37494f")

print(f"Title: {story_item.title}")
print(f"Type: {story_item.type}")
print(f"Owner: {story_item.owner}")


# In[ ]:




