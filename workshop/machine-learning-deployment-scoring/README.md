# Machine Learning Model Deployment and Scoring

In this module, we will go through the process of deploying a machine learning model so it can be used by others. Deploying a model allows us to put a model into production, so that data can be passed to it to return a prediction. The deployment will result in an endpoint that makes the model available for wider use in applications and to make business decisions. There are several types of deployments available ([depending on the model framework used](https://www.ibm.com/support/producthub/icpdata/docs/content/SSQNUZ_current/wsj/analyze-data/pm_service_supported_frameworks.html)), of which we will explore:

* Online Deployments - Creates an endpoint to generate a score or prediction in real time.
* Batch Deployments - Creates an endpoint to schedule the processing of bulk data to return predictions.

This module is broken up into several sections that explore the different model deployment options as well as the different ways to invoke or consume the model. The first section of this lab will build an online deployment and test the model endpoint using both the built in testing tool as well as external testing tools. The remaining sections are optional, they build and test the batch deployment, followed by using the model from a python application.

1. [Online Deployment for a Model](#online-model-deployment)
   * Create Online Deployment
   * Test model using Cloud Pak for Data tooling
   * (Optional) Test model using cURL

1. [(Optional) Batch Deployment for a Model](#optional-batch-model-deployment)
   * Create Batch Deployment
   * Create and Schedule a Job

1. [(Optional) Integrate Model to an External Application](#optional-integrate-model-to-python-flask-application)

>*Note: The lab instructions below assume you have completed one of the machine learning modules to promote a model to the deployment space. If not, follow the instructions in one of the machine learning modules to create and promote a machine learning model.*

## Online Model Deployment

After a model has been created and saved / promoted to our deployment space, we will want to deploy the model so it can be used by others. For this section, we will be creating an online deployment. This type of deployment will make an instance of the model available to make predictions in real time via an API. Although we will use the Cloud Pak for Data UI to deploy the model, the same can be done programmatically.

* Navigate to the left-hand (☰) hamburger menu and choose `Analyze` -> `Analytics deployments`:

![Analytics Analyze deployments](../.gitbook/assets/images/navigation/menu-analytics-deployments.png)

* Choose the deployment space you setup previously by clicking on the name of your space.

* From your deployment space overview, in the table, find the model name for the model you previously built and now want to create a deployment against. Use your mouse to hover over the right side of that table row and click the `Deploy` rocket icon (the icons are not visible by default until you hover over them).

> Note: There may be more than one model listed in them 'Models' section. This can happen if you have run the Jupyter notebook more than once or if you have run through both the Jupyter notebook and AutoAI modules to create models. Although you could select any of the models you see listed in the page, the recommendation is to start with whicever model is available that is using a `spark-mllib_2.3` runtime.

![Actions Deploy model](../.gitbook/assets/images/deployment/deploy-spark-model.png)

* On the 'Create a deployment' screen, choose `Online` for the *Deployment Type*, give the Deployment a name and optional description and click the *`Create`* button.

![Online Deployment Create](../.gitbook/assets/images/deployment/deploy-online-deployment.png)

* The Deployment will show as *In progress* and then switch to *Deployed* when done.

![Status Deployed](../.gitbook/assets/images/deployment/deploy-status-deployed.png)

### Test Online Model Deployment

Cloud Pak for Data offers tools to quickly test out Watson Machine Learning models. We begin with the built-in tooling.

* From the Model deployment page, once the deployment status shows as *Deployed*, click on the name of your deployment. The deployment *API reference* tab shows how to use the model using *cURL*, *Java*, *Javascript*, *Python*, and *Scala*.

* To get to the built-in test tool, click on the `Test` tab and then click on the *`Provide input data as JSON`* icon.

![Test deployment with JSON](../.gitbook/assets/images/deployment/deploy-model-test-page.png)

* Copy and paste the following data objects into the *Body* panel (*Note: Make sure the input below is the only content in the field. Do not append it to the default content `{ "input_data": [] }` that may already be in the field).

```json
{
  "input_data": [
    {
      "fields": [ "CheckingStatus", "LoanDuration", "CreditHistory", "LoanPurpose", "LoanAmount", "ExistingSavings", "EmploymentDuration", "InstallmentPercent", "Sex", "OthersOnLoan", "CurrentResidenceDuration", "OwnsProperty", "Age", "InstallmentPlans", "Housing", "ExistingCreditsCount", "Job", "Dependents", "Telephone", "ForeignWorker"],
      "values": [
        [ "no_checking", 13, "credits_paid_to_date", "car_new", 1343, "100_to_500", "1_to_4", 2, "female", "none", 3, "savings_insurance", 46, "none", "own", 2, "skilled", 1, "none", "yes"]
      ]
    }
  ]
}
```

* Click the *`Predict`* button. The model will be called with the input data and the results will display in the *Result* window. Scroll down to the bottom of the result to see the prediction (i.e "Risk" or "No Risk"):

![Testing the deployed model](../.gitbook/assets/images/deployment/deploy-test-model-prediction.png)

> *Note: For some deployed models (for example AutoAI based models), you can provide the request payload using a generated form by clicking on the `Provide input using form` icon and providing values for the input fields of the form. If the form is not available for the model you deployed, the icon will remain grayed out.*
> ![Input to the fields](../.gitbook/assets/images/deployment/deploy-test-input-form.png)

### (Optional) Test Online Model Deployment using cURL

Now that the model is deployed, we can also test it from external applications. One way to invoke the model API is using the cURL command.

> NOTE: Windows users will need the *cURL* command. It's recommended to [download gitbash](https://gitforwindows.org/) for this, as you'll also have other tools and you'll be able to easily use the shell environment variables in the following steps. Also note that if you are not using gitbash, you may need to change *export* commands to *set* commands.

* In order to get access token you need to have `API Key`, that you can get from your IBM cloud account. You can create one by running following command.

```bash
ibmcloud iam api-key-create <key name>
```

* In a terminal window (or command prompt in Windows), run the following command to get a token to access the API. Replace `<API Key>` with the api key that you got from running above command.

```bash
curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: application/json' --data-urlencode 'grant_type=urn:ibm:params:oauth:grant-type:apikey' --data-urlencode 'apikey=<API Key>'
```

* A json string will be returned with a value for "accessToken" that will look *similar* to this:

```json
{"access_token":"eyJraWQiOiIyMDIwMDkyMjE4MzMiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC0zMTAwMDJKUlREIiwiaWQiOiJJQk1pZC0zMTAwMDJKUlREIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiNTFhYzkyYTUtZmRhMi00ZDE5LWJkZDItN2JmMTQwZmExYTQ1IiwiaWRlbnRpZmllciI6IjMxMDAwMkpSVEQiLCJnaXZlbl9uYW1lIjoiU2FuamVldiIsImZhbWlseV9uYW1lIjoiR2hpbWlyZSIsIm5hbWUiOiJTYW5qZWV2IEdoaW1pcmUiLCJlbWFpbCI6InNhbmplZXYuZ2hpbWlyZUBpYm0uY29tIiwic3ViIjoic2FuamVldi5naGltaXJlQGlibS5jb20iLCJhY2NvdW50Ijp7InZhbGlkIjp0cnVlLCJic3MiOiJjM2JmNzBjMWExMDViYTM5Y2Q2ZTIzOTJkMGFmNDYzMyIsImZyb3plbiI6dHJ1ZX0sImlhdCI6MTYwMTMxMzYwMSwiZXhwIjoxNjAxMzE3MjAxLCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.ZbWf7cYY96yVNL7k5qmxoqasvmACvQcPlu0iO-vSamIuo1Hbdho1tUvg95o061u1wCKtsP-QNlnhNzORB2Ziy1xYaTcXTwaOBpbIU95nyf14fpmgOioiH_t2EZi8vptkokgJEL_l1vRFpuE-AoV1Yr1f0zseZvABh__J7ifFPmGsHNOAEoFL2TL8CFiKwiDsXQJRTwloBgSKLP6_bmD-IkFpw0fnOkTk-TQE9qfdiKz1zE6qyXQADl3ukPyTaWqMsrCmESNhzXWEbGbBFMa4mevD_PesmZPQOpHKURp5c4GdNNzOMXPxML6wmICIUXGsspngjOi72OxCxtL-JW5WOA","refresh_token":"OKAWi2SWPcoNMdPbt2Z2_ssrBIt38djgF0A-LMwNjc2dEjiWcf5-tl6u8I-RVX-rs8Ua40FNJi_mSaRMU7LF5Be7RThXxZKdH1n14QTYMStA7PnEMpMHFGDoUM6vCPd1vcJBYG5A0il8gec4uzs-e0MourxgLxTnYTI8MTTdoAh8Ozl6yUSr0PtdmtwTn0E6cnVv1j0Spce0sZbK0vgzydienF4UCbmqNLcUEywuj_60o3Z1GP-PAv1zPiS9EzqCeDOo87rk6ts4TEX9QMtasqPm20MIsNThljtvJCdGY6GAewyRRGuWtOSlN4Vfxt__xGtkr_Ehm-5Sow56k3NXld-6FKFCWkckK24HROtL0TX0xOQ0gpgtdBzsL9QIMGHRYo34Wuakj0PR_vmSzly6hIvltuC4p5-ywyi0s8mTuT9nbmTaBrG7eih-LrAgUu7NVkWU8jhwMPi66eOLoVpjHLi2ODyZ-bg9fv0OVxNl0bH9AtiCKssI13L6_IdDO3FPL1ZLrkS36uh3JJO3H5p8DbBtpIPnBmkeTmdg3FX1SFbuiUX_hPpJzEp1VafsadUwSbZI98xDbgiSM7t5DwmGWNfCLqKlQM44R90bAouGXqUX6HcTBmq_0btrg6cxPWKzjBZgl6RXYjUO4Cs9kkrDKeoCZWwboEHY5xH3J_u4hdlrFYSX5lmFqbgS16qxMiycoT18WLz938d82QogZuh3FEbQxaYS1i1fe5q5m-90p8h4Tb_L9-q-gDkeDOvqSxAwasqYmvzPsxUMZaTLxx0r_EruhD5Qim4rUrqFnDJ71iQ2T3H2JUpExZZthsBRyk4u7qucE0BuTF_MJqzyVAtZFlHeWw1pheGEx5B_dXsrljvBDpOZ5F_yrMQLZyvrTifdMZbxkWRCWBEqFHHo9e6bGU0P1rgAfEym5JkDAefQqVtcN5p1f_ruVlGChyxxS9W5BBZ95ouUC0D_f01DIzyb4MRRO_UszdgebwWCHovMpcoZhz9BMRcin81UXDnvYic1dvVGD_6BxEp-Mql0roHREdiTWtWSgzEWx5k0xKUzfbNoVAVdQAjS2OQE3L1S0TR7__pQWJfxtLXu44wKH78Hp1EC0ihrskJbNWQuLk2NOaePHNcG2UVeWcST7Rw42z6nmlM","token_type":"Bearer","expires_in":3600,"expiration":1601317201,"scope":"ibm openid"}
```

* You will save this access token to a temporary environment variable in your terminal. Copy the access token value (without the quotes) in the terminal and then use the following export command to save the "accessToken" to a variable called `WML_AUTH_TOKEN`.

```bash
export WML_AUTH_TOKEN=<value-of-access-token>
```

* Back on the model deployment page, gather the `URL` to invoke the deployed model from the *API reference* by copying the `Endpoint`.

![Model Deployment Endpoint](../.gitbook/assets/images/deployment/deploy-model-endpoint.png)

* Now save that endpoint to a variable named `URL` in your terminal by exporting it. URL also requires a version query parameter.

```bash
export WML_URL=<value-of-endpoint>
```

Example of an URL:

```bash
export WML_URL="https://us-south.ml.cloud.ibm.com/ml/v4/deployments/98bfa972-f32e-40d0-94db-6092848652c1/predictions?version=2020-09-01"
```

* Now run this curl command from the terminal to invoke the model with the same payload we used previousy:

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data": [{"fields": [ "CheckingStatus", "LoanDuration", "CreditHistory", "LoanPurpose", "LoanAmount", "ExistingSavings", "EmploymentDuration", "InstallmentPercent", "Sex", "OthersOnLoan", "CurrentResidenceDuration", "OwnsProperty", "Age", "InstallmentPlans", "Housing", "ExistingCreditsCount", "Job", "Dependents", "Telephone", "ForeignWorker"],"values": [[ "no_checking", 13, "credits_paid_to_date", "car_new", 1343, "100_to_500", "1_to_4", 2, "female", "none", 3, "savings_insurance", 46, "none", "own", 2, "skilled", 1, "none", "yes"]]}]}' $WML_URL
```

* A json string will be returned with the response, including a  prediction from the model (i.e a "Risk" or "No Risk" at the end indicating the prediction of this loan representing risk).

## (Optional) Batch Model Deployment

Another approach to expose the model to be consumed by other users/applications is to create a batch deployment. This type of deployment will make an instance of the model available to make predictions against data assets or groups of records. The model prediction requests are scheduled as jobs, which are exected asynchronously. For the lab, we will break this into two steps: first step is creating the deployment (which we will do using the UI), then second step is creating and scheduling a job with values.

Lets start by creating the deployment:

* Navigate to the left-hand (☰) hamburger menu and choose `Deployment Spaces` -> `View all spaces`:

![Analytics Analyze deployments](../.gitbook/assets/images/navigation/menu-analytics-deployments.png)

* Choose the deployment space you created previously by clicking on the name of the space.

* From your deployment space overview, in the table, find the model name for the model you previously built and now want to create a deployment against. Use your mouse to hover over the right side of that table row and click the `Deploy` rocket icon (the icons are not visible by default until you hover over them).

> Note: There may be more than one model listed in them 'Models' section. This can happen if you have run the Jupyter notebook more than once or if you have run through both the Jupyter notebook and AutoAI modules to create models. Although you could select any of the models you see listed in the page, the recommendation is to start with whicever model is available that is using a `spark-mllib_2.3` runtime.

![Actions Deploy model](../.gitbook/assets/images/deployment/deploy-spark-model.png)

* On the 'Create a deployment' screen: choose `Batch` for the *Deployment Type*, give the deployment a name and optional description. From the 'Hardware definition' drop down, select the smallest option (`1 standard CPU, 4GB RAM` in this case though for large or frequent batch jobs, you might choose to scale the hardware up). Click the *`Create`* button.

![Batch Deployment Create](../.gitbook/assets/images/deployment/deploy-batch-deployment.png)

* Once the status shows as *Deployed* you will be able to start submitting jobs to the deployment.

![Status Deployed](../.gitbook/assets/images/deployment/deploy-batch_dep_status.png)

### Create and Schedule a Job

Next we can schedule a job to run against our batch deployment. We could create a job, with specific input data (or data asset) and schedule, either programmatically or through the UI. For this lab, we are going to do this programmatically using the Python client SDK. For this part of the exercise we're going to use a Jupyter notebook to create and submit a batch job to our model deployment.

>*Note: The batch job input is impacted by the machine learning framework used to build the model. Currently, SparkML based model batch jobs require inline payload to be used. For other frameworks, we can use data assets (i.e CSV files) as the input payload.*

#### Run the Batch Notebook

The Jupyter notebook is already included as an asset in the project you imported earlier.

* Go the (☰) navigation menu and click on the *Projects* link and then click on your analytics project.

![(☰) Menu -> Projects](../.gitbook/assets/images/navigation/menu-projects.png)

* From the project overview page, *click* on the `Assets` tab to open the assets page where your project assets are stored and organized.

* Scroll down to the `Notebooks` section of the page and *Click* on the pencil icon at the right of the `machinelearning-creditrisk-batchscoring` notebook.

![Notebook Open](../.gitbook/assets/images/deployment/deploy_batch_open_nb.png)

* When the Jupyter notebook is loaded and the kernel is ready, we will be ready to start executing it in the next section.

##### Notebook sections

With the notebook open, spend a minute looking through the sections of the notebook to get an overview. A notebook is composed of text (markdown or heading) cells and code cells. The markdown cells provide comments on what the code is designed to do. You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook or hitting the keyboard short cut to run the cell (Shift + Enter but can vary based on platform). While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

**Please note that some of the comments in the notebook are directions for you to modify specific sections of the code. Perform any changes as indicated before running / executing the cell.**

* Section `1.0 Install required packages` will install some of the libraries we are going to use in the notebook (many libraries come pre-installed on Cloud Pak for Data). Note that we upgrade the installed version of Watson Machine Learning Python Client. Ensure the output of the first code cell is that the python packages were successfully installed.

![NB Section 1 Complete](../.gitbook/assets/images/deployment/deploy-batchnb-packageinstall.png)

* Section `2.0 Create Batch Deployment Job` will create a job for the batch deployment. To do that, we will use the Watson Machine Learning client to get our deployment and create a job.

  * In the first code cell for Section2.1, be sure to update the `wml_credentials` variable.

    * The url should be the hostname of the Cloud Pak for Data instance.
    * The username and password should be the same credentials you used to log into Cloud Pak for Data.

  * In section 2.2, be sure to update the `DEPLOYMENT_SPACE_NAME` variable with your deployment space name (copy and past the name which is within the output of the previous code cell).

  * In section 2.3, be sure to update the `DEPLOYMENT_NAME` variable with the name of the batch deployment you created previously (copy and past the name which is within the output of the previous code cell).

![NB Section 2 Complete](../.gitbook/assets/images/deployment/deploy-batchnb-dsname-set.png)

![NB Section 2 Complete](../.gitbook/assets/images/deployment/deploy-batchnb-depname-set.png)

* Continue to run the rest of the cells in section 2 which will load the batch input data set and create the job. The last code cell in section 2 will show that the job is in a queued state.

* Section `3.0 Monitor Batch Job Status` will start polling the job status until it completes or fails. The code cell will output the status every 5 seconds as the job goes from queued to running to completed or failed.

![Batch Job Status](../.gitbook/assets/images/deployment/deploy_batch_results_poll.png)

* Once the job completes, continue to run the cells until the end of the notebook.

> **Important**: *Make sure that you stop the kernel of your notebook(s) when you are done, in order to conserve resources! You can do this by going to the Asset page of the project, selecting the three vertical dots under the Action column for the notebook you have been running and selecting to `Stop Kernel` from the Actions menu. If you see a lock icon on the notebook, click it to unlock the notebook before you click the Actions so you can see the stop kernel option.*
> ![Stop kernel](../.gitbook/assets/images/ml/stop-notebook-kernel.png)

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

* To install the Python requirements, from a terminal (or command prompt) navigate to where you cloned/downloaded the Git repository. Run the following commands:

  ```bash
  cd flaskapp
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

![Get the risk percentage as a result](../.gitbook/assets/images/deployment/flaskapp-output.png)

## Conclusion

In this section we covered the followings:

* Creating and Testing Online Deployments for models.
* (Optional) Creating and Testing Batch Deployments for models.
* (Optional) Integrating the model deployment in an external application.

Taking a predictive model and infusing AI into applications.
