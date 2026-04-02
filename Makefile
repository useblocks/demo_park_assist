SPHINXBUILD := sphinx-build
SOURCEDIR   := docs
BUILDDIR    := docs/_build/html

.DEFAULT_GOAL := help

.PHONY: help html clean open test serve step_start step_2 step_3 step_4 step_5

help:
	@echo ""
	@echo "Park Assist Demo – Documentation targets"
	@echo ""
	@echo "  make html        Build the Sphinx HTML documentation"
	@echo "  make clean       Remove the build output directory"
	@echo "  make open        Build HTML and open it in the default browser"
	@echo "  make serve       Build HTML and serve on port 8080 (Codespaces)"
	@echo "  make test        Run the pytest test suite"
	@echo "  make step_start  Reset to start state (display only)"
	@echo "  make step_2      Reset to step 2 result (buzzer to be added)"
	@echo "  make step_3      Reset to step 3 result (LED strip to be added)"
	@echo "  make step_4      Reset to step 4 result (zone logic to be added)"
	@echo "  make step_5      Reset to step 5 result (complete implementation)"
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

step_start:
	@./.util/step.sh start

step_2:
	@./.util/step.sh 2

step_3:
	@./.util/step.sh 3

step_4:
	@./.util/step.sh 4

step_5:
	@./.util/step.sh 5
