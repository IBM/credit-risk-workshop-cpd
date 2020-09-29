# Load Historic Data for OpenScale

For a deployed machine learning model, OpenScale will record all of the requests for scoring and the results in the datamart using feedback logging. In this submodule, we'll emulate a production system that has been used for a week to score many requests, allowing the various configured monitors to present some interesting data. Note that this Historic Data submodule can be run at any time.

## Steps for Historical Data Load

The submodule contains the following steps:

1. [Open the notebook](#1-open-the-notebook)
1. [Run the notebook](#2-run-the-notebook)
1. [Explore the Watson OpenScale UI](#3-explore-the-watson-openscale-ui)

## 1. Open the notebook

If you [Created the Project](https://ibm-developer.gitbook.io/cloudpakfordata-credit-risk-workshop/getting-started/pre-work#create-a-new-project) using the [CreditRiskProject.zip](../../projects/CreditRiskProject.zip) file, your notebook will be present in that project.

* Go the (☰) navigation menu and click on the *Projects* link and then click on your analytics project.

  ![(☰) Menu -> Projects](../.gitbook/assets/images/navigation/menu-projects.png)

* From your *Project* overview page, click on the *`Assets`* tab to open the assets page where your project assets are stored and organized.

* Scroll down to the `Notebooks` section of the page and *Click* on the pencil icon at the right of the `openscale-historic-data` notebook.

  ![Project from zip assets tab](../.gitbook/assets/images/openscale-config/openscale-config-historic-notebook.png)

* When the Jupyter notebook is loaded and the kernel is ready, we will be ready to start executing it in the next section.

  ![Notebook loaded](../.gitbook/assets/images/openscale/openscale-fullconfignotebook-loaded.png)

* You may now skip to the next section, [running the notebook](#2-run-the-notebook).

### Import the Notebook

> **NOTE: You should probably not need this step and should only perform it if instructed to do so.**

* If, for some reason, you are not using the [Created the Project](https://ibm-developer.gitbook.io/cloudpakfordata-credit-risk-workshop/getting-started/pre-work#create-a-new-project) step in the Pre-work to import [CreditRiskProject.zip](../../projects/CreditRiskProject.zip), then you will need to import the notebook file by itself. Use the following steps for that.

* At the project overview click the *New Asset* button, and choose *Add notebook*.

* On the next panel select the *From URL* tab, give your notebook a name, provide the following 'Notebook URL', and choose the default Python 3.6 environment:

  ```bash
  https://raw.githubusercontent.com/IBM/credit-risk-workshop-cpd/master/notebooks/openscale-historic-data.ipynb
  ```

  ![Add notebook name and URL](../.gitbook/assets/images/openscale-config/openscale-config-url-historic.png)

* When the Jupyter notebook is loaded and the kernel is ready then we can start executing cells.

## 3. Run the Notebook

Spend some time looking through the sections of the notebook to get an overview. A notebook is composed of text (markdown or heading) cells and code cells. The markdown cells provide comments on what the code is designed to do.

You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook or hitting the keyboard short cut to run the cell (Shift + Enter but can vary based on platform). While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

_**Please note that there are several places in the notebook where you need to update variables. Some of the comments in the notebook are directions for you to modify specific sections of the code. Perform any changes as indicated before running / executing the cell. These changes are described below.**_

#### WOS_CREDENTIALS

* In the notebook section *2.0*  you will add your Cloud Pak for Data platform credentials for the *WOS_CREDENTIALS*.

  * For the `url`, use the URL your Cloud Pak for Data cluster, i.e something like: `"url": "https://zen.clusterid.us-south.containers.appdomain.cloud"`
  * For the `username`, use your Cloud Pak for Data login username.
  * For the `password`, user your Cloud Pak for Data login password.

> *Note: The Jupyter notebook included in the project has been cleared of output. If you would like to see the notebook that has already been completed with associated output, it is hosted in the same repo as this workshop: **Notebook with output**: [openscale-historic-data-with-output.ipynb](../../notebooks/with-output/openscale-historic-data-with-output.ipynb)*

## 4. Explore the Watson OpenScale UI

Now that we've simulated a Machine Learning deployment in production, we can look at the associated monitors again and see more detail. Re-visit the various monitors and look again at the graphs, charts and explanations after the addition of the historical data:

* [Fairness monitor and Explainability](./FAIRNESS-EXPLAINABILITY-README.md#3-begin-to-explore-the-watson-openscale-ui)

* [Quality monitor and Feedback logging](./QUALITY-FEEDBACK-README.md#3-begin-to-explore-the-watson-openscale-ui)

* [Drift monitor](./DRIFT.md#3-look-at-drift-in-the-dashboard)

## Conclusion

With the addition of historical data, we can now use the OpenScale tools in a simulated production environment. We can look at Fairness, Explainability, Quality, and Drift, and see how all transactions are logged. This workshop contains API code, configuration tools, and details around using the UI tool to enable a user to monitor production machine learning environments.

> **Important**: *Make sure that you stop the kernel of your notebook(s) when you are done, in order to conserve resources! You can do this by going to the Asset page of the project, selecting the three vertical dots under the Action column for the notebook you have been running (in this case the `openscale-historic-data`) and selecting to `Stop Kernel` from the Actions menu. If you see a lock icon on the notebook, click it to unlock the notebook before you click the Actions menu so you can see the stop kernel option.*
> ![Stop kernel](../.gitbook/assets/images/ml/stop-notebook-kernel.png)
