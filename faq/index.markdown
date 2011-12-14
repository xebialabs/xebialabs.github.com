---
layout: faq
title: Deployit Frequently Asked Questions
---

# Deployit Frequently Asked Questions #

<a class="faqlink" href="#">Server Installation</a>

### Can I perform an unattended install of Deployit, for instance using Puppet? ###

It is possible to do an unattended install. Both the server and command line interface (CLI) are distributed as separate ZIP archives. Installation for the CLI is as simple as extracting the ZIP file.

The server needs some more configuration. When the server is started, it looks for a file called _deployit.conf_ in the _conf_ directory in it's home directory. If this does not exist, it enters an interactive setup wizard to create it.

An unattended install can be performed by including a _deployit.conf_ file in the package and copy it to the _conf_ directory once the installation ZIP file is extracted. You could do the installation manually once to obtain a _deployit.conf_ file. After this installation, Deployit server can be started without entering the setup wizard. If you are using a Deployit repository on disk, you do have to create the empty repository directory manually as this is normally done by the setup wizard.

Another option is to run through the setup wizard automatically, accepting all the defaults. This Unix command will do that:

	yes yes | bin/server.sh -setup

<a class="faqlink" href="#">Server configuration and startup</a>
	
### How do I prevent Deployit from writing temporary files for imported packages? ###

When uploading a package using the CLI, Deployit stores a temporary file on the server. This file is deleted only if you shut down the JVM. An alternative is to make Deployit read the archive in memory. To do this, use the following setting when starting the Deployit server:

	-Dorg.apache.james.mime4j.defaultStorageProvider=org.apache.james.mime4j.storage.MemoryStorageProvider

### How do I enable additional logging for the Deployit server? ###

Logging is configured in the file _SERVER\_HOME/conf/logback.xml_. To enable debug mode, change the following in the logback file:

	<root level="debug">
		...
	</root>
	
If this results in too much logging, you can tailor logging for specific packages by adding loglevel definitions for them. For example:
	
	<logger name="com.xebialabs" level="info" />

Note that the server needs to be restarted to activate the new log settings.

See the [logback site](http://logback.qos.ch/) for more information.

### How do I configure Deployit to use specific file encoding? ###

Deployit uses file.encoding system property. To change file encoding other than system default set the following system property when starting the Deployit server:

	For Oracle JDK:
	-Dfile.encoding=<FileEncodingType>
	e.g: -Dfile.encoding=UTF-8
	
	For IBM JDK:
	-Dclient.encoding.override=<FileEncodingType>
	e.g: -Dclient.encoding.override=UTF-8
	

<a class="faqlink" href="#">Middleware server configuration</a>

### Where can I find more information about configuring middleware for use with Deployit? ###

See the [documentation provided with the Overthere framework](https://github.com/xebialabs/overthere).

### Do I always need a CIFS connection to my Windows middleware hosts? ###

Yes. Deployit can use Telnet or WinRM to execute commands on the middleware hosts, but needs CIFS to transfer files to the middleware host.

<a class="faqlink" href="#">CLI usage</a>

### How do I create the most common CIs in the CLI? ###

The following snippet shows examples of creating common UDM CIs.

		# Create a host
		host = factory.configurationItem('Infrastructure/sampleHost', 'overthere.SshHost', { 'os': 'UNIX', 'address': 'localhost', 'username': 'scott' })
		repository.create(host)                                                                                                                          
		deployit.print(host)
		
		# Create a dictionary
		dict = factory.configurationItem('Environments/myDict', 'udm.Dictionary')
		dict.entries = { 'a': '1', 'b': '2' }
		repository.create(dict)
		deployit.print(dict)

		# Create an environment
		env = factory.configurationItem('Environments/sampleEnv', 'udm.Environment')
		env.dictionaries = [ dict.id ]
		env.members = [ host.id ]                                                                                                                        
		repository.create(env)
		deployit.print(env)
