PhreeBooks - Enterprise Resource Planning
=========================================

`PhreeBooks`_ (formerly PhreeDom) is a modular ERP web application for 
small businesses that can track inventory, accounting, contracts, check 
writing, bank account reconciliation, and more. The objective is to 
provide the small-business community with a free multi-language end-to
-end enterprise management tool.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- PhreeBooks configurations:
   
   - Installed from upstream source code to /var/www/phreebooks

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, Adminer: username **root**
-  PhreeBooks: username **admin**


.. _PhreeBooks: http://www.phreesoft.com/phreebooks/
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: http://www.adminer.org/
