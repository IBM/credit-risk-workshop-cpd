# Machine Learning in Jupyter Notebook

This section is broken up into the following steps:

1. [Build a model](#1-build-a-model)
1. [Deploying the model](#2-deploying-the-model)
1. [Testing the model](#3-testing-the-model)
1. [(Optional) Create a Python Flask app that uses the model](#4-optional-create-a-python-flask-app-that-uses-the-model)

## 1. Build a model

For this part of the exercise we're going to build a model with a Jupyter notebook, by importing our data, and creating a machine learning model by using a Random Forest Classifier.

### Import the notebook

At the project overview, either click the `+Add to project` button, and choose `Notebook`, or to the right of *Notebooks* click `+ New notebook`:

![Add a new asset](../.gitbook/assets/images/wml/wml-1-add-asset.png)

On the next panel select the *From URL* tab, give your notebook a name, provide the following URL, and choose the Python 3.6 environment:

```bash
https://raw.githubusercontent.com/IBM/credit-risk-workshop-cpd/master/notebooks/credit-risk-notebook.ipynb
```

> The notebook is hosted in the same repo as [the workshop](https://github.com/IBM/credit-risk-workshop-cpd).
>
> * **Notebook**: [TelcoChurnICP4D.ipynb](https://github.com/IBM/credit-risk-workshop-cpd/master/notebooks/credit-risk-notebook.ipynb)
> * **Notebook with output**: [with-output/TelcoChurnICP4DOutput.ipynb](https://github.com/IBM/credit-risk-workshop-cpd/master/notebooks/credit-risk-notebook-with-output.ipynb)

![Add notebook name and URL](../.gitbook/assets/images/wml/wml-2-add-name-and-url.png)

When the Jupyter notebook is loaded and the kernel is ready then we can start executing cells.

![Notebook loaded](../.gitbook/assets/images/wml/wml-3-notebook-loaded.png)

### Run the notebook

> **Important**: *Make sure that you stop the kernel of your notebook(s) when you are done, in order to prevent conserve resources!*

![Stop kernel](../.gitbook/assets/images/wml/JupyterStopKernel.png)

Spend a minute looking through the sections of the notebook to get an overview. You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook. While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

#### Install Python packages

Section `1.0 Install required packages` will show the libraries that come pre-installed on Cloud Pak for Data. Note that we'll have to upgrade the installed version of Watson Machine Learning Python Client. This workshop uses [`pyspark`](https://spark.apache.org/docs/latest/api/python/index.html), and [`sklearn`](https://scikit-learn.org/stable/) to build our model.

#### Create the model

Section `3.0 Create a model` will split the data into training and test data, and create a model using the Random Forest Classifier algorithm.

![Building the pipeline and model](../.gitbook/assets/images/wml/wml-6-buid-pipeline-and-model.png)

Continue to run the remaining cells in the section to build the model.

#### Save the model

Section `4.0 Save the model` will save the model to your project. Update the `MODEL_NAME` variable to something unique and easisly identifiable.

```python
MODEL_NAME = "user123 customer churn model"
```

Continue to run the remaining cells in the section to save the model to Cloud Pak for Data. We'll be able to test it out with the Cloud Pak for Data tools in just a few minutes!

We've successfully built and deployed a machine learning model. Congratulations!

## 2. Deploying the model

Navigate to the left-hand (☰) hamburger menu and choose `Analyze` -> `Analytics deployments`:

![Analytics Analyze deployments](../.gitbook/assets/images/wml/AnalyzeAnalyticsDeployments.png)

Choose the existing space you setup previously.

In your space, select the model name that you just built in the notebook and click the 3 dots under `Actions`, and choose `Deploy`:

![Actions Deploy model](../.gitbook/assets/images/wml/ActionsDeployModel.png)

On the next screen, choose `Online` for the *Deployment Type*, give the Deployment a name and optional description and click `Create`:

![Online Deployment Create](../.gitbook/assets/images/wml/OnlineDeploymentCreate.png)

Once the status shows as *Deployed* , you can click on the deployment name to begin testing:

![Status Deployed](../.gitbook/assets/images/wml/StatusDeployed.png)

## 3. Testing the model

Cloud Pak for Data offers tools to quickly test out Watson Machine Learning models. We begin with the built-in tooling.

### Test the saved model with built-in tooling

Click on the *Test* tab and paste the following into the *Enter input data* cell:

```json
{
   "input_data":[
      {
         "fields":[
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges"
         ],
         "values":[
            [
               "Female",
               0,
               "No",
               "No",
               1,
               "No",
               "No phone service",
               "DSL",
               "No",
               "No",
               "No",
               "No",
               "No",
               "No",
               "Month-to-month",
               "No",
               "Bank transfer (automatic)",
               25.25,
               25.25
            ]
         ]
      }
   ]
}
```

Click `Predict` and the model will be called with the input data. The results will display in the *Result* window. Scroll down to the bottom (Line #114) to see either a "Yes" or a "No" for Churn:

![Testing the deployed model](../.gitbook/assets/images/wml/TestingDeployedModel.png)

### Test the deployed model with cURL

> NOTE: Windows users will need the *cURL* command. It's recommended to [download gitbash](https://gitforwindows.org/) for this, as you'll also have other tools and you'll be able to easily use the shell environment variables in the following steps.

In a terminal window, run the following to get a token to access the API. Use your CP4D cluster `username` and `password`:

```bash
curl -k -X GET https://<cluster-url>/v1/preauth/validateAuth -u <username>:<password>
```

A json string will be returned with a value for "accessToken" that will look *similar* to this:

```json
{"username":"scottda","role":"Admin","permissions":["access_catalog","administrator","manage_catalog","can_provision"],"sub":"scottda","iss":"KNOXSSO","aud":"DSX","uid":"1000331002","authenticator":"default","accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNjb3R0ZGEiLCJyb2xlIjoiQWRtaW4iLCJwZXJtaXNzaW9ucyI6WyJhY2Nlc3NfY2F0YWxvZyIsImFkbWluaXN0cmF0b3IiLCJtYW5hZ2VfY2F0YWxvZyIsImNhbl9wcm92aXNpb24iXSwic3ViIjoic2NvdHRkYSIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMxMDAyIiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJpYXQiOjE1NzM3NjM4NzYsImV4cCI6MTU3MzgwNzA3Nn0.vs90XYeKmLe0Efi5_3QV8F9UK1tjZmYIqmyCX575I7HY1QoH4DBhon2fa4cSzWLOM7OQ5Xm32hNUpxPH3xIi1PcxAntP9jBuM8Sue6JU4grTnphkmToSlN5jZvJOSa4RqqhjzgNKFoiqfl4D0t1X6uofwXgYmZESP3tla4f4dbhVz86RZ8ad1gS1_UNI-w8dfdmr-Q6e3UMDUaahh8JaAEiSZ_o1VTMdVPMWnRdD1_F0YnDPkdttwBFYcM9iSXHFt3gyJDCLLPdJkoyZFUa40iRB8Xf5-iA1sxGCkhK-NVHh-VTS2XmKAA0UYPGYXmouCTOUQHdGq2WXF7PkWQK0EA","_messageCode_":"success","message":"success"}
```

Export the "accessToken" part of this response in the terminal window as `WML_AUTH_TOKEN`. Get the `URL` from the *API reference* by copying the `Endpoint`, and export it as `URL`:

![Model Deployment Endpoint](../.gitbook/assets/images/wml/ModelDeploymentEndpoint.png)

```bash
export WML_AUTH_TOKEN=<value-of-access-token>
export URL=https://blahblahblah.com
```

Now run this curl command from a terminal window:

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data": [{"fields": ["gender","SeniorCitizen","Partner","Dependents","tenure","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges"],"values": [["Female",0,"No","No",1,"No","No phone service","DSL","No","No","No","No","No","No","Month-to-month","No","Bank transfer (automatic)",25.25,25.25]]}]}' $URL
```

A json string will be returned with the response, including a "Yes" of "No" at the end indicating the prediction of if the customer will churn or not.

## 4. (Optional) Create a Python Flask app that uses the model

You can also access the web service directly through the REST API. This allows you to use your model for inference in any of your apps. For this workshop we'll be using a Python Flask application to collect information, score it against the model, and show the results.

### Install dependencies

The general recommendation for Python development is to use a virtual environment ([`venv`](https://docs.python.org/3/tutorial/venv.html)). To install and initialize a virtual environment, use the `venv` module on Python 3 (you install the virtualenv library for Python 2.7):

In a terminal go to the cloned repo directory.

```bash
git clone https://github.com/IBM/cloudpakfordata-telco-churn-workshop
cd cloudpakfordata-telco-churn-workshop
```

Initialize a virtual environment with [`venv`](https://docs.python.org/3/tutorial/venv.html).

```bash
# Create the virtual environment using Python. Use one of the two commands depending on your Python version.
# Note, it may be named python3 on your system.
python -m venv venv       # Python 3.X
virtualenv venv           # Python 2.X

# Source the virtual environment. Use one of the two commands depending on your OS.
source venv/bin/activate  # Mac or Linux
./venv/Scripts/activate   # Windows PowerShell
```

> **TIP** To terminate the virtual environment use the `deactivate` command.

Finally, install the Python requirements.

```bash
cd flaskapp
pip install -r requirements.txt
```

### Update environment variables

It's best practice to store configurable information as environment variables, instead of hard-coding any important information. To reference our model and supply an API key, we'll pass these values in via a file that is read, the key-value pairs in this files are stored as environment variables.

Copy the `env.sample` file to `.env`.

```bash
cp env.sample .env
```

Edit `.env` to and fill in the `MODEL_URL` as well as the `AUTH_URL`, `AUTH_USERNAME`, and `AUTH_PASSWORD`.

* `MODEL_URL` is your web service URL for scoring which you got from the section above
* `AUTH_URL` is the preauth url of your CloudPak4Data and will look like this: `https://<cluster_url>/v1/preauth/validateAuth`
* `AUTH_USERNAME` is your username with which you login to the CloudPak4Data environment
* `AUTH_PASSWORD` is your password with which you login to the CloudPak4Data environment

Note: Alternatively, you can fill in the `AUTH_TOKEN` instead of `AUTH_URL`, `AUTH_USERNAME`, and `AUTH_PASSWORD`. You will have generated this token in the section above. However, since tokens expire after a few hours and you would need to restart your app to update the token, this option is not suggested. Instead, if you use the username/password option, the app can generate a new token every time for you so it will always have a non-expired ones.

here's an example of a completed lines of the .env file.

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

### Start the application

Start the flask server by running the following command:

```bash
python telcochurn.py
```

Use your browser to go to [http://0.0.0.0:5000](http://0.0.0.0:5000) and try it out.

> **TIP**: Use `ctrl`+`c` to stop the Flask server when you are done.

### Sample output

The user inputs various values

![Input a bunch of data...](../.gitbook/assets/images/generic/input.png)

The churn percentage is returned:

![Get the churn percentage as a result](../.gitbook/assets/images/generic/score.png)

## Conclusion

In this section we covered how the followings:

* Creating a Jupyter Notebook
* Creating Models
* Deploying Models
* Testing your deployed model
* Creating a basic app to use your model

With this knowledge you should feel right at home within the Jupyter notebook. Moreover, you now know how to operationalize a model and use it in a real life scenario.
