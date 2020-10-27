
# Analyzing Credit Risk with Cloud Pak for Data on OpenShift

Welcome to our workshop! In this workshop we'll be using the Cloud Pak for Data platform to Collect Data, Organize Data, Analyze Data, and Infuse AI into our applications. The goals of this workshop are:

* Visualize data with Data Refinery
* Create and deploy a machine learning model
* Monitor the model
* Create a Python app to use the model

## About this workshop

* [Agenda](#agenda)
* [Compatability](#compatability)
* [About Cloud Pak for Data as a Service](#about-cloud-pak-for-data-as-a-service)

### About the data set

In this workshop we will be using a credit risk / lending scenario. In this scenario, lenders respond to an increased pressure to expand lending to larger and more diverse audiences, by using different approaches to risk modeling. This means going beyond traditional credit data sources to alternative credit sources (i.e. mobile phone plan payment histories, education, etc), which may introduce risk of bias or other unexpected correlations.

![Use Case Diagram](.gitbook/assets/images/openscale-config/openscale-config-architecture.png)

The credit risk model that we are exploring in this workshop uses a training data set that contains 20 attributes about each loan applicant. The scenario and model use synthetic data based on the [UCI German Credit dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data)). The data is split into three CSV files and are located in the [data](../data/split) directory of the GitHub repository you will download in the pre-work section.

## Agenda

<table>
<thead>
  <tr>
    <th>Topic</th>
    <th>Content</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Introduction</td>
    <td>Introduction Video (xx:xx)</td>
  </tr>
  <tr>
    <td rowspan="2">Platform Overview</td>
    <td>CP4DaaS Overview (xx:xx)</td>
  </tr>
  <tr>
    <td>[Lab] Project Setup video (xx:xx) |&nbsp;&nbsp;&nbsp;Instructions</td>
  </tr>
  <tr>
    <td rowspan="2">Data Wrangling</td>
    <td>Data Wrangling Overview (xx:xx)</td>
  </tr>
  <tr>
    <td>[Lab] Data Refinery video(xx:xx) |&nbsp;&nbsp;&nbsp;Instructions</td>
  </tr>
  <tr>
    <td rowspan="2">Data Management</td>
    <td>Watson Knowledge Catalog Overview (xx:xx)</td>
  </tr>
  <tr>
    <td>[Demo] WKC (xx:xx)</td>
  </tr>
  <tr>
    <td rowspan="3">Machine Learning</td>
    <td>Machine Learning into (xx:xx)</td>
  </tr>
  <tr>
    <td>[Lab] ML with Jupyter Notebook video&nbsp;&nbsp;&nbsp;(xx:xx) | Instructions</td>
  </tr>
  <tr>
    <td>[Lab] Automated ML with AutoAI Lab video&nbsp;&nbsp;&nbsp;(xx:xx) | Instructions</td>
  </tr>
  <tr>
    <td rowspan="4">Model Deployment</td>
    <td>Model Deployment intro (xx:xx)</td>
  </tr>
  <tr>
    <td>[Lab] Online Deployment &amp; testing&nbsp;&nbsp;&nbsp;video (xx:xx) | Instructions</td>
  </tr>
  <tr>
    <td>[Lab] Batch Scoring video (xx:xx) |&nbsp;&nbsp;&nbsp;Instructions</td>
  </tr>
  <tr>
    <td>[Lab] Deploy model to Python app video&nbsp;&nbsp;&nbsp;(xx:xx) | Instructions</td>
  </tr>
  <tr>
    <td rowspan="2">Model Monitoring</td>
    <td>Monitoring &amp; Explainability intro (xx:xx)</td>
  </tr>
  <tr>
    <td>[Demo] OpenScale (xx:xx)</td>
  </tr>
  <tr>
    <td>Conclusion</td>
    <td>Conclusion Video (xx:xx)</td>
  </tr>
</tbody>
</table>


## Compatability

This workshop has been tested on the following platforms:

* **macOS**: Mojave (10.14), Catalina (10.15)
  * Google Chrome version 81

* **Microsoft**: Windows 10
  * Google Chrome, Microsoft Edge

## About Cloud Pak for Data as a Service

Cloud Pak for Data as a Service provides you with an integrated set of capabilities for collecting and organizing your data into a trusted, unified view, and then creating and scaling AI models across your business.

[Docs](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/overview-cpdaas.html?context=analytics)
