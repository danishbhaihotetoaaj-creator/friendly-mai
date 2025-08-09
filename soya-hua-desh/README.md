# "सोया हुआ देश" — भारत के 10,000 वर्षों का बहु-आयामी अध्ययन (eBook)

यह रिपोजिटरी 200+ पृष्ठ की एक शोध-आधारित eBook बनाने के लिए तैयार की गई है। परियोजना में अध्याय-वार Markdown फ़ाइलें, स्रोत-सूची (BibTeX), डेटा-आधारित चार्ट/ग्राफ़, और स्वचालित बिल्ड सिस्टम (Pandoc) शामिल हैं।

## विशेषताएँ
- हिंदी में अध्याय-वार सामग्री (संस्कृत/अंग्रेज़ी उद्धरण जहाँ आवश्यक)
- हर अध्याय में संदर्भ (in-text citations) और अंत में स्रोत-सूची
- डेटा-आधारित चार्ट/ग्राफ़ स्वचालित रूप से `scripts/generate_charts.py` से निर्मित
- Pandoc आधारित HTML/EPUB/PDF आउटपुट (यदि LaTeX/Pandoc उपलब्ध हों)

## प्रोजेक्ट संरचना
```
soya-hua-desh/
  chapters/               # अध्याय-वार Markdown फ़ाइलें
  assets/
    images/               # निर्यातित चार्ट/इंफोग्राफिक्स
    figures/              # अन्य आकृतियाँ/मानचित्र
  data/                   # CSV/TSV डेटा फ़ाइलें (चार्ट हेतु)
  scripts/
    generate_charts.py    # चार्ट/ग्राफ़ उत्पन्न करने का Python स्क्रिप्ट
  references.bib          # BibTeX स्रोत-सूची
  master_prompt.md        # लेखन के लिए मास्टर प्रॉम्प्ट व शैली-मार्गदर्शिका
  metadata.yaml           # Pandoc मेटाडेटा (शीर्षक, भाषा, आदि)
  Makefile                # बिल्ड टार्गेट्स: charts, html, epub, pdf
  requirements.txt        # Python निर्भरताएँ (चार्ट हेतु)
  README.md
```

## त्वरित शुरुआत
1) Python निर्भरता स्थापित करें:
```
pip install -r requirements.txt
```

2) चार्ट/ग्राफ़ उत्पन्न करें:
```
python scripts/generate_charts.py
```

3) eBook बिल्ड (Pandoc आवश्यक):
- HTML:
```
make html
```
- EPUB:
```
make epub
```
- PDF (LaTeX आवश्यक):
```
make pdf
```

यदि Pandoc/LaTeX उपलब्ध नहीं हैं, तो पहले उन्हें स्थापित करें या केवल HTML/EPUB बनाएं।

## अध्याय क्रम
- `01-introduction.md`
- `02-vedic-era.md`
- `03-epic-age.md`
- `04-knowledge-centres.md`
- `05-math-science-tech.md`
- `06-medieval-colonial.md`
- `07-modern-india.md`
- `08-comparative-analysis.md`
- `09-charts-timelines.md`
- `10-conclusion.md`

## लेखन और संदर्भ शैली
- प्राथमिक/द्वितीयक स्रोतों का उपयोग करें; हर तथ्य के साथ संदर्भ दें: `... [@key, p. 123]`।
- सभी संदर्भ `references.bib` में BibTeX प्रविष्टि के रूप में रखें।
- संस्कृत श्लोक: देवनागरी + IAST Transliteration + अनुवाद + संक्षिप्त व्याकरणिक टिप्पणी।
- चार्ट हेतु डेटा `data/` में CSV के रूप में जोड़ें और कोड में पाथ अपडेट करें।

## योगदान कैसे करें
- नए अनुभाग जोड़ते समय उपशीर्षक रखें, सूचियाँ/तालिकाएँ साफ़-सुथरी बनाएं।
- चित्रों को `assets/images/` या `assets/figures/` में रखें और Markdown में सापेक्ष पथ से एम्बेड करें।
- लंबे अध्यायों के अंत में "संक्षेप" सेक्शन जोड़ें।

## लाइसेंस
शैक्षिक/अनुसंधान उद्देश्य के लिए। कृपया मूल स्रोतों का आदर करें और उचित श्रेय दें।