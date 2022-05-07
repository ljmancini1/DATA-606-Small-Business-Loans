# State Small Business Credit Initiative (SSBCI) Loan Impacts

[Blogpost](./blogpost.md)
[Team Members](#Team-Members-and-Roles) | [Project Overview](#Project-Overview) | [Background](#Background) | [Dataset](#Dataset) | [References](#References)

### Team Members and Roles

**Tom Kelly** - Data cleaning and exploratory analysis. Construction of predictive models and RESTful web API creation<br>
**Len Mancini** - Data engineerring and clustering analysis. Authoring of Blog and team webpage

### Project Overview
<p>The State Small Business Credit Initiative (SSBCI) was created as part of the Small Business Jobs Act of 2010. The program appropriated $1.5 billion, distributed by the U.S. Department of the Treasury, to provide direct support to states' programs designed to increase access to credit for small businesses. Funds were allocated to all fifty states along with the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of Northern Mariana Islands, Guam, American Samoa, and the United States Virgin Islands. Funds were distributed according to a statutory formula that takes into account a state’s job losses in proportion to the aggregate job losses of all states. Under the Act, each state or territory was guaranteed a minimum allocation of 0.9 percent of the $1.5 billion.</p>

The **American Rescue Plan Act of 2021 (ARPA)** reauthorized and amended the **Small Business Jobs Act of 2010 (SBJA)** to provide $10 billion to fund the **State Small Business CreditInitiative (SSBCI)** as a response to the economic effects of the COVID-19 pandemic. This is a near 10 fold increase (nominally) in the funding for this program. ARPA provided for a $6.5 billion maincapital allocation, $1.5 billion allocation for business enterprises owned and controlled by socially and economically disadvantaged individuals (SEDI-owned businesses), $1.0 billionincentive allocation for SEDI-owned businesses, $500 million allocation for very smallbusinesses (VSBs), and $500 million allocation for technical assistance funding. 

#### Research Question
Given that the **SSBCI** has been reimplemented as part of the **ARPA** the project seeks to answer this question:

* **Can we predict based the data provided by first implementation of the SSBCI if a loan will be successful at creating and/or retaining jobs?**

This project seeks to answer this question in two distinct ways through predictive modeling using classification and regression.
1. Given a set of input features, will a business receiving a loan as part of this program create and/or retain jobs
2. How many jobs is the business likely to create or retain based on the size of the loan.



### Background
The SSBCI provides funding for two state program categories: Capital Access Programs (“CAPs”) and Other Credit Support Programs (“OCSPs”). 
  
<ul>
<li><b>CAPs</b> provide portfolio insurance for business loans based on a separate loan loss reserve fund for each participating financial institution. The reserve fund will be used to provide portfolio insurance for all loans enrolled in the CAP by participating financial institutions. To enroll a loan in the CAP, both the lender and the borrower of the loan make insurance premium payments to the reserve fund. The state also must make a payment to the reserve fund for each loan to match the insurance premium. Under the Act, states may use the federal funds allocated to them under the Act to make their matching contributions to the reserve fund. Under the Act, for a loan to be eligible for enrollment in the CAP, the borrower must have 500 employees (as defined in 13 C.F.R. Part 121.106) or less and the loan cannot exceed $5 million.</li>
<br>
<li><b>OCSPs</b> include collateral support programs, loan participation programs, state-sponsored venture capital programs, loan guarantee programs, or similar programs.Under the Act, OCSPs must target an average borrower or investee size of 500 employees (asdefined in 13 CFR Part 121.106) or less and cannot extend credit support to borrowers with more than 750 employees. The OCSP must target loans or investments with an average principal amount of $5 million or less and cannot provide credit or investment support if a giventransaction exceeds $20 million. For loan programs, the $20 million restriction applies to the principal amount of the loan directly supported by SSBCI, plus all other loans for the same loan purpose that close on or about the same date. For equity investment programs, the $20 million restriction applies to a single investment round that includes an SSBCI-funded investment, including all classes of equity instruments that close on or about the same date. OCSPs also include qualifying loan or swap funding facilities, which are contractual arrangements between a participating state and a private financial entity. Under such facilities, the state delivers funds to the private financial entity as collateral; that entity, in turn, provides funding to the state. The full amount resulting from the arrangement, less any fees or other costs of the arrangement, is contributed to, or for the account of, an approved state program.</li>
</ul>

For more information on the SSBCI Policy Guidelines, see the [Treasury Department Website](https://home.treasury.gov/system/files/256/Policy-Guidelines-9-30-2014-FINAL.pdf)

### Dataset
The dataset is provided by the Department of the Treasure and can be found below <br>
[State Small Business Credit Initiative Transaction Dataset](https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv)

The dataset consists of all loan transaction data for the program from 2010-2016. It includes contains information related to loan investment amount, lender type, metro type, income categorization, private financing, program type, and more. 

Dataset Size: 21,962 Rows, 49 Columns

A complete list of columns is provided below as well as links to the definitions for the data

In addition, to compensate for economic conditions at each point in time, we will be including columns for the monthly CPI for the time of the loan, the PPI, and the 10 year treasury note rate.

A column for net jobs created/retained will be added as well which is defined as Jobs Created + Jobs Retained

[Data Definitions](https://home.treasury.gov/system/files/256/SSBCI-Data-Definitions.pdf)<br>
[Data Documentation](https://home.treasury.gov/system/files/256/SSBCI-Data-Documentation.pdf)

Column list

Column Name|Nulls
----|----
state_id                 |            0
state_name                |           0 
year_reported              |          0
program_name                |         0
program_type                 |        0
unique_id                     |       0
disbursement_date              |      0
loan_investment_amount          |     0
ssbci_original_funds             |    0
nonprivate_amount                 |   0
concurrent_private_financing       |  0
borrower_insurance_premium          | 0
lender_insurance_premium             |0
guaranteed_amount            |        0
collateral_support            |       0
ssbci_recycled_funds           |      0
subsequent_private_financing    |     0
zip_code                         |    0
metro_type                        |   0
LMI_type                           |  0
revenue                           |   0
full_time_employees            |      0
naics_code                      |     0
year_incorporated                |    0
jobs_created                      |   0
jobs_retained                    |    0
trans_type                  |         0
lender_name                  |     1623
lender_type                   |    1637
lender_type_category           |   1677
CDFI_type                       |     0
MDI_type                         |    0
VC_cat                        |       0
optional_woman_owned         |     8696
optional_minority_owned     |      9000
optional_veteran_owned       |    12344
optional_FTE                  |   11286
optional_FTE_yr_confirmed      |  11286
optional_primary_use_of_funds   | 11684
optional_revenue                 |12466
optional_revenue_yr_confirmed  |  12466
optional_active                 | 18482
optional_active_no         |      21651
optional_active_unknown     |     19883
optional_dollars_lost        |    20122
optional_business_city        |    8685
optional_business_state        |  15805
optional_coinvestment_source    | 21025
optional_stage                   |20995

### References

You can use the [editor on GitHub](https://github.com/ljmancini1/DATA-606-Small-Business-Loans/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ljmancini1/DATA-606-Small-Business-Loans/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
