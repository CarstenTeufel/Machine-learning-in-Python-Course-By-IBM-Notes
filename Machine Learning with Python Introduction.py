#The following script and its content has been fully written by Carsten Teufel, based on the IBM course called
##Machine Learning with Python: A Practical Introduction.

#I'm back on the tracks, now with a more specific course in my way to Machine Learning and Data Science. For those
##looking to learn or recall applied Machine Learning models, this is the place for you... or I hope so.

#I will try to write scripts in a more smooth and uncomplicated way, to make it easier to find information.


                                            ###Content###
#Module 1: Introduction to Machine Learning
    #1.1 Popular Machine Learning Techniques
    #1.2 Difference between Artificial Intelligence, Machine Learning and Deep Learning
    #1.3 Python Libraries for Machine Learning
    #1.4 Supervised vs Unsupervised









                                ###Module 1: Introduction to Machine Learning###


#Machine Learning is a subfield of computer science. It gives computers ability to learn something
##without being explicitly programmed.

#This means, the Machine Learning model will create a set of rules by itself from the training dataset. For example,
## when creating a Model to diferentiate animals with a set of photos as input. The Model will learn about the features
###of every animal and sort them by species.

#Examples of machine learning in real life:

#Netflix, YouTube, Amazon Prime, etc.
##All of the actual streaming services use recommendation systems to recommend videos, movies and TV shows to its users.

#Banks
##Banks use Machine Learning to predict the probability of default by applicant
## client, thus approving or denying credits for them.

#Telecommunication companies
##Telecommunication companies use demographic data obtained from customers to segment or predict churn (whether they will
###unsubrscribe or not)

#Chatbots, Face recognition, games etc.


                              ###1.1 Popular Machine Learning Techniques###

#1. Regression/Estimation
    #Predicting continuous values

#2. Classification
    #Predicting the item class or category of a case (tumours, customer churn, etc)

#3. Clustering
    #To find the structure of data. Summarizing datasets (Customer segmentation in banking)

#4. Associations
    #Frequent co-occuring items or events are associated through this technique - like grocery items bought together by costumers.

#5. Anomaly Detection .
    #Abnormal and unusual cases detection. Used in Credit Banc fraud detection.

#6. Sequence Mining
    #Predicting upcomming events, for the case in point, click-stream in a website.

#7. Dimension Reduction
    #Reduce the size of Data (PCA)

#8. Recommendation systems
    #Recommending items such as TV shows, videos, books or whatever you can recommend.



                 ###1.2 Difference between Artificial Intelligence, Machine Learning and Deep Learning###


#AI or Artificial Intelligence tries to make computers intelligent. AI is a field with a broader scope of view that
##includes:
#-Computer vision
#-Language Processing
#-Creativity
#-and others.


#Machine Learning or ML is a branch of AI that covers the statistical side of Artificial Intelligence.
##Through ML you will try to tech the computer to solve problems by analyzing examples.
###It includes:
#-Classification
#-Clustering
#-Neural Network


#Deep learning is a field of Machine Learning, where computers can learn and make decisions based on their own intelligence.
##It involves deeper level of automation, compared with other ML models.



                                ###1.3 Python Libraries for Machine Learning###


#Use Python to write Machine-Learning models and remember to look for libraries for whatever you try to do.
##This will save you a lot of time.

#Python Libraries:

    #1. NumPy
    #Math library to work with N-dimensional Arrays in python. This library makes computation easier and effectively.
    ##NumPy is a must if you want to work with arrays, dictionaries, functions, datatypes or images.

    #2. SciPy
    #SciPy is a collection of numerical algorithms and domain specific toolboxes, such as signal processing,
    ##optimization, statistics and others. It is a nice library for scientific and high performance computation.

    #3. Matplotlib
    #Matplotlib is a well-known plotting package. It will provide 2D and 3D plotting capabilities to its user.
    ##This course will offer most of the useful tools in these packages.

    #4. Pandas
    #Pandas is one of the most used libraries, as it provides high performance and easy to use data structures.
    ##It allows the user to access functions to import, manipulate and analyze data.

    #5. SciKit Learn
    #This library is a collection of algorithms and tools for machine learning, such as most of the Classification,
    #Regression and Clustering Algorithms.
    #It is free and works with NumPy and  SciPy.
    #It includes good documentation and is easy to implement.
    #It eases the tasks that need to be done in a ML pipeline: Data preprocessing, Feature Selection, Feature Extraction,
    #train/test split, Algorithm setup
    #Model fitting, tuning parameters, prediction, evaluation and Model Export


                                   ### 1.4 Supervised vs Unsupervised###


#Supervised Learning

#Supervise means to observe and direct an execution of a task, project or activity.
#In this case, we will be supervising a Machine Learning Model.

#Supervising in this case, means to "teach" the model to make predictions from knowledge (Data) we have.

#How to teach a model? We train the model, from a labeled dataset.


#Supervised learning techniques:
    # 1) Classification: Predicting a discrete class label or category

    # 2) Regression: Predicting a continuous value instead of a categorical value.



#Unsupervised Learning

#In the case of unsupervised models, we ñet the model work by itself and discover information that could not be visible
##to the human eye.

#The Unsupervised Algorithm trains based on the dataset and draws conclusions using unlabeled data.

#These Algorithms are more difficult than supervised ones, because of the little or no information we have about the
##dataset.


#Unsupervised learning techniques:
    # 1) Dimension Reduction/Feature Selection: Reduces redundant features to make the classification easier.

    # 2) Density Estimation: Used to explore data to find structures within the data.

    # 3) Market Basket Analysis: Modeling technique based on the theory that if you purchase a group of items, you will
    ##more likely buy another group of items.

    # 4) Clustering: One of the most popular ML teachniques, based on techniques to group data points, objects that are
    ##similar. For example, for banks, to segment customers based on characteristics or help individuals to organize.