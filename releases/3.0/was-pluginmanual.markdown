---
layout: default
title: Deployit WebSphere Plugin Manual
---

# Preface #

This manual describes the Deployit WebSphere Application Server Plugin.

# Introduction #

The WebSphere Application Server (WAS) Plugin supports the deployment, re-deployment and undeployment of a deployment package to a WAS Network Deployment and Stand Alone installation.
Furthermore, it supports, creation, modification and deletion of Application Servers and Clusters.  

# WAS Plugin Requirements #

In addition to the requirements for Deployit, the WAS Plugin has the following additional requirements:

* the user account used to access the WAS server must have permission to perform the following actions:
	* execute the wsadmin.sh command located in the bin directory of your WAS installation

The target middleware needs to be set up so that the administrative interfaces of the target middleware can be accessed by running it on the machine on which the administrative server of the software is installed. Deployit does not support a setup in which the administrative client is installed on a different machine.

For WebSphere Application Server this means that Deployit will use SSH to log in to the machine on which the "deployment manager" is running, upload any Python files and other files needed to a temporary directory and then invoke the `wsadmin.sh` command. Afterwards any temporary files will be removed.

# Supported WAS Versions #

The WAS plugin supports the following versions of WAS Network Deployment and Stand Alone Server:

* **6.1.x**
* **7.0.x**

# Supported WAS Features #

The WAS Plugin supports the following features:

Concept                                   Remarks
--------                                  --------
EAR files                                 Deploy and undeploy EAR archives to WAS with support for resource references, security role user groups, jndi namespace bindings and virtual hosts.
WAR files                                 Deploy and undeploy WAR archives to WAS with support for resource references, security role user groups, jndi namespace bindings and virtual hosts.
EJB-Jar files                             Deploy and undeploy EJB-Jar archives to WAS with support for resource references, security role user groups and jndi namespace bindings.
Cluster                                   Create, Modify, Destroy and start/stop Clusters.
DataSource                                Create, Modify, Destroy Oracle and DB2 DataSources.
Was(Un)ManagedApacheHttpdServer           Create, Modify and Destroy WebServers, also allows exposing web applications (via mapping) through web servers.
WasSharedLibrary                          Create, Modif and Destroy shared libraries.
WasWmqQueueConnectionFactory              Create, Modif and Destroy WebSphere MQ Queue Connection Factories.
WasWmqTopicConnectionFactory              Create, Modif and Destroy WebSphere MQ Topic Connection Factories.
WasWmqQueue                               Create, Modif and Destroy WebSphere MQ Queue Connection Factories.
WasWmqTopic                               Create, Modif and Destroy WebSphere MQ Topic Connection Factories.

# WAS Runbook #

When the WAS runbook is triggered, the plugin populates the steplist with steps based on the executed task. First, the WAS runbook determines which servers are affected by the pending task. These are all the WAS servers that are a target of one of the deployed items in the deployment or the WAS server that a deployed application is running on in case of an undeploy. 

The WAS runbook adds steps in the following order:

* Undeploy all EAR/WAR/EJB-JAR files on servers, clusters and web servers.
* Synchronizes all nodes (if running against an ND installation).
* Destroys all Topic/Queues.
* Destroys all Connectiopn Factories.
* Destroys all JNDI properties
* Destroys all Shared Libraries.
* Deletes all Configuration Files.
* Copy configuration files to Host.
* Create/Modify Shared Libraries.
* Synchronize all nodes.
* Modify Clusters.
* Modify Servers.
* Copy and run SQL files against the database.
* Create JNDI properties.
* Create Datasource.
* Create all Connectiopn Factories.
* Create all Topic/Queues.
* Deploy all EAR/WAR/EJB-JAR files on servers, clusters and web servers.
* Start applications.
* Generate and propgate the web server plugin configuration.
* Copy static content to web servers.


# WAS Configuration Items (CIs) #

The WAS Plugin defines configuration items (CIs) needed to deploy to WAS middleware. To get more information about these CIs, use Deployit's command line interface (CLI). See the **Deployit Command Line Interface (CLI) Manual** for more information.

## WasCluster ##

