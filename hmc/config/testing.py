#!/usr/bin/env python

from plone.app.testing import (PloneSandboxLayer, applyProfile,
                               PLONE_FIXTURE, IntegrationTesting)
from plone.testing import z2
from zope.configuration import xmlconfig


class HMCConfig(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import hmc.config
        xmlconfig.file('configure.zcml',
                       hmc.config,
                       context=configurationContext,
                       )
        # Install products that use an old-style initialize()
        # function
        z2.installProduct(app, 'Products.PythonField')
        z2.installProduct(app, 'Products.TALESField')
        z2.installProduct(app, 'Products.TemplateFields')
        z2.installProduct(app, 'Products.PloneFormGen')

    def tearDownZope(self, app):
        # Uninstall products installed above
        z2.uninstallProduct(app, 'Products.PloneFormGen')
        z2.uninstallProduct(app, 'Products.TemplateFields')
        z2.uninstallProduct(app, 'Products.TALESField')
        z2.uninstallProduct(app, 'Products.PythonField')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'hmc.config:default')

HMC_CONFIG_FIXTURE = HMCConfig()
HMC_CONFIG_INTEGRATION_TESTING = \
    IntegrationTesting(
        bases=(HMC_CONFIG_FIXTURE, ),
        name="HMC:Integration",
    )
