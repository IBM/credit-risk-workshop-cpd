# Monitoring models with OpenScale GUI tool using Fastpath setup

This exercise shows a few of the features of the OpenScale GUI tool. When you first provision Watson OpenScale, either in the IBM Cloud or on Cloud Pak for Data, you will be offered the choice to automatically configure and setup OpenScale. This is called the Fastpath, and it walks the user through the required steps and loads some sample data to demonstrate the features of OpenScale. We will use this automated Fastpath setup in this lab.

> * Note: It is presumed that OpenScale Fastpath and Watson Machine Learning have already been configured.*

## Use the Insights Dashboard

The *Insights Dashboard* provides an overview of the models that OpenScale is monitoring.

* Go the (☰) navigation menu on the top left corner of the Cloud Pak for Data UI. Expand *Services* and then click on service instances.

![(☰) Menu -> service instances](../.gitbook/assets/images/navigation/menu-service-instances.png)

* Find and click on the instance of `Watson OpenScale` you have provisioned from the listed services.

  > *Note: If you have many services, you can enter `openscale` into the search bar to filter the services shown.*

  ![Openscale Tile](../.gitbook/assets/images/openscale/servicesinstances-wos-instance.png)

* Launch the OpenScale UI tooling by making sure you are on the `Manage` section from the left panel and then clicking on the *`Launch Application`* button

  ![Openscale Launch](../.gitbook/assets/images/openscale/services-wos-launch.png)

* OpenScale will load the *Insights Dashboard*. This will contain tiles for any models being monitored. The tile for `GermanCreditRiskModel` will be the one we will use for this lab, which was configured using the Fastpath script.

  ![OpenScale Insight Dashboard](../.gitbook/assets/images/openscale/openscale-insights-dashboard.png)

* Click on the left-hand menu icon for `Insights`, next click the 3-dot menu on the `GermanCreditRiskModel` tile and then the `View Details` option.

  ![OpenScale Insight Dashboard Tile Open](../.gitbook/assets/images/openscale/openscale-fp-model-viewdetails.png)

* Notice the red alert indicators on the various monitors (Fairness, Quality, Drift). You should see a red indicator under Fairness. Click on the *Fairness score*.

  ![Model Overview](../.gitbook/assets/images/openscale/openscale-fp-model-overview.png)

* Click on the triangle with `!` under `Fairness` -> `Sex`. This indicates that there has been an alert for this attribute in the `Fairness` monitor. Alerts are configurable, based on thresholds for fairness outcomes which can be set and altered as desired.

* By moving your mouse pointer over the trend chart, you can see the values change, and which contains bias. Find and click on a spot in the graph that is below the red threshold line to view details.

  ![OpenScale Fairness Monitor](../.gitbook/assets/images/openscale/openscale-fp-model-fairnessgraph.png)

* Once you open the details page, you can see more information. Note that you can select from your choice of data (Payload + Perturbed, Payload, Training, Debiased) using the `Data Set` drop down list.

  ![OpenScale Fairness Detail](../.gitbook/assets/images/openscale/openscale-fp-fairness-detail.png)

* Click the `View payload transactions` button on the right to drill deeper.

  ![OpenScale Fairness Transactions](../.gitbook/assets/images/openscale/openscale-fp-fairness-view-transactions.png)

* In the transactions page, each of the individual transactions can be examined to see them in detail. Doing so will cache that transaction, as we will see later. Note that the Explainability feature requires 1000's of REST calls to the endpoint using variations of the data that are slightly perturbed, which can require several seconds to complete.

  ![OpenScale View Transactions](../.gitbook/assets/images/openscale/openscale-fp-fairness-transactions.png)

* Now, go back to the *Insights Dashboard* page by clicking on the left-hand menu icon for `Insights`. This time open the monitor configuration for the `GermanCreditRiskModel` model by clicking the 3-dot menu on the tile and then `Configure monitors`).

  ![OpenScale Insight Dashboard Tile Open](../.gitbook/assets/images/openscale/openscale-fp-model-viewmonitors.png)

