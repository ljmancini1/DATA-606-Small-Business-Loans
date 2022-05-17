## Blogpost - Using Machine Learning to Analyze and Predict the Effectiveness of The SSBCI 

[Back to Team Page](index.md)

### Background
The State Small Business Credit Iniative (SSBCI) was created as part of the Small Business Jobs Act of 2010, with the goal of helping small businesses address a range of challenges when securing financing. The program allocated $1.4 billion dollars to be distributed to states. The states then use the funds to spur private sector investment by sharing risk. The funds are distributed through a number of programs and institutions, primarily community banks, community development financial institutions (CDFIs), and local investors. In this way, risk of repayment was shared by government and private investors, encouraging lending. States operated five types of programs under SSBCI: capital access programs, loan guarantee programs, loan participation programs, collateral support programs, and venture capital programs. 

The program ran from 2010-2017 and created $10.7 billion in new financing from over 21,000 loans and investments. Almost $9 for every $1 in SSBCI funds loaned to or invested in a small business until the program was sunset in September of 2017. 

Now, the SSBCI is being reimplemented as part of the American Rescue Plan of 2021, this time with $10 billion. This would mean nearly $100 billion in new financing for small businesses (assuming the loan creation ration stays the same). This leads to a question: Can we use machine learning models to predict the success of an individual company receiving funds? Specifically, will a company that receives funds be able to create jobs and/or retain employees?

### The Dataset
The dataset consist of data for every company participating in the program from the entirety of 2010 to 2017. It includes the type of program the business received funding through as well as how much. To normalize for changing economic conditions, the dataset will be modified to include some macroeconomic measures such as Unemployment, and the S&P 500 index level.

### Clustering Using K-Prototypes
The dataset represents a relatively heterogeneous set of companies, as each company has slightly different market conditions and geography. The suspicion was that companies are more similarly to one another than initially suspected. In fact, it is likely that the companies can be grouped in a small set of clusters.

If this is the case, it should be possible to show that each small business fits into one of several clusters. With this information, it will be possible to add the group the business belongs to as a feature for later classification. In addition, by examining the similarities of these groups using a classification algorithm, it should be possible to extract feature importance information about all small business for predictive model development.

The approach used here is derived from [Antons Rubert's](https://antonsruberts.github.io/kproto-audience/)  article on using and evaluating K-Prototypes. First, we use a dimensionality reduction technique to visualize the clusters, making them countable. Then, use a clustering algorithm to determine the appropriate number of groups. For dimensionality reduction, Uniform Manifold Approximation (UMAP) is used to map the n-feature vector onto a 2 dimensional surface, creating a projection. <br>

<img width="750" src="img/clusterplot.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" /> <br>

The dataset contains many categorical variables so K-Means is not robust enough to give accurate groupings, and the added computational cost of creating One-Hot encoded features creates a technically constraint on the clustering algorithm. The more appropriate approach is to use K-Prototypes, which accepts both numerical and categorical data. K-Prototypes measures similarity between numerical data using Euclidean distance and between categorical data using a weighted discrete function dependent on the standard deviation and mode of each categorical feature. The cost is then calculated using the Huang cost function.

Trying to run K-Means as well as the elbow plot for optimal cluster size resulted in code that would not complete running after 10 hours. K-Prototypes runs in a matter of minutes, however the elbow plot did not complete running. Overlaying the cluster groupings using color on the UMAP projection visualizes where the clusters form relative to one another.

<p>In order to evaluate the accuracy and quality of the clustering, we can treat the clusters as labels and build a classification model on top. Each point in the dataset is assigned a cluster according to the results of the K-Prototype algorithm. If the clusters are of high quality, the classification model will be able to predict them with high accuracy. At the same time, the models should use a variety of features to ensure that the clusters are not too simplistic. K-Prototypes was run for 8 clusters, 10 clusters, and 15 clusters, chosen by visual inspection of the UMAP projection.</p> <br><br>


Four Clusters<br>

<img width="541" title= "K-Prototypes with 8 Clusters" src="img/cluster4.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" /><br><br>
     
Six Clusters<br>

<img width="541" title= "K-Prototypes with 8 Clusters" src="img/cluster6.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" /><br><br>
     
Eight Clusters<br>

<img width="541" title= "K-Prototypes with 8 Clusters" src="img/cluster8.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" /><br><br>
 
Ten Clusters<br>

<img width="541"  title= "K-Prototypes with 10 Clusters"  src="img/cluster10.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" /><br><br>

Next we look at the F1 scores for the differing number of clusters. We can see that the F1 score goes down from 4 to 8 clusters but ticks back up at 10. All models appear to still be candidates.<br>

>`CV F1 score for K-Prototypes 4 clusters is 0.94119936047242`<br>
>
>`CV F1 score for K-Prototypes 6 clusters is 0.9643122786856988`<br>
>
>`CV F1 score for K-Prototypes 8 clusters is 0.9544591027034534`<br>
>
>`CV F1 score for K-Prototypes 10 clusters is 0.9599366334634558`<br>

Finally, calculating the SHAP values for feature importance demonstrates if the clustering is using a high number of features. As is shown, 10 clusters produces a high number of features used for determining the clusters. <br>

Four Clusters<br>

<img width="500"  title= "K-Prototypes with 8 Clusters"  src="img/shap4.png"  style="float: left; margin-right: 10px;" /><br>

Six Clusters<br>

<img width="500"  title= "K-Prototypes with 8 Clusters"  src="img/shap6.png"  style="float: left; margin-right: 10px;" /><br>

Eight Clusters<br>

<img width="500"  title= "K-Prototypes with 8 Clusters"  src="img/shap8.png"  style="float: left; margin-right: 10px;" /><br>

Ten Clusters<br>

<img width="500"  title= "K-Prototypes with 10 Clusters"  src="img/shap10.png"  style="float: left; margin-right: 10px;" /><br>

This analysis shows that K-Prototypes with 10 clusters is the best choice for feature diversity and F1-Score. This also indicates that clusters are well defined even with up to 10 clusters and have well defined boundaries. 
## Regression Models

#### Univariate Linear Regression Model

Linear Regression model and correlation matrix show that the number of full-time employees at the time of the loan closure is positively correlated with the number of jobs retained as a direct result of the loan. The target variable for the regression models is represented by the Job Benefit variable, which is the sum of Jobs Created and Jobs Retained as a result of the loan. The Job Benefit Variable represents the overall economic impact of the loan.

#### Correlation Matrix with Variables Used in Regression Models
 <img width="386" alt="Screen Shot 2022-05-14 at 7 29 16 PM" src="https://user-images.githubusercontent.com/74617235/168451276-3b1641a1-b1ce-41d1-a9cd-7d5e8504ab5c.png">
 

#### Univariate Linear Regression model shows that the number of full-time employees at the time of the loan closure accounts for about 60% of the variation in the job benefit resulting from the loan.

<img width="554" alt="Screen Shot 2022-05-14 at 8 09 19 PM" src="https://user-images.githubusercontent.com/74617235/168452062-eea63e15-7a4b-4f27-b18f-b151237978c2.png">


R<sup>2</sup> Value: 0.603

#### Multivariate Linear Regression Model

Multivariate linear regression model results indicate that Full Time Employees, Metro Type, Community Development Financial Institutions (CDFI) Type, and SPY Stock Close price are the strongest predictors for the number of Jobs Created and Jobs Retained. 

<img width="794" alt="Screen Shot 2022-05-14 at 9 52 48 PM" src="https://user-images.githubusercontent.com/74617235/168453868-90be54ca-1630-4d74-a863-2b3f5b4a28b1.png">

R<sup>2</sup> Value: 0.647

## Classification Models

### Classifications models that were used to predict whether jobs were created as a direct result of the SSBCI loans: 
* Logistic Regression 
* Support Vector Classifier
* Gradient Boosting Classifier 


#### Model Metrics
<img width="793" alt="Screen Shot 2022-05-14 at 10 06 54 PM" src="https://user-images.githubusercontent.com/74617235/168454214-a7479326-f2bc-415f-90e8-e4c5d48c65cc.png">

Accuracy, Precision, Recall, and F1 score were used to determine which model had the best predictive performance. Based on the metrics listed, we selected the Gradient Boosting Classifier as the model to use when predicting whether jobs were created as a direct result of the loans.

#### ROC Curves
<img width="330" alt="Screen Shot 2022-05-15 at 11 05 26 AM" src="https://user-images.githubusercontent.com/74617235/168479772-303d6d65-99a0-403c-b372-779dbed8e75f.png"> <img width="330" alt="Screen Shot 2022-05-15 at 11 08 27 AM" src="https://user-images.githubusercontent.com/74617235/168479843-2c884418-49b8-4ab2-9aec-e6a114aa4b17.png"> <img width="330" alt="Screen Shot 2022-05-15 at 11 09 45 AM" src="https://user-images.githubusercontent.com/74617235/168479921-56e3d0ff-5ea5-4376-b942-905692f36a7c.png">




#### Shapley values were used for feature selection for the Gradient Boosting Classifier. Below are the Shapley values:
<img width="541" alt="Screen Shot 2022-05-14 at 10 12 07 PM" src="https://user-images.githubusercontent.com/74617235/168454328-ed63857d-de56-47d0-8e2a-85c53c5e41f5.png">


* Feature 0: SSBCI Original Funds
* Feature 1: Revenue
* Feature 2: Full Time Employees
* Feature 3: Jobs Retained
* Feature 4: Loan Investment Amount
* Feature 5: SPY Close Price

The plot indicates that Loan Investment Amount had the highest impact on whether jobs were created as a result of the loan.
