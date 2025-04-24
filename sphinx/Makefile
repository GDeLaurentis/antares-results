# Minimal makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
NUM_JOBS = $(shell n=$$(echo "$(MAKEFLAGS)" | sed -n 's/.*-j\([0-9][0-9]*\).*/\1/p'); [ -n "$$n" ] && echo $$n || echo 1)

define process_tex
DIR=$$(dirname "$$0"); \
mkdir -p sphinx/source/_static/"$$DIR"; \
mkdir -p sphinx/source/"$$DIR"/coeffs; \
SpinorLatexCompiler "$$0" -i nonstopmode -o sphinx/source/_static/"$$DIR"; \
pdf_file="$$DIR/$$(basename "$${0%.tex}.pdf")"; \
image_file="$$DIR/$$(basename "$${0%.tex}.png")"; \
gs -sDEVICE=pngalpha -o "sphinx/source/_static/$$image_file" -r600 "sphinx/source/_static/$$pdf_file" > /dev/null 2>&1; \
rst_file="$$DIR/coeffs/$$(basename "$${0%.tex}.rst")"; \
title="$$(basename "$${0%.tex}")"; \
{ \
echo "$$title"; \
echo "=================="; \
echo ""; \
echo ".. image:: /_static/$$image_file"; \
echo "   :width: 100%"; \
} > "sphinx/source/$$rst_file"
endef

# Target to create amplitudes
amplitudes:
	@echo "Using $(NUM_JOBS) cores..."
	@cd .. && mkdir -p sphinx/source/_static/antares_results/ && \
	find antares_results/ -name "*.tex" | xargs -n1 -P$(NUM_JOBS) bash -c '$(process_tex)' 
	@cd .. && \
	for dir in $$(find antares_results/ -type d); do \
	  if [ "$$(basename $$dir)" != "coeffs" ] && [ "$$(basename $$dir)" != "__pycache__" ] && [ "$$(basename $$dir)" != ".ipynb_checkpoints" ] && [ "$$(basename $$dir)" != "amplitudes" ]; then \
	    base_dir="$$(basename $$dir)"; \
	    rst_file="sphinx/source/$$dir/$$base_dir.rst"; \
		if [ -f "$$dir/README.md" ]; then \
		echo "Converting README.md to RST"; \
		pandoc "$$dir/README.md" -t rst >> "$$rst_file"; \
		else \
		echo "$$base_dir" > "$$rst_file"; \
		echo "======================" >> "$$rst_file"; \
		fi; \
	    echo "" >> "$$rst_file"; \
	    echo ".. toctree::" >> "$$rst_file"; \
	    echo "   :glob:" >> "$$rst_file"; \
	    echo "   :maxdepth: 1" >> "$$rst_file"; \
	    echo "" >> "$$rst_file"; \
	    echo "   */*" >> "$$rst_file"; \
	    echo "" >> "$$rst_file"; \
	  fi; \
	done

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile amplitudes

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

github:
	@make html
	@cp -a $(BUILDDIR)/html/. ../docs
	@rm -r $(BUILDDIR)

clean:
	@rm -rf source/_static source/antares_results ../docs