#!/usr/bin/env python3
"""
Markdown to HTML converter for NumPy Crash Notes
Converts markdown files to beautiful standalone HTML pages
"""

import re
import os
from pathlib import Path

def escape_html(text):
    """Escape HTML special characters"""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')

def create_html_shell(title, content, page_type='content'):
    """Create a complete HTML page with navigation and styling"""
    
    nav_link_class = {
        'readme': 'readme',
        'quick-reference': 'quick-reference',
        'notebook': 'notebook',
        'index': ''
    }
    
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{title} - NumPy Crash Notes">
    <title>{title} - NumPy Crash Notes</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=Fira+Code:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #f1f5f9;
            --card-bg: white;
            --text: #1e293b;
            --muted: #64748b;
            --primary: #667eea;
            --primary-dark: #764ba2;
            --accent: #7dd3fc;
            --success: #22c55e;
            --border: #e2e8f0;
            --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            --shadow-lg: 0 4px 12px rgba(0, 0, 0, 0.15);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            color: var(--text);
            background: var(--bg);
            line-height: 1.6;
        }}

        /* ===== Navigation ===== */
        nav.navbar {{
            background: var(--card-bg);
            border-bottom: 1px solid var(--border);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: var(--shadow);
        }}

        .nav-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 2rem;
        }}

        .nav-brand {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.5rem;
            font-weight: 900;
            color: var(--text);
            text-decoration: none;
        }}

        .nav-icon {{
            font-size: 2rem;
        }}

        .nav-links {{
            display: flex;
            gap: 2rem;
            align-items: center;
            flex-wrap: wrap;
        }}

        .nav-link {{
            color: var(--muted);
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s ease;
        }}

        .nav-link:hover,
        .nav-link.active {{
            color: var(--primary);
        }}

        /* ===== Main Content ===== */
        main {{
            max-width: 900px;
            margin: 0 auto;
            padding: 2rem;
        }}

        /* ===== Article Styles ===== */
        article {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 2.5rem;
            box-shadow: var(--shadow);
            line-height: 1.8;
        }}

        article h1 {{
            font-size: 2.5rem;
            color: var(--text);
            margin: 1.5rem 0;
            border-bottom: 3px solid var(--primary);
            padding-bottom: 1rem;
        }}

        article h2 {{
            font-size: 2rem;
            color: var(--text);
            margin: 2rem 0 1rem;
            border-bottom: 2px solid var(--primary);
            padding-bottom: 0.75rem;
        }}

        article h3 {{
            font-size: 1.5rem;
            color: var(--text);
            margin: 1.5rem 0 1rem;
            margin-top: 1.75rem;
        }}

        article h4 {{
            font-size: 1.25rem;
            color: var(--text);
            margin: 1.25rem 0 0.75rem;
        }}

        article p {{
            margin: 1.25rem 0;
            color: var(--text);
        }}

        article ul, article ol {{
            margin: 1.5rem 0;
            padding-left: 2rem;
        }}

        article li {{
            margin-bottom: 0.75rem;
            color: var(--text);
        }}

        article img {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            margin: 2rem 0;
            box-shadow: var(--shadow-lg);
        }}

        article code {{
            background: #1e293b;
            color: #e2e8f0;
            padding: 0.2em 0.5em;
            border-radius: 4px;
            font-family: 'Fira Code', monospace;
            font-size: 0.9em;
        }}

        article pre {{
            background: #1e293b;
            color: #e2e8f0;
            padding: 1.5rem;
            border-radius: 10px;
            overflow-x: auto;
            margin: 1.5rem 0;
            font-family: 'Fira Code', monospace;
            font-size: 0.9rem;
            line-height: 1.6;
            border-left: 4px solid var(--primary);
        }}

        article pre code {{
            background: transparent;
            color: inherit;
            padding: 0;
            border-radius: 0;
        }}

        article table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            border: 1px solid var(--border);
            border-radius: 10px;
            overflow: hidden;
        }}

        article thead {{
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
        }}

        article th {{
            padding: 1rem;
            text-align: left;
            font-weight: 600;
        }}

        article td {{
            padding: 1rem;
            border-bottom: 1px solid var(--border);
            color: var(--text);
        }}

        article tbody tr:hover {{
            background: rgba(102, 126, 234, 0.05);
        }}

        article a {{
            color: var(--primary);
            text-decoration: none;
            border-bottom: 1px solid transparent;
            transition: all 0.3s ease;
        }}

        article a:hover {{
            border-bottom-color: var(--primary);
        }}

        article hr {{
            margin: 2rem 0;
            border: none;
            border-top: 2px solid var(--border);
        }}

        .highlight-box {{
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
            border-left: 4px solid var(--primary);
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1.5rem 0;
        }}

        .highlight-box strong {{
            color: var(--primary);
        }}

        /* ===== Footer ===== */
        footer {{
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            color: white;
            padding: 2rem 0;
            margin-top: 4rem;
            border-top: 3px solid var(--primary);
        }}

        .footer-container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            text-align: center;
        }}

        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            flex-wrap: wrap;
            margin-bottom: 1rem;
        }}

        .footer-links a {{
            color: #cbd5e1;
            text-decoration: none;
            transition: color 0.3s ease;
        }}

        .footer-links a:hover {{
            color: white;
        }}

        .footer-bottom {{
            color: #94a3b8;
            font-size: 0.95rem;
        }}

        /* ===== Navigation Links ===== */
        .nav-section {{
            display: flex;
            gap: 1rem;
            justify-content: space-between;
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 2px solid var(--border);
        }}

        .nav-section a {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
        }}

        .nav-section a:hover {{
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }}

        /* ===== Responsive ===== */
        @media (max-width: 768px) {{
            main {{
                padding: 1rem;
            }}

            article {{
                padding: 1.5rem;
            }}

            article h1 {{
                font-size: 1.75rem;
            }}

            article h2 {{
                font-size: 1.5rem;
            }}

            .nav-container {{
                flex-direction: column;
                gap: 1rem;
            }}

            .nav-links {{
                justify-content: center;
                gap: 1rem;
            }}

            .nav-section {{
                flex-direction: column;
            }}

            .nav-section a {{
                width: 100%;
                justify-content: center;
            }}
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <a href="index.html" class="nav-brand">
                <span class="nav-icon">📊</span>
                NumPy Crash Notes
            </a>
            <div class="nav-links">
                <a href="index.html" class="nav-link">Home</a>
                <a href="readme.html" class="nav-link">Tutorial</a>
                <a href="quick-reference.html" class="nav-link">Quick Reference</a>
                <a href="notebook.html" class="nav-link">Interactive Code</a>
                <a href="https://github.com/DhruvilThummar/Numpy" target="_blank" class="nav-link">GitHub</a>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main>
        <article class="markdown-content">
{content}
        </article>
    </main>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <div class="footer-links">
                <a href="index.html">Home</a>
                <a href="readme.html">Tutorial</a>
                <a href="quick-reference.html">Quick Reference</a>
                <a href="notebook.html">Interactive Code</a>
                <a href="https://github.com/DhruvilThummar/Numpy" target="_blank">GitHub</a>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 NumPy Crash Notes. Built for learners everywhere.</p>
            </div>
        </div>
    </footer>

    <script>
        // Active navigation link
        document.addEventListener('DOMContentLoaded', function() {{
            const currentPage = window.location.pathname.split('/').pop() || 'index.html';
            document.querySelectorAll('.nav-link').forEach(link => {{
                if (link.getAttribute('href') === currentPage) {{
                    link.classList.add('active');
                }}
            }});
        }});
    </script>
</body>
</html>"""

def markdown_to_html(markdown_text):
    """Convert markdown to HTML"""
    
    # Escape HTML entities (but not already formatted code)
    lines = markdown_text.split('\n')
    html_lines = []
    in_code_block = False
    
    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            if in_code_block:
                # Extract language if specified
                lang = line[3:].strip()
                if lang:
                    html_lines.append(f'<pre><code class="{lang}">')
                else:
                    html_lines.append('<pre><code>')
            else:
                html_lines.append('</code></pre>')
            continue
        
        if in_code_block:
            # Don't escape content in code blocks
            html_lines.append(escape_html(line))
        else:
            html_lines.append(line)
    
    html = '\n'.join(html_lines)
    
    # Headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Bold and italic
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    html = re.sub(r'__(.*?)__', r'<strong>\1</strong>', html)
    html = re.sub(r'_(.*?)_', r'<em>\1</em>', html)
    
    # Links
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)
    
    # Horizontal rule
    html = re.sub(r'^---$', r'<hr>', html, flags=re.MULTILINE)
    
    # Lists
    html = re.sub(r'^- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
    # Clean up nested lists
    html = re.sub(r'</ul>\n<ul>', '\n', html)
    
    # Ordered lists
    html = re.sub(r'^\d+\. (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # Blockquotes
    html = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Paragraphs (double newline = new paragraph)
    html = re.sub(r'\n\n+', '\n</p>\n<p>\n', html)
    html = '<p>\n' + html + '\n</p>'
    
    # Clean up empty paragraphs
    html = re.sub(r'<p>\s*</p>', '', html)
    
    return html

# Read README and QUICK_REFERENCE
readme_path = Path('/workspaces/Numpy/README.md')
quick_ref_path = Path('/workspaces/Numpy/QUICK_REFERENCE.md')

if readme_path.exists():
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_md = f.read()
    
    # Convert to HTML
    readme_html = markdown_to_html(readme_md)
    readme_page = create_html_shell('NumPy Tutorial', readme_html, 'readme')
    
    with open('/workspaces/Numpy/docs/readme.html', 'w', encoding='utf-8') as f:
        f.write(readme_page)
    print("✅ Created readme.html")

if quick_ref_path.exists():
    with open(quick_ref_path, 'r', encoding='utf-8') as f:
        quick_ref_md = f.read()
    
    # Convert to HTML
    qr_html = markdown_to_html(quick_ref_md)
    qr_page = create_html_shell('Quick Reference', qr_html, 'quick-reference')
    
    with open('/workspaces/Numpy/docs/quick-reference.html', 'w', encoding='utf-8') as f:
        f.write(qr_page)
    print("✅ Created quick-reference.html")

print("\n✨ All HTML files generated successfully!")
