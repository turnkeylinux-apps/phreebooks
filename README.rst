Phreedom - Enterprise Resource Planning
=======================================

`Phreedom`_ is a modular ERP web application for small businesses that
can track inventory, accounting, contracts, check writing, bank account
reconciliation, and more. The objective is to provide the small-business
community with a free multi-language end-to-end enterprise management
tool.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Phreedom configurations:
   
   - Installed from upstream source code to /var/www/phreedom

- SSL support out of the box.
- `PHPMyAdmin`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, phpMyAdmin: username **root**
-  Phreedom: username **admin**


.. _Phreedom: http://www.phreesoft.com/
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _PHPMyAdmin: http://www.phpmyadmin.net
