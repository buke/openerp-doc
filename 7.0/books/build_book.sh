#!/bin/bash

PAGES1_4=pages1-4
P1=${PAGES1_4}/page1.pdf
P2=${PAGES1_4}/page2.pdf
P3=${PAGES1_4}/page3.pdf
P4=${PAGES1_4}/page4.pdf
PEMPTY=${PAGES1_4}/5blankpages.pdf
BLANK_END_PAGES=1

# compute the number of blank pages at the end:
if [ -x $(which pdfinfo) ]; then
  TOTAL_PAGES=$(pdfinfo build/latex/openerp-logistic-stock-mrp-book.pdf | egrep 'Pages:' | awk '{print $2}')
  BLANK_END_PAGES=$(echo "(${TOTAL_PAGES} - 1 - 1 + 3) % 4" | bc)
  echo "Computed the number of blank pages to append at the end: ${BLANK_END_PAGES} page(s) to add."
else
  echo "Unable to compute the number of blank pages to append at the end. Using the default value: ${BLANK_END_PAGES}"
fi

if [ ! -x $(which pdftk) ]; then
  echo "You need the pdftk tool to build a book."
  exit 2
fi

if [ -d build/latex ]; then
  cd build/latex
  make clean
  make all
  cd ../..
  mkdir -p build/book
  BUILT_PDF=$(find build/latex -iname '*.pdf')
  OUTPUT_FILE=build/book/$(echo $(basename ${BUILT_PDF}) | sed -e 's/\.pdf$//').complete.pdf
  echo $OUTPUT_FILE

  if [ -e ${PAGES1_4}/page4.pdf ]; then
    # 4 pages at the beginning
    pdftk A=${P1} B=${P2} C=${P3} Z=${P4} D=${BUILT_PDF} E=${PEMPTY} cat A1-1 B1-1 C1-1 Z1-1 D2-end E1-${BLANK_END_PAGES} output ${OUTPUT_FILE}
  else
    # 3 pages at the beginning
    pdftk A=${P1} B=${P2} C=${P3} D=${BUILT_PDF} E=${PEMPTY} cat A1-1 B1-1 C1-1 D2-end E1-${BLANK_END_PAGES} output ${OUTPUT_FILE}
  fi
else
  echo "build/latex directory does not exists. Run make latex."
  exit 1
fi

