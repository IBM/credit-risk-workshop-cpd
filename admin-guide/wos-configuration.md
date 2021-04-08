# Admin Guide - Watson OpenScale Configuration

For the Watson OpenScale modules in the workshop, we need to run through the auto setup configuration that will deploy the sample model, configure openscale to monitor that sample model, and load some historical data.

> Note: Watson OpenScale now allows for provisioning multiple instances of the service. The steps below assume we will configure the default service instance (which is automatically provisioned after installation).

* In the Cloud Pak for Data instance, go the (☰) menu and under `Services` section, click on the `Instances` menu option.

  ![Service](../workshop/images/navigation/services.png)

* Find the `OpenScale-default` instance from the instances table and click the three vertical dots to open the action menu, then click on the `Open` option.

  ![Openscale Tile](../workshop/images/openscale/services-wos-instance.png)

* Since this is the first time we are launching OpenScale, you will be presented with a welcome message, where we can launch the auto setup process. Click on the *`Auto setup`* button.

  ![Openscale Auto Setup Launch](../workshop/images/openscale/openscale-autosetup-start.png)

* In the 'Connect to Watson Machine Learning' panel, leave the defaults since we are using the WML instance deployed in the same cluster. Click on the *`Next`* button.

  ![Openscale Auto Setup WML](../workshop/images/openscale/openscale-autosetup-wml.png)

* In the 'Connect to your database' panel, enter the connection details for your local DB2 database (this is the database you provisioned in a previous section of the admin guide). Click on the *`Next`* button.

  ![Openscale Auto Setup DB](../workshop/images/openscale/openscale-autosetup-db.png)

>*Note: If you used a DB2 Warehouse on Cloud, you will need to select the 'Use SSL' checkbox but dont need to provide a certificate.*

* The auto setup of a model will take some time to run.

  ![Openscale Auto Setup Running](../workshop/images/openscale/openscale-autosetup-running.png)

* Once it completes, you will see a message if it succeded.

  ![Openscale Auto Setup Completed](../workshop/images/openscale/openscale-autosetup-complete.png)

* Click through the insights dashboard for the deployed models to make sure the pages load.

__THIS SECTION IS COMPLETE, GO BACK AND CONTINUE WITH THE [ADMIN GUIDE](./README.md)__
