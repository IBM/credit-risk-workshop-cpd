# Pre-work

Before we get started, we will download some assets and complete some setup for our workshop. This section is broken up into the following steps:

1. [Download or Clone the Repository](#1-download-or-clone-the-repository)
1. [Create an Analytics Project and Deployment Space](#2-create-a-project-and-deployment-space)

## 1. Download or Clone the Repository

Various parts of this workshop will require the attendee to upload files or run scripts that we've stored in the repository. So let's get that done early on, you'll need [`git`](https://git-scm.com) on your laptop to clone the repository directly, or access to [GitHub.com](https://github.com/) to download the zip file.

* To Download, go to the [GitHub repo for this workshop](https://github.com/IBM/credit-risk-workshop-cpd) and download the archived version of the workshop and extract it on your laptop.

![download workshop zip](../.gitbook/assets/images/prework/github-zip-download.png)

* Alternately, run the following command:

```bash
git clone https://github.com/IBM/credit-risk-workshop-cpd.git
cd credit-risk-workshop-cpd
```

## 2. Create a Project and Deployment Space

At this point of the workshop we will be using Cloud Pak for Data for the remaining steps.

### Log into Cloud Pak for Data

* Launch a browser and navigate to your Cloud Pak for Data deployment

> **NOTE:** Your instructor will provide a URL and credentials to log into Cloud Pak for Data!

![Cloud Pak for Data login](../.gitbook/assets/images/navigation/cpd-login.png)

### Create a New project

In Cloud Pak for Data, we use the concept of a project to collect / organize the resources used to achieve a particular goal (resources to build a solution to a problem). Your project resources can include data, collaborators, and analytic assets like notebooks and models, etc.

* Go the (☰) menu and click *Projects*

![(☰) Menu -> Projects](../.gitbook/assets/images/navigation/menu-projects.png)

* Click on *New project*

![Start a new project](../.gitbook/assets/images/prework/project-new.png)

* We are going to create a project from an existing file (which contains assets we will use throughout this workshop), as opposed to creating an empty project. Select the _*Create a project from a sample or file*_ option:

![Create project from file](../.gitbook/assets/images/prework/create-project-from-sample.png)

* Navigate to where you cloned this repository, then to `projects/` and choose `CreditRisk-Project.zip`. Give the project a name and click the `Create` button:

![Browse for project files](../.gitbook/assets/images/prework/create-project-name.png)

### Create a Deployment Space

Cloud Pak for Data uses the concept of `Deployment Spaces` to configure and manage the deployment of a set of related deployable assets. These assets can be data files, machine learning models, etc.

* Go the (☰) menu and click `Analyze` -> `Analytics deployments`:

![(☰) Menu -> Analytics deployments](../.gitbook/assets/images/navigation/menu-analytics-deployments.png)

* Click on `+ New deployment space`:

![Add New deployment space](../.gitbook/assets/images/prework/deployment-space-new.png)

* Give your deployment space a unique name, optional description, then click the `Create` button. You will use this space later when you deploy a machine learning model.

* Next, we will add a collaborator to the new deployment space, so that assets we deploy can be monitored in the OpenScale model monitoring lab.

* Click on your new deployment space.

![Select deployment space](../.gitbook/assets/images/prework/deployment-space-select.png)

* Click on the `Access control` tab and then click on `Add collaborators` on the right.

![Deployment space access control](../.gitbook/assets/images/prework/deployment-space-access-control.png)

* Enter "admin" as a Collaborator and select the user from the drop down list. Then click on the `Add to list` button.

> **NOTE:** We are adding the user that configured the machine learning instance for OpenScale monitoring. In this case, the user is the admin user.

![Deployment space collaborators](../.gitbook/assets/images/prework/deployment-space-add-collaborator.png)

* Click the `Add` button to finish adding the collaborator. You should be brought back to the deployment space page and see your user ID along with the `Admin` user as collaborators for this space.
