Banking Management System Documentation
========================================

Welcome to the Banking Management System documentation. This project provides a comprehensive banking system with support for different account types, customer management, and transactions.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   modules/account
   modules/customer
   modules/transaction

Overview
--------

The Banking Management System is a Python-based application that manages:

- **Customers**: Individual and Corporate customers
- **Accounts**: Savings and Current accounts  
- **Transactions**: Direct debits and external transactions
- **Banking Groups**: Management of multiple accounts

Features
--------

- Customer account management
- Multiple account types (Savings, Current)
- Transaction processing and tracking
- Direct debit payments
- External transaction handling
- Role-based access and authentication

Quick Start
-----------

Installation
~~~~~~~~~~~~

To install the project::

    pip install -e ".[dev]"

Running Tests
~~~~~~~~~~~~~

To run the test suite::

    pytest tests/ -v

View Reports
~~~~~~~~~~~~

- **Test Report**: Open `reports.html`
- **Coverage Report**: Open `htmlcov/index.html`

API Reference
-------------

.. toctree::
   :maxdepth: 2

   api/abc_banking_group
   api/account
   api/customer
   api/transaction

Modules
-------

.. automodule:: src.models
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
