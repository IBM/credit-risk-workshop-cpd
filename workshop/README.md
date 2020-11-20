
# Analyzing Credit Risk with Cloud Pak for Data on OpenShift

Welcome to our workshop! In this workshop we'll be using the Cloud Pak for Data platform to Collect Data, Organize Data, Analyze Data, and Infuse AI into our applications. The goals of this workshop are:

* Visualize data with Data Refinery
* Create and deploy a machine learning model
* Monitor the model
* Create a Python app to use the model

## About this workshop

- [Analyzing Credit Risk with Cloud Pak for Data on OpenShift](#analyzing-credit-risk-with-cloud-pak-for-data-on-openshift)
  - [About this workshop](#about-this-workshop)
    - [About the data set](#about-the-data-set)
  - [Agenda](#agenda)
  - [Compatability](#compatability)
  - [About Cloud Pak for Data as a Service](#about-cloud-pak-for-data-as-a-service)

### About the data set

In this workshop we will be using a credit risk / lending scenario. In this scenario, lenders respond to an increased pressure to expand lending to larger and more diverse audiences, by using different approaches to risk modeling. This means going beyond traditional credit data sources to alternative credit sources (i.e. mobile phone plan payment histories, education, etc), which may introduce risk of bias or other unexpected correlations.

![Use Case Diagram](.gitbook/assets/images/openscale-config/openscale-config-architecture.png)

The credit risk model that we are exploring in this workshop uses a training data set that contains 20 attributes about each loan applicant. The scenario and model use synthetic data based on the [UCI German Credit dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data)). The data is split into three CSV files and are located in the [data](../data/split) directory of the GitHub repository you will download in the pre-work section.

## Agenda

| Topic             | Content                                                            |
|-------------------|--------------------------------------------------------------------|
| Introduction      | Introduction Video                                                 |
| Platform Overview | CP4DaaS Overview                                                   |
|                   | [Lab] Project Setup video         \|   Instructions                |
| Data Wrangling    | Data Wrangling Overview                                            |
|                   | [Lab] Data Refinery video        \|   Instructions                 |
| Data Management   | Watson Knowledge Catalog Overview                                  |
|                   | [Demo] WKC                                                         |
| Machine Learning  | Machine Learning into                                              |
|                   | [Lab] ML with Jupyter Notebook video           \| Instructions     |
|                   | [Lab] Automated ML with AutoAI Lab video           \| Instructions |
| Model Deployment  | Model Deployment intro                                             |
|                   | [Lab] Online Deployment & testing video         \| Instructions    |
|                   | [Lab] Batch Scoring video         \|   Instructions                |
|                   | [Lab] Deploy model to Python app video         \| Instructions     |
| Model Monitoring  | Monitoring & Explainability intro                                  |
|                   | [Demo] OpenScale                                                   |
| Conclusion        | Conclusion Video                                                   |


## Compatability

This workshop has been tested on the following platforms:

* **macOS**: Mojave (10.14), Catalina (10.15)
  * Google Chrome version 81

* **Microsoft**: Windows 10
  * Google Chrome, Microsoft Edge

## About Cloud Pak for Data as a Service

Cloud Pak for Data as a Service provides you with an integrated set of capabilities for collecting and organizing your data into a trusted, unified view, and then creating and scaling AI models across your business.

[Docs](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/overview-cpdaas.html?context=analytics)
