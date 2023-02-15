import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

from prepare import tts, explore_conflict

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

def model_prep():
    '''
    this function prepares the data for modeling
    '''
    conflict=explore_conflict()
    for i, n in enumerate(conflict['location']):
        if n=='India':
            conflict.at[i, 'location'] = 0
        elif n=='Russia (Soviet Union)':
            conflict.at[i, 'location'] = 1
        elif n=='Myanmar (Burma)':
            conflict.at[i, 'location'] = 2
        elif n=='Ethiopia':
            conflict.at[i, 'location'] = 3
        elif n=='Indonesia':
            conflict.at[i, 'location'] = 4
        elif n=='Nigeria':
            conflict.at[i, 'location'] = 5
        elif n=='DR Congo (Zaire)':
            conflict.at[i, 'location'] = 6
        elif n=='Iran':
            conflict.at[i, 'location'] = 7
        elif n=='Ukraine':
            conflict.at[i, 'location'] = 8
        elif n=='Pakistan':
            conflict.at[i, 'location'] = 9
        else:
            conflict.at[i, 'location'] = 10
    for i, n in enumerate(conflict['side_a']):
        if n=='Government of India':
            conflict.at[i, 'side_a'] = 0
        elif n=='Government of France':
            conflict.at[i, 'side_a'] = 1
        elif n=='Government of Russia (Soviet Union)':
            conflict.at[i, 'side_a'] = 2
        elif n=='Government of Myanmar (Burma)':
            conflict.at[i, 'side_a'] = 3
        elif n=='Government of Ethiopia':
            conflict.at[i, 'side_a'] = 4
        elif n=='Government of China':
            conflict.at[i, 'side_a'] = 5
        elif n=='Government of Iran':
            conflict.at[i, 'side_a'] = 6
        elif n=='Government of United Kingdom':
            conflict.at[i, 'side_a'] = 7
        elif n=='Government of Indonesia':
            conflict.at[i, 'side_a'] = 8
        elif n=='Government of DR Congo (Zaire)':
            conflict.at[i, 'side_a'] = 9
        else:
            conflict.at[i, 'side_a'] = 10 
    for i, n in enumerate(conflict['side_b']):
        if n=='IS':
            conflict.at[i, 'side_b'] = 0
        elif n=='Government of Thailand':
            conflict.at[i, 'side_b'] = 1
        elif n=='Government of United Kingdom':
            conflict.at[i, 'side_b'] = 2
        elif n=='Government of Russia (Soviet Union)':
            conflict.at[i, 'side_b'] = 3
        elif n=='Government of Israel':
            conflict.at[i, 'side_b'] = 4
        elif n=='Government of Vietnam (North Vietnam)':
            conflict.at[i, 'side_b'] = 5
        elif n=='Government of Iraq':
            conflict.at[i, 'side_b'] = 6
        elif n=='PLA':
            conflict.at[i, 'side_b'] = 7
        elif n=='UCK':
            conflict.at[i, 'side_b'] = 8
        elif n=='POLISARIO':
            conflict.at[i, 'side_b'] = 9
        elif n=='National Liberation Army':
            conflict.at[i, 'side_b'] = 10
        elif n=='Government of India':
            conflict.at[i, 'side_b'] = 11
        elif n=='CPM':
            conflict.at[i, 'side_b'] = 12
        elif n=='Government of Nigeria':
            conflict.at[i, 'side_b'] = 13
        elif n=='Government of United States of America':
            conflict.at[i, 'side_b'] = 14
        elif n=='NLA':
            conflict.at[i, 'side_b'] = 15
        elif n=='CPI':
            conflict.at[i, 'side_b'] = 16
        elif n=='UPC':
            conflict.at[i, 'side_b'] = 17
        elif n=='Military faction (navy)':
            conflict.at[i, 'side_b'] = 18
        elif n=='AQIM':
            conflict.at[i, 'side_b'] = 19
        else:
            conflict.at[i, 'side_b'] = 20
    for i, n in enumerate(conflict.start_date.astype('str').str.startswith('19')):
        if n==True:
            conflict.at[i, 'start_date'] = 0
        else:
            conflict.at[i, 'start_date'] = 1
    for i, n in enumerate(conflict['time_to_conflict']):
        if n<=30:
            conflict.at[i, 'time_to_conflict'] = 1
        elif 30<n<=365:
            conflict.at[i, 'time_to_conflict'] = 2
        elif n>365:
            conflict.at[i, 'time_to_conflict'] = 3
    conflict=pd.get_dummies(conflict, columns=['location','side_a', 'side_a_2nd', 'side_b',
                                           'side_b_2nd', 'type_of_conflict',
                                           'region', 'incompatibility', 'start_date'])
    conflict=conflict.drop(columns=['territory_name', 'start_date2'])
    conflict=conflict.astype('int')
    return conflict


