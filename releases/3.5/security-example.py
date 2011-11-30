#
# Security example based on KvK security matrix
#
# User groups:
#   - Administrator
#   - Developer
#   - Deployer
#   - Senior Deployer

# Create test data

# Dev env
devEnv = repository.create("Environments/DEV", factory.configurationItem("Environment"))
devServer1 = repository.create("Infrastructure/DevServer1", factory.configurationItem("DummyJeeServer", {"name":"DevServer1", "stepDelayTimeInMilliSeconds":"1000"}))
devEnv.values['members'] = [devServer1.id]
devEnv = repository.update("Environments/DEV", devEnv)

# Test env
testEnv = repository.create("Environments/TEST", factory.configurationItem("Environment"))
testServer1 = repository.create("Infrastructure/TestServer1", factory.configurationItem("DummyJeeServer", {"name":"TestServer1", "stepDelayTimeInMilliSeconds":"1000"}))
testEnv.values['members'] = [testServer1.id]
testEnv = repository.update("Environments/TEST", testEnv)

# Acc env
accEnv = repository.create("Environments/ACC", factory.configurationItem("Environment"))
accServer1 = repository.create("Infrastructure/AccServer1", factory.configurationItem("DummyJeeServer", {"name":"AccServer1", "stepDelayTimeInMilliSeconds":"1000"}))
accEnv.values['members'] = [accServer1.id]
accEnv = repository.update("Environments/ACC", accEnv)

# Prod env
prodEnv = repository.create("Environments/PROD", factory.configurationItem("Environment"))
prodServer1 = repository.create("Infrastructure/ProdServer1", factory.configurationItem("DummyJeeServer", {"name":"ProdServer1", "stepDelayTimeInMilliSeconds":"1000"}))
prodEnv.values['members'] = [prodServer1.id]
prodEnv = repository.update("Environments/PROD", prodEnv)

# Create users
adminUser = security.createUser("administrator", "administrator")
devUser = security.createUser("developer", "developer")
deployerUser = security.createUser("deployer", "deployer")
srDeployerUser = security.createUser("srdeployer", "srdeployer")

#
# Permissions:
#   - Administrator: can modify environment memberships
#   - Developer: can import new versions of (selected) applications, can upgrade (selected) applications on DEV and TEST
#   - Deployer: import new versions of applications, deploy to DEV, TEST, view PROD
#   - Senior Deployer: import new versions of applications, deploy to DEV, TEST, PROD

security.grant("login", 'administrator')
security.grant("login", 'deployer')
security.grant("login", 'srdeployer')
security.grant("login", 'developer')

# Administrator privileges
# Permission infrastructure#management means the user can add/remove ALL infrastructure and add/remove ALL environments
security.grant("infrastructure#management", 'administrator')
# To grant rights to specific infrastructure or environments, use:
#security.grant("infrastructure#management", 'administrator', ['Environments/PROD'])

# Developer privileges
security.grant("import#upgrade", 'developer')
security.grant("deploy#upgrade", 'developer', ['Environments/DEV', 'Environments/TEST'])

# The developer user has permission to import new versions of all applications.
# To restrict to new versions of a specific application, use:
#security.grant('import#upgrade', 'developer', ['Applications/PetClinic'])

security.grant("import#initial", 'deployer')
security.grant("import#upgrade", 'deployer')
security.grant("deploy#initial", 'deployer', ['Environments/DEV', 'Environments/TEST'])
security.grant("deploy#upgrade", 'deployer', ['Environments/DEV', 'Environments/TEST'])
# In order to allow deployer to see the deployments to PROD, he needs rights on both the environment and the infrastructure in the environment.
prodEnv = repository.read('Environments/PROD')
security.grant("read", 'deployer', [prodEnv.id] + prodEnv.values['members'])

# Sr Deployer privileges
security.grant("import#initial", 'srdeployer')
security.grant("import#upgrade", 'srdeployer')
security.grant("deploy#initial", 'srdeployer')
security.grant("deploy#upgrade", 'srdeployer')
