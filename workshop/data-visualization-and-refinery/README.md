# Data Visualization and Data Refinery

Let's take a quick detour to the *Data Refinery* tool. Data Refinery can quickly filter and mutate data, create quick 
visualizations, and do other data cleansing tasks from an easy-to-use user interface.

>*Note: The lab instructions below assume you have a project already and have data you will refine. If not, follow the instructions in the pre-work and import data to project sections to create a project and assign data to your project.*

## 1. Load Data

* Go the (☰) navigation menu and under the *Projects* section click on *`All Projects`*.

![(☰) Menu -> Projects](../images/navigation/menu-projects.png)

* Click the project name you created in the pre-work section to open it.

![Project select](../images/general/project-select.png)

* From the `Project` home, under the `Assets` tab, ensure the `Data assets` section is expanded or click on the arrow to toggle it and open up the list of data assets.

* Click the merged data asset  *`XXXAPPLICANTFINANCIALPERSONALLOANDATA`* (the name of the file may vary, `XXX` may be your initials or the initials of the person who granted you data access) to open it. If this is the first time you are opening the data asset, you will be asked to unlock the connection. Select 'Username/password' from the dropdown, click the `Use your Cloud Pak for Data credentials to authenticate to the data source` checkbox and then click the *`Connect`* button.

* Once the preview of the data asset opens, click on the *`Prepare data`* button on the top right of the table.

![Launch the action button](../images/dr/dr-launch-button.png)

* Data Refinery will launch and open to the `Data` tab. It will also display the information panel with details of the data refinery flow and where the output of the flow will be placed. Click the `X` to the right of the `About this asset` panel to close it.

![Data Refinery view](../images/dr/dr-open-table.png)

## 2. Refine Data

We'll start out in the `Data` tab where we wrangle, shape and refine our data. As you refine your data, IBM Data Refinery keeps track of the steps in your data flow. You can modify them and even select a step to return to a particular moment in your data’s transformation.

### Create Transformation Flow

* With Data Refinery, we can transform our data by directly entering operations in [R syntax](https://cran.r-project.org/manuals.html) or interactively by selecting operations from the menu. For example, start typing `filter` on the Command line and observe that the list of operations displayed will get updated. Click on the filter operation.

![Command line filter](../images/dr/dr-cli-filter.png)

* A `filter` operation syntax will be displayed in the Command line. Clicking on each element of the operation will give hints on the syntax and how to use the command. For instance, to filter for customers who have paid credits up to date, build the expression shown below. To enact the filter, you would `Apply` the expression.

```R
filter(`CreditHistory` == 'credits_paid_to_date')
```

* We can remove this custom filter by clicking on 'Delete' from the drop-down menu on the `Custom code` step of our data workflow.

![Clear custom filter](../images/dr/dr-clearcustomfilter.png)

* We can remove records with empty values in a particular column. Scroll over to the `StreetAddress` column, click on the three dots to open the action menu, and select `Remove empty rows`. You will see an entry added to the `Steps` view.

![Remove empty rows](../images/dr/dr-remove-empty-rows.png)

* Let's say we've decided that there are columns that we don't want to leave in our dataset ( maybe because they might not be useful features in our Machine Learning model or because we don't want to make those data attributes accessible to others). We'll remove the `FirstName`, `LastName`, `Email`, `StreetAddress`, `City`, `State`, `PostalCode` columns.

* For each column to be removed: Click the `New step` button at the bottom of the page. Find the column in the table, click on the three dots to see the action menu, then select `Remove column`.

![New step](../images/dr/dr-new-step.png)

![Search operations](../images/dr/dr-search-operations.png)

![Select column](../images/dr/dr-select-column.png)

* At this point, you have a data transformation flow with 8 steps. As we saw in the last section, we keep track of each of the steps and we can even undo (or redo) an action using the circular arrows. To see the steps in the data flow that you have performed, click the `Steps` button. The operations that you have performed on the data will be shown.

![Flow](../images/dr/dr-final-flow.png)

### Schedule Jobs

Data Refinery allows you to run jobs at scheduled times, and save the output. In this way, you can regularly refine new data as it is updated.

* Click on the "jobs" icon and then `Save and create job` option from the menu.

![Click jobs icon](../images/dr/dr-save-and-create-job.png)

* Give the job a name and optional description, then click the *`Next`* button.

![jobs name](../images/dr/dr-savejob-name.png)

* The job will configure a default input and output data asset, as well as the runtime environment. Click the *`Next`* button.

![jobs name](../images/dr/dr-savejob-environment.png)

* We can set the job to run on a schedule. For now, leave the schedule off and click the *`Next`* button.

![jobs name](../images/dr/dr-savejob-schedule.png)

* We can get notifications from job runs. For now, skip the notification configuration and click the *`Next`* button.

![jobs name](../images/dr/dr-savejob-notify.png)

* Click the *`Create and Run`* button to save and run this job.

![Create and Run Refinery job](../images/dr/dr-create-and-run-job.png)

* This refinery flow will be saved to your project in the `Data Refinery flows` section of the project overview page. From that section you could revisit the flow to edit the steps or even see any execution jobs you have run. For now, we will move on to exploring our data.

