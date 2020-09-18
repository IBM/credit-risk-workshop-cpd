# Admin Guide

This section covers the setup and configuration of Cloud Pak for Data as a Service as well as supporting services necessary for the workshop. This involves the following steps:

1. [Create/Load Database(s)](#database-setup)
1. [Configure Watson Knowledge Catalog](#watson-knowledge-catalog-configuration)
1. [Configure Watson OpenScale](#watson-openscale-configuration)

## Database Setup

The workshop uses data stored in various data sources, these databases need to be installed / provisioned and setup prior to the workshop. This involves:

* Provisioning databases.
* Loading data.
* Gathering connection information.

Run through the instructions in the [Database Setup Readme](./database-setup.md)

## Watson Knowledge Catalog Configuration

In order to run through the WKC modules in the workshop, we need to configure WKC.

* Loading assets into database.
* Setting up the enterprise catalog.

Run through the instructions in the [WKC Configuration Readme](./wkc-configuration.md)

## Watson OpenScale Configuration

We setup the a sample model and content in Watson OpenScale. (_Note: You must complete the *Database Setup* section before this section._).

* Run fastpath configuration.

Run through the instructions in the [OpenScale Configuration Readme](./wos-configuration.md)
