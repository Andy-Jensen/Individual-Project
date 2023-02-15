import numpy as np
import pandas as pd
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import sklearn.preprocessing
from sklearn.preprocessing import MinMaxScaler

def explore_conflict():
    '''
    This function gets the data from the local machine and cleans/prepares the data for the explore phase of the project.
    Calculates target variable
    Drops unnecessart columns
    Encodes some columns
    '''
    conflict=pd.read_csv('ucdp-prio-acd-221.csv')
    conflict['start_date']=pd.to_datetime(conflict['start_date'])
    conflict['start_date2']=pd.to_datetime(conflict['start_date2'])
    conflict['time_to_conflict']= conflict['start_date2'].subtract(conflict['start_date'])
    conflict['time_to_conflict']=(conflict['time_to_conflict']/ np.timedelta64(1, 'D')).astype('int')
    
    
    clean = pd.DataFrame(columns=conflict.columns)
    unique = list(conflict['conflict_id'].unique())
    for n in unique:
        add = conflict[conflict['conflict_id']==n].sort_values(by=['year'], ascending=True).iloc[:1]
        clean = pd.concat([clean, add], axis=0, ignore_index=True)
        
    clean=clean.drop(columns=['version', 'ep_end', 'ep_end_date', 'ep_end_prec', 'cumulative_intensity', 'gwno_a',
                              'gwno_a_2nd', 'gwno_b', 'gwno_b_2nd', 'gwno_loc', 'start_prec', 'start_prec2', 'side_a_id',
                              'side_b_id', 'conflict_id', 'intensity_level', 'year'])
    
    for i, n in enumerate(clean['side_a_2nd']):
        if pd.isna(n):
            clean.at[i, 'side_a_2nd'] = 0
        else:
            clean.at[i, 'side_a_2nd'] = 1
    
    for i, n in enumerate(clean['side_b_2nd']):
        if pd.isna(n):
            clean.at[i, 'side_b_2nd'] = 0
        else:
            clean.at[i, 'side_b_2nd'] = 1
    
    for i, n in enumerate(clean['territory_name']):
        if pd.isna(n):
            clean.at[i, 'territory_name'] = 'Government'
    clean['time_to_conflict']=clean['time_to_conflict'].astype('int')
    return clean

def tts(df, stratify=None):
    '''
    removing your test data from the data
    '''
    train_validate, test=train_test_split(df, 
                                 train_size=.9, 
                                 random_state=8675309,
                                 stratify=None)
    '''
    splitting the remaining data into the train and validate groups
    '''            
    train, validate =train_test_split(train_validate, 
                                      test_size=.2, 
                                      random_state=8675309,
                                      stratify=None)
    return train, validate, test