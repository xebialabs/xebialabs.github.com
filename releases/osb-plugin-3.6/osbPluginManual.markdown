# Preface #

This document describes the functionality provided by the Oracle Service Bus (OSB) plugin.

See the **Deployit Reference Manual** for background information on Deployit and deployment concepts.

# Overview #

The OSB plugin is a Deployit plugin that adds capability for importing and deleting OSB projects.

##Features##

* OSB Configuration (import and delete)
* OSB Customization files (during import) with placeholders replacement

# Requirements #

* **Deployit requirements**
	* **Deployit**: version 3.6+
	* **WLS versions**: from ALSB 3.0 to OSB 11gR5
	* **Other Deployit Plugins**: WebLogic plugin version  3.6+

* **Infrastructural requirements**
	* **WebLogic Domain user credentials**
	* **User credentials** for accessing the Host managing the WebLogic Administration Server.
	* **User credentials** for accessing target Hosts of managed Servers (for NoStage mode)

# Usage in Deployment Packages #

The plugin works with the standard deployment package of DAR format. Please see the _Packaging Manual_ for more details about the DAR format and the ways to
compose one.

The following is a sample MANIFEST.MF file that can be used to create an OSB specific deployment package.
It contains declarations for an [osb.Configuration](#osb.Configuration) that contains two  projects: project1 and project2

	Manifest-Version: 1.0
	Deployit-Package-Format-Version: 1.3
	CI-Application: MyFrontEndServices
	CI-Version: 2.0

	Name: osbConfiguration
	CI-Type: osb.Configuration
	CI-projectNames-EntryValue-1: project1
	CI-projectNames-EntryValue-1: project2

osb.Configuration is a folder that contains one jar file containing the projects and one or more customization files in xml.

# Using the deployables and deployeds #

The following table describes which deployable/container combinations are possible.

## Deployable vs. Container table ##
<table class="deployed-matrix">
<tr>
	<th>Deployable</th>
	<th>Container</th>
	<th>Generated deployed</th>
</tr>
<tr>
	<td>osb.Configuration</td>
	<td>osb.Domain<br/>wls.Server</td>
	<td>osb.DeployedConfiguration</td>
</tr>
</table>

The following table describes the effect a deployed has on it's container

## Deployed Actions Table ##

<table class="deployed-matrix">
<tr>
	<th class="borderless-bottom">Deployed</th>
	<th colspan="3">Actions performed for operations</th>
</tr>
<tr>
	<th class="borderless-top">&nbsp;</th>
	<th align="center">Create</th>
	<th align="center">Destroy</th>
	<th align="center">Modify</th>
</tr>
<tr>
	<td>osb.Configuration</td>
	<td>Import the projects in the OSB Domain</td>
	<td>
		<ul>
		<li>Delete the projects from the OSB Domain</li>
		<li>Import the projects in the OSB Domain</li>
		</ul>
	</td>
</tr>
</table>
