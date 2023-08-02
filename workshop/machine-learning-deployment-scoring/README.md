# Machine Learning Model Deployment and Scoring

In this module, we will go through the process of deploying a machine learning model so it can be used by others. Deploying a model allows us to put a model into production, so that data can be passed to it to return a prediction. The deployment will result in an endpoint that makes the model available for wider use in applications and to make business decisions. There are several types of deployments available ([depending on the model framework used](https://www.ibm.com/support/producthub/icpdata/docs/content/SSQNUZ_current/wsj/analyze-data/pm_service_supported_frameworks.html)), of which we will explore:

* Online Deployments - Creates an endpoint to generate a score or prediction in real time.
* Batch Deployments - Creates an endpoint to schedule the processing of bulk data to return predictions.

This module is broken up into several sections that explore the different model deployment options as well as the different ways to invoke or consume the model. The first section of this lab will build an online deployment and test the model endpoint using both the built in testing tool as well as external testing tools. The remaining sections are optional, they build and test the batch deployment, followed by using the model from a python application.

> *Note: It is assumed that you have followed the instructions in the pre-work section to create a project based on an existing project file. If you did not use the project import or do not see the Jupyter notebooks mentioned in this module, see the `Workshop Resources` -> `FAQs / Tips` section for instructions to import the necessary notebooks. Also note that the Jupyter notebooks included in the project have been cleared of output. If you would like to see the notebook that has already been completed with output, see the `Workshop Resources` -> `FAQs / Tips` section for links to the completed notebooks.*

>*Note: It is also assumed that you have completed one of the machine learning modules to promote a model to the deployment space. If not, follow the instructions in one of the machine learning modules to create and promote a machine learning model.*

## Online Model Deployment

After a model has been created and saved / promoted to our deployment space, we will want to deploy the model so it can be used by others. For this section, we will be creating an online deployment. This type of deployment will make an instance of the model available to make predictions in real time via an API. Although we will use the Cloud Pak for Data UI to deploy the model, the same can be done programmatically.

* Navigate to the left-hand (☰) hamburger menu and click on `Deployments`.

![Analytics Analyze deployments](../images/navigation/menu-analytics-deployments.png)

* Click on the `Spaces` tab and then choose the deployment space you setup previously by clicking on the name of your space.

![Deployments space](../images/deployment/select-depspace.png)

* From your deployment space overview, in the table, find the model name for the model you previously built and now want to create a deployment against. Use your mouse to hover over the right side of that table row and click the `Deploy` rocket icon (the icons are not visible by default until you hover over them).

> Note: There may be more than one model listed in the 'Models' section. This can happen if you have run the Jupyter notebook more than once or if you have run through both the Jupyter notebook and AutoAI modules to create models. Although you could select any of the models you see listed in the page, the recommendation is to start with whichever model is available that is using a `spark-mllib_2.4` software specification.

![Actions Deploy model](../images/deployment/deploy-spark-model.png)

* On the 'Create a deployment' screen, choose `Online` for the `Deployment Type`, give the Deployment a name and optional description and click the *`Create`* button.

![Online Deployment Create](../images/deployment/deploy-online-deployment.png)

* Click on the `Deployments` tab. The online deployment will show as `In progress` and then switch to `Deployed` when done.

![Status Deployed](../images/deployment/deploy-status-deployed.png)

### Test Online Model Deployment

Cloud Pak for Data offers tools to quickly test out Watson Machine Learning models. We begin with the built-in tooling.

* From the Model deployment page, once the deployment status shows as `Deployed`, click on the name of your deployment. The deployment `API reference` tab shows how to use the model using `cURL`, `Java`, `Javascript`, `Python`, and `Scala`.

* To get to the built-in test tool, click on the `Test` tab and then click on the *`Provide input data as JSON`* icon.

![Test deployment with JSON](../images/deployment/deploy-model-test-page.png)

* Copy and paste the following data objects into the `Body` panel (replace the text that was in the input panel).

    > *Note: Click the tab appropriate for the model you are testing (either an AutoAI model or one built using the Jupyter notebook). Also make sure the input below is the only content in the field. Do not append it to the default content `{ "input_data": [] }` that may already be in the test input panel.*

    === "Jupyter Spark Model"

        ```json
        { "input_data": [{
            "fields": [ "CheckingStatus", "LoanDuration", "CreditHistory", "LoanPurpose", "LoanAmount", "ExistingSavings", "EmploymentDuration", "InstallmentPercent", "Sex", "OthersOnLoan", "CurrentResidenceDuration", "OwnsProperty", "Age", "InstallmentPlans", "Housing", "ExistingCreditsCount", "Job", "Dependents", "Telephone", "ForeignWorker"],
            "values": [[ "no_checking", 13, "credits_paid_to_date", "car_new", 1343, "100_to_500", "1_to_4", 2, "female", "none", 3, "savings_insurance", 46, "none", "own", 2, "skilled", 1, "none", "yes"]]
        }]}
        ```

    === "AutoAI Model"

        ```json
        { "input_data": [{
            "fields": [ "CustomerId", "CheckingStatus", "LoanDuration", "CreditHistory", "LoanPurpose", "LoanAmount", "ExistingSavings", "EmploymentDuration", "InstallmentPercent", "Sex", "OthersOnLoan", "CurrentResidenceDuration", "OwnsProperty", "Age", "InstallmentPlans", "Housing", "ExistingCreditsCount", "Job", "Dependents", "Telephone", "ForeignWorker"],
            "values": [[ "", "no_checking", 13, "credits_paid_to_date", "car_new", 1343, "100_to_500", "1_to_4", 2, "female", "none", 3, "savings_insurance", 46, "none", "own", 2, "skilled", 1, "none", "yes"]]
        }]}
        ```

* Click the *`Predict`* button. The model will be called with the input data and the results will display in the *Result* window. Scroll down to the bottom of the result to see the prediction (i.e "Risk" or "No Risk"):

![Testing the deployed model](../images/deployment/deploy-test-model-prediction.png)

> *Note: For some deployed models (for example AutoAI based models), you can provide the request payload using a generated form by clicking on the `Provide input using form` icon and providing values for the input fields of the form. If the form is not available for the model you deployed, the icon will not be displayed.*
> ![Input to the fields](../images/deployment/deploy-test-input-form.png)

### (Optional) Test Online Model Deployment using cURL

Now that the model is deployed, we can also test it from external applications. One way to invoke the model API is using the cURL command.

> NOTE: Windows users will need the *cURL* command. It's recommended to [download gitbash](https://gitforwindows.org/) for this, as you'll also have other tools and you'll be able to easily use the shell environment variables in the following steps. Also note that if you are not using gitbash, you may need to change *export* commands to *set* commands.

* In a terminal window (or command prompt in Windows), run the following command to get a token to access the API. Replace `<username>` and `<password>` with the username and password you used to log into the Cloud pak for data cluster. Replace `<cluster-url>` with just the hostname of the cloud pak for data cluster (i.e the url from your web browser address bar)

```bash
curl -k -X GET https://<cluster-url>/v1/preauth/validateAuth -u <username>:<password>
```

* A json string will be returned with a value for "accessToken" that will look *similar* to this:

```json
{"username":"scottda","role":"Admin","permissions":["access_catalog","administrator","manage_catalog","can_provision"],"sub":"scottda","iss":"KNOXSSO","aud":"DSX","uid":"1000331002","authenticator":"default","accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNjb3R0ZGEiLCJyb2xlIjoiQWRtaW4iLCJwZXJtaXNzaW9ucyI6WyJhY2Nlc3NfY2F0YWxvZyIsImFkbWluaXN0cmF0b3IiLCJtYW5hZ2VfY2F0YWxvZyIsImNhbl9wcm92aXNpb24iXSwic3ViIjoic2NvdHRkYSIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMxMDAyIiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJpYXQiOjE1NzM3NjM4NzYsImV4cCI6MTU3MzgwNzA3Nn0.vs90XYeKmLe0Efi5_3QV8F9UK1tjZmYIqmyCX575I7HY1QoH4DBhon2fa4cSzWLOM7OQ5Xm32hNUpxPH3xIi1PcxAntP9jBuM8Sue6JU4grTnphkmToSlN5jZvJOSa4RqqhjzgNKFoiqfl4D0t1X6uofwXgYmZESP3tla4f4dbhVz86RZ8ad1gS1_UNI-w8dfdmr-Q6e3UMDUaahh8JaAEiSZ_o1VTMdVPMWnRdD1_F0YnDPkdttwBFYcM9iSXHFt3gyJDCLLPdJkoyZFUa40iRB8Xf5-iA1sxGCkhK-NVHh-VTS2XmKAA0UYPGYXmouCTOUQHdGq2WXF7PkWQK0EA","_messageCode_":"success","message":"success"}
```

* You will save this access token to a temporary environment variable in your terminal. Copy the access token value (without the quotes) in the terminal and then use the following export command to save the "accessToken" to a variable called `WML_AUTH_TOKEN`.

```bash
export WML_AUTH_TOKEN=<value-of-access-token>
```

* Back on the model deployment page, gather the `URL` to invoke the deployed model from the *API reference* by copying the `Endpoint`.

![Model Deployment Endpoint](../images/deployment/deploy-model-endpoint.png)

* Now save that endpoint to a variable named `URL` in your terminal by exporting it.

```bash
export URL=<value-of-endpoint>
```

* Now run this curl command from the terminal to invoke the model with the same payload we used previousy:

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data": [{"fields": [ "CheckingStatus", "LoanDuration", "CreditHistory", "LoanPurpose", "LoanAmount", "ExistingSavings", "EmploymentDuration", "InstallmentPercent", "Sex", "OthersOnLoan", "CurrentResidenceDuration", "OwnsProperty", "Age", "InstallmentPlans", "Housing", "ExistingCreditsCount", "Job", "Dependents", "Telephone", "ForeignWorker"],"values": [[ "no_checking", 13, "credits_paid_to_date", "car_new", 1343, "100_to_500", "1_to_4", 2, "female", "none", 3, "savings_insurance", 46, "none", "own", 2, "skilled", 1, "none", "yes"]]}]}' $URL
```

* A json string will be returned with the response, including a  prediction from the model (i.e a "Risk" or "No Risk" at the end indicating the prediction of this loan representing risk).

## (Optional) Batch Model Deployment

Another approach to expose the model to be consumed by other users/applications is to create a batch deployment. This type of deployment will make an instance of the model available to make predictions against data assets or groups of records. The model prediction requests are scheduled as jobs, which are exected asynchronously. For the lab, we will break this into two steps:

1. Creating the deployment (which we will do using the UI).
1. Creating and scheduling a job with values (which we will do using a Jupyter Notebook).

Lets start by creating the deployment:

* Navigate to the left-hand (☰) hamburger menu and click on `Deployments`.

![Analytics Analyze deployments](../images/navigation/menu-analytics-deployments.png)

* Click on the `Spaces` tab and then choose the deployment space you setup previously by clicking on the name of your space.

![Deployments space](../images/deployment/select-depspace.png)

* From your deployment space overview, in the table, find the model name for the model you previously built and now want to create a deployment against. Use your mouse to hover over the right side of that table row and click the `Deploy` rocket icon (the icons are not visible by default until you hover over them).

> Note: There may be more than one model listed in them 'Models' section. This can happen if you have run the Jupyter notebook more than once or if you have run through both the Jupyter notebook and AutoAI modules to create models. Although you could select any of the models you see listed in the page, the recommendation is to start with whicever model is available that is using a `spark-mllib_2.4` software specification.

![Actions Deploy model](../images/deployment/deploy-spark-model.png)

* On the 'Create a deployment' screen: choose `Batch` for the `Deployment Type`, give the deployment a name and optional description. From the 'Hardware definition' drop down, select the smallest option (`1 standard CPU, 4GB RAM` in this case though for large or frequent batch jobs, you might choose to scale the hardware up). Click the *`Create`* button.

![Batch Deployment Create](../images/deployment/deploy-batch-deployment.png)

* Once the status shows as `Deployed` you will be able to start submitting jobs to the deployment.

![Status Deployed](../images/deployment/deploy-batch_dep_status.png)

### Create and Schedule a Job

Next we can schedule a job to run against our batch deployment. We could create a job, with specific input data (or data asset) and schedule, either programmatically or through the UI. For this lab, we are going to do this programmatically using the Python client SDK. For this part of the exercise we're going to use a Jupyter notebook to create and submit a batch job to our model deployment.

>*Note: The batch job input is impacted by the machine learning framework used to build the model. Currently, SparkML based model batch jobs require inline payload to be used. For other frameworks, we can use data assets (i.e CSV files) as the input payload.*

#### Run the Batch Notebook

The Jupyter notebook is already included as an asset in the project you imported earlier.

* Go the (☰) navigation menu and under the *Projects* section click on *`All Projects`*.

![(☰) Menu -> Projects](../images/navigation/menu-projects.png)

* Click the project name you created in the pre-work section.

* From your `Project` overview page, click on the *`Assets`* tab to open the assets page where your project assets are stored and organized.

* Scroll down to the `Notebooks` section of the page and click on the pencil icon at the right of the `machinelearning-creditrisk-sparkmlmodel` notebook.

![Notebook Open](../images/deployment/deploy_batch_open_nb.png)

* When the Jupyter notebook is loaded and the kernel is ready, we will be ready to start executing it in the next section.

##### Notebook sections

With the notebook open, spend a minute looking through the sections of the notebook to get an overview. A notebook is composed of text (markdown or heading) cells and code cells. The markdown cells provide comments on what the code is designed to do. You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook or hitting the keyboard short cut to run the cell (Shift + Enter but can vary based on platform). While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

**Please note that some of the comments in the notebook are directions for you to modify specific sections of the code. Perform any changes as indicated before running / executing the cell.**

* Section `1.0 Install required packages` will install some of the libraries we are going to use in the notebook (many libraries come pre-installed on Cloud Pak for Data). Note that we upgrade the installed version of Watson Machine Learning Python Client. Ensure the output of the first code cell is that the python packages were successfully installed.

![NB Section 1 Complete](../images/deployment/deploy-batchnb-packageinstall.png)

* Section `2.0 Create Batch Deployment Job` will create a job for the batch deployment. To do that, we will use the Watson Machine Learning client to get our deployment and create a job.

  * In the first code cell for `Section2.1`, be sure to update the `wml_credentials` variable.

    * The url should be the hostname of the Cloud Pak for Data instance.
    * The username and password should be the same credentials you used to log into Cloud Pak for Data.

  * In section 2.2, be sure to update the `DEPLOYMENT_SPACE_NAME` variable with your deployment space name (copy and past the name which is within the output of the previous code cell).

  * In section 2.3, be sure to update the `DEPLOYMENT_NAME` variable with the name of the batch deployment you created previously (copy and past the name which is within the output of the previous code cell).

![NB Section 2 Complete](../images/deployment/deploy-batchnb-dsname-set.png)

![NB Section 2 Complete](../images/deployment/deploy-batchnb-depname-set.png)

* Continue to run the rest of the cells in section 2 which will load the batch input data set and create the job. The last code cell in section 2 will show that the job is in a queued state.

* Section `3.0 Monitor Batch Job Status` will start polling the job status until it completes or fails. The code cell will output the status every 5 seconds as the job goes from queued to running to completed or failed.

![Batch Job Status](../images/deployment/deploy_batch_results_poll.png)

* Once the job completes, continue to run the cells until the end of the notebook.

### Cleanup and Stop Environment

**Important**: In order to conserve resources, make sure that you stop the environment used by your notebook(s) when you are done.

* Navigate back to your project information page by clicking on your project name from the navigation drill down on the top left of the page.

![Back to project](../images/ml/navigate-to-project.png)

* Click on the `Environments` tab near the top of the page. Then in the `Active environment runtimes` section, you will see the environment used by your notebook (i.e the `Tool` value is `Notebook`). Click on the three vertical dots at the right of that row and select the `Stop` option from the menu.

![Stop environment](../images/ml/stop-notebook-environment.png)

* Click the `Stop` button on the subsequent pop up window.

## (Optional) Integrate Model to Python Flask Application

You can also access the online model deployment directly through the REST API. This allows you to use your model for inference in any of your apps. For this workshop we'll be using a Python Flask application to collect information, score it against the model, and show the results.

> **IMPORTANT: This SAMPLE application only runs on python 3.6 and above, so the instructions here are for python 3.6+ only. You will need to have Python 3.6 or later already installed on your machine**
> *Note: The instructions below assume you have completed the pre-work module and thus have the Git repository already on your machine (cloned or downloaded).*

### Install Dependencies

The general recommendation for Python development is to use a virtual environment ([`venv`](https://docs.python.org/3/tutorial/venv.html)). To install and initialize a virtual environment, use the `venv` module on Python 3:

* Initialize a virtual environment with [`venv`](https://docs.python.org/3/tutorial/venv.html). Run the following commands in a terminal (or command prompt):

  ```bash
  # Create the virtual environment using Python.
  # Note, it may be named python3 on your system.
  python -m venv venv       # Python 3.X

  # Source the virtual environment. Use one of the two commands depending on your OS.
  source venv/bin/activate  # Mac or Linux
  ./venv/Scripts/activate   # Windows PowerShell
  ```

  > **TIP** To terminate the virtual environment use the `deactivate` command.

* Unzip the python application zip file that you downloaded in the pre-work section.

* To install the Python requirements, from a terminal (or command prompt) navigate to where you unzipped the python application. Run the following commands:

  ```bash
  pip install -r requirements.txt
  ```

### Update Environment Variables

It's best practice to store configurable information as environment variables, instead of hard-coding any important information. To reference our model and supply an API key, we'll pass these values in via a file that is read, the key-value pairs in this files are stored as environment variables.

* Copy the `env.sample` file to `.env`.

  ```bash
  cp env.sample .env
  ```

* Edit `.env` to and fill in the `MODEL_URL` as well as the `AUTH_URL`, `AUTH_USERNAME`, and `AUTH_PASSWORD`.

  * `MODEL_URL` is your web service URL for scoring which you got from the section above
  * `AUTH_URL` is the preauth url of your CloudPak4Data and will look like this: `https://<cluster_url>/v1/preauth/validateAuth`
  * `AUTH_USERNAME` is your username with which you login to the CloudPak4Data environment
  * `AUTH_PASSWORD` is your password with which you login to the CloudPak4Data environment

  >Note: Alternatively, you can fill in the `AUTH_TOKEN` instead of `AUTH_URL`, `AUTH_USERNAME`, and `AUTH_PASSWORD`. You will have generated this token in the section above. However, since tokens expire after a few hours and you would need to restart your app to update the token, this option is not suggested. Instead, if you use the username/password option, the app can generate a new token every time for you so it will always have a non-expired ones.

* Here's an example of a completed lines of the .env file.

  ```bash
  # Required: Provide your web service URL for scoring.
  # E.g., MODEL_URL=https://<cluster_url>/v4/deployments/<deployment_space_guid>/predictions
  MODEL_URL=https://cp4d.cp4dworkshops.com/v4/deployments/5f939979-14c2-4538-a2af-a970aeb59abd/predictions

  # Required: Please fill in EITHER section A OR B below:

  # #### A: Authentication using username and password
  #   Fill in the authntication url, your CloudPak4Data username, and CloudPak4Data password.
  #   Example:
  #     AUTH_URL=<cluster_url>/v1/preauth/validateAuth
  #     AUTH_USERNAME=my_username
  #     AUTH_PASSWORD=super_complex_password
  AUTH_URL=https://cp4d.cp4dworkshops.com/v1/preauth/validateAuth
  AUTH_USERNAME=username_001
  AUTH_PASSWORD=my_secure_password_!
  ```

### Start Application

* Start the flask server by running the following command:

  ```bash
  python creditriskapp.py
  ```

* Use your browser to go to [http://0.0.0.0:5000](http://0.0.0.0:5000) and try it out.

  > **TIP**: Use `ctrl`+`c` to stop the Flask server when you are done.

#### Test the application

* Either use the default values pre-filled in the input form, or modify the value and then click the `Submit` button. The python application will invoke the predictive model and a risk prediction & probability is returned:

![Get the risk percentage as a result](../images/deployment/flaskapp-output.png)

## Conclusion

In this section we covered the followings:

* Creating and Testing Online Deployments for models.
* (Optional) Creating and Testing Batch Deployments for models.
* (Optional) Integrating the model deployment in an external application.

Taking a predictive model and infusing AI into applications.
