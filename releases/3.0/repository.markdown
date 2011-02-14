Opening file ./src/markdown/onlinehelp/repository.markdown
----
layout: default
title: Deployit GUI 
----

# The Repository Screen #

This screen is used to view and edit the Deployit repository. The following shows an example of the Repository Screen:

![Repository screen](images/repository-screen-overview.png "The Repository Screen")

The screen consists of the following components:

* **Repository Browser**. This component is used to locate CIs in Deployit.
* **Editor Window**. This window is used to work with CIs.
    * **CI Editor Tab**. This tab is used to edit CIs.
    * **CI Comparison Tab**. This tab is used to compare CIs with each other.

## The Repository Browser ##

The Repository Browser is used to locate CIs in Deployit.

### Overview ###

The following is a snapshot of the Repository Browser:

![Repository Browser showing two applications](images/repository-browser-overview.png "The Repository Browser")

The Repository Browser shows those parts of the Deployit repository that the logged in user is allowed to see. In the above snapshot, there are four applications and a list of environments shown.

If the list of items is longer than can fit on one screen, the Repository Browser will display one screen of items and a scrollbar. If you drag the thumb down to the bottom of the scrollbar, the browser will retrieve and display the next screen of items.

### Toolbar ###

The Repository Browser has the following toolbar:

![Repository Browser toolbar](images/repository-browser-toolbar.png "The Repository Browser toolbar")

It contains the following controls:

* **Edit CI button**. This button is used edit the selected CI. This function can also be performed using the context-menu.
* **Delete CI button**. This button is used to delete a CI from the repository.
* **Search box**. This box is used to search for CIs based on a text string.

### Searching for CIs ###

The content of the Repository Browser can be searched by typing text in the search box and pressing _Enter_ or clicking on the magnifying glass. The Repository Browser will show only those entries matching your search string (either as a complete match or a substring). Note that only the top-level of the entities in the Repository Browser is being searched. If you want to search for entities that are not at the top-level, restrict the scope of the browser to a lower-level item and then apply search (see below).

### Navigating the Repository ###

To quickly locate a particular CI, the scope of the Repository Browser can be restricted by double-clicking on a particular item. This narrows the scope of the data being shown and makes it possible to search through it.

For example, after double-clicking the _**AnimalZoo-ear**_ application in the situation shown above, the Repository Browser shows the following:

![Restricting Scope to the AnimalZoo-ear Application](images/repository-browser-breadcrumbs-app.png "Restricting Scope to the AnimalZoo-ear application")

Using the _Search box_ it is possible to search for a particular deployment package _version_. 

By double-clicking on the deployment package with version _**1.0**_, the Package Browser shows the following:

![Restricting Scope to the AnimalZoo-ear/1.0 Package](images/repository-browser-breadcrumbs-package.png "Restricting Scope to the AnimalZoo-ear/1.0 Package")

Using the _Search box_ it is possible to search for a particular _member_ of this deployment package. 

Also note the breadcrumbs shown above the deployment package tree. The breadcrumb trail shows the following items (the text will expand when you position the mouse cursor over the breadcrumb):

* **/**. This is the repository tree root node. Clicking on this resets the Repository Browser scope to show the entire repository.
* **Applications**. This is the applications tree root node. Clicking on this resets the Repository Browser scope to show all applications.
* **AnimalZoo-ear**. This is the _**AnimalZoo-ear**_ application tree node. Clicking on this changes the Repository Browser scope to display all deployment packages for this application.
* **1.0**. This is the _**1.0**_ deployment package tree node and is shown in the previous diagram.

### Creating new CIs ###

The Repository Browser is also used to create new CIs. The following image shows how this is done:

![Creating CIs in the Repository Browser](images/repository-browser-create-ci.png "Creating CIs in the Repository Browser")

To create a new CI, do the following:

* **Select the CI type**. The dropdown list at the bottom of the Repository Browser shows all CI types that Deployit supports. The exact contents of this list is dependent on the plugins installed in Deployit.
* **Press the Create button**. This opens a CI Editor tab in the Editor window containing a blank CI of the desired type.

## The Editor Window ##

### The CI Editor Tab ###

The CI Editor tab is used to edit CIs found in the Repository Browser. The following image shows an example of the editor:

![CI Editor tab](images/ci-editor-tab.png "CI Editor tab")

The Editor tab shows the properties of the CI being edited. Depending on the CI type, different properties will be shown.

**Id Property**

The id property of a CI determines it's place in the repository. It is a string consisting of folder nodes and terminated by a leaf node, all of which are separated by `/` characters. For example:

	/Applications/PetClinic/1.0/PetClinic.ear

This denotes a CI stored in the **PetClinic.ear** leaf node under the **Applications**, **PetClinic** and **1.0** folder nodes.

To allow efficient searching through the repository, the CIs must be stored in the proper folder nodes. If a CI is saved with an id that places it in a wrong part of the tree, Deployit will show an error message.

**List of Values**

If a CI contains a property with a restricted number of values, the following control is shown:

![List of Values in the CI Editor tab](images/ci-editor-tab-dropdown.png "List of Values in the CI Editor tab")

Select one of the available values by clicking on it.

**CI References**

If a CI contains a collection of references to other CIs, the following control is shown:

![CI Selection in the CI Editor tab](images/ci-editor-tab-ci-selection.png "CI Selection in the CI Editor tab")

The right box shows the CIs currently in the collection. Use the arrow pointing left or double-click on the item to remove it from the collection.

The left box is used to locate CIs for inclusion in the collection, either by using the scrollbar or searching using the textfield. Use the arrow pointing right or double-click on the item to include it in the collection.

**Data Grid**

If a CI contains a list of objects that each have several properties, the following control is shown:

![Data Grid in the CI Editor tab](images/ci-editor-tab-datagrid.png "Data Grid in the CI Editor tab")

Depending on the number of properties in the contained object type, the datagrid may show more columns.

Use the `+` and `-` buttons to add or remove rows. The `tab` key can be used to navigate to the next cell in the datagrid.

### The CI Comparison Tab ###

The CI Comparison tab is used to compare CIs found in the Repository Browser. The following image shows an example:

![CI Comparison tab](images/ci-comparison-tab.png "CI Comparison tab")

The Comparison tab shows a grid with the CIs properties as rows and columns for each of the CIs being compared. If a CI has a value that is different from the first, reference CI, the property and the differing values are colored red.

To perform a comparison, follow these steps:

* Locate the CI you want to use as the reference for the comparison in the Repository Browser.
* Select the reference CI and click on the Compare toolbar button. Alternatively, use the right-click context menu on the selected CI. A CI Comparison tab will open, displaying the selected CI.
* Navigate to the CI you want to compare to the reference CI.
* Drag the CI into the CI Comparison tab. A column will be added to the grid, showing the dropped CI and it's values.
* Repeat the last two steps up to a maximum of 5 CIs.
