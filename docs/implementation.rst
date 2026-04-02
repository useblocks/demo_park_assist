Implementation
==============

Board
-----

Implementation needs are defined directly in the source code of
``src/metro_rp2040/code.py`` using one-line CodeLinks comments:

.. code-block:: python

   # @ <title>, <id>, impl, [<linked need ids>]

`sphinx-codelinks <https://codelinks.useblocks.com>`_ extracts these comments
automatically and renders them as ``impl`` needs with a remote link to the
exact source line on GitHub.

.. src-trace::
   :project: rp2040


Tests
-----

Test implementation needs are extracted from the unit test suite in
``tests/`` using the same one-line comment style:

.. code-block:: python

   # @ <title>, <id>, test_impl, [<linked TC_ ids>]

Each comment links a concrete Python test function to its corresponding
Test Case need, making the full traceability chain
``US → TC → TI`` navigable in the graph view.

.. src-trace::
   :project: tests
