
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import json


# In[2]:


df = pd.read_csv("2018-01-01-bus-positions.csv")


# In[ ]:


#remove all unnecessary columns from the dataset


# In[3]:


df = df.drop(["trip_start_time", "vehicle_label", "vehicle_license_plate", "occupancy_status", "congestion_level", "progress",
                  "block_assigned", "dist_along_route", "dist_from_stop"], axis=1) #get rid of the Nan column




# In[ ]:


#get all the vehicles running around the city


# In[5]:


data_lst = []
for element in df["vehicle_id"]:
    if element not in data_lst:
        data_lst.append(element)
print(len(data_lst))


# In[6]:


# get one vehicle from the dataset as a demo

df1 = df[df["vehicle_id"] == "MTA NYCT_8204"]


# In[7]:


#create the name for the file
#sort the data by time
#export the dataset as a csv file


name = "cleanedMTA NYCT_8204.csv"
df1 = df1.sort_values(by='timestamp',ascending=True)
# df1.to_csv(name)


# In[66]:


def get_streetnames(latlong_lst):
    apikey = ""
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + str(latlong_lst[0]) + "," + str(latlong_lst[1]) + "&key=" + apikey
    json_res = requests.post(url)
    my_json = json_res.content.decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    name = data["results"][0]["formatted_address"]
    return name


# In[31]:


df_test = df1.iloc[0:1,:]


# In[44]:


a = df_test[["latitude", "longitude"]].apply(get_streetnames,axis = 1)


# In[71]:


df1["street name"] = df1[["latitude", "longitude"]].apply(get_streetnames,axis = 1)


# In[62]:





# In[68]:





# In[73]:


df1 = df1.sort_values(by='timestamp',ascending=True)


# In[74]:




