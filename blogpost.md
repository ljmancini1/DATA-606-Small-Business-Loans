## Blogpost - Using Machine Learning to Analyze and Predict the Effectiveness of The SSBCI 

[Back to Team Page](index.md)

### Background
The State Small Business Credit Iniative (SSBCI) was created as part of the Small Business Jobs Act of 2010, with the goal of helping small businesses address a range of challenges when securing financing. The program allocated $1.4 billion dollars to be distributed to states. The states then use the funds to spur private sector investment by sharing risk. The funds are distributed through a number of programs and institutions, primarily community banks, community development financial institutions (CDFIs), and local investors. In this way, risk of repayment was shared by government and private investors, encouraging lending. States operated five types of programs under SSBCI: capital access programs, loan guarantee programs, loan participation programs, collateral support programs, and venture capital programs. 

The program ran from 2010-2017 and created $10.7 billion in new financing from over 21,000 loans and investments. Almost $9 for every $1 in SSBCI funds loaned to or invested in a small business until the program was sunset in September of 2017. 

Now, the SSBCI is being reimplemented as part of the American Rescue Plan of 2021, this time with $10 billion. This would mean nearly $100 billion in new financing for small businesses (assuming the loan creation ration stays the same). This leads to a question: Can we use machine learning models to predict the success of an individual company receiving funds? Specifically, will a company that receives funds be able to create jobs and/or retain employees?

The Dataset
The dataset consist of data for every company participating in the program from the entirety of 2010 to 2017. It includes the type of program the business received funding through as well as how much. To normalize for changing economic conditions, the dataset will be modified to include some macroeconomic measures such as CPI, PPI, Unemployment, and the S&P 500 index level.

!(Scatter)[img/scatter1.png]
