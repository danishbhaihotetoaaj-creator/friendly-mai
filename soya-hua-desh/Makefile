TITLE = "सोया हुआ देश"
AUTHOR = ""
OUTDIR = build
CHAPTERS = \
  chapters/01-introduction.md \
  chapters/02-vedic-era.md \
  chapters/03-epic-age.md \
  chapters/04-knowledge-centres.md \
  chapters/05-math-science-tech.md \
  chapters/06-medieval-colonial.md \
  chapters/07-modern-india.md \
  chapters/08-comparative-analysis.md \
  chapters/09-charts-timelines.md \
  chapters/10-conclusion.md

PANDOC_OPTS = \
  --from markdown+smart \
  --toc --toc-depth=3 \
  --metadata title=$(TITLE) \
  --metadata author=$(AUTHOR) \
  --metadata-file=metadata.yaml \
  --citeproc \
  --bibliography=references.bib \
  --resource-path=.:./assets:./chapters \
  --embed-resources \
  --standalone

all: charts html

charts:
	python scripts/generate_charts.py

html: | $(OUTDIR)
	bash scripts/pandoc.sh $(PANDOC_OPTS) $(CHAPTERS) -o $(OUTDIR)/book.html

epub: | $(OUTDIR)
	bash scripts/pandoc.sh $(PANDOC_OPTS) $(CHAPTERS) -o $(OUTDIR)/book.epub

pdf: html
	. .venv/bin/activate 2>/dev/null || true; python scripts/html_to_pdf.py $(OUTDIR)/book.html $(OUTDIR)/book.pdf

$(OUTDIR):
	mkdir -p $(OUTDIR)

clean:
	rm -rf $(OUTDIR)