# Makefile for Sphinx documentation

.PHONY: help html publish clean dot

### * Variables

SPHINX_DIR=".sphinx-forge"
CONF_FILE=".conf.py"
ORG2RST_SCRIPT=".org2rst.sh"
IMAGE_DIR="images"
RESOURCES_DIR="resources"
REPORTS_DIR="reports"
PUBLISH_DIR="/home/mabrunea/work/lab_jyvaskyla/wwwpages/html/collaborations/Serratia-epigenetics"
WWW_DIR="/home/mabrunea/work/lab_jyvaskyla/wwwpages"

### * Help

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  publish    to publish the HTML files on the Jyu pages"
	@echo "  clean      to clean all sphinx files"

html: clean dot
	@cp $(CONF_FILE) $(SPHINX_DIR)/conf.py
	@cp *.rst $(SPHINX_DIR)
	@cp -r $(IMAGE_DIR) $(RESOURCES_DIR) $(REPORTS_DIR) $(SPHINX_DIR)
	@bash $(ORG2RST_SCRIPT) $(SPHINX_DIR)
	@cp .my_theme.css $(SPHINX_DIR)/_static/my_theme.css
	@cd $(SPHINX_DIR); make html
	@python .addGitLog.py $(SPHINX_DIR)/_build/html/index.html $(SPHINX_DIR)/_build/html/index.html
	@echo
	@echo "Build finished. The HTML pages are in $(SPHINX_DIR)/_build/html/."
	@ln -s $(SPHINX_DIR)/_build/html/index.html .index.html

labnotebookPdf:
	# Requires poppler to be installed on RHEL
	pdfunite lab-notebook/paper-labnotebook/*.pdf resources/paper-labnotebook.pdf

dot:
	@bash .convertDotToPng.sh images/dot images

publish: html
	rm -fr $(PUBLISH_DIR)/*
	cp -r $(SPHINX_DIR)/_build/html/* $(PUBLISH_DIR)
	cd $(WWW_DIR); make upload_JYU

clean:
	rm -fr $(SPHINX_DIR)/_build
	rm -f $(SPHINX_DIR)/*.rst
	rm -fr $(SPHINX_DIR)/images
	rm -fr $(SPHINX_DIR)/resources
	rm -fr $(SPHINX_DIR)/reports
	rm -f $(SPHINX_DIR)/conf.py
	rm -f .index.html
