
# Analyzing Credit Risk with Cloud Pak for Data on OpenShift

Welcome to our workshop! In this workshop we'll be using the Cloud Pak for Data platform to Collect Data, Organize Data, Analyze Data, and Infuse AI into our applications. The goals of this workshop are:

* Visualize data with Data Refinery
* Create and deploy a machine learning model
* Monitor the model
* Create a Python app to use the model

## About this workshop

* [Agenda](#agenda)
* [Compatability](#compatability)
* [About Cloud Pak for Data](#about-cloud-pak-for-data)
* [Credits](#credits)

### About the data set

In this workshop we will be using a credit risk / lending scenario. In this scenario, lenders respond to an increased pressure to expand lending to larger and more diverse audiences, by using different approaches to risk modeling. This means going beyond traditional credit data sources to alternative credit sources (i.e. mobile phone plan payment histories, education, etc), which may introduce risk of bias or other unexpected correlations.

![Use Case Diagram](.gitbook/assets/images/openscale-config/openscale-config-architecture.png)

The credit risk model that we are exploring in this workshop uses a training data set that contains 20 attributes about each loan applicant. The scenario and model use synthetic data based on the [UCI German Credit dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data)). The data is split into three CSV files and are located in the [data](../data/split) directory of the GitHub repository you will download in the pre-work section.

#### [Applicant Financial Data](../../data/split/applicant_financial_data.csv)

This file has the following attributes:

* CUSTOMERID (hex number, used as Primary Key)
* CHECKINGSTATUS
* CREDITHISTORY
* EXISTINGSAVINGS
* INSTALLMENTPLANS
* EXISTINGCREDITSCOUNT

#### **[Applicant Loan Data](../../data/split/applicant_loan_data.csv)**

This file has the following attributes:

* CUSTOMERID
* LOANDURATION
* LOANPURPOSE
* LOANAMOUNT
* INSTALLMENTPERCENT
* OTHERSONLOAN
* RISK

#### **[Applicant Personal Data](../../data/split/applicant_personal_data.csv)**

This file has the following attributes:

* CUSTOMERID
* EMPLOYMENTDURATION
* SEX
* CURRENTRESIDENCEDURATION
* OWNSPROPERTY
* AGE
* HOUSING
* JOB
* DEPENDENTS
* TELEPHONE
* FOREIGNWORKER
* FIRSTNAME
* LASTNAME
* EMAIL
* STREETADDRESS
* CITY
* STATE
* POSTALCODE

## Agenda

|   |   |
| - | - |
| [Pre-work](pre-work/README.md) | Creating a project, downloading the data set, seeding a database |
| [Data Visualization with Data Refinery](./data-visualization-and-refinery/README.md) | Refining the data, vizualizing and profiling the data |
| [Machine Learning with Jupyter](machine-learning-in-jupyter-notebook/README.md) | Building a model with Spark, deploying the model with Watson Maching Learning, testing the model with a Python Flask app |
| [Machine Learning with AutoAI](machine-learning-autoai/README.md) | Use AutoAi to quickly generate a Machine Learning pipeline and model |
| [Deploy and Test Machine Learning Models](machine-learning-deployment-scoring/README.md) | Deploy and machine learning models using several approaches |

## Compatability

This workshop has been tested on the following platforms:

* **macOS**: Mojave (10.14), Catalina (10.15)
  * Google Chrome version 81

* **Microsoft**: Windows 10
  * Google Chrome, Microsoft Edge
