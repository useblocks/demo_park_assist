Park Assist Demo – Documentation
=================================

Software documentation for the **Park Assist Demo** project running on the
Adafruit Metro RP2040 (Setup 2).

This documentation captures User Stories, SW Architecture, Implementation
details (with code links), and Test Cases using
`sphinx-needs <https://sphinx-needs.readthedocs.io>`_.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   user_stories
   architecture
   implementation
   test_cases

----

Traceability Overview
---------------------

The table below lists all needs across the project.

.. needtable::
   :columns: id, type, title, status
   :style: datatables
   :sort: type

----

Traceability Graph
------------------

End-to-end link graph connecting User Stories → Architecture → Implementation
and Test Cases → User Stories.

.. needflow::
   :link_types: realizes, verifies
   :show_link_names:
   :filter: type in ["story", "arch", "impl", "test"]
