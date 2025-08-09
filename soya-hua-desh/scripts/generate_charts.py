import os
import csv
import math
import pygal

BASE_DIR = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'assets', 'images')
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')


def ensure_output_dir() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def parse_year(value: str) -> float:
    if value is None:
        return float('nan')
    s = str(value).strip()
    if '-' in s and s.count('-') == 1 and not s.startswith('-'):
        a, b = s.split('-')
        try:
            return (float(a) + float(b)) / 2.0
        except Exception:
            return float('nan')
    try:
        return float(s)
    except Exception:
        return float('nan')


def plot_timeline():
    path = os.path.join(DATA_DIR, 'timeline.csv')
    if not os.path.exists(path):
        return
    rows = []
    categories = set()
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            y = parse_year(r.get('year'))
            if math.isnan(y):
                continue
            c = (r.get('category') or '').strip() or 'Uncategorized'
            categories.add(c)
            rows.append({'x': y, 'event': r.get('event', ''), 'category': c})
    categories = sorted(categories)
    cat_to_y = {c: i for i, c in enumerate(categories)}

    chart = pygal.XY(stroke=False, show_legend=True, x_title='वर्ष (BCE/CE)', y_title='श्रेणी (श्रेणी क्रमांक)')
    chart.title = '10,000 वर्षों की टाइमलाइन (सार)'
    chart.y_labels = sorted(cat_to_y.values())

    # group by category
    for c in categories:
        pts = [(r['x'], cat_to_y[c]) for r in rows if r['category'] == c]
        chart.add(c, pts)

    out = os.path.join(OUTPUT_DIR, 'timeline_overview.svg')
    chart.render_to_file(out)


def plot_math_contributions():
    path = os.path.join(DATA_DIR, 'maths_contributions.csv')
    if not os.path.exists(path):
        return
    xs, ys = [], []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                xs.append(int(float(r['year'])))
                ys.append(float(r['contributions']))
            except Exception:
                continue
    chart = pygal.Line(x_title='वर्ष', y_title='योगदान (मानकीकृत सूचक)')
    chart.title = 'गणितीय योगदान (समय के साथ)'
    chart.x_labels = [str(x) for x in xs]
    chart.add('गणित', ys)
    out = os.path.join(OUTPUT_DIR, 'math_contributions.svg')
    chart.render_to_file(out)


def plot_vedic_calendar():
    path = os.path.join(DATA_DIR, 'vedic_calendar.csv')
    if not os.path.exists(path):
        return
    months, days = [], []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            months.append(r['month'])
            try:
                days.append(int(float(r['days'])))
            except Exception:
                days.append(0)
    chart = pygal.Bar(x_title='मास', y_title='दिन')
    chart.title = 'यज्ञ/वर्ष-चक्र का सरलीकृत कैलेंडर'
    chart.x_labels = months
    chart.add('दिन', days)
    out = os.path.join(OUTPUT_DIR, 'vedic_calendar.svg')
    chart.render_to_file(out)


def plot_vedic_modern_map():
    path = os.path.join(DATA_DIR, 'vedic_modern_map.csv')
    if not os.path.exists(path):
        return
    vedic_labels = []
    modern_fields = []
    strengths = {}
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            v = r['vedic_concept']
            m = r['modern_field']
            try:
                s = float(r['strength'])
            except Exception:
                s = 0.0
            if v not in vedic_labels:
                vedic_labels.append(v)
            if m not in modern_fields:
                modern_fields.append(m)
            strengths.setdefault(m, [0.0] * len(vedic_labels))
            # ensure alignment if new vedic label added later
            for key in strengths:
                if len(strengths[key]) < len(vedic_labels):
                    strengths[key].extend([0.0] * (len(vedic_labels) - len(strengths[key])))
            idx = vedic_labels.index(v)
            strengths[m][idx] = s
    chart = pygal.Bar(x_title='वैदिक अवधारणा', y_title='संबंध की तीव्रता (0-10)', legend_at_bottom=True)
    chart.title = 'वैदिक सूत्र बनाम आधुनिक विज्ञान — तुलनात्मक मानचित्र (बार चार्ट)'
    chart.x_labels = vedic_labels
    for m in modern_fields:
        chart.add(m, strengths.get(m, [0.0] * len(vedic_labels)))
    out = os.path.join(OUTPUT_DIR, 'vedic_modern_map.svg')
    chart.render_to_file(out)


if __name__ == '__main__':
    ensure_output_dir()
    plot_timeline()
    plot_math_contributions()
    plot_vedic_calendar()
    plot_vedic_modern_map()