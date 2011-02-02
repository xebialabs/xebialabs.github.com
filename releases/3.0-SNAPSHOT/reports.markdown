% Deployit GUI - Reports Screen Help
%
% January, 2011

# The Reports Screen #

This screen is used report on data in the Deployit repository. The following shows an example of the Reports Screen:

![Reports screen](images/reports-screen-overview.png "The Reports Screen")

The screen consists of the following components:

* **Reports Browser**. This component is used to select a particular report type to display.
* **Report Window**. This window is used to show generated reports.

## The Reports Browser ##

The reports browser shows all available report types. Deployit supports two report types:

* **Deployed Applications per Environment**. Shows all deployed applications that were deployed in a certain environment at a particular date.
* **Deployments per Data Range**. Shows all deployments performed with Deployit in a particular data range.

Click on a report type to create a report of the specified type.

The reports types will be described in more detail below.

## The Report Window ##

This window displays tabs per report type and allows generating of a particular report.

### Deployed Applications per Environment Report ###

This report shows all deployed applications that were deployed in a certain environment at a particular date. The following is an example of such a report:

![Deployed Applications per Environment Report](images/reports-deployed-applications.png "Deployed Applications per Environment Report")

The report shows the following columns:

* **Application**. The application on the environment.
* **Version**. The version of the application. 
* **User**. The user that performed the deployment.
* **Date of Deployment**. The date on which this version of the application was deployed.

### Deployments per Date Range Report ###

This report shows all deployments that were performed with Deployit. The following is an example of such a report:

![Deployments per Date Range Report](images/reports-deployments.png "Deployments per Date Range Report")

The report shows the following columns:

* **Package**. The package and version that was deployed.
* **Environment**. The environment to which it was deployed.
* **User**. The user that performed the deployment.
* **Status**. The status of the deployment. 
* **Start Date**. The date on which the deployment was started.
* **Completion Date**. The date on which the deployment was completed.
* **Deployment Type**. The type of the deployment (*Initial*, *Upgrade* or *Undeployment*).
