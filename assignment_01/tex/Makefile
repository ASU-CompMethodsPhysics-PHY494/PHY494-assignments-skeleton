NAME  := assignment_01
LATEX := $(NAME).tex
PDF   := $(NAME).pdf

SKELETON := $(HOME)/Documents/Teaching/ASU/CompPhys_PHY494/2019/PHY494-assignments-skeleton/$(NAME)
SUBMISSION := $(SKELETON)/Submission
TEX := $(SKELETON)/tex


%.pdf: %.tex
	pdflatex $<
	pdflatex $<

.phony: all see copy

all: $(PDF)

see: $(PDF)
	open $^

copy: $(PDF)
	-mkdir -p $(SKELETON)
	-mkdir $(SUBMISSION) $(TEX)
	cp $^ $(SKELETON)
	cp $(LATEX) Makefile $(TEX)

