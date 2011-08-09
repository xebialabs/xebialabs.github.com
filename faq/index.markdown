---
layout: default
title: Deployit Frequently Asked Questions
---

# Deployit Frequently Asked Questions #

## Server Configuration and Startup ##

### How do I prevent Deployit from writing temporary files for imported packages? ###

When uploading a package using the CLI, Deployit stores a temporary file on the server. This file is deleted only if you shut down the JVM. An alternative is to make Deployit read the archive in memory. To do this, use the following setting when starting the Deployit server:

	-Dorg.apache.james.mime4j.defaultStorageProvider=org.apache.james.mime4j.storage.MemoryStorageProvider

