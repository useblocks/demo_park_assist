SPHINXBUILD := sphinx-build
SOURCEDIR   := docs
BUILDDIR    := docs/_build/html

.DEFAULT_GOAL := help

.PHONY: help html clean open test serve

help:
	@echo ""
	@echo "Park Assist Demo – Documentation targets"
	@echo ""
	@echo "  make html    Build the Sphinx HTML documentation"
	@echo "  make clean   Remove the build output directory"
	@echo "  make open    Build HTML and open it in the default browser"
	@echo "  make serve   Build HTML and serve on port 8080 (Codespaces)"
	@echo "  make test    Run the pytest test suite"
	@echo ""

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)

clean:
	rm -rf $(BUILDDIR)

open: html
	xdg-open $(BUILDDIR)/index.html

serve: html
	@echo "Serving docs on http://localhost:8080"
	cd $(BUILDDIR) && python3 -m http.server 8080

test:
	.venv/bin/pytest tests/ -v