## 3. Profile Data

* Back on the top level of the data refinery view, click on the `Profile` tab to bring up a view of several statistics and histograms for the attributes in your data.

![Data Refinery Profile tab](../images/dr/dr-profile.png)

* Once the data profile loads, you can get insight into the data from the views and statistics:

  * The median age of the applicants is 36, with the bulk under 49.

  * About as many people had credits_paid_to_date as prior_payments_delayed. Few had no_credits.

  * The median was 3 years for duration at current residence. Range was 1-6 years.

## 4. Visualize Data

Let's do some visual exploration of our data using charts and graphs. Note that this is an exploratory phase and we're looking for insights in out data. We can accomplish this in Data Refinery interactively without coding.

* Choose the `Visualizations` tab to bring up the page where you can select columns that you want to visualize. Select `LoanAmount` from the "Columns to visualize" drop down list as the first column and click `Add another column` to add another column. Next add `LoanDuration` and click the *`Visualize data`* button. The system will pick a suggested plot for you based on your data and show more suggested plot types at the top.

![Select columns](../images/dr/dr-vis-choose-column-loan.png)

* Remember that we are most interested in knowing how these features impact a loan being at the risk. So, let's add the `Risk` as a color on top of our current scatter plot. That should help us visually see if there's something of interest here. From the left panel, click the `Color Map` drop down and select `Risk`. Also, to see the full data, drag the right side of the data selector at the bottom all the way to the right, in order to show all the data inside your plot.

![Amount v Duration Scatter](../images/dr/dr-vis-loan-amountduration-scatter.png)

* We notice that there are more blue (risk) on this plot towards the top right, than there is on the bottom left. This is a good start as it shows that there is probably a relationship between the riskiness of a loan and its duration and amount. It appears that the higher the amount and duration, the riskier the loan. Interesting, let's dig in further in how the loan duration could play into the riskiness of a loan.

> *Note: The colors used in your visualization may be different. Be sure to look at chart legend for clarification*

* Let's plot a histogram of the `LoanDuration` to see if we can notice anything. First, select `Histogram` from the `Chart Type`.

* On the left, select `LoanDuration` for the 'X-axis', select `Risk` in the 'Split By' section, check the `Stacked` option, uncheck the `Show kde curve` toggle, uncheck the `Show distribution curve` toggle. You should see a chart that looks like the following image.

![Visualize loan duration](../images/dr/dr-vis-loanduration-hist.png)

* It looks like the longer the duration the larger the blue bar (risky loan count) become and the smaller the dark blue bars (non risky loan count) become. That indicate loans with longer duration are in general more likely to be risky. However, we need more information.

* We next explore if there is some insight in terms of the riskiness of a loan based on its duration when broken down by the loan purpose. To do so, let's create a Heat Map plot.

* At the top of the page, in the `Chart Type` section, open the arrows on the right, select `Heat Map`.

![Switch to heat map](../images/dr/dr-vis-switch-heatmap.png)

* Next, select `Risk` in the column section and `LoanPurpose` for the `Row` section. Additionally, to see the effects of the loan duration, select `Mean` in the summary section, and select `LoanDuration` in the `Value` section.

![Loan purpose heat map](../images/dr/dr-vis-loanpurpose-heatmap.png)

* You can now see that the least risky loans are those taken out for purchasing a new car and they are on average 10 years long. To the left of that cell we see that loans taken out for the same purpose that average around 15 years for term length seem to be more risky. So one could conclude the longer the loan term is, the more likely it will be risky. In contrast, we can see that both risky and non-risky loans for the other category seem to have the same average term length, so one could conclude that there's little, if any, relationship between loan length and its riskiness for the loans of type other.

* In general, for each row, the bigger the color difference between the right and left column, the more likely that loan duration plays a role for the riskiness of the loan category.

* Now let's look into customizing our plot. Under the Actions panel, notice that you can perform tasks such as `Start over`, `Download chart details`, `Download chart image`, or set `Global visualization preferences` *(Note: Hover over the icons to see the names)*. Click on the drop down arrow next to `Action`. Then click on the `Global visualization preferences` option from the menu.

![Visualize theme preferences](../images/dr/dr-vis-actions-menu.png)

* We see that we can do things in the `Global visualization preferences` for `Titles`, `Tools`, `Theme`, and `Notifications`. Click on the `Theme` tab and update the color scheme to `Dark`. Then click the `Apply` button, now the colors for all of our charts will reflect this. Play around with various Themes and find one that you like.

![Visualize set theme and choose preferences](../images/dr/dr-vis-choose-theme.png)

## Conclusion

We've seen a some of the capabilities of the Data Refinery. We saw how we can transform data using R code, as well as using various operations on the columns such as changing the data type, removing empty rows, or deleting the column altogether. We next saw that all the steps in our Data Flow are recorded, so we can remove steps, repeat them, or edit an individual step. We were able to quickly profile the data, to see histograms and statistics for each column. And finally we created more in-depth Visualizations, creating a scatter plot, histogram, and heatmap to explore the relationship between the riskiness of a loan and its duration, and purpose.
