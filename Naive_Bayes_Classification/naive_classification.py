# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:20:29 2020

@author: KrmFitt
"""

import pandas as pd
import sqlalchemy as sql

connect_string = 'mysql://karim:karim@192.168.1.226:3306/karirm'

sql_engine = sql.create_engine(connect_string)

query =query = "select * from karim_article"
df = pd.read_sql_query(query, sql_engine)

# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:12:46 2020

@author: DELL
"""

import pandas as pd
import sqlalchemy as sql
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

connect_string = 'mysql://karim:karim@192.168.1.226:3306/karirm'

sql_engine = sql.create_engine(connect_string)

query =query = "select * from karim_article"
dataset = pd.read_sql_query(query, sql_engine)



#1. Prepare the data
lb_make = LabelEncoder()
dataset['tag_code'] = lb_make.fit_transform(dataset['tag'])

labales=dataset[['tag_code','tag']]
labales.sort_values("tag_code", inplace = True) 
labales.drop_duplicates(subset ="tag", keep = 'last', inplace = True) 
  

#2. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(dataset['title'], dataset['tag_code'], random_state=1)

#-----------
#.3 Convert abstracts into word count vectors
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

#.3.  view the data and investigate the word counts
word_freq_df = pd.DataFrame(X_train_cv.toarray(), columns=cv.get_feature_names())
top_words_df = pd.DataFrame(word_freq_df.sum()).sort_values(0, ascending=False)


#4. Fit the model and make predictions
#Now we’re ready to fit a Multinomial Naive Bayes classifier model to our training data and use it to predict the test data’s labels:
from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_cv, y_train)
predictions = naive_bayes.predict(X_test_cv)



#5. Check the results
#Let’s see how the model performed on the test data:
from sklearn.metrics import accuracy_score, precision_score, recall_score
print('Accuracy score : ', accuracy_score(y_test, predictions))
print('Precision score: ', precision_score(y_test, predictions))
print('Recall score   : ', recall_score(y_test, predictions))



#To understand these scores, it helps to see a breakdown:
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, square=True, annot=True, cmap='RdBu', cbar=False,
xticklabels=['sport', 'monde','culture','regions','economie','societe','sante-science-technologie'], yticklabels=['sport', 'monde','culture','regions','economie','societe','sante-science-technologie'])
plt.xlabel('true label')
plt.ylabel('predicted label')




#6. Investigate the model’s misses
#To investigate the incorrect labels, we can put the actual labels and the predicted labels side-by-side in a DataFrame.
sr_karim2=pd.Series( predictions);
sr_karim1=X_test.reset_index()
df_karim=pd.concat([sr_karim1,sr_karim2], axis=1)
df_karim.columns = ['index','title','tag_code']

df_karim['tag_name']=lb_make.inverse_transform(df_karim['tag_code'])


testing_predictions = []
for i in range(len(X_test)):
    
    
    
    if predictions[i] == 1:
        testing_predictions.append('culture')
    else:
        if predictions[i] == 0:
            
            testing_predictions.append('algerie')
check_df = pd.DataFrame({'actual_label': list(y_test), 'prediction': testing_predictions, 'abstract':list(X_test)})

check_df = pd.DataFrame.from_dict(testing_predictions, orient='index')
check_df.replace(to_replace=1, value='algerie', inplace=True)
check_df.replace(to_replace=0, value='culture', inplace=True)

