# Admin guide

> **NOTE**: This section requires `Admin` user access to the Cloud Pak for Data cluster. An administrator will present this part for the workshop.

## Virtualize Db2 data with Data Virtualization

For this section we'll now use the Data Virtualization tool to import the data from Db2 Warehouse, which is now exposed as a Connection in Cloud Pak for Data.

## Create an IBM Cloud instance of DB2 Warehouse

It is suggested to use [DB2 Warehouse on IBM Cloud](https://cloud.ibm.com/catalog/services/db2-warehouse) in order to conserve resources on the CPD cluster. IF you wish to use the local DB2 on the cluster, skip to the next section.

Provision an instance of DB2 Warehouse on the IBM Cloud.

Go to `Service Credentials` and click `New credential +`. Open `View credentials` and copy the credentials for use later:

![Get DB2 Warehouse credentials](../.gitbook/assets/images/dv/dv-get-cloud-db2-credentials.png)

Now go to `Manage` and click `Open Console`:

![DB2 Warehouse Cloud open console](../.gitbook/assets/images/dv/dv-manage-db2-warehouse-cloud.png)

From the upper-left (☰) hamburger menu click `Load` -> `Load data`:

![DB2 Warehouse Cloud load data](../.gitbook/assets/images/dv/dv-cloud-load-data.png)

Choose `Browse file` and navigate to where you cloned this repository, then to `data/split/` and choose `financial_data.csv`, then click `Next`.
Choose Schema `NULLIDRA` and click `+ New table`. Under "New Table Name" type "FINANCIAL" and click `Create`, then `Next`. Accept the defaults and click `Next`. Click `Begin Load`.
Repeat for the `personal_data_id.csv` file, naming the table `PERSONAL` and the `non_financial_data.csv` file, naming the table `NONFIN`.

### Get IBM Cloud DB2 SSL cert

You will need an SSL cert for Cloud Pak for Data to use the IBM Cloud DB2 Warehouse instance.

In the DB2 Warehouse console, from the upper-left (☰) hamburger menu click `Connection Info` -> `Connection Information`. Then click `Download SSL Certificate`:

![DB2 get SSL certificate](../.gitbook/assets/images/dv/dv-db2-cloud-get-ssl-cert.png)

You'll need to convert the SSL certificate from `.crt` to a `.pem` file using [openssl](https://www.openssl.org/). Run the following command:

```bash
openssl x509 -in DigiCertGlobalRootCA.crt -out DigiCertGlobalRootCA.pem -outform PEM -inform DER
```

## Load Data into Local DB2 Warehouse

These instructions are for loading the data into the local CP4D version of DB2 Warehouse. If you've used the IBM Cloud instance of DB2 Warehouse, you can skip to the next section.

You will need to already have done the `Provision instance` for DB2 Warehouse.
Got to `Services` and click on `DB2 Warehouse` and click `Open`:

![Open Service DB2 Warehouse](../.gitbook/assets/images/dv/dv-open-db2-warehouse.png)

Under `Menu` choose `Load` and `Load Data`:

![Menu Load Data](../.gitbook/assets/images/dv/dv-db2-load-data.png)

Choose `Browse file` and navigate to where you cloned this repository, then to `data/split/` and choose `financial_data.csv`, then click `Next`.
Choose Schema `NULLIDRA` and click `+ New table`. Under "New Table Name" type "FINANCIAL" and click `Create`, then `Next`. Accept the defaults and click `Next`. Click `Begin Load`.
Repeat for the `personal_data_id.csv` file, naming the table `PERSONAL` and the `non_financial_data.csv` file, naming the table `NONFIN`.

### Add DB Connections & Virtualization prep

For Cloud Pak for Data to read our Db2 Warehouse data we need to add a new *Data Source* to Cloud Pak for Data. This requires inputting the usual JDBC details.

#### Get IBM Cloud DB2 connection info

If you didn't already copy this when you provisioned the IBM Cloud DB2 instance above, go back and get the credentials as instructed.

#### Get local DB2 connection info

To get the connection info for you local DB2 Warehouse, go to the (☰) menu and click on the *My Instances* option.

![(☰) Menu -> My Instances](../.gitbook/assets/images/dv/dv-menu-my-instances.png)

In *My instances* go to the *Provisioned instances* tab. Highlight you local DB2 Warehouse and click the 3 vertical dots on the far right, and then click `View Details`:

![Provisioned local DB2 details](../.gitbook/assets/images/dv/dv-provisioned-db-view-details.png)

Either keep this window open in a separate tab, or copy the required Connection info: *Host*, *Port*, *Database name*, *Username*, and *Password*. You can get the port from the *JDBC Connection URL*, i.e for the URL `jdbc:db2://os-workshop-nov22worker-05.vz-cpd-nov22.com:30290/BLUDB` the port is the number after the colin in the URL `30290`:

![DB2 Connection credentials](../.gitbook/assets/images/dv/dv-local-db2-details.png)

#### Add DB2 as new data source

To add a new data source, go to the (☰) menu and click on the *Connections* option.

![(☰) Menu -> Collections](../.gitbook/assets/images/connections/conn-menu.png)

At the overview, click *Add connection*.

![Overview page](../.gitbook/assets/images/connections/conn-overview-empty.png)

Start by giving your new *Connection* a name and select *Db2 Warehouse on Cloud* as your connection type. More fields should apper. Fill the new fields with the same credentials for your own Db2 Warehouse connection from the previous section .

Click the check box for `Use SSL`. Next click `Select file` and navigate to where you converted the SSL certificate for DB2 Warehouse form a `.crt` file to a `.pem` file (probably called DigiCertGlobalRootCA.pem).

Click `Test Connection` and, after that succeeds, click `Add`.

![Add a Db2 Warehouse on Cloud connection](../.gitbook/assets/images/connections/conn-details.png)

The new connection will be listed in the overview.

![Connection has been added!](../.gitbook/assets/images/connections/conn-overview-db2.png)

## 2. Add a Data Source to Data Virtualization

To launch the data virtualization tool, go the (☰) menu and click `Collect` and then `Data Virtualization`.

![(☰) Menu -> Collect -> Data Virtualization](../.gitbook/assets/images/dv/dv-menu.png)

At the empty overview, click *Add* and choose *Add data source*.

![No data sources, yet](../.gitbook/assets/images/dv/dv-data-sources-empty.png)

Select the data source we made in the previous step, and click *Next*.

![Add the Db2 Warehouse connection](../.gitbook/assets/images/dv/dv-data-sources-add.png)

The new connection will be listed as a data source for data virtualization.

![Db2 Warehouse connection is now associated with Data Virtualization](../.gitbook/assets/images/dv/dv-data-sources-shown.png)

### Start virtualizing data

In this section, since we now have access to the Db2 Warehouse data, we can virtualize the data to our Cloud Pak for Data project. Click on the *Menu* button and choose *Virtualize*.

![Menu -> Virtualize](../.gitbook/assets/images/dv/dv-virtualize-menu.png)

Several tables will appear (many are created as sample data when a Db2 Warehouse instance is provisioned) in the table. Find the tables you created earlier, the instructions suggested naming them: `FINANCIAL`, `PERSONAL`, and `NONFIN`. Once selected click on *Add to cart* and then on *View Cart*.
You can search for the Schema `NULLIDRA` and they should show up:

![Choose the tables to virtualize](../.gitbook/assets/images/dv/dv-virtualize-tables.png)

The next panel prompts the user to choose which project to assign the data to, choose the project you created in the previous exercise. Click *Virtualize* to start the process.

![Add virtualized data to your project](../.gitbook/assets/images/dv/dv-virtualize-assign.png)

You'll be notified that the virtual tables have been created! Let's see the new virtualized data from the Data Virtualization tool by clicking *View my data*.

![We've got virtualized data](../.gitbook/assets/images/dv/dv-virtualize-complete.png)

### Join the virtualized data

Now we're going to **join** the tables we created so we have a merged set of data. It will be easier to do it here rather than in a notebook where we'd have to write code to handle three different data sets. Click on any two tables (`PERSONAL` and `FINANCIAL` for instance) and click the *Join view* button.

![Choose to join two tables](../.gitbook/assets/images/dv/dv-data-join-overview.png)

To join the tables we need to pick a key that is common to both data sets. Here we choose to map `customerID` from the first table to `customerID` on the second table. Do this by clicking on one and dragging it to another. When the line is drawn click on *Join*.

![Map the two customerID keys](../.gitbook/assets/images/dv/dv-data-join-columns.png)

In the next panel we'll give our joined data a name, I chose `FINANCIALPERSONAL`, then review the joined table to ensure all columns are present and only one `customerID` column exists. Click *Next* to continue.

![Review the proposed joined table](../.gitbook/assets/images/dv/dv-data-join-review.png)

Next we choose which project to assign the joined view to, choose the project you created in the previous exercise. Click *Create view* to start the process.

![Add joined data tables to your project](../.gitbook/assets/images/dv/dv-data-join-assign.png)

You'll be notified that the join has succeeded! Click on *View my data*. to repeat this again so we have all three tables.

![The data join succeeded!](../.gitbook/assets/images/dv/dv-data-join-created.png)

**IMPORTANT** Repeat the same steps as above, but this time choose to join the new joined view (`FINANCIALPERSONAL`) and the last virtualized table (`NONFIN`), to create a new joined view that has all three tables, let's call it `FINANCIALPERSONALNONFIN`. Switching to our project should show all three virtualized tables, and two joined tables. Do not go to the next section until this step is performed.

![Our data sets at the end of this section](../.gitbook/assets/images/dv/dv-project-data-all.png)

### Assign the "Steward" role to the attendees

Go to *Data Virtualization* option from the menu. Click on *User management*

![Manage users in Data Virtualization](../.gitbook/assets/images/dv/dv-manage-users.png)

Click on *Add user* and ensure all users have the *Steward* role.

![Manage users in Data Virtualization](../.gitbook/assets/images/dv/dv-steward-role.png)

## Adding users to the cluster

From the hamburger menu, click manage users, then add user!

![Add a user](../.gitbook/assets/images/manage/manage-add-users.png)
