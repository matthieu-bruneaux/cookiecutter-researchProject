.PHONY: help run report

### * Variables

CURRENT_DIR=010-first-module
DATA_DIR=../../data/derived/$(CURRENT_DIR)
REPORT_DIR=../../documentation/reports/$(CURRENT_DIR)

### * Help

help:
	@echo 'Makefile for $(CURRENT_DIR)                                       '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make run               run the local pipeline                       '
	@echo '   make report            move html reports to the doc folder          '
	@echo '   make all               make run and report                          '

### * Rules for main targets

run:
	mkdir -p $(DATA_DIR)

report :
	mkdir -p $(REPORT_DIR)
	mv *.html $(REPORT_DIR)/

all : run report
