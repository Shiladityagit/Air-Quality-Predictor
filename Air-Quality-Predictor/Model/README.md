Air Quality Prediction

GOAL

Implementtion of different algorithms like random forest, logistic regression, and XGBoost to see which gives better accuracy.

DATASET

https://www.kaggle.com/rohanrao/air-quality-data-in-india

DESCRIPTION

The main aim of the project is to use 3-4 algorithms to implement the models and compare all the algorithms to find out the best fitted algorithm for the model by checking the accuracy score.

WORK DONE

Analyzed the data and found insights such as correlation, missing values and plotted different plots and compared them with pre and post covid times.
Next trained model with algorithms:
SVM
Random Forest
XGBoost
In this XGBoost performed the best with 100% accuracy
MODELS USED

RBF SVM : SVM performs well on classification problems when size of dataset is not too large. Support Vector Machine can also be used as a regression method, maintaining all the main features that characterize the algorithm (maximal margin).
Random Forest : It provides higher accuracy through cross validation. Random forest regressor will handle the missing values and maintain the accuracy of a large proportion of data. If there are more trees, it won't allow over-fitting trees in the model.
XGBoost : XGBoost is a library for developing fast and high performance gradient boosting tree models. XGBoost achieves the best performance on a range of difficult machine learning tasks.
LIBRARIES NEEDED

Numpy
Pandas
Matplotlib
scikit-learn
xgboost
seaborn
missingno
chart_studio
cufflinks
PLOTS



CONCLUSION

We investigated the data, checking for data unbalancing, visualizing the features, and understanding the relationship between different features. We made a comparision of data between pre covid times (2015-2019) and Post covid times (>2020). We then investigated three predictive models. We saw we had imbalanced dataset. This will cause data imbalance problem. In order to overcome this problem we use the technique called SMOTE(Synthetic Minority Oversampling Technique). This approach solve this problem by oversample the examples in the minority class.

We predicted with models SVM, Random Forest and XGBoost and found accuracy of 96.15%, 99.89% and 100% on test dataset.

We also concluded that :

Vehicular pollution contents are more related to air quality index.
Delhi is the most polluted city in terms of vehicular pollution contents.
Ahmadabad is the most polluted city in terms of industrial pollution content.
After COVID19 pandemic there is gradual dicrease in vehicular pollution contents, industrial pollution content.
Random Forest classifier 99.97% accurately classify the target variable.