import re, hashlib, base64, glob

known_hashes = {
    "QPWJdH2Xx2v2CzE8RVy5L9rC6fhIET9Pnixbid924r4=",
    "VCvmqXiWJiFhvLS+C/PK66WI9nwXxcE6SbvzEM9gxWo=",
    "YAhqsGAb4rs+S5kO4XH1/9mGQq/8NQVJLKJrhNpdFo8=",
    "sIQZEeUKs3m0A0BCZOn3F1h6UL7MV2YEDi2FUm+m0Jg=",
}

script_pattern = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', re.DOTALL | re.IGNORECASE)
style_pattern = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL | re.IGNORECASE)

for filepath in sorted(glob.glob('check_*.html')):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    new_found = False
    for label, pattern in [('script', script_pattern), ('style', style_pattern)]:
        for m in pattern.finditer(html):
            content = m.group(1)
            h = base64.b64encode(hashlib.sha256(content.encode('utf-8')).digest()).decode()
            if h not in known_hashes:
                new_found = True
                print(f"[NOWY HASH] {filepath} <{label}>: sha256-{h}")
                print(f"  preview: {content[:80]!r}")

    if not new_found:
        print(f"[OK] {filepath} — brak nowych bloków")