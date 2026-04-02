Implementation
==============

Implementation needs are defined directly in the source code of
``src/metro_rp2040/code.py`` using one-line CodeLinks comments:

.. code-block:: python

   # @ <title>, <id>, impl, [<linked need ids>]

`sphinx-codelinks <https://codelinks.useblocks.com>`_ extracts these comments
automatically and renders them as ``impl`` needs with a remote link to the
exact source line on GitHub.

----

.. src-trace::
   :project: rp2040
