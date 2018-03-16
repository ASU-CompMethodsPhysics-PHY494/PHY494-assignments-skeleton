NUM := 07
NAME  := assignment_$(NUM)
LATEX := $(NAME).tex
PDF   := $(NAME).pdf

AUX   := hw07.py ode.py 
LATEX_AUX :=  $(NAME).bib physbiol-natbib.bst
TESTS := test_baseball.py

SKELETON := /Users/oliver/Documents/Teaching/ASU/CompPhys_PHY494/2018/PHY494-assignments-skeleton/assignment_$(NUM)
SUBMISSION := $(SKELETON)/Submission
TEX := $(SKELETON)/tex


%.pdf: %.tex
	pdflatex -shell-escape $<
	bibtex $*
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
	cp -r figs $(LATEX) $(LATEX_AUX) Makefile $(TEX)

