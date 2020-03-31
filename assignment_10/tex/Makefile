NUM := 10
YEAR := 2020

NAME  := assignment_$(NUM)
LATEX := $(NAME).tex
PDF   := $(NAME).pdf

AUX   := final_overview_2019.pdf
LATEX_AUX :=
TESTS := test_functions.py

SKELETON := /Users/oliver/Documents/Teaching/ASU/CompPhys_PHY494/$(YEAR)/PHY494-assignments-skeleton/assignment_$(NUM)
SUBMISSION := $(SKELETON)/Submission
TEX := $(SKELETON)/tex


%.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

.phony: all copy

all: $(PDF)

see: $(PDF)
	open $^

copy: $(PDF) $(TESTS) $(AUX)
	-mkdir -p $(SKELETON)
	-mkdir $(SUBMISSION) $(TEX)
	cp -v $(PDF) $(AUX) $(SKELETON)
	cp -v $(TESTS) $(SUBMISSION)
	cp -r $(LATEX) $(LATEX_AUX) Makefile $(TEX)

