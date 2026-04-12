> To use this project, first download the _1.0-hja-acme-analysis.ipynb_ file (found in _notebooks_), and add a copy of _ACME-HappinessSurvey2020.xlsx_ (found in _data_) to your local GDrive environment.

# Background

The goal of this machine learning exercise is to predict the satisfaction of customers based on self-reported survey data, which takes the following form:

> Y = target attribute (Y) with values indicating 0 (unhappy) and 1 (happy) customers\
X1 = my order was delivered on time\
X2 = contents of my order was as I expected\
X3 = I ordered everything I wanted to order\
X4 = I paid a good price for my order\
X5 = I am satisfied with my courier\
X6 = the app makes ordering easy for me

> Attributes X1 to X6 indicate the responses for each question and have values from 1 to 5, where the smaller number indicates less and the higher number indicates more towards the answer.\
Attribute Y indicates whether a customer is happy (1) or unhappy (0) with their order, and is the target for prediction.

By training the machine learning model(s) on available data (i.e. past survey data from customers), the likelihood that a given future customer is happy or unhappy (attribute Y) with their order can be predicted based on their answers to the survey (attributes X1 to X6).

# Process

* The process began by reviewing the available data, ensuring that there were no missing or erroneous data entries. No such issues were found.
* Next, a Pearson correlation matrix was constructed to identify (1) which attributes/features among X1 to X6 were meaningfully correlated with the target attribute Y, and (2) which attributes/features were strongly correlated with each other.

![alt text](https://github.com/hazash97/jrVziAXIJvmftE4U/blob/main/correlation.png)

> 1. Inspecting the correlations with the target attribute, features X2 ("contents of my order was as I expected") and X4 ("I paid a good price for my order") were found to have a very weak correlation with the target attribute, and thus have poor predictive power. For simplicity at this stage, it has been assumed that no higher-order interactions exist between combinations of attributes, and therefore it is reasonable to eliminate X2 and X4 as features in the model.
> 2. Inspecting the correlations of each attribute with each other attribute, we find some moderately correlated attributes - such as X1 with X5 (r=0.43) and X1 with X6 (r=0.41). However, these are not sufficiently correlated to warrant immediate elimination or combination. Therefore, the remaining feature set will remain unchanged.

* Following these preparatory steps, a selection of machine learning algorithms were trained on the data, using a repeated stratified K-fold to split the data into training and testing sets.
* A grid search was performed for each algorithm to find the best-performing hyperparameters.
* Finally, the best-performing algorithm was selected, based foremost on its f1 score.

# Outcomes

The following machine learning algorithms were tested:

| model | f1 score | hyperparameters tested |
| ----- | -------- | ----------------- |
| LogisticRegression | 0.708129 | _solvers_: newton-cg, lbfgs, **liblinear** <br>_penalty_: **l2** <br>_c_values_: 100, 10, 1.0, 0.1, **0.01** |
| SVC | 0.707719 | _kernel_: poly, rbf, **sigmoid** <br>_C_: **50**, 10, 1.0, 0.1, 0.01 <br>_gamma_: **scale** |
| BaggingClassifier | 0.676505 | _n_estimators_: 10, **100**, 1000 |
| DecisionTreeClassifier | 0.687772 | _max_depth_: 1,2,3,4,5,6,7,8,**9** <br>_max_features_: **None**, sqrt, log2 | _ccp_alpha_: {various, **0.005291005291005291**} |
| RandomForestClassifier | 0.681882 | _n_estimators_: 10, **100**, 1000 <br>_max_features_: **sqrt**, log2 |
| GaussianNB | 0.668060 | _var_smoothing_: **1**, e-01,e-02,...,e-09 |
| KNeighborsClassifier | 0.674465 | _n_neighbors_: 1,3,5,7,9,11,**13**,...,21 <br>_weights_: **uniform**, distance <br>_metric_: euclidean, **manhattan**, minkowski |

_*Bold hyperparameters are those which received the best f1 score_

According to these results, the best-performing algorithm is logistic regression, followed closely by SVC:

| model | f1 score | accuracy score | hyperparameters |
| ----- | -------- | -------------- | --------------- |
| LogisticRegression | 0.708129 | 0.653846 | _solver_: liblinear <br>_penalty_: l2 <br>_c_value_: 0.01|
| SVC | 0.707719 | 0.615385 | _kernel_: sigmoid <br>_C_: 50 <br>_gamma_: scale |

As logistic regression is a more computationally lightweight algorithm, and produced a slightly better accuracy score, it was selected as the final best-performing algorithm.
