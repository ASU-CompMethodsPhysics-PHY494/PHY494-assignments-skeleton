NAME  := assignment_02
LATEX := $(NAME).tex
PDF   := $(NAME).pdf


%.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

.phony: all

all: $(PDF)

see: $(PDF)
	open $^


