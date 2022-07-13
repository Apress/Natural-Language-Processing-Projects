import pandas as pd
import numpy as np


def text_to_features(sent, i):
    word = sent[i][0]
    

    features = {
        'bias': 1.0,
        'word.lower()': word.lower(),
        'word[-3:]': word[-3:],
        'word[-2:]': word[-2:],
        'word.isupper()': word.isupper(),
        'word.istitle()': word.istitle(),
        'word.isdigit()': word.isdigit(),
        
        
    }
    if i > 0:
        word1 = sent[i-1][0]
        
        features.update({
            '-1:word.lower()': word1.lower(),
            '-1:word.istitle()': word1.istitle(),
            '-1:word.isupper()': word1.isupper(),
            
            
        })
    else:
      features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
       
        features.update({
            '+1:word.lower()': word1.lower(),
            '+1:word.istitle()': word1.istitle(),
            '+1:word.isupper()': word1.isupper(),
            
            
        })
    else:
        features['EOS'] = True

    return features
