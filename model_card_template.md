# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
The model that was chosen for this assignment is a Random Forest classifier which was built using scikit-learn. The model looks at data features to predict whether a person's annual salary is greater, less than or equal to $50,000.

## Intended Use
This model has been built following the requirements of Udacity's Machine Learning Devops program to showcase a machine learning classification pipeline on publicly available Census data. It is constructed to make a prediction on whether a person's salary is greater than, less than or equal to $50,000 a year. It is for educational purposes ONLY.

## Training Data
The model has been trained using a publicly available dataset provided by Udacity. It is the Census dataset (census.csv) that contains demographic and employment related information such as age, workclass, education, occupation, relationship, race, hours worked per week, country and sex. The data had an 80/20 split, with 80% of the data used for model training. 

## Evaluation Data
The data had an 80/20 split, where 20% of the original dataset was used for model evaluation. The same encoder used on the training data was used in the evaluation process.

## Metrics
The model was evaluated using precision, recall and F1 score. The model produced the following results: 

Precision: 0.7208
Recall:    0.6261
F1:        0.6702

## Ethical Considerations
Predictions from this model are for educational purposes only. There are attributes, such as race and sex, in the dataset that could contain biases and therefore the predictions should not be used to assess an individual's value.

## Caveats and Recommendations
Before considering utilizing the model outside of its educational context, several considerations would need to be taken into account. Additional data and evaluation on smaller groups or categories would be needed to ensure performace was reliable. Furthermore the dataset would need to be investigated to ensure there are no societal biases baked into the data itself. It may also be beneficial to compare performance with other classification algorithms. 