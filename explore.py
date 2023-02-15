import numpy as np
import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from prepare import explore_conflict, tts


def target(conflict):
    '''
    this plots an initial look at the target variable
    '''
    plt.figure(figsize=(10,10))
    low=conflict[conflict['time_to_conflict']<7000]
    sns.histplot(x='time_to_conflict', data=low)
    plt.title('All Conflict\'s Time to Conflict')
    plt.xlabel('Time to Conflict')
    plt.show()



def q1_plots(train):
    '''
    This function plots the necessary plots to visualize explore question 1
    '''
    asia=train[train['region']=='3']
    notasia=train[train['region']!='3']
    plt.figure(figsize=(10,5))
    plt.subplot(221)
    sns.histplot(x='time_to_conflict', data=asia)
    plt.title('Time to Conflict (Asia)')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')

    plt.subplot(222)
    sns.histplot(x='time_to_conflict', data=notasia)
    plt.title('All Regions Excluding Asia')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.figure(figsize=(25,10))
    plt.subplot(223)
    plt.title('Asia vs Other Regions (Time to Conflict)')
    sns.histplot(x='time_to_conflict', data=asia, alpha=.5, color='green', label= 'Asia')
    sns.histplot(x='time_to_conflict', data=notasia, alpha=.5, label='Regions not Asia')
    plt.xlabel('Time to Conflict')
    plt.axvline(x=(asia['time_to_conflict'].mean()), color='red', label='Asia Mean')
    plt.axvline(x=(notasia['time_to_conflict'].mean()), color='yellow', label='Regions not Asia Mean')
    plt.legend()
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.subplots_adjust(left=0.1,
                            bottom=-0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    plt.show()
    
    asiam=round(asia['time_to_conflict'].mean(),2)
    notasiam=round(notasia['time_to_conflict'].mean(),2)
    print(f'The mean time to conflict for Asia is {asiam}.')
    print(f'The mean time to conflict for all other regions is {notasiam}.')



def q1_stat(train):
    '''
    this function will perform the statistical test for question 1
    '''
    asia=train[train['region']=='3']
    notasia=train[train['region']!='3']
    t, p=stats.ttest_ind(asia['time_to_conflict'], notasia['time_to_conflict'], alternative='greater')
    alpha = 0.05
    if p < alpha:
        print('After an independent t-test was conducted:')
        print(f'The p-value ({round(p,3)}) is lower than the alpha ({alpha}).')



def q2_plots(train):
    '''
    This function plots the necessary plots to visualize explore question 2
    '''
    ame=train[(train['region']=='2') | (train['region']=='4')]
    
    plt.figure(figsize=(10,5))
    plt.subplot(221)
    sns.histplot(x='time_to_conflict', data=ame)
    plt.title('Time to Conflict (Africa and Middle East)')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')

    plt.subplot(222)
    sns.histplot(x='time_to_conflict', data=train)
    plt.title('All Regions')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.figure(figsize=(25,10))
    plt.subplot(223)
    plt.title('Africa and Middle East vs All Regions (Time to Conflict)')
    sns.histplot(x='time_to_conflict', data=ame, alpha=.5, color='green', label= 'Africa and Middle East')
    sns.histplot(x='time_to_conflict', data=train, alpha=.5, label='All Regions')
    plt.xlabel('Time to Conflict')
    plt.axvline(x=(ame['time_to_conflict'].mean()), color='red', label='Africa and Middle East Mean')
    plt.axvline(x=(train['time_to_conflict'].mean()), color='yellow', label='All Regions Mean')
    plt.legend()
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.subplots_adjust(left=0.1,
                            bottom=-0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    plt.show()
    
    asiam=round(ame['time_to_conflict'].mean(),2)
    notasiam=round(train['time_to_conflict'].mean(),2)
    print(f'The mean time to conflict for Africa and the Middle East is {asiam}.')
    print(f'The mean time to conflict for all regions is {notasiam}.')



def q2_stat(train):
    '''
    this function will perform the nessessary stat test for question 2
    '''
    ame=train[(train['region']=='2') | (train['region']=='4')]
    trainmean=train['time_to_conflict'].mean()
    t, p = stats.ttest_1samp(ame['time_to_conflict'], trainmean, alternative='less')
    alpha = 0.05
    if p > alpha:
        print('After a one sample t-test was conducted:')
        print(f'The p-value ({round(p,3)}) is not lower than the alpha ({alpha}).')


def q3_plots(train):
    '''
    This function plots the necessary plots to visualize explore question 3
    '''
    intra=train[(train['type_of_conflict']==3)&(train['incompatibility']==2)]
    inter=train[(train['type_of_conflict']==2)&(train['incompatibility']==1)]
    
    plt.figure(figsize=(10,5))
    plt.subplot(221)
    sns.histplot(x='time_to_conflict', data=intra)
    plt.title('Time to Conflict (Intrastate/Government)')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')

    plt.subplot(222)
    sns.histplot(x='time_to_conflict', data=inter)
    plt.title('Time to Conflict (Interstate/Territory)')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.figure(figsize=(25,10))
    plt.subplot(223)
    plt.title('Intrastate/Government vs Interstate/Territory Time to Conflict')
    sns.histplot(x='time_to_conflict', data=intra, alpha=.2, color='green', label= 'Intrastate/Government')
    sns.histplot(x='time_to_conflict', data=inter, alpha=1, label='Interstate/Territory')
    plt.xlabel('Time to Conflict')
    plt.axvline(x=(intra['time_to_conflict'].mean()), color='red', label='Intrastate/Government')
    plt.axvline(x=(inter['time_to_conflict'].mean()), color='yellow', label='Interstate/Territory')
    plt.legend()
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.subplots_adjust(left=0.1,
                            bottom=-0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    plt.show()
    
    asiam=round(intra['time_to_conflict'].mean(),2)
    notasiam=round(inter['time_to_conflict'].mean(),2)
    print(f'The mean time to conflict for countries with intrastate conflict over government is {asiam}.')
    print(f'The mean time to conflict for countries with an interstate conflict over territory is {notasiam}.')


def q3_stat(train):
    '''
    this function performs the necessary stats test for question 3
    '''
    intra=train[(train['type_of_conflict']==3)&(train['incompatibility']==2)]
    inter=train[(train['type_of_conflict']==2)&(train['incompatibility']==1)]
    t, p=stats.mannwhitneyu(intra['time_to_conflict'], inter['time_to_conflict'], alternative='greater')
    alpha = 0.05
    if p > alpha:
        print('After a mannwhitneyu stats test was conducted:')
        print(f'The p-value ({round(p,3)}) is greater than the alpha ({alpha}).')


def q4_plots(train):
    '''
    This function plots the necessary plots to visualize explore question 4
    '''
    ii=train[train['type_of_conflict']==4]
    
    plt.figure(figsize=(10,5))
    plt.subplot(221)
    sns.histplot(x='time_to_conflict', data=ii)
    plt.title('Internationalized Intrastate Time to Conflict')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')

    plt.subplot(222)
    sns.histplot(x='time_to_conflict', data=train)
    plt.title('All Regions')
    plt.xlabel('Time to Conflict (days)')
    plt.grid(True, alpha=0.3, linestyle='--')
    
    plt.figure(figsize=(25,10))
    plt.subplot(223)
    plt.title('Internationalized Intrastate vs All Regions Time to Conflict')
    sns.histplot(x='time_to_conflict', data=ii, alpha=.5, color='green', label= 'Internationalized Intrastate')
    sns.histplot(x='time_to_conflict', data=train, alpha=.25, label='All Regions')
    plt.xlabel('Time to Conflict')
    plt.axvline(x=(ii['time_to_conflict'].mean()), color='red', label='Internationalized Intrastate')
    plt.axvline(x=(train['time_to_conflict'].mean()), color='yellow', label='All Regions Mean')
    plt.legend()
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.subplots_adjust(left=0.1,
                            bottom=-0.1,
                            right=0.9,
                            top=0.9,
                            wspace=0.4,
                            hspace=0.4)
    plt.show()
    
    asiam=round(ii['time_to_conflict'].mean(),2)
    notasiam=round(train['time_to_conflict'].mean(),2)
    print(f'The mean time to conflict for Internationalized Intrastate conflicts is {asiam}.')
    print(f'The mean time to conflict for all regions is {notasiam}.')


def q4_stat(train):
    '''
    this function performs the necessary stats test for question 4
    '''
    ii=train[train['type_of_conflict']==4]
    ii2=[]
    for x in ii['time_to_conflict']:
        ii2.append(x-359)
    t,p=stats.wilcoxon(ii2, alternative='less')
    alpha = 0.05
    if p < alpha:
        print('After a wilcoxon stats test was conducted:')
        print(f'The p-value ({round(p,3)}) is lower than the alpha ({alpha}).')