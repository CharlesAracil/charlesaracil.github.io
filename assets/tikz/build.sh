#!/bin/bash

# THIS SCRIPT MUST BE EXECUTED FROM ITS DIRECTORY!

pdflatex password-certification-hashing.tex
pdflatex password-certification-creation.tex
pdflatex password-certification-login.tex

convert -density 300 password-certification-hashing.pdf -resize 50% -quality 90 password-certification-hashing.png
convert -density 300 password-certification-creation.pdf -resize 55% -quality 90 password-certification-creation.png
convert -density 300 password-certification-login.pdf -resize 740x -quality 90 password-certification-login.png

mv *.png ../figures/
