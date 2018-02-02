NAME  := assignment_01
LATEX := $(NAME).tex
PDF   := $(NAME).pdf


%.pdf: %.tex
	pdflatex $<
	pdflatex $<

.phony: all

all: $(PDF)

see: $(PDF)
	open $^