A WebSphere cluster managed by a deployment manager (WAS ND)

_Type_: com.xebialabs.deployit.plugin.was.ci.WasCluster

_Properties:_

* **cell(com.xebialabs.deployit.plugin.was.ci.WasDeploymentManager)**: Deployment manager that manages this this cluster
* **name(STRING)**: Name of the WebSphere cluster, e.g. cluster1
* _servers(Set<com.xebialabs.deployit.plugin.was.ci.WasManagedServer>)_: Servers that are part of this cluster



## WasConfigurationToWasScopeMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasConfigurationToWasScopeMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _sourcePropertyOverrides(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Overrides for properties of the mapping's source. The key is the property name (consult the documentation or run 'describe' in the CLI), the value is the value to set. Only string, integer and enumerable properties can be overridden. Example: Key: redeliveryLimits, Value: 2



## WasDataSource ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasDataSource

_Properties:_

* **dataStoreHelperClass(STRING)**: DataStoreHelper implementation class that extends the capabilities of the JDBC driver. E.g. 'com.ibm.websphere.rsadapter.Oracle10gDataStoreHelper'
* **jndiName(STRING)**: JNDI name, used by applications to lookup the datasource.
* **name(STRING)**: Name of the datasource.
* **password(STRING)**: Password used to authenticate the username with the database instance.
* **provider(STRING)**: Name of the JDBC provider, used to create the datasource.
* **username(STRING)**: Username used to connect to the database instance.
* _databaseName(STRING)_: Database name, for non-Oracle datasources. Use together with properties 'databaseServerName', and 'databasePortNumber'.
* _databasePortNumber(INTEGER)_: Port number of the database, for non-Oracle datasources. Use together with properties 'databaseName', and 'databaseServerName'.
* _databaseServerName(STRING)_: Name or IP address of the server on which the database resides, for non-Oracle datasources. Use together with properties 'databaseName', and 'databasePortNumber'
* _statementCacheSize(INTEGER)_: The statement cache size sets the allocation of procedure cache memory and limits the amount of memory from the procedure cache pool used for cached statements.
* _url(STRING)_: DataBase Connection URL for Oracle datasources. E.g. 'jdbc:oracle:thin:@was-61:1521:orcl'. For non-Oracle datasources use the three properties 'databaseName', 'databaseServerName', and 'databasePortNumber'



## WasDefaultQueue ##

A queue in WebSphere's V5 default messaging provider

_Type_: com.xebialabs.deployit.plugin.was.ci.WasDefaultQueue

_Properties:_

* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name



## WasDefaultQueueConnectionFactory ##

A queue connection factory in WebSphere's V5 default messaging provider

_Type_: com.xebialabs.deployit.plugin.was.ci.WasDefaultQueueConnectionFactory

_Properties:_

* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name



## WasDeploymentManager ##

A WebSphere Application Server deployment manager (WAS ND)

_Type_: com.xebialabs.deployit.plugin.was.ci.WasDeploymentManager

_Properties:_

* **host(com.xebialabs.deployit.ci.Host)**: Host on which the WAS deployment manager runs
* **name(STRING)**: Name of the WebSphere cell, e.g. MyCell, WASCell, Cell01
* **version(ENUM)**: Version of WebSphere Application Server
    * Values: [WAS_61, WAS_70]
* **wasHome(STRING)**: Root path of the WebSphere deployment manager profile. e.g. /opt/ws/6.1/profiles/dmgr
* _password(STRING)_: Password which is used to login to the WebSphere deployment manager
* _port(INTEGER)_: TCP port which is used to login to the WebSphere deployment manager, default is 8879
* _username(STRING)_: Username which is used to login to the WebSphere deployment manager



## WasEarMapping ##

A mapping of an EAR to a WebSphere target

_Type_: com.xebialabs.deployit.plugin.was.ci.WasEarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _classLoaderMode(ENUM)_: Specifies the Classloader mode
    * Values: [PARENT_FIRST, PARENT_LAST]
