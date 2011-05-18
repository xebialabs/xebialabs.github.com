---
layout: default
title: Deployit Tomcat Plugin Manual
---

# Preface #

This manual describes the Deployit Tomcat Plugin.

# Introduction #

The Tomcat Plugin supports the deployment, re-deployment and undeployment of a deployment package to a Tomcat servlet container.

# Tomcat Plugin Requirements #

In addition to the requirements for Deployit, the Tomcat Plugin has the following additional requirements:

* the user account used to access the Tomcat server must have permission to perform the following actions:
	* write to the Tomcat context file.
	* run the Tomcat start / stop script (e.g. `catalina.sh`)

# Supported Tomcat Versions #

The Tomcat plugin supports the following versions of Tomcat:

* **5.5.x**
* **6.0.x**

# Supported Tomcat Features #

The Tomcat Plugin supports the following features:

Concept                                 | Remarks
--------                                | --------
WAR files                               | Deploy and undeploy WAR archives to Tomcat.
Context files                           | Deploy and undeploy folders containing context files.
ActiveMQ connection factory             | Deploy and undeploy ActiveMQ connection factories.
Datasources                             | Deploy and undeploy datasources to Tomcat.
JNDI Resources                          | Deploy and undeploy resources in the Tomcat JNDI tree.
Libraries                               | Deploy and undeploy Java libraries to Tomcat.
Tomcat Managed Server                   | Deploy and undeploy to Tomcat servers using the Tomcat manager app.
Tomcat Unmanaged Server                 | Deploy and undeploy to Tomcat servers without the Tomcat manager app.

# Tomcat Runbook #

When the Tomcat runbook is triggered, the plugin populates the steplist with steps based on the executed task. First, the Tomcat runbook determines which servers are affected by the pending task. These are all the Tomcat servers that are a target of one of the deployed items in the deployment or the Tomcat server that a deployed application is running on in case of an undeploy. 

The Tomcat runbook adds steps in the following order:

* Stop all servers affected by the deployment.
* Undeploy removed datasources from the Tomcat server.
* Undeploy removed wars from the Tomcat server.
* Undeploy removed libraries from the host.
* Undeploy removed configuration files from the host.
* Deploy SQL folders and scripts to the host.
* Deploy added libraries on the host.
* Deploy added configuration files on the host.
* Deploy added datasources to the Tomcat server.
* Deploy added wars to the Tomcat server.
* Start all affected servers.
* Deploy wars to managed Tomcat servers.

# Tomcat Configuration Items (CIs) #

The Tomcat Plugin defines configuration items (CIs) needed to deploy to Tomcat middleware. To get more information about these CIs, use Deployit's command line interface (CLI). See the **Deployit Command Line Interface (CLI) Manual** for more information.

## ContextFiles ##

Folder in the Deployment Package containing Tomcat context files

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.ContextFiles

_Properties:_

* **location(STRING)**: Location of the artifact.
* **name(STRING)**: The technical name of the artifact as it will be used within application servers.



## ContextFilesMapping ##

A mapping of a ContextFiles CI to a TomcatServer

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.ContextFilesMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]



## TomcatActiveMQConnectionFactory ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatActiveMQConnectionFactory

_Properties:_

* _brokerName(STRING)_: Broker Name
* _brokerURL(STRING)_: Broker URL
* _factory(STRING)_: Factory
* _jndiName(STRING)_: Jndi Name



## TomcatConfigurationFilesMapping ##

A mapping of Configuration Files  CI to a TomcatServer

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatConfigurationFilesMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* **targetDirectory(STRING)**: The directory on the target host to which the configuration is to be copied. Example: /data/petclinic/1.0/conf. It can be overidden by using Key TARGET_DIRECTORY
* _createIfNotExist(BOOLEAN)_: create the target directory and sub directory if they are not exist
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _shared(BOOLEAN)_: The target directory is shared when another resources using it as well, default true.



## TomcatDataSource ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatDataSource

_Properties:_

* _accessToUnderlyingConnectionAllowed(BOOLEAN)_: Controls if the PoolGuard allows access to the underlying connection, default value is false
* _connectionInitSqls(STRING)_: A Collection of SQL statements that will be used to initialize physical connections when they are first created, default value is null
* _connectionProperties(STRING)_: The connection properties that will be sent to our JDBC driver when establishing new connections
* _connectionUrl(STRING)_: The connection URL to be passed to our JDBC driver to establish a connection
* _defaultAutoCommit(BOOLEAN)_: The default auto-commit state of connections created by this pool, default value is true
* _defaultCatalog(STRING)_: The default catalog of connections created by this pool
* _defaultReadOnly(STRING)_: The default read-only state of connections created by this pool, default value is driver default
* _driverClass(STRING)_: The fully qualified Java class name of the JDBC driver to be used
* _initialSize(INTEGER)_: The initial number of connections that are created when the pool is started, default value is 0
* _jndiName(STRING)_: Jndi Name
* _logAbandoned(BOOLEAN)_: Flag to log stack traces for application code which abandoned a Statement or Connection, default value is false
* _maxActive(INTEGER)_: The maximum number of active connections that can be allocated from this pool at the same time, or negative for no limit, default value is 8
* _maxIdle(INTEGER)_: The maximum number of connections that can remain idle in the pool, without extra ones being released, or negative for no limit, default value is 8
* _maxOpenPreparedStatements(INTEGER)_: The maximum number of open statements that can be allocated from  the statement pool at the same time, or zero for no limit, default value is unlimited
* _maxWait(INTEGER)_: The maximum number of milliseconds that the pool will wait (when thereare no available connections) for a connection to be returned before throwing an exception, or -1 to wait indefinitely, default value is indefinitely
* _minEvictableIdleTimeMillis(INTEGER)_: The minimum amount of time an object may sit idle in the pool before it is eligable for eviction by the idle object evictor (if any), default value is 1000 * 60 * 30
* _minIdle(INTEGER)_: The minimum number of connections that can remain idle in the pool, without extra ones being created, or zero to create none, default value is 0
* _numTestsPerEvictionRun(INTEGER)_: The number of objects to examine during each run of the idle object evictor thread (if any), default value is 3
* _password(STRING)_: The connection password to be passed to our JDBC driver to establish a connection
* _poolPreparedStatements(BOOLEAN)_: Enable prepared statement pooling for this pool, default value is false
* _removeAbandoned(BOOLEAN)_: Flag to remove abandoned connections if they exceed the removeAbandonedTimout, default value is false
* _removeAbandonedTimeout(INTEGER)_: Timeout in seconds before an abandoned connection can be removed, default value is 300
* _testOnBorrow(BOOLEAN)_: The indication of whether objects will be validated before being borrowed from the pool, default value is true
* _testOnReturn(BOOLEAN)_: The indication of whether objects will be validated before being returned to the pool, default value is false
* _testWhileIdle(BOOLEAN)_: The indication of whether objects will be validated by the idle object  evictor (if any), default value is false
* _timeBetweenEvictionRunsMillis(INTEGER)_: The number of milliseconds to sleep between runs of the idle object evictor thread, default value is -1
* _username(STRING)_: The connection username to be passed to our JDBC driver to establish a connection
* _validationQuery(STRING)_: The SQL query that will be used to validate connections from this pool before returning them to the caller



## TomcatJNDIResources ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatJNDIResources

_Properties:_

* _resourceLinks(List<com.xebialabs.deployit.plugin.tomcat.ci.ResourceLink>)_: Resources links that are to stored in the Tomcat JNDI tree



## TomcatJNDIResourcesMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatJNDIResourcesMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _resourceLinks(List<com.xebialabs.deployit.plugin.tomcat.ci.ResourceLink>)_: Resources links that are to stored in the Tomcat JNDI tree



## TomcatLibrariesMapping ##

