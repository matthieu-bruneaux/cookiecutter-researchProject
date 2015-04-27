### * Variables

PELICAN_DIR=docs-with-pelican
PELICAN_PAGES_DIR=$(PELICAN_DIR)/content/pages
PELICAN_ARTICLES_DIR=$(PELICAN_DIR)/content/articles
PELICAN_RESOURCES_DIR=$(PELICAN_DIR)/content/resources
PELICAN_OUTPUT_DIR=$(PELICAN_DIR)/output

REPORTS_DIR=reports

WWW_DIR={{ cookiecutter.doc_www_dir }}
WWW_PUBLISH_DIR=$(WWW_DIR){{ cookiecutter.doc_www_publish_dir }}
WWW_DIR_MAKE_COMMAND={{ cookiecutter.www_dir_make_command }}

ORG_HTML_REPORT_PAGE=include-html-reports.org
ORG_PAGES_FILES=$(wildcard page-*.org)
HTML_REPORT_FILES=$(wildcard $(REPORTS_DIR)/*/*)
HTML_PAGES_FILES=$(patsubst %.org,%.html,$(ORG_PAGES_FILES))

ORG2HTML_CMD=python $(PELICAN_DIR)/org2html.py
REPORTS2ORG_CMD= python $(PELICAN_DIR)/reports2org.py $(REPORTS_DIR)

### * Help

help:
	@echo 'Makefile for the documentation                                               '
	@echo '                                                                             '
	@echo 'Usage:                                                                       '
	@echo '   make publish         (pelican) generate pages using production settings   '
	@echo '   make serve           (pelican) serve site at http://localhost:8000        '
	@echo '   make clean           remove the generated documentation (not the reports) '
	@echo '   make upload-doc      upload the documentation to WWW                      '

### * Rules for main targets

publish: updateContent
	cd $(PELICAN_DIR); make publish

serve :
	cd $(PELICAN_DIR); make serve

clean:
	cd $(PELICAN_DIR); make clean
	rm -fr $(PELICAN_PAGES_DIR)/*
	rm -fr $(PELICAN_ARTICLES_DIR)/*
	rm -fr $(PELICAN_RESOURCES_DIR)/*
	rm -f include-html-reports.org
	rm -f ./workflow/workflow.png

upload-doc: publish
	rm -fr $(WWW_PUBLISH_DIR)
	mkdir $(WWW_PUBLISH_DIR)
	cp -r $(PELICAN_OUTPUT_DIR)/* $(WWW_PUBLISH_DIR)/
	cd $(WWW_DIR); $(WWW_DIR_MAKE_COMMAND)

### * Rules for secondary targets

updateContent: createDirs $(ORG_HTML_REPORT_PAGE) \
  $(addprefix $(PELICAN_PAGES_DIR)/, $(HTML_PAGES_FILES)) \
  ./workflow/workflow.png
	cp -r workflow $(PELICAN_RESOURCES_DIR)/
	cp -r reports $(PELICAN_RESOURCES_DIR)/

createDirs:
	mkdir -p $(PELICAN_PAGES_DIR)
	mkdir -p $(PELICAN_ARTICLES_DIR)
	mkdir -p $(PELICAN_RESOURCES_DIR)

$(PELICAN_PAGES_DIR)/page-%.html: page-%.org
	$(ORG2HTML_CMD) $<
	mv $(notdir $@) $(PELICAN_PAGES_DIR)/

./workflow/workflow.png: ./workflow/workflow.dot
	dot -Tpng workflow/workflow.dot -o workflow/workflow.png
	convert workflow/workflow.png -geometry 700 workflow/workflow-small.png

$(ORG_HTML_REPORT_PAGE): $(HTML_REPORT_FILES)
	$(REPORTS2ORG_CMD) $@
	touch page-analysis.org
