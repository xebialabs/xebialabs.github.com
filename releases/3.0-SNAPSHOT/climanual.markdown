---
layout: default
title: Deployit Command Line Interface (CLI) Manual
---

# Preface #

This manual describes how to use the Deployit CLI.

The Deployit server must be running before accessing the CLI. See the **Deployit System Administrator Manual** for more information.

See **Deployit Reference Manual** for background information on Deployit and deployment concepts.

# Starting and Stopping #

To start the CLI, open a terminal window, change directory to the location of the CLI and enter the command:

	./cli.sh

The CLI will start, prompting the user for a username and password and attempting to connect to the Deployit server on `localhost` running on it's standard port of `4516`.

By starting the CLI with the `-h` flag, a message is printed that shows the possible options it supports:

	java -jar deployit-cli-<version>.jar [options...] arguments...
		-configuration VAL : Specify the location of the configuration file (deployit.conf)
		-f (-source) VAL   : Execute a specified python source file (Optional)
		-host VAL          : Connect to a specified host, defaults to 127.0.0.1 (Optional)
		-password VAL      : Connect with the specified password (Optional)
		-port N            : Connect to a specified port, defaults to 4516 (Optional)
		-username VAL      : Connect as the specified user (Optional)

The options are:

* `-configuration /path/to/config/file` -- this option is used to pass the location of the Deployit configuration file. The default location for the configuration file is `conf/deployit.conf` in the Deployit installation directory.
* `-f /path/to/Python/script` -- starts the CLI in batch mode and instruct it to execute the specified script. Once the script completes, the CLI will terminate.
* `-source /path/to/Python/script` -- alternative for the `-f` option.
* `-host myhost.domain.com` -- specifies the host to connect to. The default host is `127.0.0.1`.
* `-password mypassword` -- specifies the password on the command line. If the password is not specified, the CLI will enter interactive mode and prompt the user.
* `-port 1234` -- specifies the port at which to connect to the server. If the port is not specified, the CLI will use default port `4516`.
* `-username myusername` -- specifies the username on the command line. If the username is not specified, the CLI will enter interactive mode and prompt the user.

# Logging in and Logging out #

When the CLI has obtained the username and password to use (either from the command line or interactively), it will attempt to contact the server at the specified (or default) address and port. If this is not successful, a stacktrace will be printed and the CLI will terminate. If the CLI is run in interactive mode and the login is successful, the CLI will display a welcome message.

# Help #

Help is available in the CLI by issuing CLI commands. The following message is shown when first logging in and describes the available options:

	Welcome to the Deployit Jython CLI!
	Use the 'deployit' object to interact with the Deployit server.
	
	Deployit Objects available on the CLI
	To know more about a specific object, type <objectname>.help()
	To get to know more about a specific method of an object, type <objectname>.help("<methodname>")
		
	repository: Gateway to doing CRUD operations on all types of CIs
	factory: Helper that can construct archetypes, CIs and artifacts
	deployit: The main gateway to interfacing with Deployit.
	security: Access to the security settings of Deployit.

# Objects #

## Deployit ##

The `deployit` helper object provides access to the main functions of the Deployit application. The CLI itself provides help information about the object:

	deployit > deployit.help()
	deployit: The main gateway to interfacing with Deployit.
	
	The methods available are:
	deployit.print(RepositoryObject ci) : void
	deployit.importPackage(String importablePackage) : RepositoryObject
	deployit.realityCheck(String id) : RepositoryObject
	deployit.deployAndWait(String source, String target) : String
	deployit.deployAndWait(String source, String target, RepositoryObject[] mappings) : String
	deployit.deploy(String source, String target) : String
	deployit.deploy(String source, String target, RepositoryObject[] mappings) : String
	deployit.prepareDeployment(String source, String target) : String
	deployit.prepareDeployment(String source, String target, RepositoryObject[] mappings) : String
	deployit.retrieveTaskInfo(String taskId) : TaskInfo
	deployit.stopTask(String taskId) : void
	deployit.startTask(String taskId) : void
	deployit.abortTask(String taskId) : void
	deployit.cancelTask(String taskId) : void
	deployit.skipSteps(String taskId, Integer[] stepIds) : void
	deployit.describe(String shortName) : void

### print ###

