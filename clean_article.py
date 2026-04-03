import re
with open("action_interview_001.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace <div class="article-body" style="..."> with <div class="article-body">
content = re.sub(r'<div class="article-body" style="[^"]*">', '<div class="article-body">', content)

# Remove all inline styles from p, h2, blockquote within article-body
# A simple way is to find <p style="...">, <h2 style="...">, <blockquote style="...">
content = re.sub(r'<p style="[^"]*">', '<p>', content)
content = re.sub(r'<h2 style="[^"]*">', '<h2>', content)
content = re.sub(r'<blockquote style="[^"]*">', '<blockquote>', content)

# Clean up top header info styles
content = re.sub(r'<h1 style="[^"]*">', '<h1>', content)
content = re.sub(r'<p style="[^"]*">\s*도서관 대신 공연장으로\s*</p>', '<p class="lead-text">\n                 도서관 대신 공연장으로\n            </p>', content)

# Simplify previous/next nav classes to use article-nav instead of inline
content = re.sub(r'<div style="margin-top: 80px; padding-top: 40px; border-top: 1px solid var\(--border-color-dark\); display: grid; grid-template-columns: 1fr 1fr; gap: 24px;">', '<div class="article-nav">', content)

# the previous/next card inline margin
content = re.sub(r'<a href="action\.html" class="window-card dark-context" style="margin-bottom: 0;">', '<a href="action.html" class="window-card dark-context">', content)


with open("action_interview_001.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Inline styles cleaned.")