A mapping of Librairies Files  CI to a TomcatServer

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatLibrariesMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* **targetDirectory(STRING)**: The directory on the target host to which the configuration is to be copied. Example: /data/petclinic/1.0/conf. It can be overidden by using Key TARGET_DIRECTORY
* _createIfNotExist(BOOLEAN)_: create the target directory and sub directory if they are not exist
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _shared(BOOLEAN)_: The target directory is shared when another resources using it as well, default true.



## TomcatManagedServer ##

Tomcat Server instance

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatManagedServer

_Properties:_

* **host(com.xebialabs.deployit.ci.Host)**: Host on which the Tomcat server is running.
* **managerAppUrl(STRING)**: URL of the manager app URL, e.g. http://tomcat-6:8080/manager
* **managerPassword(STRING)**: Password to be used for the manager application deployed on tomcat
* **managerUsername(STRING)**: Username to be used for the manager application deployed on tomcat
* **tomcatHome(STRING)**: Place where Tomcat is installed such as /opt/apache-tomcat-6.0.24.
* _ajpPort(INTEGER)_: AJP Port for the Tomcat Server, default is 8009
* _appBase(STRING)_: Tomcat appBase, ex webapps
* _service(STRING)_: Tomcat service, ex Catalina



## TomcatResourceMapping ##

Description unavailable

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatResourceMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _sourcePropertyOverrides(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Overrides for properties of the mapping's source. The key is the property name (consult the documentation or run 'describe' in the CLI), the value is the value to set. Only string, integer and enumerable properties can be overridden. Example: Key: redeliveryLimits, Value: 2



## TomcatUnmanagedServer ##

Tomcat Server instance

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatUnmanagedServer

_Properties:_

* **baseUrl(STRING)**: The base URL which will be used to check whether server is running, e.g. http://tomcat-6:8080
* **host(com.xebialabs.deployit.ci.Host)**: Host on which the Tomcat server is running.
* **startCommand(STRING)**: Command that should be executed to start the Tomcat server, e.g./opt/tomcat/bin/catalina.sh start.
* **stopCommand(STRING)**: Command that should be executed to stop the Tomcat server, e.g. /opt/tomat/bin/catalina.sh stop
* **tomcatHome(STRING)**: Place where Tomcat is installed such as /opt/apache-tomcat-6.0.24.
* _ajpPort(INTEGER)_: AJP Port for the Tomcat Server, default is 8009
* _appBase(STRING)_: Tomcat appBase, ex webapps
* _service(STRING)_: Tomcat service, ex Catalina



## TomcatWarMapping ##

A mapping of a WAR to a Tomcat server

_Type_: com.xebialabs.deployit.plugin.tomcat.ci.TomcatWarMapping

_Properties:_

* **source(java.io.Serializable)**: Source
* **target(java.io.Serializable)**: Target
* _appBase(STRING)_: aaabsolute path of the directory where wars are deployed. Only needed when context path specified in the mapping is different from the war name
* _contextRoot(STRING)_: Context root to deploy to
* _ejbReferences(List<com.xebialabs.deployit.ci.mapping.EjbReference>)_: Specifies the mapping from ejb reference jndi names and locals used in the web.xml to bean jndi names available in middleware
* _exploded(BOOLEAN)_: Explode the war file on tomcat server (does not work when using the Tomcat manager).
* _keyValuePairs(List<com.xebialabs.deployit.ci.mapping.KeyValuePair>)_: Key Value Pairs
* _placeholderFormat(ENUM)_: Placeholder Format
    * Values: [SPRING, WINDOWS_SHELL, STARS, NONE]
* _resourceEnvironmentEntryReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource environment references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _resourceReferences(List<com.xebialabs.deployit.ci.mapping.ResourceReference>)_: Specifies the mapping from resource references jndi names and types used in the web.xml to resource references jndi names available in middleware
* _virtualHost(STRING)_: Virtual host to deploy to