def models(train, val):
    '''
    this function prints results for models
    '''
    x_train= train.drop(columns=['time_to_conflict'])
    y_train= train['time_to_conflict']

    x_val= val.drop(columns=['time_to_conflict'])
    y_val= val['time_to_conflict']
    
    results=[]
    logit = LogisticRegression(C=.5, random_state=8675309, intercept_scaling=1, solver='lbfgs')
    logit.fit(x_train, y_train)
    in_sample=logit.score(x_train,y_train)
    out_of_sample=logit.score(x_val, y_val)
    output={
        'model': 'LogisticRegression (lbfgs)',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    logit = LogisticRegression(C=1, random_state=8675309, solver='liblinear')
    logit.fit(x_train, y_train)
    in_sample=logit.score(x_train,y_train)
    out_of_sample=logit.score(x_val, y_val)
    output={
        'model': 'LogisticRegression (liblinear)',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    knn= KNeighborsClassifier(n_neighbors=3, weights='uniform')
    knn.fit(x_train,y_train)
    in_sample= knn.score(x_train, y_train)
    out_of_sample= knn.score(x_val, y_val)
    output={
        'model': 'KNeighborsClassifier',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    dtc=DecisionTreeClassifier(max_depth=2, min_samples_leaf=1, random_state=8675309)
    dtc.fit(x_train, y_train)
    in_sample= dtc.score(x_train, y_train)
    out_of_sample= dtc.score(x_val, y_val)
    output={
        'model': 'DecisionTreeClassifier',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    rm= RandomForestClassifier(max_depth= 2, min_samples_leaf= 1, random_state=8675309)
    rm.fit(x_train, y_train)
    in_sample= rm.score(x_train, y_train)
    out_of_sample= rm.score(x_val, y_val)
    output={
        'model': 'RandomForestClassifier',
        'train_accuracy': in_sample,
        'validate_accuracy': out_of_sample
    }
    results.append(output)
    
    results=pd.DataFrame(data=results)
    results['difference']=results['train_accuracy']-results['validate_accuracy'] 
    return results


def baseline(train):
    '''
    this function gives the baseline'''
    train['baseline']=1
    x_train= train.drop(columns=['time_to_conflict'])
    y_train= train['time_to_conflict']
    base=accuracy_score(y_train, train['baseline'])
    train=train.drop(columns=['baseline'])
    return print(f'The baseline to try and beat for modeling is {round(base,3)}.')


def test(train,val,test):
    '''
    this function shows the results of the test data
    '''
    x_train= train.drop(columns=['time_to_conflict'])
    y_train= train['time_to_conflict']

    x_val= val.drop(columns=['time_to_conflict'])
    y_val= val['time_to_conflict']

    x_test= test.drop(columns=['time_to_conflict'])
    y_test= test['time_to_conflict']

    results=[]
    logit = LogisticRegression(C=.5, random_state=8675309, intercept_scaling=1, solver='lbfgs')
    logit.fit(x_train, y_train)
    trainacc = logit.score(x_train,y_train)
    valacc = logit.score(x_val, y_val)
    testacc=logit.score(x_test, y_test)
    output={
        'train_accuracy': trainacc,
        'validate_accuracy': valacc,
        'test_accuracy': testacc
    }
    results.append(output)

    logit = LogisticRegression(C=1, random_state=8675309, solver='liblinear')
    logit.fit(x_train, y_train)
    trainacc2 = logit.score(x_train,y_train)
    valacc2 = logit.score(x_val, y_val)

    train['baseline']=1

    plt.figure(figsize=(10,5))
    X = ['Logistic Regression (lbfgs)','Logistic Regression (liblinear)']
    baseline=accuracy_score(y_train, train['baseline'])

    X_axis = np.arange(len(X))

    plt.bar(X_axis[0] - 0.2, trainacc, 0.2, label = 'Train Accuracy', color=['blue'], ec='black')
    plt.bar(X_axis[0] + 0, valacc, 0.2, label = 'Validate Accuracy', color=['green'], ec='black')
    plt.bar(X_axis[0] + 0.2, testacc, 0.2, label = 'Test Accuracy', color=['rebeccapurple'], ec='black')


    plt.bar(X_axis[1] - 0.1, trainacc2, 0.2, color=['blue'], ec='black')
    plt.bar(X_axis[1] + 0.1, valacc2, 0.2, color=['green'], ec='black')


    plt.axhline(y = baseline, color = 'r', linestyle = '-', label='Baseline Accuracy')

    plt.xticks(X_axis, X)
    plt.xlabel("Model")
    plt.ylabel("Accuracy")
    plt.title("Accuracy of Models vs Baseline")
    plt.ylim(.4, 1)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend()
    plt.show()
    results=pd.DataFrame(data=results)
    return results