----
layout: default
title: Deployit Graphical User Interface 
----

# Preface #

This manual describes how to use the Deployit GUI. The GUI is used to import packages, perform deployments, view and edit the repository and run reports. The GUI provides a subset of the functionality of the CLI. Specifically, the following functions can only be performed from the CLI:

* discovering middleware
* configuring security

The Deployit server must be running before accessing the GUI. See the **Deployit System Administrator Manual** for more information.

See **Deployit Reference Manual** for background information on Deployit and deployment concepts.

# Starting and Stopping #

To start the GUI, start a browser[^1] and enter the URL of the Deployit server (for example, `http://deployit:4516`).

[^1]: IE 7.0 or up, Firefox 3.0 or up, Safari 3.0 or up

# Logging in and Logging out #

When you open the GUI, the browser will show a popup window to prompt you for a username and password. Enter your Deployit username and password to log in.

To log out of the GUI, simply close the browser tab or window.

# Help #

To access help information while using the GUI, click on the help icon in the top-right of the window. The GUI contains help for each of the major screens (Deployment, Repository and Reports).

# Generic GUI Components #

## Tree Component ##

The tree component is a component that is used often in the GUI. It shows a hierarchical view of the Deployit data. Nodes can be expanded or collapsed.

To facilitate installations with large amounts of data, the tree component lazily loads it's data. That is, when the scrollbar is pulled down to the bottom, the GUI queries the server for more data. This prevents the GUI from loading all data at once.

Searching the data in the tree is also possible using the search field in the top of the tree component. Note that searching always happens on the top-level nodes in the tree. If you want to search on a lower level, first narrow the scope of the tree by double-clicking the node in the tree so that the sub-nodes become top-level nodes. The tree component includes a breadcrumb that shows all levels of the hierarchy and allows quick access to previous levels.

## Tabs ##

The editor windows in the GUI use tabs to allow the user to perform multiple tasks in parallel. The tabs will be opened in response to user actions in other parts of the GUI. Tabs can also be closed.

# Importing Packages #

Deployit maintains a repository of data about the packages, environments and deployments it works with. The repository stores this data and all it's revisions.

The first step to performing a deployment with Deployit is to import your package into the application's repository. These are the steps you need to follow:

1. **Start the Import Wizard**. To start the Import Wizard, click the Import button on the Package Browser:

![Start Import Button](images/import-package-button.png "Start Import Button")\

Alternatively, you can select the **Import** option from the context menu, accessed by right-clicking on any node in the Package Browser.

2. **Choose the import source**. The Import Wizard provides a choice where to import the package from:

![Choose the Import Source](images/import-package-wizard.png "Choose the Import Source")\

The available import sources are:

**Server**. This is a directory on the server where packages can be imported from. By default this is the `importablePackages` directory in the directory where Deployit is installed, but this can be changed during the setup. New packages must be uploaded to this directory before they can be imported.

3. **Select the Deployment Package to import**. The dropdown list shows all packages available for import in the import source. Select the Deployment Package to import from this list. The Import button will be enabled. Note that it is not possible to import a package more than once. If you have changed your package and would like to import it again, you must rename the package and give it a new version number.
4. **Start the import process**. Click on the Import button to start the import. Once the import is complete, the Import button will change to a Close button.
5. **Close the Import Wizard**. Click on the Close button to complete the import procedure.

For more information about the Deployit packaging format, see the **Deployit Packaging Manual**.

# Deployments #

## Initial deployment ##

Once your package is imported, you can deploy it to any of the environments in Deployit. To deploy your package to an environment for the first time, follow these steps:

1. **Start a new deployment**. To start a new deployment, click the New Deployment button on the Application Browser:

![New Deployment Button](images/new-deployment-button.png "New Deployment Button")\

2. **Select the deployment package**. Find the package you want to deploy in the Package Browser and drag it into the new deployment tab. The package will be loaded into the Package Box and it's contents will be shown. This is an example of the Deployment Tab after selecting a deployment package:

