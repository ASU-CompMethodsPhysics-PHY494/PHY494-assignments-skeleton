NAME  := project_1
LATEX := $(NAME).tex
PDF   := $(NAME).pdf

SKELETON := $(HOME)/Documents/Teaching/ASU/CompPhys_PHY494/2018/PHY494-assignments-skeleton/$(NAME)
TEX := $(SKELETON)/tex

%.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

.phony: all see copy

all: $(PDF)

see: $(PDF)
	open $^

copy: $(PDF)
	-mkdir -p $(SKELETON)
	-mkdir $(TEX)
	cp $^ $(SKELETON)
	cp $(LATEX) Makefile $(TEX)