**Purpose**

This method produces an easy-to-read, hierarchical pretty-print of a CI, it's properties and it's relationships. The input to the method is a CI as returned by the `repository` helper object.

**Usage**

	deployit > deployit.help("print") 
	deployit.print(RepositoryObject ci) : void
	Print a tree-view of a CI
	Returns: void - void
	
	ci: The CI to print

**Example**

	deployit > deployit.print(repository.read('Environments/Test-WAS'))
	com.xebialabs.deployit.ci.Environment
	+-- id: Environments/Test-WAS
	+-- lastModified: 2011-01-12 12:01:40.659
	\-- values
    	\-- members
        	+-- com.xebialabs.deployit.ci.Host
        	|   +-- id: Infrastructure/T-Host at was-61
        	|   +-- lastModified: 2011-01-12 12:01:40.417
        	|   \-- values
        	|       \-- address: was-61
        	+-- com.xebialabs.deployit.plugin.was.ci.WasCluster
        	|   +-- id: Infrastructure/T-was-61/T-was-61-demo-cluster
        	|   +-- lastModified: 2011-01-12 12:01:40.579
        	|   \-- values
        	|       +-- servers
        	|       |   \-- com.xebialabs.deployit.plugin.was.ci.WasManagedServer
        	|       |       +-- id: Infrastructure/T-was-61/T-was-61-appserver-node
        	|       |       +-- lastModified: 2011-01-12 12:01:40.538
        	|       |       \-- values
        	|       |           +-- initHeapSize: 512
        	|       |           +-- stdErr: ${SERVER_LOG_ROOT}/native_stderr.log
        	|       |           +-- node: com.xebialabs.deployit.plugin.was.ci.WasNodeAgent
        	|       |           |   +-- id: Infrastructure/T-was-61/T-was-61-appserver-node
        	|       |           |   +-- lastModified: 2011-01-12 12:01:40.489
        	|       |           |   \-- values
        	|       |           |       +-- name: was-61-appserver-node
        	|       |           |       \-- cell: com.xebialabs.deployit.plugin.was.ci.WasDeploymentManager
        	|       |           |           +-- id: Infrastructure/T-was-61
        	|       |           |           +-- lastModified: 2011-01-12 12:01:40.452
        	|       |           |           \-- values
        	|       |           |               +-- host: com.xebialabs.deployit.ci.Host
        	|       |           |               |   +-- id: Infrastructure/T-Host at was-61
        	|       |           |               |   +-- lastModified: 2011-01-12 12:01:40.417
        	|       |           |               |   \-- values
        	|       |           |               |       \-- address: was-61
        	|       |           |               \-- name: was-61
			...
			...

### importPackage ###

**Purpose**

This method imports a package with the given name into Deployit. The package must already be present in the server's import directory (see **Deployit System Administration Manual**).

**Usage**

	deployit > deployit.help("importPackage")
	deployit.importPackage(String importablePackage) : RepositoryObject
	Import a package located on the server or local file system.
	Returns: RepositoryObject - void
	
	importablePackage: This is either:
		- The name of the importable package on the server
		- The absolute path to a local importable package.

**Return Value**

This method returns the CI representing the imported package.

**Example**

	deployit > deployit.print(deployit.importPackage('AnimalZoo-1.0.dar'))
	com.xebialabs.deployit.ci.DeploymentPackage
	+-- id: Applications/AnimalZoo/1.0
	+-- lastModified: 2011-01-25 10:01:19.092
	\-- values
    	+-- application: com.xebialabs.deployit.ci.Application
    	|   +-- id: Applications/AnimalZoo
    	|   +-- lastModified: 2011-01-25 10:01:16.949
    	|   \-- values
    	+-- deployableArtifacts
    	|   \-- com.xebialabs.deployit.ci.artifact.Ear
    	|       +-- id: Applications/AnimalZoo/1.0/PetClinic
    	|       +-- lastModified: 2011-01-25 10:01:19.435
    	|       \-- values
    	|           \-- name: PetClinic
    	\-- version: 1.0

### realityCheck ###

**Purpose**

This method performs a reality check on the middleware specified. The middleware CI as stored in Deployit is compared with the middleware in reality and an updated CI is returned. A reality check can be performed on the following types of CIs:

xxx which types of CI's can you pass into this method??? xxx

**Usage**

	deployit > deployit.help("realityCheck")                              
	deployit.realityCheck(String id) : RepositoryObject
	Do a reality check on the middleware specified by the id. The updated values are returned 
		and should be manually stored.
	Returns: RepositoryObject - The updated (but not persisted) repository object.
	
	id: The id of the discoverable middleware component

**Return Value**

This method returns the CI representing the updated and unpersisted  middleware CI.

**Example**

First, print the values of the current middleware CI:

	deployit > deployit.print(repository.read('Infrastructure/A-jboss-Host at jboss-51/A-jboss-51-1'))      
	com.xebialabs.deployit.plugin.jbossas.ci.JbossasServer
	+-- id: Infrastructure/A-jboss-Host at jboss-51/A-jboss-51-1
	+-- lastModified: 2011-01-12 12:01:40.729
	\-- values
    	+-- home: /opt/jboss/5.1.0.GA
    	+-- host: com.xebialabs.deployit.ci.Host
    	|   +-- id: Infrastructure/A-jboss-Host at jboss-51
    	|   +-- lastModified: 2011-01-12 12:01:40.697
    	|   \-- values
    	|       \-- address: jboss-51
    	+-- name: default
    	\-- version: JBOSSAS_50

Executing a reality check results in the following CI:

	deployit > deployit.print(deployit.realityCheck('Infrastructure/A-jboss-Host at jboss-51/A-jboss-51-1'))
	com.xebialabs.deployit.plugin.jbossas.ci.JbossasServer
	+-- id: Infrastructure/A-jboss-Host at jboss-51/A-jboss-51-1
	+-- lastModified
	\-- values
    	+-- deploymentCompletionWaitTime: 10000
    	+-- home: /opt/jboss/5.1.0.GA
    	+-- host: com.xebialabs.deployit.ci.Host
    	|   +-- id: Infrastructure/A-jboss-Host at jboss-51
    	|   +-- lastModified: 2011-01-12 12:01:40.697
    	|   \-- values
    	|       \-- address: jboss-51
    	+-- controlPort: 1099
    	+-- name: default
    	+-- ajpPort: 8009
    	+-- strategy: RESTART
    	\-- version: JBOSSAS_50

### deployAndWait ###

**Purpose**

This method performs a synchronous deployment, that is, it starts a deployment and waits until it is finished before returning control to the CLI. There are several forms of this method, one that xxx complete xxx

**Usage**

	deployit > deployit.help("deployAndWait")
	deployit.deployAndWait(String source, String target) : String
	Deploy or upgrade a deployment-package on the targeted environment using default mappings,
		and wait for it to be completed.
	Returns: String - The id of the task that was executed
	
	source: The source deployment-package that is to be deployed
	target: Can either be:
		- The target environment to which you want to deploy
		- The existing deployment that needs to be upgraded
		
	deployit.deployAndWait(String source, String target, RepositoryObject[] mappings) : String
	Deploy or upgrade a deployment-package on the targeted environment using the mappings specified,
		and wait for it to be completed.
	Returns: String - The id of the task that was executed
		
	source: The source deployment-package that is to be deployed
	target: Can either be:
		- The target environment to which you want to deploy
		- The existing deployment that needs to be upgraded
	mappings: The mappings to use for the deployment, if no mappings are specified, default mappings
		will be used.

**Return Value**

This method returns the id of the deployment task that was executed.

**Example**

xxx make an example xxx

## Repository ##



## Factory ##



## Security ##



# Performing Common Tasks #

This section describes common tasks you can perform with the CLI.

## Deploying an Application ##



## Working with Archetypes ##



## Discovering CIs ##

	discoveredCIs = deployit.discover(...)

xxx not yet implemented xxx

## Adding CIs to Environments ##

Middleware that is used as a deployment target must be grouped together in an environment. Environments are CIs and like all CIs, they can be created from the CLI. The following command can be used for this:

	devEnv = factory.configurationItem('Environment') 

Add the discovered CIs to the environment:

	devEnv.members = discoveredCIs

Store the new environment:

	devEnv = repository.create('Environments/Dev', devEnv)

The newly created environment can now be used as a deployment target.

# Help #


# Troubleshooting #