* _classLoaderPolicy(ENUM)_: Specifies the Classloader policy
    * Values: [SINGLE, MULTIPLE]
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _securityRoleUserGroupMappings(List<com.xebialabs.deployit.plugin.was.ci.SecurityRoleUserGroupMappings>)_: Map Security role to users and groups used by EnterPrise Application
* _sharedLibraries(Set<com.xebialabs.deployit.plugin.was.ci.WasSharedLibrary>)_: Set of shared library which will used by the ear
* _startingWeight(INTEGER)_: Specifies the order in which applications are started. Lower values start earlier.
* _suffixArtifactNameWithTarget(BOOLEAN)_: If true, the artifact name will be suffixed with the name of the target.
* _virtualHost(STRING)_: Virtual Host
* _warClassLoaderMapping(List<com.xebialabs.deployit.plugin.was.ci.WasWarClassLoaderMapping>)_: Specifies the Class loader mode to WARs in EAR
* _warsWebserversVirtualHostMapping(List<com.xebialabs.deployit.plugin.was.ci.WarsWebserversVirtualHostMapping>)_: Map Wars to Webservers and Virtual hosts in EnterPrise Application
* _webservers(Set<com.xebialabs.deployit.plugin.was.ci.WasManagedApacheHttpdServer>)_: Set of webservers that expose the Eneterprise Application



## WasEjbJarMapping ##

A mapping of an EJB JAR to a WebSphere target

_Type_: com.xebialabs.deployit.plugin.was.ci.WasEjbJarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _mdbListenerPortJndiNameBindings(List<com.xebialabs.deployit.ci.mapping.MdbListenerPortBinding>)_: Bindings of message driven beans JNDI names to the corresponding listener ports present on the target middleware
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _sharedLibraries(Set<com.xebialabs.deployit.plugin.was.ci.WasSharedLibrary>)_: Set of shared library which will used by the ejb
* _startingWeight(INTEGER)_: Specifies the order in which applications are started. Lower values start earlier.



## WasJndiProperties ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasJndiProperties

_Properties:_

