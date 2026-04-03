import re
import os
import glob

html_files = glob.glob("*.html")

global_css_path = "css/global.css"
main_js_path = "js/main.js"
article_css_path = "css/article.css"

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

style_match = re.search(r"<style>(.*?)</style>", content, re.DOTALL)
if style_match:
    global_css = style_match.group(1).strip()
    with open(global_css_path, "w", encoding="utf-8") as f:
        f.write(global_css)

script_match = re.search(r"<script>\s*document\.addEventListener\('DOMContentLoaded'.*?</script>", content, re.DOTALL)
if script_match:
    main_js_content = re.search(r"<script>(.*?)</script>", script_match.group(0), re.DOTALL).group(1).strip()
    with open(main_js_path, "w", encoding="utf-8") as f:
        f.write(main_js_content)

with open("action_interview_001.html", "r", encoding="utf-8") as f:
    article_content = f.read()
    
style_blocks = re.findall(r"<style>(.*?)</style>", article_content, re.DOTALL)
article_css = ""
if len(style_blocks) > 1:
    article_css = style_blocks[1].strip()
    with open(article_css_path, "w", encoding="utf-8") as f:
        f.write(article_css)

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Replace all matching global styles
    html_content = re.sub(r"<style>\s+:root\s+{.*?</style>", '<link rel="stylesheet" href="css/global.css">', html_content, flags=re.DOTALL)
    
    # Replace all matching article styles
    if article_css:
        html_content = re.sub(r"<style>\s+\.breadcrumb.*?</style>", '<link rel="stylesheet" href="css/article.css">', html_content, flags=re.DOTALL)

    # Replace scripts
    html_content = re.sub(r"<script>\s*document\.addEventListener\('DOMContentLoaded'.*?</script>", '<script src="js/main.js"></script>', html_content, flags=re.DOTALL)

    # Clean <title> in action_interview_001.html
    html_content = re.sub(r"<title>CUE \| ([\s\S]*?)\nShort Description:[\s\S]*?</title>", r"<title>CUE | \1</title>", html_content)
    
    # Clean <h1> in action_interview_001.html
    html_content = re.sub(r"(<h1[^>]*>[\s\S]*?)\nShort Description:[\s\S]*?(</h1>)", r"\1\2", html_content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(html_content)

print("Refactoring done.")
