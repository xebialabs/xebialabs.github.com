---
layout: default
title: Deployit System Administration Manual
---

# Preface #

This manual describes how to install and setup Deployit.

# Installing Deployit #

This section contains information on the installation of the Deployit server.

## Prerequisites ##

### Server Requirements ###

To install the Deployit server, the following prerequisites **must** be met:

* **Operating system**: Windows or Unix-family operating system running Java.
* **Java Runtime Environment**: JDK 1.6 (Sun/IBM or Apple)
* **RAM**: At least 2GB of internal memory, of which 1 GB should be allocated to the JVM.
* **Harddisk space**: Sufficient harddisk space to store the Deployit repository. xxx JvE, VP: how much? xxx

Depending on the intended usage of Deployit, the following may also be required:

* **Database**: Deployit's Jackrabbit repository supports a number of different databases. For more information see [Jackrabbit's persistence manager FAQ](http://wiki.apache.org/jackrabbit/PersistenceManagerFAQ).
* **LDAP**: To enable group based security, an LDAP x.509 compliant registry is needed.

### Middleware Server Requirements ###

The middleware servers that Deployit interacts with must meet the following requirements:

* **Operating system**: The target systems should run a Unix compatible operating system.
* **SSH Access**: The target systems should be accessible by SSH, i.e. they should run an SSH2 server. [^1]
* **Credentials**: Deployit should be able to log in to the target systems using a login/password combination that allows it to perform at least the following Unix commands:
    * `cp`
    * `ls`
    * `mv`
    * `rm`
    * `mkdir`
    * `rmdir`

	If the login user cannot perform these actions, a `sudo` user may be selected that can execute these commands.

**Note**: Care should be taken that users specified in the connection settings for a host have limited rights. It should be assumed that a user with write permissions on infrastructure that runs on a host is able to execute arbitrary commands on that host, using the connection settings for that host.

[1]: The SSH daemon on AIX is known to hang with certain types of SSH traffic. 

### Middleware Requirements ###

The target middleware needs to be set up so that the administrative interfaces of the target middleware can be accessed by running it on the machine on which the administrative server of the software is installed. Deployit does not support a setup in which the administrative client is installed on a different machine.

For WebSphere Application Server this means that Deployit will use SSH to log in to the machine on which the "deployment manager" is running, upload any Python files and other files needed to a temporary directory and then invoke the `wsadmin.sh` command. Afterwards any temporary files will be removed.

For WebLogic Server this means that Deployit will use SSH to log in to the machine on which the "admin server" is running, upload any Python files and other files needed to a temporary directory and then invoke the `wlst.sh` command. Afterwards any temporary files will be removed.

### Client Requirements ###

The clients that access Deployit must meet the following requirements:

* **Web browser**: The following web browsers are supported:
    * IE 7.0 or up
    * Firefox 3.0 or up
    * Safari 3.0 or up
* **Flash Player**: A flash player is required, versions 9.0, 10.0 and up are supported.

## Installation Procedure ##

### Installing the Server ###

Follow these steps to install the Deployit server application:

1. **Login to the server where Deployit will be installed**. The recommended way to install Deployit is to use a non-root user.
2. **Create an installation directory**.
3. **Copy the Deployit release distribution to the directory**.
3. **Unzip the release into the created directory**.

### Running the Setup Wizard ###

Run the Deployit Setup Wizard to start the Deployit server and make it ready for use. The command `deployit.sh -setup` starts the wizard. If you want to stop the Setup Wizard at any time, enter `exitsetup`. All changes to the configuration will be discarded.

The Setup Wizard displays the following welcome message:

	Welcome to the Deployit setup.
	You can always exit by typing 'exitsetup'.
	To re-run this setup and make changes to the Deployit server configuration 
	you can run deployit.cmd -setup on Windows or deployit.sh -setup on Unix.
	
	Do you want to use the simple setup?
	Default values are used for all properties. To make changes to the default 
	properties, please answer no.
	Options are yes or no.
	[yes]: 

Answer **yes** (or press Enter) to use the simple setup. Simple setup makes it easy to quickly get started with Deployit and to use the product's default configuration. See **Simple Setup** for more information.

Answer **no** to use the manual setup. Manual setup provides explicit control over all Deployit settings. See **Manual Setup** for more information.

**Note**: if you installed Deployit in the same location before, the Setup Wizard will display the following message:

	An existing configuration was found. Do you want to edit it?
	Options are yes or no. (selecting no will create an empty configuration)
	[yes]: 

Answer **yes** (or press Enter) to edit the existing configuration. The Setup Wizard will load all settings from the existing configuration and allow you to choose simple or manual setup.

Answer **no** to start over with an empty configuration.

#### Simple Setup ####

Using simple setup, the Setup Wizard will assume default values for all configuration parameters. Specifically, the following defaults will be used:

* Users must log in to use Deployit.
* The server will **not** use secure communication between the Deployit GUI and the Deployit server.
* The server will listen on Deployit's standard HTTP port (4516).
* The server will use a minimum of 3 and a maximum of 24 threads.
* The task recovery file will deleted.
* Applications can be imported from the `importablePackages` directory.

The Setup Wizard will ask one more question:

	Do you want Deployit to initialize the JCR repository?
	Options are yes or no.
	[yes]: 

Answer **yes** (or press Enter) if you want the Deployit repository to be recreated. The Setup Wizard must have write access to the repository directory.

Answer **no** to leave the repository intact.

See **Finishing the Setup Wizard** for completing the setup process.

**Warning**: if you choose to recreate the Deployit repository and you have installed Deployit in the same location before, any information stored in the repository will be lost.

#### Manual Setup ####

The manual setup procedure contains the following steps:

**Secure Communication Configuration**

The Setup Wizard will show the following message:

	Would you like to enable SSL?
	Options are yes or no.
	[yes]: 

Answer **no** to use regular unsecured communication between the GUI and the server. Continue with the **port configuration** section.

Answer **yes** (or press Enter) if you want to use a secure connection from the GUI to the server.

If you answer **yes**, the Setup Wizard will ask the following question to help you configure secure communication:

	Would you like Deployit to generate a keystore with a self-signed 
	certificate for you?
	N.B.: Self-signed certificates do not work correctly with some versions 
	of the Flash Player and some browsers!
	Options are yes or no.
	[yes]: 

Answer **yes** (or press Enter) if you want the Setup Wizard to generate a digital certificate automatically. The digital certificate is required to secure communication and is normally signed by a Certificate Authority (CA). The Setup Wizard can generate a _self-signed_ certificate if there is no official certificate available. Beware that using a self-signed certificate may trigger security warnings in some Flash players and browsers. Continue with the **port configuration** section.

Answer **no** if you want to use your own keystore. Deployit uses the built-in Jetty webserver to communicate with the GUI. Jetty requires a certificate with the name `Jetty` to be present in the keystore.

The Setup Wizard prompts you for the following keystore information:

	What is the path to the keystore?
	[]: 
	
	What is the password to the keystore?
	[]: 
	
	What is the password to the key in the keystore?
	[]: 

Enter the filesystem location of the keystore (for example, _mykeystore.jks_), the password to unlock the keystore and the password for the `Jetty` certificate in the keystore.  

**Port Configuration**

The Setup Wizard shows the following question:

	What http port number would you like the server to listen on?
	[4516]: 

**Note**: if you chose to enable secure communication, the default port will be _4517_ instead of _4516_.

Enter the port number that the Deployit server listens on for connections.

**Thread Configuration**

The Setup Wizard shows the following questions:

	Enter the minimum number of threads the HTTP server should use (recommended: 
		3 per client, so 3 for single user usage)
	[3]: 

Enter the minimum number of threads that the Deployit server uses to handle incoming connections. The recommended minimum number of threads is 3 per Deployit application client.

	Enter the maximum number of threads the HTTP server should use (recommended :
		3 per client, so 24 for 8 concurrent users)
	[24]: 

Enter the maximum number of threads that the Deployit server uses to handle incoming connections. The recommended maximum number of threads is 3 per Deployit application client.

**Repository Configuration**

The Setup Wizard shows the following questions:

	Where would you like Deployit to store the JCR repository?
	[repository]: 

Enter the filesystem path to a directory where Deployit will create the repository. If the directory does not exist, the Setup Wizard will create it.

	Do you want Deployit to initialize the JCR repository?
	Options are yes or no.
	[yes]: 

Answer **yes** (or press Enter) if you want the Deployit repository to be recreated. The Setup Wizard must have write access to the repository directory.

Answer **no** to leave the repository intact.

**Warning**: if you choose to recreate the Deployit repository and you have installed Deployit in the same location before, any information stored in the repository will be lost.

**Importable Packages Configuration**

The Setup Wizard shows the following question:

	Where would you like Deployit to import packages from?
	[importablePackages]: 

Enter the filesystem path to a directory where Deployit will import packages. The Setup Wizard assumes that this directory exists once the Deployit server starts and will not create it.

#### Finishing the Setup Process ####

Once you have completed configuration of the setup process, the Setup Wizard displays an overview of all selected options. The following text is an example:

	Do you agree with the following settings for Deployit and would you like 
		to save them?
	Changes will be saved in deployit.conf
		Security is always enabled
		SSL will be disabled
		HTTP port is 4516
		HTTP server will use a minimum of 3 and a maximum of 24 threads
		JCR repository will be initialized.
		Task recovery file will deleted
		Application import location is importablePackages
	[yes]:         

Answer **yes** (or press Enter) to store the configuration settings and end the Setup Wizard. If you selected the option to initialize the repository, this will be done now.

Answer **no** to abort the Setup Wizard.

If the Setup Wizard is successfully completed, it will display the following message:

	You can now start your Deployit server by executing the command deployit.cmd 
		on Windows or deployit.sh on Unix.
	Note: If your Deployit server is running please restart it.
	Finished setup.

## High Availability Setup ##

Deployit can be configured to ensure maximum uptime of the application. In such a high availability setup, two instances of Deployit are running in an _active/passive_ configuration. At any one time, only one Deployit instance is active but as soon as a failure is detected, the passive Deployit instance is activated and the failed instance is taken down for repair. 

The easiest way to achieve such a configuration is by using the same configuration for each Deployit instance.

**Warning**: unpredictable results may occur when running two Deployit instances _at the same time_. 

When switching from one Deployit instance to another, any running tasks will be recovered by the new instance (see **Task Recovery**). 

To configure such a setup, a router with _active/passive_ support must be used. xxx verify this xxx

# Configuring Deployit #

This section contains information on the configuration of the Deployit server.

## Configuring Security ##

### Security in Deployit ###

Deployit supports a fine-grained access control scheme to ensure the security of your middleware and deployments. Deployit's security mechanism is based on the concepts of _principals_, _permissions_ and _privileges_.

**Principals**

A (security) principal is an entity that can be authenticated and that can be assigned rights over resources in Deployit. Out of the box, Deployit supports only users as principals -- users are authenticated by means of a username and password and rights within Deployit are assigned to the user itself. When using an **LDAP** repository, groups in LDAP are also treated as principals.

There is one special user, `admin`, who has special rights in Deployit. xxx what are these special rights? xxx

**Permissions**

Permissions in Deployit are rights to execute particular actions. They are independent of the resources on which the action is executed.

Deployit supports the following permissions:

* **import#initial**. The right to import a package for which the application does not yet exist in the repository and for which a new application will be created.
* **import#upgrade**. The right to import a package for which the application already exists in the repository.
* **deployment#initial**. The right to perform an initial deployment of a package to an environment.
* **deployment#upgrade**. The right to perform an upgrade of a package on an environment.
xxx are there more? repo editing? undeployment? xxx

**Privileges**

Privileges in Deployit are access rights to resources in the repository. They are independent of the actions being executed on the resources. Privileges are also _hierarchical_. This means that privileges defined on a particular node in the repository also apply to the nodes for which this node is a parent (unless the privileges are explicitly revoked for the child nodes). The available privileges are defined as part of the JCR standard.

Deployit supports the following privileges:

* **READ**. The right to read the resource it is attached to, or any of it's children.
* **WRITE**. The right to write the resource it is attached to, or any of it's children.
* **ALL**. All rights to the resource it is attached to, or any of it's children.

xxx is ALL the same as READ + WRITE??? xxx

### Granting, Revoking and Denying ###

Access rights in Deployit can be _granted_ to a principal or _revoked_ from a principal. When rights are granted, the principal is allowed to perform some action or access repository entities. Rights once granted can be revoked again to prevent the action in the future. Granting and revoking rights are applicable to both _privileges_ as well as _permissions_.

Privileges can also be explicitly _denied_. Denying a privilege acts as a negative grant -- the right is explicitly disallowed.

### Securing User Actions ###

When a user attempts to execute a particular action in Deployit, permissions and privileges are combined to verify whether the user is allowed to execute the action.

**Initial Import**

For an initial import, the user must have **import#initial** permission. No further privileges are required. The user performing the import will have **READ** and **WRITE** privileges on the newly created _Application_ and _DeploymentPackage_ CIs.

**Upgrade Import**

For an upgrade import, the user must have **import#upgrade** permission as well as **WRITE** privilege on the target CI, the _Application_ CI for which the package is imported. The user performing the import will have **READ** and **WRITE** privileges on the newly created _DeploymentPackage_ CI.

**Initial Deployment**

For an initial deployment, the user must have **deployment#initial** permission. Also, the user needs **READ** permission on the _Package_ CI and **WRITE** permission on both the _Environment_ and _Infrastructure_ CIs that is being deployed to. The user performing the deployment will have **READ** and **WRITE** privileges on the newly created _Deployment_ and deployed item CIs.

**Upgrade Deployment**

For an upgrade deployment, the user must have **deployment#upgrade** permission. Also, the user needs **READ** permission on the _Package_ CI and **WRITE** permission on both the _Environment_ and _Infrastructure_ CIs that is being deployed to. The user performing the deployment will have **READ** and **WRITE** privileges on the newly created _Deployment_ CI and any created deployed item CIs.

**Undeployment**

For undeployment, the user needs **WRITE** permission on the _Deployment_ CI that is being undeployed.

### Configuring Repository Security ###

Security in the Deployit repository can be configured using the **Command Line Interface**. See the **Deployit Command Line Manual** for more information.

**Creating Users**

Deployit can only create users in it's own repository, even if it is configured to use an **LDAP** repository for authentication and authorization. To do this, use a statement such as the following:

	deployer = security.createUser("john", "secret")

xxx will it be moved to the proxies??? xxx

**Granting Permissions and Privileges**

To grant a particular permission to a principal, use a statement such as the following:

	security.grant("john", ["import#initial"])

To grant a particular privilege to a principal on a resource, use a statement such as the following:

	security.grant("mary", "Environments/Dev", ["ALL"])

**Revoking Permissions and Privileges**

To revoke a particular permission from a principal, use a statement such as the following:

	security.revoke("john", ["import#initial"])

To revoke a particular privilege from a principal on a resource, use a statement such as the following:

	security.revoke("mary", "Environments/Dev", ["ALL"])

### Security Configuration Example ###

xxx make up a sample xxx

### Configuring LDAP Security ###

By default, Deployit authenticates users and retrieves authorization information from it's repository. Deployit can also be configured to use an LDAP repository to authenticate users and to retrieve role (group) membership. In this scenario, Deployit works with both users and groups as principals. This means that rights can be assigned to both users and groups. The rights assigned to a principal are always stored in the JCR repository. 

Deployit treats the LDAP repository as **read-only**. This means that Deployit will use the information from the LDAP repository, but can not make changes to that information. 

When authenticating a user, Deployit first tries to locate the user in the LDAP repository. If this fails, Deployit will check it's own repository as a backup.

To configure Deployit to use an LDAP repository, the built-in JCR repository, Jackrabbit, must defer to the LDAP server for authentication. This requires modification of the default Deployit Jackrabbit configuration. Follow these steps:

1. **Create `jackrabbit_jaas.config` file**. The file must be accessible for the Deployit server. The following is a sample file:

		Jackrabbit {
			org.apache.jackrabbit.core.security.authentication.DefaultLoginModule 
				sufficient adminId=admin anonymousId=anonymous;
			com.sun.security.auth.module.LdapLoginModule required 
				userProvider="ldap://localhost:14516/ou=system" 
				userFilter="(&(uid={USERNAME})(objectClass=inetOrgPerson))" 
				useSSL=false
			principalProvider=com.xebialabs.deployit.security.LdapPrincipalProvider;
		};

    Modify the LDAP settings (URL, port or user filter, etc.) to suit your needs.

2. **Modify the Deployit server startup command**. Notify the Deployit server of the new configuration file by including the following parameter on the Java command line:

		-Djava.security.auth.login.config==/path/to/jackrabbit_jaas.config


The class **LdapPrincipalProvider** is an example of how to connect Deployit to LDAP through Jackrabbit. If your LDAP server has a different structure or to connect Jackrabbit to another user store, see the information about Jackrabbit configuration on the [the Jackrabbit website](http://jackrabbit.apache.org/).

## Configuring the Repository ##

### Using a Database ###

xxx how to store JCR repo stuff in MySQL or Oracle? xxx
xxx anything else? xxx

## Installing Plugins ##

Deployit uses plugins to communicate with different types of middleware. The Deployit server dynamically loads plugins when it starts. Any plugins added or removed when Deployit server is running will not take effect until the server is restarted.

Plugins are stored in the `plugins` directory in the Deployit installation directory.

**Installing a Plugin**

To install a new plugin, simply stop the Deployit server and copy the plugin JAR archive into the `plugins` directory, then restart the Deployit server.

**Deinstalling a Plugin**

To deinstall a plugin, simply stop the Deployit server and remove the plugin JAR archive from the `plugins` directory, then restart the Deployit server.

## Installing CLI Extensions ##

The Deployit **CLI** is used to communicate with the Deployit server. It can be extended with Python scripts that are loaded on CLI startup.

To install CLI extensions follow these steps:

1. **Create a directory called `ext`**. This directory in the same directory from which you start the CLI.
2. **Copy Python scripts into the `ext` directory**.
3.  **Start the CLI**. The CLI will load and execute all scripts with the `py` or `cli` suffix found in the extension directory.

## Configuring Logging ##

Out of the box, Deployit server writes informational, warning and error log messages to standard output when running. It is possible to change this behavior to write log output to a file or to log output from a specific source. 

Deployit uses the Logback logging framework for it's logging. To change it's behavior, edit the file `logback.xml` in the `conf` directory of the Deployit server installation directory.

The following is an example `logback.xml` file:

	<configuration>
        <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
    		<!-- encoders are assigned the type
         		ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
    		<encoder>
      			<pattern>%d{yyyy-MM-dd HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
    		</encoder>
		</appender>
		
		<!-- Create a file appender that writes log messages to a file -->
		<appender name="FILE" class="ch.qos.logback.core.FileAppender">
        	<layout class="ch.qos.logback.classic.PatternLayout">
                <pattern>%-4relative [%thread] %-5level %class - %msg%n</pattern>
        	</layout>
       		<File>log/my.log</File>
		</appender>
		
		<!-- Set logging of classes in com.xebialabs to DEBUG level -->
		<logger name="com.xebialabs" level="debug"/>
		
		<!-- Set logging of class HttpClient to DEBUG level -->
		<logger name="HttpClient" level="debug"/>
		
		<!-- Set the logging of all other classes to INFO -->
		<root level="info">
			<!-- Write logging to STDOUT and FILE appenders -->
			<appender-ref ref="STDOUT" />
			<appender-ref ref="FILE" />
		</root>
		
	</configuration>

Place a file called `logback-test.xml` on the server classpath to temporarily change the server's logging settings.

For more information see the [Logback website](http://logback.qos.ch/).

# Setting up Deployit #

This section describes how to setup Deployit server in your environment.

Deployit must be setup for your environment before it can be used to execute deployments. This entails the following steps:

1. **Start the Deployit server**.
2. **Discover your middleware**. Deployit can inspect your environment and automatically create CIs for your middleware.
3. **Ådd the discovered middleware to an environment**. CIs must be grouped in an environment to use them for deployment.

Setup of Deployit is performed using the Deployit **Command Line Interface (CLI)**. For more information about the CLI, see the **Deployit Command Line Manual**.

## Starting and Stopping ##

**Starting the Server**

Open a terminal window and change to the Deployit server directory. Start the Deployit server with the command:

	bin/server.sh

on Unix and
	
	bin/server.cmd

on Windows.

By starting the server with the `-h` flag, a message is printed that shows the possible options it supports:

	java -cp deployit-server-<version>.jar [options...] com.xebialabs.deployit.Deployit arguments...
		-reinitialize : Reinitialize the repository, only useful with -setup
		-setup        : (Re-)run the setup for Deployit

The options are:

* `-reinitialize` -- tells Deployit to reinitialize the repository. Used only in conjunction with `-setup`.
* `-setup` -- runs the Deployit Setup Wizard.
* `-test-mode` -- enables Deployit serer test-mode. When test-mode is enabled, WebDAV access to the JCR repository is installed. The repository can be accessed using a URL such as `http://localhost:4516/repository/default/`.

**Stopping the Server**

It is possible to stop the Deployit server using a REST API call. The command requires a username and password with administrator privileges (xxx true? xxx). The following is an example of a command to generate such a call:

	curl -X POST --basic -u admin:admin 
		http://admin:admin@localhost:4516/deployit/server/shutdown

This requires the external `curl` command, available for both Unix and Windows. xxx wget example? xxx

## Editing CIs ##

The CIs in the Deployit repository can also be edited, either using the command line interface (CLI) or graphical user interface (GUI). See the respective manuals for more details.

# Maintaining Deployit #

This section describes how to maintain the Deployit server in your environment.

## Backing up Deployit ##

To create a backup of Deployit, several components may need to be backed up depending on your configuration:

* **JCR repository**. 
    * Built-in repository: Create a backup of the built-in JCR repository by backing up the files in the repository directory. **Note: to create the backup, Deployit must be stopped.**
    * Database repository: Create a backup of the database using the tools provdided by your vendor.
* **LDAP repository**. Create a backup of the LDAP repository using the tools provdided by your vendor.
* **Configuration**. Create a backup of the Deployit configuration by backing up the files in the `conf` directory in the installation directory.
