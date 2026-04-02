SPHINXBUILD := sphinx-build
SOURCEDIR   := docs
BUILDDIR    := docs/_build/html

.DEFAULT_GOAL := help

.PHONY: help html clean open test serve step_1 step_2 step_3 step_4 step_5

help:
	@echo ""
	@echo "Park Assist Demo – Documentation targets"
	@echo ""
	@echo "  make html    Build the Sphinx HTML documentation"
	@echo "  make clean   Remove the build output directory"
	@echo "  make open    Build HTML and open it in the default browser"
	@echo "  make serve   Build HTML and serve on port 8080 (Codespaces)"
	@echo "  make test    Run the pytest test suite"
	@echo "  make step_1  Switch code + docs to start state (display only)"
	@echo "  make step_2  Switch code + docs to step 3 start (add buzzer)"
	@echo "  make step_3  Switch code + docs to step 4 start (add LED strip)"
	@echo "  make step_4  Switch code + docs to step 5 start (add zone logic)"
	@echo "  make step_5  Switch code + docs to final state (complete)"
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

step_1:
	@./step.sh 1

step_2:
	@./step.sh 2

step_3:
	@./step.sh 3

step_4:
	@./step.sh 4

step_5:
	@./step.sh 5