* Click the `Endpoints` menu on the left, then the Endpoints tab. Use the Endpoint pulldown to select `Debiased transactions`. This is the REST endpoint that offers a debiased version of the credit risk ML model, based on the features that were configured (i.e. Sex and Age). It will present an inference that attempts to remove the bias that has been detected.

  ![OpenScale Monitors Endpoints](../.gitbook/assets/images/openscale/openscale-fp-endpoints.png)

* You could also use the Code language pulldown to see example code for using the Fairness Debiased endpoint. You can see code snippets using cURL, Java, and Python, which can be used in your scripts or applications.

* Similarly, you can choose the `Feedback logging` endpoint to get code for Feedback Logging. This provides an endpoint for sending fresh test data for ongoing quality evaluation. You can upload feedback data here or work with your developer to integrate the code snippet provided to publish feedback data to your Watson OpenScale database.

### Examine an individual transaction

* Click on the left-hand menu icon for `Explain a transaction`. Below the transaction input field you may see a table with transaction ids. These are the transactions that have been explained and cached. Click on one of these cached transaction ids if it is present.

> If you do not have cached transaction IDs, you can use one of the following approaches to find a transaction to explain: (1) As you did in the section above, you can go back to the transactions page that you navigated to from the Fairness alert and click the `Explain prediction` link under the 'Actions' column.  (2) If you've run one of the OpenScale Jupyter Notebook / Manual config modules. You can enter a transaction UID you copied from that notebook into the search bar.

  ![Explain a transaction](../.gitbook/assets/images/openscale/openscale-explain-transaction.png)

> *NOTE: Each time you create the Explainibility data, the perterbation algorithm is sending 1000's of requests to the deployed Machine Learning REST endpoint, so the first time this is done can take a few seconds.*

* You can see under `Features influencing this prediction`, the Feature and Weight of the most important factors for this prediction. As well as the top features influencing the model towards a different prediction.

  ![Feature Influence](../.gitbook/assets/images/openscale/openscale-transaction-features.png)

* Click on the `Inspect` tab and then click on the `Run analysis` button. OpenScale will analyze the model and provide suggestions on which features would need to change, along with the indicated minimum value, in order for the prediction to change. It will also provide a feature importance value ( a higher feature importance numbers indicate a greater likelihood of changing the prediction).

  ![Feature Analysis](../.gitbook/assets/images/openscale/openscale-explain-transaction-runanalysis.png)

* Note that from this page we can also change the feature values and run a new prediciton with those values.

  ![Feature Change](../.gitbook/assets/images/openscale/openscale-explain-transaction-changevalues.png)

## Using the Analytics tools

* Click on the left-hand menu icon for `Insights`, next click the 3-dot menu on the `GermanCreditRiskModel` tile and then the `View Details` option.

  ![OpenScale Insight Dashboard Tile Open](../.gitbook/assets/images/openscale/openscale-fp-model-viewdetails.png)

* Notice the red alert indicators on the various monitors (Fairness, Quality, Drift). You should see a red indicator under Fairness. Click on the *Fairness score*.

  ![Model Overview](../.gitbook/assets/images/openscale/openscale-fp-model-overview.png)

* From this dashboard click on `Analytics` -> `Chart Builder`. Here you can create charts using various Measurements, Features, and Dimensions of your machine learning model. You can  see a chart that breaks down *Predictions by Confidence* (*Note: You may need to click the date range for 'Past Week' or 'Yesterday' to load the data).

  ![Analytics Predictions by Confidence](../.gitbook/assets/images/openscale/openscale-analytics-predictions-confidence.png)

* You can experiment with changing the values and examine the charts that are created.

  ![Analytics Chart builder](../.gitbook/assets/images/openscale/openscale-analytics-chart-builder-example.png)

## Conclusion

This lab provides a walkthrough of many of the GUI features using the Watson OpenScale tools. The Fastpath deployment creates a machine learning model, deploys it, and inserts historical data to simulate a model that has been used in production over time. The OpenScale monitors are configured, and the user can then explore the various metrics and data. Please continue to explore on your own.
