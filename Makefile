SPHINXBUILD := sphinx-build
SOURCEDIR   := docs
BUILDDIR    := docs/_build/html

.DEFAULT_GOAL := help

.PHONY: help html clean open

help:
	@echo ""
	@echo "Park Assist Demo – Documentation targets"
	@echo ""
	@echo "  make html    Build the Sphinx HTML documentation"
	@echo "  make clean   Remove the build output directory"
	@echo "  make open    Build HTML and open it in the default browser"
	@echo ""

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR)

open: html
	xdg-open $(BUILDDIR)/index.html
