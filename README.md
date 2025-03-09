# NHL Shot Analyzer

This is a machine learning algorithim I wrote to predict the outcome of NHL shots on certain goalies. It uses a `HistGradientBoostingClassifier`

Built with Python + Jupyter Notebooks + Pandas + Scikit-Learn

Data sourced from [MoneyPuck](moneypuck.com)

## Accuracy

This is the classification report from the model:

```
   precision    recall  f1-score   support

           0       0.94      0.81      0.87     24988
           1       0.24      0.56      0.33      2699

    accuracy                           0.78     27687
   macro avg       0.59      0.68      0.60     27687
weighted avg       0.88      0.78      0.82     27687
```

It has an average accuracy of `~78%`

## License

This project is licensed under the MIT license
