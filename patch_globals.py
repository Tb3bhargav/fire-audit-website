import os
import glob

html_files = glob.glob(r"c:\Users\nj322ws\OneDrive\Desktop\fire audit website\*.html")

float_css = """
    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-8px); }
    }
    .animate-float {
      animation: float 4s ease-in-out infinite;
    }
"""

alive_js = """
    <script>
      // Interactive Alive Feeling script
      document.addEventListener('mousemove', (e) => {
        const x = (window.innerWidth / 2 - e.pageX) / 25;
        const y = (window.innerHeight / 2 - e.pageY) / 25;
        
        document.querySelectorAll('.interact-element').forEach((el) => {
          const speed = el.getAttribute('data-speed') || 1;
          el.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
        });
      });
      lucide.createIcons();
    </script>
</body>
"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add float CSS
    if '.animate-float' not in content:
        content = content.replace('  @layer utilities {', '  @layer utilities {\n' + float_css)
        
    # 2. Add interact js
    if 'Interactive Alive Feeling script' not in content:
        content = content.replace('<script>\n        lucide.createIcons();\n    </script>\n</body>', alive_js)
        # fallback
        if 'Interactive Alive Feeling script' not in content:
            content = content.replace('</body>', alive_js)

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Patched global CSS and JS in all files.")
