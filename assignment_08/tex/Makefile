NUM := 08

NAME  := assignment_$(NUM)
LATEX := $(NAME).tex
PDF   := $(NAME).pdf

AUX   :=
LATEX_AUX :=
TESTS := test_functions.py

SKELETON := /Users/oliver/Documents/Teaching/ASU/CompPhys_PHY494/2018/PHY494-assignments-skeleton/assignment_$(NUM)
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
	cp -v $(PDF) $(SKELETON)
	cp -v $(TESTS) $(AUX) $(SUBMISSION)
	cp -r $(LATEX) $(LATEX_AUX) Makefile $(TEX)

