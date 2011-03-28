---
layout: default
title: Deployit JBoass AS Plugin Manual
---

# Preface #

This manual describes the Deployit JBoss AS Plugin.

# Introduction #

The JBoss AS Plugin supports the deployment, re-deployment and undeployment of a deployment package to a JBoss Application Server.

# JBoss AS Plugin Requirements #

In addition to the requirements for Deployit, the JBoss AS Plugin has the following additional requirements:

Because the plugin executes its deployment and configuration tasks by connecting to the target host systems and executing [Twiddle](http://www.jboss.org/community/wiki/Twiddle) commands there, the following must be possible:

* creating a connection to the host on which the "deployment manager" is running, using the host's specified connection methods
* starting `_jboss-installation-dir_/bin/twiddle.sh` (Unix) or `twiddle.bat` (Windows) on the target host server under the user Deployit uses to connect to the host (or the SUDO user, if specified)

Further, the following configuration settings must be applied to the JBoss AS instances being managed:

* the **DeleteWorkDirOnContextDestroy** attribute in `server-profile/deploy/jboss-web.deployer/META-INF/jboss-service.xml` must be set to **true**
* the ScanEnabled attribute in `_server-profile_/conf/jboss-service.xml` must be set to **false**

# Supported JBoss AS Versions #

The JBoss AS plugin supports the following versions of JBoss AS:

* **4.2**
* **5.1**

# Supported JBoss Features #

The JBoss AS Plugin supports the following features:

Concept                                 | Remarks
--------                                | --------
WAR files                               | Deploy and undeploy WAR archives.
EAR files                               | Deploy and undeploy EAR archives.
Topics / Queues                         | Deploy and undeploy topics and queues.
Datasources                             | Deploy and undeploy datasources.
Libraries                               | Deploy and undeploy Java libraries.
Folders                                 | Deploy and undeploy folders.
Configuration files                     | Deploy and undeploy configuration files.
SQL files                               | Deploy and undeploy SQL files.
SQL folders                             | Deploy and undeploy folders containing SQL files.

# Known Limitations #

The plugin does not currently support the following:

* installation, maintenance or removal of JBoss installations and profiles.

# JBoss AS Runbook #

When the JBoss AS runbook is triggered, the plugin populates the steplist with steps based on the executed task. First, the JBoss AS runbook determines which servers are affected by the pending task. These are all the JBoss AS servers that are a target of one of the deployed items in the deployment or the JBoss AS server that a deployed application is running on in case of an undeploy. 

The JBoss AS runbook adds steps in the following order:

* Undeploy EARs 
* Undeploy WARs
* Destroy JBoss resources
* Deploy EARs
* Deploy WARs
* Create JBoss resources
* Undeploy libraries from the host
* Undeploy configuration files from the host
* Deploy libraries to the host
* Deploy configuration files to the host

# JBoss AS Configuration Items (CIs) #

The JBoss AS Plugin defines configuration items (CIs) needed to deploy to JBoss AS middleware. To get more information about these CIs, use Deployit's command line interface (CLI). See the **Deployit Command Line Interface (CLI) Manual** for more information.

## JbossasDataSource ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasDataSource

_Properties:_

* _connectionUrl(STRING)_: Connection Url
* _driverClass(STRING)_: Driver Class
* _jndiName(STRING)_: Jndi Name
* _maxPoolSize(INTEGER)_: Max Pool Size
* _minPoolSize(INTEGER)_: Min Pool Size
* _password(STRING)_: Password
* _useJavaContext(BOOLEAN)_: Use Java Context
* _username(STRING)_: Username



## JbossasEarMapping ##

A mapping of an EAR to a JBoss server

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasEarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _deploymentStrategy(ENUM)_: Deployment Strategy
    * Values: [ENABLED_HOT_DEPLOYMENT_STRATEGY, DISABLED_HOT_DEPLOYMENT_STRATEGY]
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _virtualHost(STRING)_: Virtual Host



## JbossasEjbJarMapping ##

A mapping of an EJB JAR to a JBoss server

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasEjbJarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _deploymentStrategy(ENUM)_: Deployment Strategy
    * Values: [ENABLED_HOT_DEPLOYMENT_STRATEGY, DISABLED_HOT_DEPLOYMENT_STRATEGY]
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _mdbListenerPortJndiNameBindings(List<com.xebialabs.deployit.ci.mapping.MdbListenerPortBinding>)_: Bindings of message driven beans JNDI names to the corresponding listener ports present on the target middleware
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]



## JbossasPath ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasPath

_Properties:_

* _name(STRING)_: Name



## JbossasQueue ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasQueue

_Properties:_

* **name(STRING)**: Name
* _jndiName(STRING)_: Jndi Name
* _maxDepth(INTEGER)_: Max. depth



## JbossasResourceMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasResourceMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _sourcePropertyOverrides(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Overrides for properties of the mapping's source. The key is the property name (consult the documentation or run 'describe' in the CLI), the value is the value to set. Only string, integer and enumerable properties can be overridden. Example: Key: redeliveryLimits, Value: 2



## JbossasServer ##

JBoss Application Server instance

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasServer

_Properties:_

* **home(STRING)**: Place where JBoss is installed such as /usr/local/jboss-5.1.0.GA.
* **host(com.xebialabs.deployit.ci.Host)**: Host on which the JBoss server is running.
* **name(STRING)**: Name of the JBoss server instance, e.g. default or minimal.
* **startCommand(STRING)**: Path to the script that should be executed to start the JBoss server in the background
* **version(ENUM)**: Version of the JBoss server.
    * Values: [JBOSSAS_40, JBOSSAS_50, JBOSSAS_60, JBOSSAS_UNKNOWN]
* _ajpPort(INTEGER)_: AJP Port for the JBoss Server, default is 8009
* _controlPort(INTEGER)_: ControlPort of the JBoss Server, default is 1099 for JBoss 5, 1090 for JBoss 6+
* _deployDirectories(List<com.xebialabs.deployit.plugin.jbossas.ci.JbossasPath>)_: Deploy Directories
* _deploymentCompletionWaitTime(INTEGER)_: Estimated time in miliseconds to wait for the deployment completion.
* _restartCommand(STRING)_: Command that should be executed to restart the JBoss server.
* _stopCommand(STRING)_: Command that should be executed to stop the JBoss server.
* _strategy(ENUM)_: Strategy
    * Values: [RESTART, STOP_START]



## JbossasTopic ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasTopic

_Properties:_

* **name(STRING)**: Name
* _jndiName(STRING)_: Jndi Name
* _maxDepth(INTEGER)_: Max. depth



## JbossasWarMapping ##

A mapping of a WAR to a JBoss server

_Type_: com.xebialabs.deployit.plugin.jbossas.ci.JbossasWarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _contextRoot(STRING)_: Context root to deploy to
* _deploymentStrategy(ENUM)_: Deployment Strategy
    * Values: [ENABLED_HOT_DEPLOYMENT_STRATEGY, DISABLED_HOT_DEPLOYMENT_STRATEGY]
* _ejbReferences(List<com.xebialabs.deployit.ci.mapping.EjbReference>)_: Specifies the mapping from ejb reference jndi names and locals used in the web.xml to bean jndi names available in middleware
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _resourceEnvironmentEntryReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource environment references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _resourceReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _virtualHost(STRING)_: Virtual host to deploy to


