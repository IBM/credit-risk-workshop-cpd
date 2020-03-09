# Machine Learning with AutoAI

For this part of the workshop, we'll learn how to use [AutoAI](https://www.ibm.com/support/producthub/icpdata/docs/content/SSQNUZ_current/wsj/analyze-data/autoai-overview.html).
AutoAI is a capability that automates machine learning tasks to ease the tasks of data scientists. It automatically prepares your data for modeling, chooses the best algorithm for your problem, and creates pipelines for the trained models.

This section is broken up into the following steps:

1. [Upload data to project](#1-upload-the-dataset)
2. [Set up your AutoAI environment and generate pipelines](#2-set-up-your-autoai-environment-and-generate-pipelines)
3. [Save AutoAI Model](#3-save-autoai-model)
4. [Deploy and test the model](#4-deploy-and-test-the-model)

>*Note: The lab instructions below assume you have a project already. If not, follow the instructions in the pre-work section to create a project.*

## 1. Upload the Dataset

* We will upload the dataset used to train our model. If you have not yet downloaded or cloned Git Repo as outlined in the pre-work section. You can download/save the [german-credit-data.csv](https://raw.githubusercontent.com/IBM/credit-risk-workshop-cpd/master/data/original/german_credit_data.csv) directly to your machine.

* From the project overview page, click on the `Assets` tab to open the assets page where your project assets are stored and organized. You can load a local dataset using the interface on the right.

* Click `browse` to find and upload the [german-credit-data.csv](../dataset/Telco-Customer-Churn.csv) dataset from your machine:

![Upload dataset](../.gitbook/assets/images/autoai/autoai-upload-data-set.png)

## 2. Set up your AutoAI environment and generate pipelines

* To start the AutoAI experiment, click `Add to Project` from the top and select `AutoAI experiment`:

![Adding a project](../.gitbook/assets/images/autoai/autoai-add-project.png)

* Name your experiment asset and choose one of the compute configuration options listed with a drop-down menu. Then, click `Create`:

![Naming your services](../.gitbook/assets/images/autoai/autoai-name-service.png)

* Select your dataset by clicking the `Select from project` option, then clicking on the `german_credit_data.csv` asset and click the 'Select asset' button:

![Select data](../.gitbook/assets/images/autoai/autoai-select-dataset.png)

* AutoAI will load your data set and allow you to select what the model is predicting. Under *Select prediction column* find and click `Risk`. AutoAI will set default values for the experiment based on your dataset and the value being predicted. Click `> Run experiment`:

![Choose Churn column and run](../.gitbook/assets/images/autoai/autoai-choose-prediction-and-run.png)

* The AutoAI experiment will now run. The UI will show progress as different algorithms/evaluators are selected and as different pipelines are created & evaluated:

![autoai progress](../.gitbook/assets/images/autoai/autoai-pipeline-progress.png)

* As the experiment runs, you can view the performance of the pipelines that have completed by expanding each pipeline section.

![autoai progress](../.gitbook/assets/images/autoai/autoai-pipeline-metrics.png)

* The experiment can take several minutes to run. Upon completion you will see a message that the pipelines have been created:

![autoai pipelines created](../.gitbook/assets/images/autoai/autoai-pipelines-complete.png)

## 3. Save AutoAI Model

The AutoAI process follows this sequence to build candidate pipelines:

* Data pre-processing
* Automated model selection (Pipeline 1)
* Hyperparameter optimization (Pipeline 2)
* Automated feature engineering (Pipeline 3)
* Hyperparameter optimization (Pipeline 4)

You can review each pipeline and select to deploy the top performing pipeline from this experiment.

* Scroll down to see the *Pipeline leaderboard*. The top performing pipeline is in the first rank.

* The next step is to select the model that gives the best result by looking at the metrics. In this case, Pipeline 4 gave the best result with the metric "Area under the ROC Curve (ROC AUC)." You can view the detailed results by clicking the corresponding pipeline from the leaderboard:

![pipeline leaderboard](../.gitbook/assets/images/autoai/autoai-pipeline-leaderboard.png)

* The model evaluation page will show metrics for the experiment, feature transformations that were performed (if any), which features contribute to the model, and more details of the pipeline.

![Model evaluation](../.gitbook/assets/images/autoai/autoai-model-evaluation.png)

* In order to deploy this model, we will Click on the `Save as model` button to save it.

* A window opens that asks for the model name, description (optional), and so on. You can accept the defaults or give your model a meaningful name/description and then click `Save`:

![Save model name](../.gitbook/assets/images/autoai/autoai-save-model-name.png)

* You receive a notification to indicate that your model is saved to your project. Go back to your project main page by clicking on the project name on the navigator on the top left:

![choose AI model](../.gitbook/assets/images/autoai/autoai-project-navigator.png)

* You will see the new model under *Models* section of the *Assets* page, click the name of your saved model under *Models*:

![choose AI model](../.gitbook/assets/images/autoai/autoai-choose-asset-ai-model.png)

## 4. Deploy and test the model

* To prepare the model for deployment click `Promote to deployment space`:

![Deploying the model](../.gitbook/assets/images/autoai/autoai-deploy-model.png)

* You will be prompted that you cannot yet promote the asset. To promote an asset, you must associate your project with a deployment space. Click `Associate Deployment Space`:

![Associate Deployment Space](../.gitbook/assets/images/autoai/autoai-associate-deployment-space.png)

* You should have already created a deployment space in the *pre-work* section of the workshop. Click on `Existing`, select that deployment space and then click `Associate`.

* If you did not have an existing deployment, go to `New` tab, and give a name for your deployment space, then click `Associate`.

* After you promote the model to the deployment space succesfully, a notification will pop-up on the top as below. Click `deployment space` from this notification. Also you can reach this page by using the (☰) hamburger menu and click `Analyze` -> `Analytics deployments`:

![deployment space](../.gitbook/assets/images/autoai/autoai-view-deployment.png)

* If you came in through the `Menu` -> `Analyze` -> `Analytics deployments` path, Click on your deployment space:

![click deployment space](../.gitbook/assets/images/autoai/autoai-click-deployment-space.png)

* Under the *Assets* tab, click on your model:

![click model in deployment space](../.gitbook/assets/images/autoai/autoai-deployment-space-choose-model.png)

* Under the *Deployments* tab, click `Deploy` to deploy this model:

![click deploy button](../.gitbook/assets/images/autoai/autoai-click-deploy.png)

* Give your deployment an name and optional description and click `Create`:

![create deployment](../.gitbook/assets/images/autoai/autoai-name-and-create-deployment.png)

* The Deployment will show as *In-Progress* and then switch to *Deployed* when done. Click on the deployment:

![click final deployment](../.gitbook/assets/images/autoai/autoai-deployed.png)

* The Deployment *API reference* tab show how to use the model using *cURL*, *Java*, *Javascript*, *Python*, and *Scala*:

![Deployment API reference](../.gitbook/assets/images/autoai/autoai-api-reference-curl.png)

### Testing the deployed model with the GUI tool

Now you can test your model from the interface that is provided after the deployment.

* Click on the `Test` tab.

* Click on the *Provide input data as JSON* icon:

![Deployment API reference](../.gitbook/assets/images/autoai/autoai-test-switch-jsoninput.png)

* Paste the following data under *Body*, then click `Predict`:

```json
{
  "input_data": [
    {
      "fields": [
       "CustomerID",
        "CheckingStatus",
        "LoanDuration",
        "CreditHistory",
        "LoanPurpose",
        "LoanAmount",
        "ExistingSavings",
        "EmploymentDuration",
        "InstallmentPercent",
        "Sex",
        "OthersOnLoan",
        "CurrentResidenceDuration",
        "OwnsProperty",
        "Age",
        "InstallmentPlans",
        "Housing",
        "ExistingCreditsCount",
        "Job",
        "Dependents",
        "Telephone",
        "ForeignWorker"
      ],
      "values": [
        [
          "1",
          "no_checking",
          13,
          "credits_paid_to_date",
          "car_new",
          1343,
          "100_to_500",
          "1_to_4",
          2,
          "female",
          "none",
          3,
          "savings_insurance",
          46,
          "none",
          "own",
          2,
          "skilled",
          1,
          "none",
          "yes"
        ],
        [
          "2",
          "no_checking",
          24,
          "prior_payments_delayed",
          "furniture",
          4567,
          "500_to_1000",
          "1_to_4",
          4,
          "male",
          "none",
          4,
          "savings_insurance",
          36,
          "none",
          "free",
          2,
          "management_self-employed",
          1,
          "none",
          "yes"
        ]
      ]
    }
  ]
}
```

* The `Test` page will load the results of the model prediction. In this case, two predictions.

![Test deployment with JSON](../.gitbook/assets/images/autoai/autoai-test-json.png)

* Alternately, you can click the *Provide input using form* icon and input the various fields, then click `Predict`.

### Test the deployed model with cURL

We can also test the models REST interface using a variety of other tools. In this section, we will test using the cURL command.

> NOTE: Windows users will need the *cURL* command. It's recommended to [download gitbash](https://gitforwindows.org/) for this, as you'll also have other tools and you'll be able to easily use the shell environment variables in the following steps.

* Open a terminal (or command prompt) window and run the following to get a token to access the API. Replace the username and password with your own CP4D cluster `username` and `password`:

```bash
curl -k -X GET https://<cluster-url>/v1/preauth/validateAuth -u <username>:<password>
```

* A json string will be returned with a value for "accessToken" that will look *similar* to this:

```json
{"username":"scottda","role":"Admin","permissions":["access_catalog","administrator","manage_catalog","can_provision"],"sub":"scottda","iss":"KNOXSSO","aud":"DSX","uid":"1000331002","authenticator":"default","accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNjb3R0ZGEiLCJyb2xlIjoiQWRtaW4iLCJwZXJtaXNzaW9ucyI6WyJhY2Nlc3NfY2F0YWxvZyIsImFkbWluaXN0cmF0b3IiLCJtYW5hZ2VfY2F0YWxvZyIsImNhbl9wcm92aXNpb24iXSwic3ViIjoic2NvdHRkYSIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMxMDAyIiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJpYXQiOjE1NzM3NjM4NzYsImV4cCI6MTU3MzgwNzA3Nn0.vs90XYeKmLe0Efi5_3QV8F9UK1tjZmYIqmyCX575I7HY1QoH4DBhon2fa4cSzWLOM7OQ5Xm32hNUpxPH3xIi1PcxAntP9jBuM8Sue6JU4grTnphkmToSlN5jZvJOSa4RqqhjzgNKFoiqfl4D0t1X6uofwXgYmZESP3tla4f4dbhVz86RZ8ad1gS1_UNI-w8dfdmr-Q6e3UMDUaahh8JaAEiSZ_o1VTMdVPMWnRdD1_F0YnDPkdttwBFYcM9iSXHFt3gyJDCLLPdJkoyZFUa40iRB8Xf5-iA1sxGCkhK-NVHh-VTS2XmKAA0UYPGYXmouCTOUQHdGq2WXF7PkWQK0EA","_messageCode_":"success","message":"success"}
```

* We will temporarily save the "accessToken" part of this response to a variable in the terminal window as `WML_AUTH_TOKEN`. Copy the `accessToken` value and then run the following command to save it as a variable in your terminal:

```bash
export WML_AUTH_TOKEN=<value-of-access-token>
```

* Get the `URL` to invoke the model by going to the *API reference* tab and copying the `Endpoint`, and export it as `URL`:

![Model Deployment Endpoint](../.gitbook/assets/images/autoai/autoai-modeldeployment-endpoint.png)

* Run the following command to save the endpoint as a variable in your terminal:

```bash
export URL=https://blahblahblah.com
```

* Now run this curl command from a terminal window:

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data":[{"fields":["CustomerID","CheckingStatus","LoanDuration","CreditHistory","LoanPurpose","LoanAmount","ExistingSavings","EmploymentDuration","InstallmentPercent","Sex","OthersOnLoan","CurrentResidenceDuration","OwnsProperty","Age","InstallmentPlans","Housing","ExistingCreditsCount","Job","Dependents","Telephone","ForeignWorker"],"values":[["1","no_checking",13,"credits_paid_to_date","car_new",1343,"100_to_500","1_to_4",2,"female","none",3,"savings_insurance",46,"none","own",2,"skilled",1,"none","yes"]]}]}' $URL
```

* A json string will be returned with the model prediction.

## Conclusion

In this section we you have built, deployed and consumed (tested) a machine learning model. In this example, you did not have to perform many of the traditional data science / machine learning tasks associated with building models. By using the AutoAI capability of the platform, the tasks around data preparation, feature engineering, model selection, and more have been automated for you.