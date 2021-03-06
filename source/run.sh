cd ../
mkdir -p output
cd source

python pendulum_with_friction.py
pdflatex report.tex
bibtex report.aux
pdflatex report.tex
pdflatex report.tex

mv report.pdf ../output

rm ../output/pendulum.png
rm *.aux *.log *.out *.bbl *.blg