![Selecting a Deployment Package](images/initial-deployment-package.png "Selecting a Deployment Package")\

Alternatively, you can select a deployment package in the Package Browser and choose the **Deploy** option from the context menu.

3. **Select the environment**. Find the environment you want to deploy to in the Application Browser and drag it into the new deployment tab. The environment will be loaded into the Environment Box and it's contents will be shown. This is an example of the Deployment Tab after selecting an environment:

![Selecting an Environment](images/initial-deployment-environment.png "Selecting an Environment")\

Alternatively, you can select an environment in the Application Browser and select the **Deploy to** option from the context menu.

4. **Map the deployment package to the environment**. Now that Deployit knows which deployment package you want to deploy on which environment, you can configure the way the package members are installed on the targets. To do this, you create _deployed items_ for each of the package members you want to deploy. There are several ways to do this:

**Let Deployit create default deployed items**. Deployit can generate default deployed items for each valid combination of a package member and target. The generated deployed items can then be configured manually. There are two ways to do this: either generate default deployed items for **all** package members or select one or more package members and generate deployed items only for them. You can also remove all deployed items for a package member. The buttons to perform these functions are in the top of the Package Box in the Deployment Configuration Page.

![Package Box Buttons](images/deployment-package-box-buttons.png "Package Box Buttons")\

**Manually create deployed items**. If you want to manually generate a deployed item, drag the package member from the left box to the target on the right. The mouse cursor will indicate whether it is possible to drop the package member and to generate a deployed item. If there are more possible deployed items that can be created, Deployit will display a popup so you can select which one to use. After the deployed item is created, the Deployed Item Configuration Balloon will open, allowing you to configure the deployed item. The balloon can also be opened by using the Edit Deployed Item button in the top of the Environment Box. You can also remove deployed items here.

![Environment Box Buttons](images/deployment-environment-box-buttons.png "Environment Box Buttons")\

5. **Configure the deployed items**. The deployed items may need to be configured before the deployment can be started. To do this, open the Deployed Item Configuration Balloon by double-clicking on a deployed item or use the Edit Deployed Item button in the toolbar. A balloon will open, showing the properties of the deployed item:

![Deployed Item Configuration Balloon](images/balloon-component.png "Deployed Item Configuration Balloon")\

When saving changes in the deployed item, Deployit will validate the data you entered and provide error messages if there are any problems.

6. **Generate the steplist**. When all of the deployed items are properly configured, proceed with the deployment by clicking on the **Next** button. Deployit will validate all deployed items and, if they are correct, generate a list of steps needed to perform your deployment. If the deployed items are not configured correctly or completely, Deployit will show an error message and allow you to rectify the situation.

7. **Configure the steplist**. The steplist contains all steps that Deployit will execute to perform your deployment. You have the opportunity to review it before starting the deployment. If there are steps that you want to skip, select the step from the list and press the **Skip** button. This step will not be executed when you run the deployment. Skipped steps can be unskipped by pressing the **Unskip** button. The deployment can be cancelled by pressing the **Cancel** button. The deployment task and it's associated deployed items will be removed. To navigate back to the Deployment Configuration Page, press the **Previous** button.

8. **Execute the deployment**. Press the **Deploy** button to start the deployment. Deployit will execute all steps in the steplist sequentially. The log of a step will be shown in the Log Window below the steplist. Select a step by clicking on it to see it's log. When the deployment is being executed, the following scenario's may occur:

**A step in the deployment fails**. If a step fails to execute successfully, Deployit stops executing the deployment and marks the step as _Failed_. This allows you to view the step's log output to determine what to do next. If the error is of a transient nature, the deployment can be restarted with the failed step by pressing the **Continue** button. If the step is incorrect and should be skipped, select the step, press the **Skip** button and then continue the deployment with the **Continue** button. To abort the deployment altogether, press the **Cancel** button.

**The deployment must be stopped**. If you want to gracefully stop a running deployment, press the **Stop** button. Deployit will wait until the currently executing step is finished and then stop the deployment. The deployment can be continued (**Continue** button) or cancelled (**Cancel** button).

**The deployment must be aborted**. If you want to forcefully abort a running deployment (or if stopping the deployment gracefully is not working, for instance due to a hanging script), press the **Abort** button. Deployit will attempt to kill the currently executing step and mark it as _Failed_. The deployment can then be continued starting with the aborted step (**Continue** button) or cancelled (**Cancel** button). The aborted step can also be skipped.

**The deployment completes successfully**. 

9. **Complete the deployment**. Press the **Close** button to close the Deployment Tab.

## Upgrading ##

Once you have performed an initial deployment of your package to an environment, upgrading that deployed application is easy. Follow these steps:

1. **Start an upgrade**. Click the New Deployment button on the Application Browser:

![New Deployment Button](images/new-deployment-button.png "New Deployment Button")\

2. **Select the deployment package**. Find the package you want to deploy in the Package Browser and drag it into the new deployment tab. The package will be loaded into the Package Box and it's contents will be shown. This is an example of the Deployment Tab after selecting a deployment package:

![Selecting a Deployment Package](images/initial-deployment-package.png "Selecting a Deployment Package")\

Alternatively, you can select a deployment package in the Package Browser and choose the **Deploy** option from the context menu.

3. **Select the deployment to upgrade**. Find the deployed application you want to upgrade to in the Application Browser and drag it into the new deployment tab. The environment will be loaded into the Environment Box and it's contents will be shown. This is an example of the Deployment Tab after selecting an environment:

![Selecting an Environment](images/initial-deployment-environment.png "Selecting an Environment")\

Alternatively, you can select a deployed application in the Application Browser and select the **Upgrade** option from the context menu.

4. **Map the deployment package to the environment**. Deployit will attempt to reuse the deployed items from the initial deployment, including their configuration. If the structure of your package is unchanged and the initial deployment was correct, most likely the reused mappings will suffice and you can continue with the deployment.

If the new package contains a new package member, it will be shown in orange in the left box. You can proceed with the deployment as-is if you do not want to deploy the new package member. Alternatively, create a new deployed item for the package member (see the section **Initial Deployment** above for details).

If the new package is missing a package member that was in the previous deployment, the deployed item for the missing member will be shown in red in the right box. You can, however, open the deployed item to look at it's settings if necessary.

5. **Configure the deployed items**. The deployed items will be configured as in the initial deployment. If this configuration needs to be changed, configure the deployed item as described above in **Initial Deployment**.

From this point on, upgrading is identical to an initial deployment. For more information, see the **Initial Deployment** section.

## Undeploying ##

To remove the application and all of it's components from an environment, you need to _undeploy_ the applcation. Follow these steps:

1. **Find the deployed application**. In the Deployment Screen, find the environment the application is deployed on in your Deployed Application Browser. If there are a lot of environments or applications, use the filter and search capabilities of the browser component.

2. **Start an undeployment**. Select the option **Undeploy** from the context-menu of the deployed application or select the deployed application and click the **Undeploy** button in the browser's toolbar. Deployit will open a new Undeployment Tab, showing a Steplist Page. The page shows the steps generated for the undeployment. 

3. **Configure the steplist**. The steplist contains all steps that Deployit will execute to perform your undeployment. For information on how to configure the steplist, see **Initial Deployment**.

4. **Execute the undeployment**. Deployit will execute each of the steps in the steplist. For more information on executing a steplist, see **Initial Deployment**.

5. **Complete the deployment**. Press the **Close** button to close the Undeployment Tab.

# Editing the Repository #

Deployit stores all of it's information in the repository. It is possible that the information in Deployit's repository becomes out-of-date with reality, for instance if a manual change is made to the deployment environment. In such cases, it can be necessary to manually bring the Deployit repository in sync with reality. This can be done by editing the information in the repository on the **Repository** screen.

## Creating a new CI ##

To create a new CI in the repository, do the following:

1. **Select the type of CI to create**. On the **Repository** screen, open the dropdown list located directly below the Repository Browser. This dropdown list contains all available CI types in Deployit, including the CI types added by plugins in your Deployit installation. Select the CI type you want to create.

2. **Create a new CI**. Click on the **Create** button next to the dropdown list to create a new CI. The new CI will be opened in the CI Editor Tab so you can fill out it's properties.

**Note**: the **Id** field of the CI is a special property that determines the place of the CI in the repository. For more information about the **Id** property, see the **Deployit Reference Manual**.

3. **Save the new CI**. Click on the **Save** button to save the new CI in the repository. Deployit will perform validation on the CI to ensure that all properties have appropriate values. If this is not the case, an error message is shown.

## Modifying a CI ##

To modify an existing CI, follow these steps:

1. **Select the CI in the Repository Browser**. Navigate the repository to find the CI you want to modify. For more information about the repository structure, see the **Deployit Reference Manual**.
2. **Edit the CI**. Use the context-menu on the CI to edit it in the CI Editor Tab.
3. **Save the CI**. Click on the **Save** button to save the new CI in the repository. Deployit will perform validation on the CI to ensure that all properties have appropriate values. If this is not the case, an error message is shown.

## Deleting a CI ##

To delete an existing CI, follow these steps:

1. **Select the CI in the Repository Browser**. Navigate the repository to find the CI you want to modify. For more information about the repository structure, see the **Deployit Reference Manual**.
2. **Delete the CI**. Click the **Delete** button in the Repository Browser toolbar. Deployit will confirm whether you want to delete the CI and, if yes, the CI will be deleted. 

Note that deleting a CI will also delete all nested CIs. For example, by deleting an environment CI, all deployments on that environment will also be deleted. The deployment package that was deployed on the environment, however, will remain under the **Applications** root node.

There is no way to recover a deleted CI.

# Comparing Configuration Items (CIs) #

Depending on your environment, deploying the same application to multiple environments may use different settings. With all these differences, it is easy to lose track of what is running where and how it is configured. Using Deployit's CI comparison feature, it is easy to spot the differences between two or more deployments, making troubleshooting a breeze.

To compare multiple CIs, follow these steps:

1. **Select the reference CI in the Repository Browser**. The reference CI is the basis for the comparison, the CI that the other CIs are compared against. Select it in the Repository Browser and press the **Compare** button in the browser's toolbar. Alternatively, select **Compare** in the context-menu.

2. **Drag comparison CIs into the Comparison Tab**. To add more CIs into the comparison, locate them in the Repository Browser and drag them into the Comparison Tab. Deployit will show which properties for the CIs have different values.

# Reporting #

Deployit contains information on all your environments, infrastructure and deployments. Using the tool's reporting functionality, you can gain insight into the state of your environments and applications.

## Deployed Applications per Environment Report ##

This report shows all deployed applications that were deployed in a certain environment at a particular date. The following is an example of such a report:

![Deployed Applications per Environment Report](images/reports-deployed-applications.png "Deployed Applications per Environment Report")\

The report shows the following columns:

* **Application**. The application on the environment.
* **Version**. The version of the application. 
* **User**. The user that performed the deployment.
* **Date of Deployment**. The date on which this version of the application was deployed.

## Deployments per Date Range Report ##

This report shows all deployments that were performed with Deployit. The following is an example of such a report:

![Deployments per Date Range Report](images/reports-deployments.png "Deployments per Date Range Report")\

The report shows the following columns:

* **Package**. The package and version that was deployed.
* **Environment**. The environment to which it was deployed.
* **User**. The user that performed the deployment.
* **Status**. The status of the deployment. 
* **Start Date**. The date on which the deployment was started.
* **Completion Date**. The date on which the deployment was completed.
* **Deployment Type**. The type of the deployment (*Initial*, *Upgrade* or *Undeployment*).
