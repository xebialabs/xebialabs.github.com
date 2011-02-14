---
layout: default
title: Deployit Oracle WebLogic Server 
---

# Preface #

This manual describes the Deployit Tomcat Plugin.

# Introduction #

The  Oracle WebLogic Server (WLS) Plugin supports the deployment, re-deployment and undeployment of a deployment package to a WLS servlet container.

# Tomcat Plugin Requirements #

In addition to the requirements for Deployit, the WLS Plugin has the following additional requirements:

* the user account used to access the WLS server must have permission to perform the following actions:
	* run the WLS, wlst.sh script (or wlst.bat on Windows)

The target middleware needs to be set up so that the administrative interfaces of the target middleware can be accessed by running it on the machine on which the administrative server of the software is installed. Deployit does not support a setup in which the administrative client is installed on a different machine.

For WebLogic Server this means that Deployit will use SSH to log in to the machine on which the "admin server" is running, upload any Python files and other files needed to a temporary directory and then invoke the `wlst.sh` command. Afterwards any temporary files will be removed.

# Supported WLS Versions #

The WLS plugin supports the following versions of WLS:

* **10.3.x**

# Supported WLS Features #

The WLS Plugin supports the following features:

Concept                                   Remarks
--------                                  --------
EAR/WAR/EJB-Jar                           Deploy and undeploy EAR, WAR and EJB-Jar's.
LibraryJar                                
Apache Httpd Wls Plugin Configuration     Create and destroy Apache HTTPD Server configuration.
DataSource                                Create and destroy datasources.
Foreign Jms Connection Factory            Create and destroy JMS Connection factories.
Foreign Jms Destination                   Create and destroy JMS destinations.
Foreign Jms Server                        Create and destroy JMS Servers.
Maximum Threads Constraint                Configure maximum thread constraints in the server.
Shared Library Jar                        Deploy and undeploy sharedl library jars.
Work Manager                              Configure the work manager in the server instances.

# WLS Runbook #

When the WLS runbook is triggered, the plugin populates the steplist with steps based on the executed task. First, the WLS runbook determines which servers are affected by the pending task. These are all the WLS servers that are a target of one of the deployed items in the deployment or the WLS server that a deployed application is running on in case of an undeploy. 

The WLS runbook adds steps in the following order:

* Undeploy EAR/WAR/EJB-Jar
* Undeploy library Jars
* Activate changes
* Delete queues and topics
* Delete connection factories
* Delete datasources
* Unconfigure work managers
* Unconfigure maximum threads constraint
* Delete configuration files on host
* Copy configuration files to host
* Copy and configure libraries
* Modify servers and clusters
* Modify Queues
* Activate changes
* Copy and execute SQL scripts against databases
* Create queues and topics
* Create datasources
* Configure maximum threads constraint
* Configure work managers
* Deploy EAR/WAR/EJB-Jar
* Start applications

# WLS Configuration Items (CIs) #

The WLS Plugin defines configuration items (CIs) needed to deploy to Tomcat middleware. To get more information about these CIs, use Deployit's command line interface (CLI). See the **Deployit Command Line Interface (CLI) Manual** for more information.

## ApacheHttpdWlsPluginConfiguration ##

An abstraction of Apache Weblogic Plugin Configuration. It is used to generate the configuration file which is included in the Apache main httpd.conf file

_Type_: com.xebialabs.deployit.plugin.wls.ci.ApacheHttpdWlsPluginConfiguration

_Properties:_

* **name(STRING)**: configuration name
* _errorPage(STRING)_: Error Page
* _mimeMatchExpressions(STRING)_: Comma separated list of match expression to proxy requests by MIME type
* _pathExpressions(STRING)_: Comma separated list of path to be used for proxing requests by path



## ApacheHttpdWlsPluginConfigurationMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.wls.ci.ApacheHttpdWlsPluginConfigurationMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _clusters(Set<com.xebialabs.deployit.plugin.wls.ci.WlsCluster>)_: Clusters
* _sourcePropertyOverrides(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Overrides for properties of the mapping's source. The key is the property name (consult the documentation or run 'describe' in the CLI), the value is the value to set. Only string, integer and enumerable properties can be overridden. Example: Key: redeliveryLimits, Value: 2
* _virtualHost(STRING)_: Virtual Host



## WlsCluster ##

A WebLogic Cluster, a member of WebLogic Domain. It can have WebLogicServers as it's members

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsCluster

_Properties:_

* **domain(com.xebialabs.deployit.plugin.wls.ci.WlsDomain)**: The domain to which the WebLogic Cluster belongs
* **name(STRING)**: Name of the WebLogic Cluster
* _servers(Set<com.xebialabs.deployit.plugin.wls.ci.WlsServer>)_: Servers in the WebLogic Cluster



## WlsClusterResourceMapping ##

A mapping of a WebLogic resource for a WlsCluster to a WlsCluster

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsClusterResourceMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _sourcePropertyOverrides(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Overrides for properties of the mapping's source. The key is the property name (consult the documentation or run 'describe' in the CLI), the value is the value to set. Only string, integer and enumerable properties can be overridden. Example: Key: redeliveryLimits, Value: 2



## WlsDataSource ##

A datasource to connect to a database.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsDataSource

_Properties:_

* **driver(STRING)**: The driver of the datasource, the classname, e.g. oracle.jdbc.xa.client.OracleXADataSource
* **init(INTEGER)**: The initial connectionpool size.
* **jndiName(STRING)**: The JNDI name of the datasource, e.g. jdbc/orderdb
* **max(INTEGER)**: The maximum connectionpool size.
* **name(STRING)**: The name of the datasource in the WebLogic configuration, e.g. Order DataSource
* **uri(STRING)**: The JDBC uri to the database, e.g. jdbc:oracle:thin:@ora-prod:1521:orders
* _password(STRING)_: The password credential for the database, e.g. tiger
* _properties(STRING)_: A comma separated list of name=value pairs.
* _userName(STRING)_: The username credential for the database, e.g. scott



## WlsDeploymentPlan ##

Deployable Oracle Service bus Custumization File artifact.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsDeploymentPlan

_Properties:_

* **location(STRING)**: Location of the artifact.
* **name(STRING)**: The technical name of the artifact as it will be used within application servers.



## WlsDomain ##

A WebLogic Domain.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsDomain

_Properties:_

* **activeHost(com.xebialabs.deployit.ci.Host)**: The host that runs the admin server
* **adminServerName(STRING)**: The name of the admin server
* **name(STRING)**: Name of the WebLogic Domain
* **password(STRING)**: Password which is used to login to the WebLogic Domain.
* **port(INTEGER)**: Port to be used by the AdminServer for this domain
* **startMode(ENUM)**: Tells how a managed server is start and stop, default is NodeManager, others are Script or Windows Service
    * Values: [NodeManager, Script, WindowsService]
* **username(STRING)**: Username which is used to login to the WebLogic Domain.
* **wlHome(STRING)**: The location of the WebLogic Server installation
* _domainHome(STRING)_: The location of the WebLogic domain. Defaults to '<WebLogicHome>/../user_projects/domains/<Name>'
* _enableWlstShWorkaround(BOOLEAN)_: Enable workaround for broken wlst.sh script found in some versions of WLS
* _wlsVersion(ENUM)_: Wls Version
    * Values: [WEBLOGIC_8, WEBLOGIC_9, WEBLOGIC_10, WEBLOGIC_11]



## WlsEarMapping ##

A mapping of an EAR to a WebLogic target

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsEarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _deploymentPlan(com.xebialabs.deployit.plugin.wls.ci.WlsDeploymentPlan)_: Deployment Plan
* _deploymentPlanStagingDirectory(STRING)_: Deployment Plan Staging Directory
* _deploymentStrategy(ENUM)_: Deployment Strategy
    * Values: [CLASSIC, STOP_START, SIDE_BY_SIDE]
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _stageMode(ENUM)_: Deployment staging mode (default is stage)
    * Values: [Stage, NoStage]
* _stagingDirectory(STRING)_: Remote directory where the archives (ear,jar,war) are copied before deploying
* _virtualHost(STRING)_: Virtual Host



## WlsEjbJarMapping ##

A mapping of an EjbJar to a WebLogic target

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsEjbJarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _deploymentPlan(com.xebialabs.deployit.plugin.wls.ci.WlsDeploymentPlan)_: Deployment Plan
* _deploymentPlanStagingDirectory(STRING)_: Deployment Plan Staging Directory
* _deploymentStrategy(ENUM)_: Deployment Strategy
    * Values: [CLASSIC, STOP_START, SIDE_BY_SIDE]
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _mdbListenerPortJndiNameBindings(List<com.xebialabs.deployit.ci.mapping.MdbListenerPortBinding>)_: Bindings of message driven beans JNDI names to the corresponding listener ports present on the target middleware
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _stageMode(ENUM)_: Deployment staging mode (default is stage)
    * Values: [Stage, NoStage]
* _stagingDirectory(STRING)_: Remote directory where the archives (ear,jar,war) are copied before deploying



## WlsForeignJmsConnectionFactory ##

Foreign connection factory represents a connection factory that resides on another server, and which is accessible via JNDI.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsForeignJmsConnectionFactory

_Properties:_

* **foreignJmsServer(com.xebialabs.deployit.plugin.wls.ci.WlsForeignJmsServer)**: The foreign server in which the foreign connection factory is included.
* **localJndiName(STRING)**: The name that the remote object will be bound to in the local server's JNDI tree.
* **name(STRING)**: The name of the foreign connection factory.
* **remoteJndiName(STRING)**: The name of the remote object that will be looked up in the remote JNDI directory.



## WlsForeignJmsDestination ##

A foreign destination (topic or queue) is a destination on a remote server. When this destination is looked up on the local server, a look-up will be performed automatically on the remote JNDI directory, and the object will be returned from that directory

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsForeignJmsDestination

_Properties:_

* **foreignJmsServer(com.xebialabs.deployit.plugin.wls.ci.WlsForeignJmsServer)**: The name of the Foreign JMS Server
* **localJndiName(STRING)**: The name that the remote object will be bound to in the local server's JNDI tree
* **name(STRING)**: The name of this foreign destination
* **remoteJndiName(STRING)**: The name of the remote object that will be looked up in the remote JNDI directory



## WlsForeignJmsServer ##

A WebLogic foreign server representing a JNDI provider that resides outside a WebLogic Server.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsForeignJmsServer

_Properties:_

* **connectionURL(STRING)**: The URL that WebLogic Server will use to contact the JNDI provider
* **initContextFactory(STRING)**: The initial context of the foreign connection
* **name(STRING)**: The name of the foreign server



## WlsJmsConnectionFactory ##

A WebLogic JMS Connection Factory

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsJmsConnectionFactory

_Properties:_

* **jndiName(STRING)**: Jndi Name
* **name(STRING)**: The name of the connection factory.



## WlsJmsQueue ##

A WebLogic JMS Queue

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsJmsQueue

_Properties:_

* **expirationPolicy(ENUM)**: The message Expiration Policy to use when an expired message is encountered on a destination
    * Values: [DISCARD, LOG, REDIRECT]
* **jndiName(STRING)**: Jndi Name
* **name(STRING)**: The name of the queue
* _errorQueue(com.xebialabs.deployit.plugin.wls.ci.WlsJmsQueue)_: The name of the target error destination for messages that have expired or reached their redelivery limit
* _expirationLoggingFormat(STRING)_: The policy that defines what information about the message is logged when the Expiration Policy is set to Log
* _jmsServer(com.xebialabs.deployit.plugin.wls.ci.WlsJmsServer)_: Jms Server
* _redeliveryDelayOverride(INTEGER)_: The delay, in milliseconds, before rolled back or recovered messages are redelivered, regardless of the RedeliveryDelay specified by the consumer and/or connection factory
* _redeliveryLimits(INTEGER)_: The number of redelivery attempts a message can make before it is moved to the error destination



## WlsJmsServer ##

WebLogic JMSServer that can run on a WebLogic Server.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsJmsServer

_Properties:_

* **fileStorePath(STRING)**: Path to the file store that the JMSServer will use to store JMS messages. e.g. /var/jms/store1
* **name(STRING)**: Name of the JMSServer. e.g. JMSServer1



## WlsMaximumThreadsConstraint ##

Work Manager that defines a set of request classes and thread constraints that manage work performed by WebLogic Server instances.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsMaximumThreadsConstraint

_Properties:_

* **name(STRING)**: Name of the Work Manager
* **threadCount(INTEGER)**: Thread Count
* _notes(STRING)_: Notes



## WlsServer ##

A standard Weblogic Server

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsServer

_Properties:_

* **domain(com.xebialabs.deployit.plugin.wls.ci.WlsDomain)**: WebLogic Domain to which this server belongs
* **host(com.xebialabs.deployit.ci.Host)**: Host on which this server is running
* **name(STRING)**: Name of the WebLogic Server
* **port(INTEGER)**: Port for the WebLogic Server
* _arguments(STRING)_: The arguments for this server, including initial heapsize (e.g. -Xms64m), maxheap size (-Xms256m), and bootclasspath (-Xbootclasspath/p:/var/lib/addons.jar)
* _classpath(STRING)_: Classpath entries for this server.
* _enableJVMLogRedirection(BOOLEAN)_: Enable JVM StdOut to Server Log file
* _logFileLocation(STRING)_: Absolute path of log file. Example; /opt/bea/user_projects/domain/managedserver1/ms1.log
* _stageMode(ENUM)_: Deployment staging mode (default is stage)
    * Values: [Stage, NoStage]
* _startCommand(STRING)_: Command that should be executed to start the managed server.
* _stopCommand(STRING)_: Command that should be executed to stop the managed server.



## WlsServerResourceMapping ##

A mapping of a WebLogic resource for a WlsServer to a WlsServer

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsServerResourceMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _sourcePropertyOverrides(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Overrides for properties of the mapping's source. The key is the property name (consult the documentation or run 'describe' in the CLI), the value is the value to set. Only string, integer and enumerable properties can be overridden. Example: Key: redeliveryLimits, Value: 2



## WlsSharedLibraryJar ##

Deployable WebLogic library JAR artifact.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsSharedLibraryJar

_Properties:_

* **location(STRING)**: Location of the artifact.
* **name(STRING)**: The technical name of the artifact as it will be used within application servers.



## WlsSharedLibraryJarMapping ##

A mapping of a JAR library to WebLogic middleware

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsSharedLibraryJarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _deploymentStrategy(ENUM)_: Deployment Strategy
    * Values: [CLASSIC, STOP_START, SIDE_BY_SIDE]
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _stageMode(ENUM)_: Deployment staging mode (default is stage
    * Values: [Stage, NoStage]
* _stagingDirectory(STRING)_: Remote directory where the archives (ear, jar, war) are copied before deploying



## WlsWarMapping ##

A mapping of a WAR to WebLogic middleware

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsWarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _contextRoot(STRING)_: Context root to deploy to
* _deploymentPlan(com.xebialabs.deployit.plugin.wls.ci.WlsDeploymentPlan)_: Deployment Plan
* _deploymentPlanStagingDirectory(STRING)_: Deployment Plan Staging Directory
* _deploymentStrategy(ENUM)_: Deployment Strategy
    * Values: [CLASSIC, STOP_START, SIDE_BY_SIDE]
* _ejbReferences(List<com.xebialabs.deployit.ci.mapping.EjbReference>)_: Specifies the mapping from ejb reference jndi names and locals used in the web.xml to bean jndi names available in middleware
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _resourceEnvironmentEntryReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource environment references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _resourceReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _stageMode(ENUM)_: Deployment staging mode (default is stage
    * Values: [Stage, NoStage]
* _stagingDirectory(STRING)_: Remote directory where the archives (ear, jar, war) are copied before deploying
* _virtualHost(STRING)_: Virtual host to deploy to



## WlsWorkManager ##

Work Manager that defines a set of request classes and thread constraints that manage work performed by WebLogic Server instances.

_Type_: com.xebialabs.deployit.plugin.wls.ci.WlsWorkManager

_Properties:_

* **name(STRING)**: Name of the Work Manager
* _maximumThreadsConstraint(com.xebialabs.deployit.plugin.wls.ci.WlsMaximumThreadsConstraint)_: Maximum Threads Constraint


