import re, hashlib, base64

with open('page.html', 'r', encoding='utf-8') as f:
    html = f.read()

script_pattern = re.compile(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', re.DOTALL | re.IGNORECASE)
style_pattern = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL | re.IGNORECASE)

print("=== Inline <script> blocks (no src) ===")
for i, m in enumerate(script_pattern.finditer(html), 1):
    content = m.group(1)
    h = base64.b64encode(hashlib.sha256(content.encode('utf-8')).digest()).decode()
    print(f"Block {i}: sha256-{h}")
    print(f"  length={len(content)} preview={content[:60]!r}")

print()
print("=== Inline <style> blocks ===")
for i, m in enumerate(style_pattern.finditer(html), 1):
    content = m.group(1)
    h = base64.b64encode(hashlib.sha256(content.encode('utf-8')).digest()).decode()
    print(f"Block {i}: sha256-{h}")
    print(f"  length={len(content)} preview={content[:60]!r}")