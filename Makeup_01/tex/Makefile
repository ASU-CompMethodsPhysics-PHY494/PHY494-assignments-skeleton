NUM := 01

NAME  := makeup_$(NUM)
LATEX := $(NAME).tex
LATEX_AUX :=
PDF   := $(NAME).pdf

AUX := makeup01.py
TESTS := solution/test_makeup01.py

SKELETON := /Users/oliver/Documents/Teaching/ASU/CompPhys_PHY494/2018/PHY494-assignments-skeleton/Makeup_$(NUM)
SUBMISSION := $(SKELETON)/Submission
TEX := $(SKELETON)/tex


%.pdf: %.tex
	pdflatex $<
	pdflatex $<

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

