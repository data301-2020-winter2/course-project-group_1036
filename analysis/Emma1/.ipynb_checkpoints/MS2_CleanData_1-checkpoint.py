#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

def load_clean_Art_and_History(path):
    Art_and_History = (pd.read_csv(path, header = 'infer')
                     .rename(columns = {'User':'Google User ID','Category 1':'Churches','Category 2':'Resorts',
                          'Category 3':'Beaches','Category 4':'Parks','Category 5':'Theatres',
                          'Category 6':'Museums','Category 7':'Malls','Category 8':'Zoos',
                          'Category 9':'Restaurants','Category 10':'Pubs & Bars','Category 11':'Local Services',
                          'Category 12':'Burger & Pizza Shops','Category 13':'Hotels & Lodgings','Category 14':'Juice Bars',
                          'Category 15':'Art Galleries','Category 16':'Dance Clubs','Category 17':'Swimming Pools',
                          'Category 18':'Gyms','Category 19':'Bakeries','Category 20':'Beauty & Spas',
                          'Category 21':'Cafes','Category 22':'View Points', 'Category 23':'Monuments','Category 24':'Gardens'})


                    .drop(['Resorts', 'Beaches', 'Parks', 'Malls', 'Zoos', 'Restaurants','Pubs & Bars','Local Services',
                          'Burger & Pizza Shops','Hotels & Lodgings','Juice Bars','Dance Clubs','Swimming Pools','Gyms',
                          'Bakeries','Beauty & Spas','Cafes','View Points','Gardens'], axis=1)
                    )
    Art_and_History = Art_and_History[(Art_and_History != 0).all(1)]

    Art_and_History.to_csv('../../data/processed/Art_and_History_Cleaned.csv')

    return Art_and_History

def load_clean_Food_and_Beverage(path):
    Food_and_Beverage = (pd.read_csv(path, header = 'infer')
                     .rename(columns = {'User':'Google User ID','Category 1':'Churches','Category 2':'Resorts','Category 3':'Beaches',
                          'Category 4':'Parks','Category 5':'Theatres','Category 6':'Museums','Category 7':'Malls','Category 8':'Zoos',
                          'Category 9':'Restaurants','Category 10':'Pubs & Bars','Category 11':'Local Services',
                          'Category 12':'Burger & Pizza Shops','Category 13':'Hotels & Lodgings','Category 14':'Juice Bars',
                          'Category 15':'Art Galleries','Category 16':'Dance Clubs','Category 17':'Swimming Pools','Category 18':'Gyms',
                          'Category 19':'Bakeries','Category 20':'Beauty & Spas','Category 21':'Cafes','Category 22':'View Points',
                          'Category 23':'Monuments','Category 24':'Gardens'})


                    .drop(['Churches','Resorts','Beaches','Parks','Theatres','Museums','Malls','Zoos',
                           'Local Services','Hotels & Lodgings','Art Galleries','Dance Clubs','Swimming Pools',
                           'Gyms','Beauty & Spas','View Points','Monuments','Gardens'], axis=1)
                    )
    Food_and_Beverage = Food_and_Beverage[(Food_and_Beverage != 0).all(1)]

    Food_and_Beverage.to_csv('../../data/processed/Food_and_Beverage_Cleaned.csv')

    return Food_and_Beverage

def load_clean_Ammenities(path):
    Ammenities = (pd.read_csv(path, header = 'infer')
                     .rename(columns = {'User':'Google User ID','Category 1':'Churches','Category 2':'Resorts','Category 3':'Beaches',
                          'Category 4':'Parks','Category 5':'Theatres','Category 6':'Museums','Category 7':'Malls','Category 8':'Zoos',
                          'Category 9':'Restaurants','Category 10':'Pubs & Bars','Category 11':'Local Services',
                          'Category 12':'Burger & Pizza Shops','Category 13':'Hotels & Lodgings','Category 14':'Juice Bars',
                          'Category 15':'Art Galleries','Category 16':'Dance Clubs','Category 17':'Swimming Pools','Category 18':'Gyms',
                          'Category 19':'Bakeries','Category 20':'Beauty & Spas','Category 21':'Cafes','Category 22':'View Points',
                          'Category 23':'Monuments','Category 24':'Gardens'})


                    .drop(['Resorts','Beaches','Theatres','Museums','Zoos','Restaurants','Pubs & Bars',
                           'Burger & Pizza Shops','Juice Bars','Art Galleries','Dance Clubs','Swimming Pools',
                           'Bakeries','Beauty & Spas','Cafes','View Points','Monuments','Gardens'], axis=1)
                    )
    Ammenities = Ammenities[(Ammenities != 0).all(1)]

    Ammenities.to_csv('../../data/processed/Ammenities_Cleaned.csv')

    return Ammenities

def load_clean_Recreation(path):
    Recreation = (pd.read_csv(path, header = 'infer')
                     .rename(columns = {'User':'Google User ID','Category 1':'Churches','Category 2':'Resorts','Category 3':'Beaches',
                          'Category 4':'Parks','Category 5':'Theatres','Category 6':'Museums','Category 7':'Malls','Category 8':'Zoos',
                          'Category 9':'Restaurants','Category 10':'Pubs & Bars','Category 11':'Local Services',
                          'Category 12':'Burger & Pizza Shops','Category 13':'Hotels & Lodgings','Category 14':'Juice Bars',
                          'Category 15':'Art Galleries','Category 16':'Dance Clubs','Category 17':'Swimming Pools','Category 18':'Gyms',
                          'Category 19':'Bakeries','Category 20':'Beauty & Spas','Category 21':'Cafes','Category 22':'View Points',
                          'Category 23':'Monuments','Category 24':'Gardens'})


                    .drop(['Churches','Theatres','Museums','Malls','Restaurants','Pubs & Bars','Local Services',
                           'Burger & Pizza Shops','Hotels & Lodgings','Juice Bars','Art Galleries','Gyms',
                           'Bakeries','Cafes','Monuments'], axis=1)
                    )
    Recreation = Recreation[(Recreation != 0).all(1)]
    df = df.append(line, ignore_index=False)
    df = df.sort_index().reset_index(drop=True)
    df = df.reindex(['Name', 'Age'], axis=1)
    OutdoorClassifier = [ False, True, True, False, False, False, False, True, True ] 

    Recreation.to_csv('../../data/processed/Recreation_Cleaned.csv')

    return Recreation


# In[ ]:





# In[ ]:





# In[ ]:




