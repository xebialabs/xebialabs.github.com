---
layout: default
title: Deployit GUI 
---

# The Deployment Screen #

This screen is used to import packages and deploy / undeploy applications. The following shows an example of the Deployment Screen:

![Deployment screen](images/deployment-screen-overview.png "The Deployment Screen")

The screen consists of the following components:

* **Package Browser**. This component is used to import and locate packages in Deployit.
* **Editor Window**. This window contains the tabs of tasks that the user is working on. The following tabs can appear here:
    * **Deployment Tab**. This tab is shown when performing a deployment. The tab contains two pages:
        * **Deployment Configuration Page**. This page is used to configure a deployment.
        * **Steplist Page**. This page shows the executing steps for a deployment.
* **Application Browser**. This component shows the deployed applications on different environments.

## The Package Browser ##

The Package Browser is used to import and select deployment packages in Deployit.

### Overview ###

The following is a snapshot of the Package Browser:

![Package Browser showing two applications](images/package-browser-overview.png "The Package Browser")

Deployment packages are grouped by the application they contain. In the above snapshot, there are three versions of the _**AnimalZoo-ear**_ application and one of the _**PetClinic-ear**_ application. When importing a deployment package for an application that does not yet exist, Deployit automatically creates the application for you.

If the list of packages is longer than can fit on one screen, the Package Browser will display one screen of packages and a scrollbar. If you drag the thumb down to the bottom of the scrollbar, the Package Browser will retrieve and display the next screen of packages.

### Toolbar ###

The Package Browser has the following toolbar:

![Package Browser toolbar](images/package-browser-toolbar.png "The Package Browser toolbar")

It contains the following controls:

* **Import Deployment Package button**. This button is used to import a new deployment package. The same function can be activated by using the context menu.
* **Delete Deployment Package button**. This button is used to delete an existing deployment package.
* **Search box**. This box is used to search for deployment packages based on a text string.

### Searching for Packages ###

The content of the Package Browser can be searched by typing text in the search box and pressing _Enter_ or clicking on the magnifying glass. The Package Browser will show only those entries matching your search string (either as a complete match or a substring). Note that only the top-level of the entities in the Package Browser is being searched. If you want to search for entities that are not at the top-level (for instance, searching for a particular deployment package version of the _**AnimalZoo-ear**_ in the situation shown above), restrict the scope of the Package Browser to _**AnimalZoo-ear**_ and then apply search (see below).

### Navigating Packages ###

Deployit may contain many applications and deployment packages. To quickly locate a particular deployment package, the scope of the Package Browser can be restricted by double-clicking on a particular package. This narrows the scope of the data being shown and makes it possible to search through it.

For example, after double-clicking the _**AnimalZoo-ear**_ application in the situation shown above, the Package Browser shows the following:

![Restricting Scope to the AnimalZoo-ear Application](images/package-browser-breadcrumbs-app.png "Restricting Scope to the AnimalZoo-ear application")

Using the _Search box_ it is possible to search for a particular deployment package _version_. 

By double-clicking on the deployment package with version _**1.0**_, the Package Browser shows the following:

![Restricting Scope to the AnimalZoo-ear/1.0 Package](images/package-browser-breadcrumbs-package.png "Restricting Scope to the AnimalZoo-ear/1.0 Package")

Using the _Search box_ it is possible to search for a particular _member_ of this deployment package. 

Also note the breadcrumbs shown above the deployment package tree. The breadcrumb trail shows the following items (the text will expand when you position the mouse cursor over the breadcrumb):

* **/**. This is the deployment package tree root node. Clicking on this resets the Package Browser scope to show all applications.
* **AnimalZoo-ear**. This is the _**AnimalZoo-ear**_ application tree node. Clicking on this changes the Package Browser scope to display all deployment packages for this application.
* **1.0**. This is the _**1.0**_ deployment package tree node and is shown in the previous diagram.

## The Deployment Tab ##

The Deployment Tab is used to configure and execute deployments.

### The Deployment Configuration Page ###

When starting a new deployment, the Deployment Tab looks like this:

![Empty Deployment Tab](images/deployment-tab-empty.png "Empty Deployment Tab")

This is the Deployment Configuration page. It contains two areas that need to be filled in to create a deployment. The left half of the tab requires a **deployment package** and the right half an **environment** or **deployed application**. Once both are in place, deployed items can be created and configured after which the deployment can start.

### Initial Deployment ###

If you drag an **environment** into the right half of the Deployment Configuration page, Deployit will create an **initial deployment**. The following picture shows an example.

![Deployment Tab with Initial Deployment](images/deployment-tab-initial.png "Deployment Tab with Initial Deployment")

The left box shows the contents of the deployment package, **smallApp/1.0**. Both artifacts are colored orange, indicating that they have not yet been mapped to a target server. The right box shows the selected environment, **10smallEnv10**. The environments middleware, two servers, are shown in the _UNMAPPED_ section of the box. Once an artifact or middleware resource is mapped to a target server, the server moves to the _MAPPED_ section.

### Upgrade Deployment ###

If you drag a **deployed application** into the right half of the Deployment Configuration page, Deployit will create an **upgrade deployment**. The following picture shows an example.

![Deployment Tab with Upgrade Deployment](images/deployment-tab-upgrade.png "Deployment Tab with Upgrade Deployment")

The left box shows the contents of the deployment package, **AnimalZoo-ear/2.0**. One artifact is colored orange, indicating that it has not yet been mapped to a target server. The right box shows the selected deployment, **AnimalZoo-ear/1.0 on 10smallEnv10**. The deployed items for **AnimalZooBE** are reused from the previous deployment. Artifact **AnimalZooFE** that was present in the previous deployment, is now missing from the current deployment package and therefore stricken out.

### Creating Deployed Items ###

Depending on your deployment, you may need to create and configure deployed items. In the case of an initial deployment, this is a requirement. For upgrade deployments, most mappings will be inherited from the previous deployment. When the package has only code changes and no structural changes (no artifacts or middleware resources added or removed), the upgrade deployment can proceed immediately.

The following image shows an example of the Deployment Tab when adding and removing deployed items.

![Adding and Removing Deployed Items](images/deployment-tab-add_remove-deployed-items.png "Adding and Removing Deployed Items")

When selecting a package member on the left, lines are shown to indicate where this member has been mapped to.

**Adding a Deployed Item**

To add a deployed item, drag the artifact or middleware resource from the deployment package in the left hand box to the target server in the right hand box. A new deployed item will be created which can be edited in an editor component.

The toolbars in both boxes can also help. This is the toolbar in the package box:

![Deployment Package Box Toolbar](images/deployment-tab-package-box-toolbar.png "Deployment Package Box Toolbar")

It contains the following buttons:

* **Generate All Deployed Items button**. This button requests Deployit to generate deployed items for all artifacts and middleware resources in the deployment package. Whether any deployed items are generated depends on the configuration of your Deployit system and plugins. Deployit only generates deployed items for package members that have not yet been mapped.
* **Generate Deployed Item button**. This button requests Deployit to generate deployed items for the selected artifact or middleware resource only.
* **Remove Deployed Items button**. This button removes all deployed items for the selected package member.

This is the toolbar in the deployment target box:

![Deployment Target Box Toolbar](images/deployment-tab-target-box-toolbar.png "Deployment Target Box Toolbar")

It contains the following buttons:

* **Configure Deployed Item button**. This button brings up the Deployed Item Configuration balloon.
* **Remove Deployed Item button**. This button removes the currently selected deployed item.

### Configuring Deployed Items ###

To configure a deployed item, double-click it in the target box of the deployment tab. The Deployed Item Configuration balloon is shown:

![Deployed Item Configuration Balloon](images/deployment-tab-balloon.png "Deployed Item Configuration Balloon")

In this window, all properties of the deployed item can be edited. This includes primitive properties (strings, integers), lists of values, (collections of) references to other CIs and placeholders to be replaced in deployed files. The window can contain multiple tabs for different types of properties. Any changes made to the deployed item can be saved or cancelled.

The actual properties that can be edited depend on the deployed item being edited. Typically, these are provided by one of Deployit's plugins. For more information about the plugins, see the **Plugin Manual** for the specific plugin.

### Generating the Steplist ###

The **Next** button at the bottom of the deployment tab submits the deployment to the server and requests Deployit to generate a steplist to perform the particular deployment. Deployit validates the deployed items and their configuration and reports any errors it finds. If all deployed items are correct, the Steplist Page is shown. 

### The Deployment Execution Page ###

When Deployit has generated a steplist, the Deployment Execution page appears. This is an example:

![Deployment Execution Page](images/deployment-tab-execution.png "Deployment Execution Page")

As shown in the example, all steps to be executed to perform the deployment are shown in order. Each step lists a step sequence number, description and the state (PENDING, SKIPPED, SEXECUTING or FAILED). The following buttons are shown at the bottom of the screen:

* **Previous button**. This button navigates back to the Deployment Configuration page. This is not always possible, for example in the case of a recovered task.
* **Skip button**. This button marks the selected step as _skipped_. When executing the steplist, this step will be skipped. The same button can be used to un-skip a step.
* **Stop button**. This button attempts to stop the currently running deployment right after the currently executing step finishes.
* **Abort button**. This button attempts to abort the currently running deployment by killing the currently executing step.
* **Cancel button**. This button cancels the pending, stopped or aborted deployment.
* **Deploy button**. This button starts execution of the deployment.

Once the deployment is running, the log for every executed step will be shown in the log window.

After the deployment finishes, the tab can be closed using the **Close** button.

## The Application Browser ##

The Application Browser is used to display deployed applications in Deployit.

### Overview ###

The following is a snapshot of the Application Browser:

![Application Browser](images/application-browser-overview.png "The Application Browser")

Deployment applications are grouped by the environment they are deployed on. In the above snapshot, the _**10smallEnv10**_ environment contains deployed application _**AnimalZoo-ear/1.0**_ and _**smallApp/1.0**_.

If the list of environments is longer than can fit on one screen, the Application Browser will display one screen of environments and a scrollbar. If you drag the thumb down to the bottom of the scrollbar, the Application Browser will retrieve and display the next screen of environments.

### Toolbar ###

The Application Browser has the following toolbar:

![Application Browser toolbar](images/application-browser-toolbar.png "The Application Browser toolbar")

It contains the following controls:

* **Deploy Application button**. This button is used to start a new deployment. The same function can be activated by using the context menu.
* **Undeploy Application button**. This button is used to undeploy an existing deployed application.
* **Search box**. This box is used to search for deployed applications based on a text string.

### Searching for Deployed Applications ###

The content of the Application Browser can be searched by typing text in the search box and pressing _Enter_ or clicking on the magnifying glass. The Application Browser will show only those entries matching your search string (either as a complete match or a substring). Note that only the top-level of the entities in the Application Browser is being searched. If you want to search for entities that are not at the top-level (for instance, searching for a particular server that the application is deployed on), restrict the scope of the Application Browser to _**AnimalZoo-ear**_ and then apply search (see below).

### Navigating Deployed Applications ###

To quickly locate a particular deployed application or item, the scope of the Application Browser can be restricted by double-clicking on a particular item. This narrows the scope of the data being shown and makes it possible to search through it.

For a more thorough explanation, see the **Package Browser** above.
