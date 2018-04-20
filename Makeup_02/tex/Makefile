NUM := 02

NAME  := makeup_$(NUM)
LATEX := $(NAME).tex
LATEX_AUX := CapacitorInBox.pdf
PDF   := $(NAME).pdf

AUX := capacitor.py
TESTS := solution/test_capacitor.py

SKELETON := /Users/oliver/Documents/Teaching/ASU/CompPhys_PHY494/2018/PHY494-assignments-skeleton/Makeup_$(NUM)
SUBMISSION := $(SKELETON)/Submission
TEX := $(SKELETON)/tex


%.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

.phony: all see copy

all: $(PDF)

see: $(PDF)
	open $^

copy: $(PDF) $(TESTS) $(AUX)
	-mkdir -p $(SKELETON)
	-mkdir $(SUBMISSION) $(TEX)
	cp -v $(PDF) $(SKELETON)
	cp -v $(TESTS) $(AUX) $(SUBMISSION)
	cp -v $(LATEX) $(LATEX_AUX) Makefile $(TEX)


