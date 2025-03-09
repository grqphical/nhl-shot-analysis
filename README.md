# NHL Shot Analyzer

This is a machine learning algorithim I wrote to predict the outcome of NHL shots on certain goalies. It uses a `HistGradientBoostingClassifier`

There are two models in the notebook: a small model trained on 2023 data and a large model trained on 2008-2023 data

Built with Python + Pandas + Scikit-Learn

Data sourced from [MoneyPuck](moneypuck.com)

## Accuracy

### Small Model Accuracy:

```
   precision    recall  f1-score   support

           0       0.94      0.81      0.87     24988
           1       0.24      0.56      0.33      2699

    accuracy                           0.78     27687
   macro avg       0.59      0.68      0.60     27687
weighted avg       0.88      0.78      0.82     27687
```

It has an average accuracy of `~78%`

### Large Model Accuracy:

```
              precision    recall  f1-score   support

           0       0.95      0.88      0.91    396739
           1       0.28      0.49      0.36     38819

    accuracy                           0.84    435558
   macro avg       0.61      0.68      0.63    435558
weighted avg       0.89      0.84      0.86    435558
```

It has an average accuracy of `~84%`

## License

This project is licensed under the MIT license