* _stringNameSpaceBindings(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key/value pairs that are to stored in the WebSphere JNDI tree



## WasJndiPropertiesToWasScopeMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasJndiPropertiesToWasScopeMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Values for placeholders in the WasJndiProperties that are to be replaced. The key is the placeholder name. Example: Key: DATABASE_USER, Value: testUser



## WasManagedApacheHttpdServer ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasManagedApacheHttpdServer

_Properties:_

* **accessLogLocation(STRING)**: Location where deployit will create a directory where access log will be placed.
* **apachectlPath(STRING)**: Path of the executable that will restart apache, e.g. /usr/sbin/apachectl
* **configurationLocation(STRING)**: Location where deployit will generate apache httpd.conf fragment files.
* **errorLogLocation(STRING)**: Location where deployit will create a directory where error log will be placed.
* **host(com.xebialabs.deployit.ci.Host)**: Host on which the web server runs
* **htdocsLocation(STRING)**: Location where deployit will create a directory (based on the vhost name) where static content will be placed.
* **name(STRING)**: Name
* **node(com.xebialabs.deployit.plugin.was.ci.WasNode)**: The WAS node on which Apache is installed.
* **pluginInstallationDirPath(STRING)**: The directory where the WebSphere plugin for Apache has been installed.
* **port(INTEGER)**: The port where the Apache HTTPD server is running on. e.g. 80, 443
* **webServerVendorType(ENUM)**: The Web server vendor type.
    * Values: [APACHE, IHS]
* _modules(Set<com.xebialabs.deployit.plugin.apache.httpd.ci.ApacheModule>)_: Modules
* _pluginConfigurationPath(STRING)_: The path of the WebSphere plugin configuration file. Defaults to <pluginInstallationDirPath>/config/<webservername>/plugin-cfg.xml



## WasManagedServer ##

A WebSphere server managed by a node that is part of a deployment manager (WAS ND)

_Type_: com.xebialabs.deployit.plugin.was.ci.WasManagedServer

_Properties:_

* **name(STRING)**: Name of the WebSphere server, e.g. server1
* _applicationClassLoaderPolicyAndMode(ENUM)_: Server-wide application classloader policy and mode
    * Values: [DEFAULT, MULTIPLE, SINGLE_PARENT_FIRST, SINGLE_PARENT_LAST]
* _bootClasspath(STRING)_: Boot classpath for this server.
* _classpath(STRING)_: Classpath for this server.
* _cookieDomain(STRING)_: Session cookie domain
* _cookieName(STRING)_: Session cookie name
* _cookiePath(STRING)_: Session cookie path
* _disableJit(BOOLEAN)_: Disable just-in-time compiler.
* _enableSessionCookies(BOOLEAN)_: Enable session cookies
* _environmentEntries(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Environment entries
* _initHeapSize(INTEGER)_: Initial heap size to be allocated to the JVM (in megabytes).
* _jvmArguments(STRING)_: Generic JVM arguments.
* _jvmStdErr(STRING)_: Path to the JVM stderr log file. Example; /data/waslogs/jvm_stderr.log
* _jvmStdOut(STRING)_: Path to the JVM stdout log file. Example; /data/waslogs/jvm_stdout.log
* _maxHeapSize(INTEGER)_: Maximum heap size to be allocated to the JVM (in megabytes).
* _maximumSessionsInMemory(INTEGER)_: Maximum # of HTTP sessions in memory
* _node(com.xebialabs.deployit.plugin.was.ci.WasNodeAgent)_: Node on which the server runs
* _servletCaching(BOOLEAN)_: Enable servlet caching
* _sessionTimeout(INTEGER)_: HTTP session timeout in minutes
* _stdErr(STRING)_: Path to the stderr log file. Example; /data/waslogs/stderr.log
* _stdOut(STRING)_: Path to the stdout log file. Example; /data/waslogs/stdout.log
* _umask(STRING)_: Umask of started process.
* _workingDir(STRING)_: Working directory of started process.



## WasNodeAgent ##

A WebSphere node agent.

_Type_: com.xebialabs.deployit.plugin.was.ci.WasNodeAgent

_Properties:_

* **cell(com.xebialabs.deployit.plugin.was.ci.WasDeploymentManager)**: Deployment manager that manages this node agent
* **name(STRING)**: Name of the WebSphere node in the WebSphere cell, e.g. MyNode, Node01



## WasResourceMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasResourceMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _sourcePropertyOverrides(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Overrides for properties of the mapping's source. The key is the property name (consult the documentation or run 'describe' in the CLI), the value is the value to set. Only string, integer and enumerable properties can be overridden. Example: Key: redeliveryLimits, Value: 2



## WasSharedLibrary ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasSharedLibrary

_Properties:_

* **name(STRING)**: Name of the shared library so it can be used by reference in an Application
* _classPath(STRING)_: classpath of the shared library, e.g. /var/shared/log4j.jar;/var/shared/lib/ora/ojdbc14.jar
* _configurationFiles(Set<com.xebialabs.deployit.ci.artifact.ConfigurationFiles>)_: The set of configuration files that are part of this shared library
* _libraries(Set<com.xebialabs.deployit.ci.artifact.Libraries>)_: The set of libraries that are part of this shared library



## WasSharedLibraryToWasScopeTargetMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasSharedLibraryToWasScopeTargetMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Values for placeholders in the deployable artifact that are to be replaced. The key is the placeholder name. Example: Key: DATABASE_USER, Value: testUser



## WasSibJmsActivationSpec ##

An activation specification in WebSphere's Default messaging provider

_Type_: com.xebialabs.deployit.plugin.was.ci.WasSibJmsActivationSpec

_Properties:_

* **destination(com.xebialabs.deployit.plugin.was.ci.WasSibJmsTarget)**: The SIB JMS Destination the Activation Specification should listen on
* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name



## WasSibJmsQueue ##

A queue in WebSphere's Default messaging provider

_Type_: com.xebialabs.deployit.plugin.was.ci.WasSibJmsQueue

_Properties:_

* **busName(STRING)**: The name of the Service Integration Bus in which a destination should be created
* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name
* **queueName(STRING)**: The name of the Service Integration Bus destination for this queue



## WasSibJmsQueueConnectionFactory ##

A queue connection factory in WebSphere's Default messaging provider

_Type_: com.xebialabs.deployit.plugin.was.ci.WasSibJmsQueueConnectionFactory

_Properties:_

* **busName(STRING)**: Bus Name
* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name



## WasSibJmsTopic ##

A topic in WebSphere's Default messaging provider

_Type_: com.xebialabs.deployit.plugin.was.ci.WasSibJmsTopic

_Properties:_

* **busName(STRING)**: The name of the Service Integration Bus in which a destination should be created
* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name
* **topicName(STRING)**: The name of the Service Integration Bus destination for this topic



## WasSibJmsTopicConnectionFactory ##

A topic connection factory in WebSphere's Default messaging provider

_Type_: com.xebialabs.deployit.plugin.was.ci.WasSibJmsTopicConnectionFactory

_Properties:_

* **busName(STRING)**: Bus Name
* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name



## WasUnManagedApacheHttpdServer ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasUnManagedApacheHttpdServer

_Properties:_

* **accessLogLocation(STRING)**: Location where deployit will create a directory where access log will be placed.
* **apachectlPath(STRING)**: Path of the executable that will restart apache, e.g. /usr/sbin/apachectl
* **configurationLocation(STRING)**: Location where deployit will generate apache httpd.conf fragment files.
* **errorLogLocation(STRING)**: Location where deployit will create a directory where error log will be placed.
* **host(com.xebialabs.deployit.ci.Host)**: Host on which the web server runs
* **htdocsLocation(STRING)**: Location where deployit will create a directory (based on the vhost name) where static content will be placed.
* **name(STRING)**: Name
* **node(com.xebialabs.deployit.plugin.was.ci.WasNode)**: The WAS node on which Apache is installed.
* **pluginInstallationDirPath(STRING)**: The directory where the WebSphere plugin for Apache has been installed.
* **port(INTEGER)**: The port where the Apache HTTPD server is running on. e.g. 80, 443
* **webServerVendorType(ENUM)**: The Web server vendor type.
    * Values: [APACHE, IHS]
* _modules(Set<com.xebialabs.deployit.plugin.apache.httpd.ci.ApacheModule>)_: Modules
* _pluginConfigurationPath(STRING)_: The path of the WebSphere plugin configuration file. Defaults to <pluginInstallationDirPath>/config/<webservername>/plugin-cfg.xml



## WasUnmanagedServer ##

An unmanaged WebSphere Applicaton Server (WAS Base/SA)

_Type_: com.xebialabs.deployit.plugin.was.ci.WasUnmanagedServer

_Properties:_

* **cellName(STRING)**: Name of the WebSphere cell, e.g. MyCell, WASCell, Cell01
* **host(com.xebialabs.deployit.ci.Host)**: Host on which the unmanaged WAS server runs
* **name(STRING)**: Name of the WebSphere server, e.g. server1
* **nodeName(STRING)**: Name of the WebSphere node
* **version(ENUM)**: Version of WebSphere Application Server.
    * Values: [WAS_61, WAS_70]
* **wasHome(STRING)**: Root path of the WebSphere installation path. e.g. /opt/ws/6.1/appserver/profiles/AppSrv01
* _applicationClassLoaderPolicyAndMode(ENUM)_: Server-wide application classloader policy and mode
    * Values: [DEFAULT, MULTIPLE, SINGLE_PARENT_FIRST, SINGLE_PARENT_LAST]
* _bootClasspath(STRING)_: Boot classpath for this server.
* _classpath(STRING)_: Classpath for this server.
* _cookieDomain(STRING)_: Session cookie domain
* _cookieName(STRING)_: Session cookie name
* _cookiePath(STRING)_: Session cookie path
* _disableJit(BOOLEAN)_: Disable just-in-time compiler.
* _enableSessionCookies(BOOLEAN)_: Enable session cookies
* _environmentEntries(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Environment entries
* _initHeapSize(INTEGER)_: Initial heap size to be allocated to the JVM (in megabytes).
* _jvmArguments(STRING)_: Generic JVM arguments.
* _jvmStdErr(STRING)_: Path to the JVM stderr log file. Example; /data/waslogs/jvm_stderr.log
* _jvmStdOut(STRING)_: Path to the JVM stdout log file. Example; /data/waslogs/jvm_stdout.log
* _maxHeapSize(INTEGER)_: Maximum heap size to be allocated to the JVM (in megabytes).
* _maximumSessionsInMemory(INTEGER)_: Maximum # of HTTP sessions in memory
* _password(STRING)_: Password which is used to login to the WebSphere Administration.
* _port(INTEGER)_: TCP port which is used to login to the WebSphere Administration, default is 8880
* _resourceEnvironmentJndiNames(Set<String>)_: Resource environment jndi names
* _servletCaching(BOOLEAN)_: Enable servlet caching
* _sessionTimeout(INTEGER)_: HTTP session timeout in minutes
* _stdErr(STRING)_: Path to the stderr log file. Example; /data/waslogs/stderr.log
* _stdOut(STRING)_: Path to the stdout log file. Example; /data/waslogs/stdout.log
* _umask(STRING)_: Umask of started process.
* _username(STRING)_: Username which is used to login to the WebSphere Administration.
* _workingDir(STRING)_: Working directory of started process.



## WasWarClassLoaderMapping ##

A mapping of an EAR to a WebSphere target

_Type_: com.xebialabs.deployit.plugin.was.ci.WasWarClassLoaderMapping

_Properties:_

* _classLoaderMode(ENUM)_: Class Loader Mode
    * Values: [PARENT_FIRST, PARENT_LAST]
* _warName(STRING)_: War Name



## WasWarMapping ##

A mapping of a WAR to WebSphere middleware

_Type_: com.xebialabs.deployit.plugin.was.ci.WasWarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _classLoaderMode(ENUM)_: Specifies the Classloader mode
    * Values: [PARENT_FIRST, PARENT_LAST]
* _contextRoot(STRING)_: Context root to deploy to
* _ejbReferences(List<com.xebialabs.deployit.ci.mapping.EjbReference>)_: Specifies the mapping from ejb reference jndi names and locals used in the web.xml to bean jndi names available in middleware
* _fileServing(ENUM)_: Set File Serving enabled to WAR
    * Values: [DO_NOT_OVERRIDE, FALSE, TRUE]
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _resourceEnvironmentEntryReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource environment references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _resourceReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _securityRoleUserGroupMappings(List<com.xebialabs.deployit.plugin.was.ci.SecurityRoleUserGroupMappings>)_: Map Security role to users and groups used by EnterPrise Application
* _sharedLibraries(Set<com.xebialabs.deployit.plugin.was.ci.WasSharedLibrary>)_: Set of shared library which will used by the war
* _startingWeight(INTEGER)_: Specifies the order in which applications are started. Lower values start earlier.
* _suffixArtifactNameWithTarget(BOOLEAN)_: If true, the artifact name will be suffixed with the name of the target.
* _virtualHost(STRING)_: Virtual host to deploy to
* _webservers(Set<com.xebialabs.deployit.plugin.was.ci.WasManagedApacheHttpdServer>)_: Set of webservers that expose the Eneterprise Application



## WasWmqQueue ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasWmqQueue

_Properties:_

* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name
* _baseQueueName(STRING)_: Base Queue Name



## WasWmqQueueConnectionFactory ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasWmqQueueConnectionFactory

_Properties:_

* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name
* _channel(STRING)_: Channel
* _queueManagerHost(com.xebialabs.deployit.ci.Host)_: Queue Manager Host
* _queueManagerName(STRING)_: Queue Manager Name
* _queueManagerPort(INTEGER)_: Queue Manager Port



## WasWmqTopic ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasWmqTopic

_Properties:_

* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name
* _baseTopicName(STRING)_: Base Topic Name



## WasWmqTopicConnectionFactory ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.was.ci.WasWmqTopicConnectionFactory

_Properties:_

* **jndiName(STRING)**: JNDI name
* **name(STRING)**: WebSphere name
* _channel(STRING)_: Channel
* _queueManagerHost(com.xebialabs.deployit.ci.Host)_: Queue Manager Host
* _queueManagerName(STRING)_: Queue Manager Name
* _queueManagerPort(INTEGER)_: Queue Manager Port


