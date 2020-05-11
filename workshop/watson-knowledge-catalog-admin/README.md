# Watson Knowledge Catalog for Admins

This exercise demonstrates how to solve the problems of enterprise data governance using Watson Knowledge Catalog on the Cloud Pak for Data platform. We'll explain how to use governance, data quality and active policy management in order to help your organization protect and govern sensitive data, trace data lineage and manage data lakes. This knowledge will help users quickly discover, curate, categorize and share data assets, data sets, analytical models and their relationships with other members of your organization. It serves as a single source of truth for data engineers, data stewards, data scientists and business analysts to gain self-service access to data they can trust.

You will need the *Admin* role to create a catalog.

This section is comprised of the following steps:

1. [Set up Catalog and Data](#1-set-up-catalog-and-data)
1. [Add collaborators and control access](#2-add-collaborators-and-control-access)
1. [Add categories](#3-add-categories)
1. [Add data classes](#4-add-data-classes)
1. [Add Business terms](#5-add-business-terms)
1. [Add rules for policies](#6-add-rules-for-policies)

## 1. Set up Catalog and Data

> NOTE: The default catalog is your enterprise catalog. It is created automatically after you install the Watson Knowledge Catalog service and is the only catalog to which advanced data curation tools apply. The default catalog is governed so that data protection rules are enforced. The information assets view shows additional properties of the assets in the default catalog to aid curation. Any subsequent catalogs that you create can be governed or ungoverned, do not have an information assets view, and supply basic data curation tools.

First we'll create a catalog and load some data

### Create the catalog

#### Provision Watson Knowledge Catalog the First Time

If you haven't yet started Watson Knowledge Catalog, you'll need to provision it.

* Open Watson Knowledge Catalog by clicking the *Services* icon at the top right of the home page:

![click services icon](../.gitbook/assets/images/wkc-admin/wkc-click-services-icon.png)

* Under the *Data Governance* section, click the 3 horizontal dots on the *Watson Knowledge Catalog* tile, and click `Open`:

![open wkc](../.gitbook/assets/images/wkc-admin/wkc-open-service.png)

#### Open Watson Knowledge Catalog

* Go to the upper-left (☰) hamburger menu and choose `Organize` -> `All catalogs`:

![open catalog menu](../.gitbook/assets/images/wkc-admin/wkc-admin-open-catalog-menu.png)

* From the *Your catalogs* page, click either `Create catalog` or `New Catalog`:

![create WKC catalog](../.gitbook/assets/images/wkc-admin/wkc-create-catalog.png)

* Give your catalog a name and optional description, and click `create`:

![name and create wkc catalog](../.gitbook/assets/images/wkc-admin/wkc-admin-name-create-catalog.png)

### Add data assets

* Under the *Browse Assets* tab, below "Now you can add assets!" click `here` to add your data:

![click here to add assets](../.gitbook/assets/images/wkc-admin/wkc-add-data-asset.png)

*OR* you can click `+ Add to catalog` in the top right and, for example, choose `Local files`:

![add local files to catalog](../.gitbook/assets/images/wkc-admin/wkc-add-to-catalog-local-files.png)

* Browse to the `/data/split/applicant_personal_data.csv` file and double-click or click `Open`. Add an optional description and click `Add`:

![click add for local files to catalog](../.gitbook/assets/images/wkc-admin/wkc-admin-file-selected-now-add.png)

>NOTE: Stay in the catalog until loading is complete! If you leave the catalog, the incomplete asset will be deleted.

* The newly added *wkc-admin-file-selected-now-add.png* file will show up under the *Browse Assets* tab of your catalog:

![newly added data in catalog](../.gitbook/assets/images/wkc-admin/wkc-admin-browse-assets.png)

### Add Connection

* You can add a connection to a remote DB, for example *DB2 Warehouse in IBM Cloud*, by choosing `+ Add to catalog` -> `Connection`:

![add connection to catalog](../.gitbook/assets/images/wkc-admin/wkc-add-connection.png)

* Choose your remote DB and click:

![chose db2 warehouse connection ](../.gitbook/assets/images/wkc-admin/wkc-choose-db2-warehouse-conn.png)

* Enter the connection details and click `Create`:

![enter db2 warehouse connection details](../.gitbook/assets/images/wkc-admin/wkc-enter-connection-details.png)

* The connection now shows up in the catalog:

![db2 warehouse connection shows up](../.gitbook/assets/images/wkc-admin/wkc-new-connection-shows-up.png)

### Add Virtualized Data

Virtualized data can be added to the *Default* catalog by someone with Administrator or Editor access to that catalog.

* Go to the upper-left (☰) hamburger menu and choose `Organize` -> `All catalogs`. Click `+Add to Catalog` -> `Connected asset`:

![add connected asset](../.gitbook/assets/images/wkc-admin/wkc-add-connected-asset.png)

* Click *Source* -> `Select source`. Browse under `DV` to you Schema (i.e. UserXYZW) and choose the joined table. Click `Select`.

A user can now add this to a project like any other asset from a catalog.

## 2. Add collaborators and control access

* Under the *Access Control* tab you can click `Add Collaborator` to give other users access to your catalog:

![give users access to the catalog](../.gitbook/assets/images/wkc-admin/wkc-admin-access-control-add-collaborator.png)

* You can search for a user, click on the name to select them, and click `Add`:

![search for user and add as collaborator](../.gitbook/assets/images/wkc-admin/wkc-admin-choose-user-and-add.png)

* You can choose a role for the user - Admin, Editor, or Viewer:

![choose role for collaborator](../.gitbook/assets/images/wkc-admin/wkc-admin-user-roll-choice.png)

* To access data in the catalog, click on the name of the data:

![click data name to open](../.gitbook/assets/images/wkc-admin/wkc-admin-click-data-name-to-open.png)

* A preview of the data will open, with metadata and the first few rows:

![preview of data](../.gitbook/assets/images/wkc-admin/wkc-admin-data-preview.png)

* You can click the `Review` tab and rate the data, as well as comment on it, to provide feedback for your teammates:

![review data](../.gitbook/assets/images/wkc-admin/wkc-admin-review-data.png)

## 3. Add categories

The fundamental abstraction in Watson Knowledge Catalog is the Category. A category is analogous to a folder.
You can add categories as needed, or you can import them in .csv format.

### Import categories

* Import a category for your assets by going to the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Categories`, then click `Import`:

![Import categories](../.gitbook/assets/images/wkc-admin/wkc-import-categories.png)

* Click `Add file` and navigate to where you cloned the workshop repository, choosing `data/wkc/glossary-organize-categories.csv`.

* Under `Select merge option` choose `Replace all values` and click `Import`:

![Import select merge option](../.gitbook/assets/images/wkc-admin/wkc-import-select-merge-option.png)

You will see "The import completed succesfully" when it is completed.

In this way, you can import Categories, Business Terms, Classifications, Policies, etc. to populate your governance catalogs.

### Add category manually

* Add a category for your assets by going to the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Categories`, then click `Create category`:

![organize data categories](../.gitbook/assets/images/wkc-admin/wkc-menu-organize-categories.png)

* Give your category a name, such as *Personal Data*, and an optional description, and then click `Save`:

![new category billing](../.gitbook/assets/images/wkc-admin/wkc-admin-new-category-personal-data.png)

* Now, if you hit `Create category` again on the *Personal Data* category screen, you can create a sub-category, such as *Residence Information*:

![sub category residence information](../.gitbook/assets/images/wkc-admin/wkc-admin-new-subcategory-residence-information.png)

* For the *Personal Data* category you can select a *Type*, such as `Business term`:

![select business term type](../.gitbook/assets/images/wkc-admin/wkc-admin-category-select-type.png)

* We can also create classifications for assets, similar to *Confidential*, *Personally Identifiable Information*, or *Sensitive Personal Information* in a similar way, by going to the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Classifications` and clicking `+Create classification`. These classifications can then be added to your category as a *Type*:

![select classification type](../.gitbook/assets/images/wkc-admin/wkc-add-classifications.png)

## 4. Add data classes

When you profile your assets, a data class will be inferred from the contents where possible. We'll see more on this later. You can also add your own data classes.

* Add a data class for your assets by going to the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Data class`, then click `Create data class`:

![organize data classes](../.gitbook/assets/images/wkc-admin/wkc-menu-organize-data-classes.png)

* Give your new data class a name, i.e. *numerical*, and an optional Primary category and/or description, and click `Save as draft`:

![new data class](../.gitbook/assets/images/wkc-admin/wkc-create-data-class.png)

* Once the data class is created, we can add *Stewards* for this class, and also associate *classifications* and *business terms*. When you are ready, click `Publish`:

![tools for data class](../.gitbook/assets/images/wkc-admin/wkc-data-class-add-term-publish.png)

Now let's add that data class to a column in our *applicant_personal_data.csv* asset.

* Go back to your *CreditDataCatalog* and open it up to the column view ((☰) hamburger menu `Organize` -> `All catalogs` and choose `CreditDataCatalog`). Under the *Browse assets* tab, click on the data set *applicant_personal_data.csv* to get the column/row preview. Scroll right to get to the *CustomerID* column and click the down arrow next to "Customer Number" and then *View all*:

![change data class](../.gitbook/assets/images/wkc-admin/wkc-admin-existing-data-class.png)

* In the window that opens, search for your newly created data class, *Numerical* and click it when it returns in the search. Then click *Select*:

![Set colunn to numerical data class](../.gitbook/assets/images/wkc-admin/wkc-admin-numeric-data-class.png)

## 5. Add Business terms

You can use [Business terms](https://dataplatform.cloud.ibm.com/docs/content/wsj/governance/dmg16.html) to standardize definitions of business concepts so that your data is described in a uniform and easily understood way across your enterprise.

You already saw how to create a category and make it a *business term*. You can also create the business term as it's own entity.

* From the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Business terms`:

![organize Data Business terms](../.gitbook/assets/images/wkc-admin/wkc-admin-organize-data-business-terms.png

* Click on the upper-right `+ Create Business term` button:

![create business term](../.gitbook/assets/images/wkc-admin/wkc-create-business-term.png)

* Give the new Business term a name such as *Contact Information* and optional description, and click `Save as draft`. NOTE that others on the platform will be creating a business term for this workshop, so perhaps pre-pend your term with something unique, i.e *scottda-ContactInfo*:

![name new business term](../.gitbook/assets/images/wkc-admin/wkc-admin-name-business-term.png)

* A window will come up once the term is created. You can see a rich set of options for creating related terms and adding other metadata. For now, click `Publish` to make this term available to users of the platform:

![publish business term](../.gitbook/assets/images/wkc-admin/wkc-admin-publish-business-term.png)

* Add an optional comment and click `Publish` in the new window:

![verify publish business term](../.gitbook/assets/images/wkc-admin/wkc-admin-click-publish.png)

* Now go back to your *CreditDataCatalog* by opening it up to the column view ((☰) hamburger menu `Organize` -> `All catalogs` and choose `CreditDataCatalog`). Under the *Browse assets* tab, click on the data set *applicant_personal_data.csv* to get the column/row preview. Scroll right to get to the *email* column and click the *Column information* icon (looks like an "eye"):

![choose email columnn information](../.gitbook/assets/images/wkc-admin/wkc-admin-email-column-information.png)

* In the window that opens, click the *edit* icon (looks like a "pencil") next to *Business terms* :

![edit business terms](../.gitbook/assets/images/wkc-admin/wkc-admin-assign-terms-to-column.png)

* Enter *Contact Information* (or your uniquely named term such as *scottda-ContactInfo*) under *Business terms* and the term will be searched for. Click on the `Contact Information`` term that is found, and click `Apply`:

![search business terms](../.gitbook/assets/images/wkc-admin/wkc-admin-search-contact-to-assign-term.png)

Close that window once the term has been applied.
Now, do the same thing to add the *Contact Information* Business term to the *Telephone* column.

* You will now be able to search for these terms from within the platform. For example, going back to your top level *CreditDataCatalog*, in the search bar with the comment "What assets are you searching for?" enter your unique *<unique_string>Contact Information* term:

![search using business terms](../.gitbook/assets/images/wkc-admin/wkc-admin-search-business-terms.png)

The *applicant_personal_data.csv* data set will show up, since it contains columns tagged with the *Contact Infomation* business term.

## 6. Add rules for policies

We can now create rules to control how a user can access data.

* Create a business term called *CustomerID* and assign it to your *CustomerID* column in the data set using the instructions above. See below if you need details, but try it yourself first, and skip to *Adding a rule* below if you do not need a reminder.

### How to create a Business term review

* From the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Business terms`.

* Click on the upper-right `+ Create Business term` button.

* Give the new Business term the name *CustomerID* and optional description, and click `Save as draft`. In the next window, click `Publish`.

* Now go back to your *CreditDataCatalog* by opening it up to the column view ((☰) hamburger menu `Organize` -> `All catalogs` and choose `CreditDataCatalog`). Under the *Browse assets* tab, click on the data set *applicant_personal_data.csv* to get the column/row preview. Scroll right to get to the *CustomerID* column and click the *Column information* icon (looks like an "eye").

* In the window that opens, click the *edit* icon (looks like a "pencil") next to *Business terms* .

* Enter *CustomerID* under *Business terms* and the term will be searched for. Click on the `CustumerID` term that is found, and click `Apply`.

### Adding a rule

* From the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Rules`, then click `Create rule`.

* For the *New rule* -> *Select the type of rule to create* choose `Data protection rule`.

* Under *Details* give your rule a *Name*, *Type* = *Access*, and a *Business definition*.

* Next, under *Rule builder* *Condition1* fill out If *Business term* *Contains any* *CustomerID*  and Action then *mask data* *in columns containing* *Numerical*. Choose the tile for `Substitute`, which will make a non-identifiable hash. This obscures the actual CustomerID, but allows actions like database joins to still work. Click `Create`:

![define rule for masking customerID](../.gitbook/assets/images/wkc-admin/wkc-rule-substitute-customer-id.png)

* Now if we go back to our *applicant_personal_data.csv* asset in the catalog at the *CustomerID* column, it will look the same as before. But a non-admin user will see the "lock" icon and see that the customerID has now been substituted with a hash value:

![customerID is now masked](../.gitbook/assets/images/wkc-admin/wkc-admin-masked-column-customerid.png)

* To add a rule to *Obfuscate* data, create a new data class called *Age*. See the instructions above if needed.

* Back in the *CreditDataCatalog*, under the *applicant_personal_data.csv* asset, go to the `Overview` tab and scroll to the *Age* column. Click the "down arrow" and you can see that the data has been inferred to be classified as a *Code*:

![Age classified as Code](../.gitbook/assets/images/wkc-admin/wkc-admin-inferred-classifier-code.png)

* Change the classifier by clicking `View all`.

* Now change the classifier by starting to type *Age*. When this comes up in the search, click `Use` and then `Close`:

![Change classifier and use](../.gitbook/assets/images/wkc-admin/wkc-admin-change-classifier-select.png)

* You can build a rule to *Obfuscate* this *Age* column:

![Age obfuscate rule ](../.gitbook/assets/images/wkc-admin/wkc-admin-create-obfuscate-rule.png)

* And now when that column is viewed by a non-admin user, it will have data that is replaced with similarly formatted data:

![Age column obfuscated](../.gitbook/assets/images/wkc-admin/wkc-admin-age-column-obfuscated.png)

## Wrap up

In this lab, we learned how to:

* Set up Catalog and Data
* Add collaborators and control access
* Add categories
* Add data classes
* Add Business terms
* Add rules for policies
