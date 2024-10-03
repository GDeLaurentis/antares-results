# Minimal makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Target to create amplitudes
amplitudes:
	@cd .. && mkdir -p sphinx/source/_static/amplitudes/ && \
	for texfile in $$(find amplitudes/ -name "*.tex"); do \
	  DIR=$$(dirname $$texfile); \
	  mkdir -p sphinx/source/_static/$$DIR; \
	  mkdir -p sphinx/source/$$DIR/coeffs; \
	  lualatex -interaction=nonstopmode -output-directory=sphinx/source/_static/$$DIR $$texfile; \
	  rm sphinx/source/_static/$$DIR/*.log sphinx/source/_static/$$DIR/*.aux sphinx/source/_static/$$DIR/*.toc sphinx/source/_static/$$DIR/*.out; \
	  pdf_file="$$DIR/$$(basename $${texfile%.tex}.pdf)"; \
	  image_file="$$DIR/$$(basename $${texfile%.tex}.png)"; \
	  gs -sDEVICE=pngalpha -o "sphinx/source/_static/$$image_file" -r600 "sphinx/source/_static/$$pdf_file"; \
	  rst_file="$$DIR/coeffs/$$(basename $${texfile%.tex}.rst)"; \
	  title="$$(basename $${texfile%.tex})"; \
	  echo "$$title" >> "sphinx/source/$$rst_file"; \
	  echo "==================" >> "sphinx/source/$$rst_file"; \
	  echo "" >> "sphinx/source/$$rst_file"; \
	  echo ".. image:: /_static/$$image_file" >> "sphinx/source/$$rst_file"; \
	  echo "   :width: 100%" >> "sphinx/source/$$rst_file"; \
	  echo "   :height: 200px" >> "sphinx/source/$$rst_file"; \
	done; \
	for dir in $$(find amplitudes/ -type d); do \
	  if [ "$$(basename $$dir)" != "coeffs" ] && [ "$$(basename $$dir)" != "amplitudes" ]; then \
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
	@rm -rf source/_static source/amplitudes ../docs