# Admin Guide

This section covers the setup and configuration of the Cloud Pak for Data cluster as well as supporting services necessary for the workshop. This involves the following steps:

1. [Configure Cloud Pak for Data](#platform-configuration)
1. [Create/Load Database(s)](#database-setup)
1. [Configure Database Connections](#database-connection-configuration)
1. [Configure Data Virtualization](#data-virtualization-configuration)
1. [Configure Watson Knowledge Catalog](#watson-knowledge-catalog-configuration)
1. [Configure Watson OpenScale](#watson-openscale-configuration)

> **NOTE**: Many of these sections either require or should be completed by a user with `Administrator` user role to the Cloud Pak for Data cluster (i.e the `admin` account in a default installation).

## Platform Configuration

There are a couple of steps to configure services and setup the platform so users can access the environment. This covers:

* Adding user accounts to cluster.

Run through the instructions in the [Platform Configuration Readme](./platform-configuration.md)

## Database Setup

The workshop uses data stored in various data sources, these databases need to be installed / provisioned and setup prior to the workshop. This involves:

* Provisioning databases.
* Loading data.
* Gathering connection information.

Run through the instructions in the [Database Setup Readme](./database-setup.md)

## Database Connection Configuration

For Cloud Pak for Data to access the databases we setup above, we need to add *Data Connections* to connect to them via JDBC. (_Note: You must complete the *Database Setup* section before this section._)

* Adding global connection.

Run through the instructions in the [Database Connection Configuration Readme](./database-connection-configuration.md)

## Data Virtualization Configuration

In order to run through the data virtualization module in the workshop, we need to configure the DV instance that has been provisioned in the cluster. (_Note: You must complete the *Database Connection* and *Platform Configuration* sections before this section._). This involves:

* Provisioning Data Virtualization instance.
* Adding users to Data Virtualization instance.
* Add connections to DV.
* Setup virtualized data for backup.

Run through the instructions in the [Database Virtualization Configuration Readme](./datavirtualization-configuration.md)

## Watson Knowledge Catalog Configuration

In order to run through the WKC modules in the workshop, we need to configure WKC.

* Loading assets into database.
* Setting up the enterprise catalog.

Run through the instructions in the [WKC Configuration Readme](./wkc-configuration.md)

## Watson OpenScale Configuration

We setup the a sample model and content in Watson OpenScale. (_Note: You must complete the *Database Setup* section before this section._).

* Run auto setup configuration.

Run through the instructions in the [OpenScale Configuration Readme](./wos-configuration.md)
