# Frequently Asked Questions 

## What do I do if importing the project into the platform takes a long time?

If you are facing any issues with importing the project into the IBM Cloud Pak for Data as a Service platform, all you need to do is import the relevant notebooks and/or data assets for each lab.

### Accessing Files

If you ran the following commands to download the project, navigate to `projects` then unzip the folder named `CreditRiskProject.zip` to access the content you need for each lab. All files you need are in the `assests` folder.

```bash
   git clone https://github.com/IBM/credit-risk-workshop-cpd.git
   cd credit-risk-workshop-cpd
   ```
If you downloaded the zip folder from the link provided in the Pre-work section, make sure you extract the zip folder after it's downloaded. After that, navigate to `projects` then unzip the folder named `CreditRiskProject.zip`. All files you need are in the `assests` folder. 
### Importing Files into the Cloud Pak for Data as a Service platform

You will need to create a new empty project to import the files you'll use into.

* Go the (☰) navigation menu, expand *Projects* and click on the `View all projects` link.

![(☰) Menu -> Projects](../.gitbook/assets/images/navigation/menu-projects.png)

* Click on the `New +` button on the top.

![Start a new project](../.gitbook/assets/images/prework/new-project.png)

* We are going to create an empty project. Select the `Create an empty project` option.

![Create project from file](../.gitbook/assets/images/faq/new-empty-project.png)

* Give the project a name. You also need to provide an object storage instance for this project. If you haven't already created a Cloud Object Storage instance in your IBM Cloud account, you can create one now by clicking `Add`.

![Project name](../.gitbook/assets/images/faq/project-name.png)

* A new tab opens up, where you can create the Cloud Object Service. By default, a `Lite` (Free) plan will be selected. Scroll down and update the name of your Cloud Object Storage service if you wish, and click `Create`.

![Create COS instance](../.gitbook/assets/images/prework/create-cos-instance.png)

* The browser tab will automatically close when the Cloud Object Storage instance has been created. Back on IBM Cloud Pak for Data as a Service, click `Refresh`.

![Refresh COS](../.gitbook/assets/images/faq/refresh-cos.png)

* The newly created Cloud Object Storage instance will now be displayed under "Storage". Click `Create` to finish creating the project.

![Create project](../.gitbook/assets/images/faq/create-project.png)

* To import the notebook you need for a lab, 
