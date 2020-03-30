# Supervised_Author_Identification
 Use Supervised algorithms ( Naive Bayes, Support Vector Machine, Decision Tree ) to identify emails from the Enron corpus by their authors
 
 
 We’ll do something very similar in this project. We have a set of emails, half of which were written by one person and the other half by another person at the same company . Our objective is to classify the emails as written by one person or the other based only on the text of the email.
 
 
 
 <h3>Naive Bayes</h3>
  We will start with Naive Bayes in this mini-project, and then expand in later projects to other algorithms.

We will start by giving you a list of strings. Each string is the text of an email, which has undergone some basic preprocessing; we will then provide the code to split the dataset into training and testing sets. (In the next lessons you’ll learn how to do this preprocessing and splitting yourself, but for now we’ll give the code to you).

One particular feature of Naive Bayes is that it’s a good algorithm for working with text classification. When dealing with text, it’s very common to treat each unique word as a feature, and since the typical person’s vocabulary is many thousands of words, this makes for a large number of features. The relative simplicity of the algorithm and the independent features assumption of Naive Bayes make it a strong performer for classifying texts. 

<h3>Support Vector Machine</h3>
   We’ll tackle the exact same email author ID problem as the Naive Bayes mini-project, but now with an SVM. What we find will help    clarify some of the practical differences between the two algorithms.
  Import, create, train and make predictions with the sklearn SVC classifier. When creating the classifier, use a linear kernel (if you forget this step, you will be unpleasantly surprised by how long the classifier takes to train). 
  One way to speed up an algorithm is to train it on a smaller training dataset. The tradeoff is that the accuracy almost always goes down when you do this. Let’s explore this more concretely: add in the following two lines immediately before training your classifier.

 features_train = features_train[:len(features_train)/100]
 labels_train = labels_train[:len(labels_train)/100]

 These lines effectively slice the training dataset down to 1% of its original size, tossing out 99% of the training data. You can leave all other code unchanged.


<h3>Decision Tree</h3>
     We will again try to identify the authors in a body of emails, this time using a decision tree. The starter code is in    decision_tree/dt_author_id.py.
