import os
import glob
import re

ui_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui'
index_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\index.ts'

# Get all .vue files
vue_files = glob.glob(os.path.join(ui_path, '*.vue'))

exports = []

for file in vue_files:
    basename = os.path.basename(file)
    component_name = basename.replace('.vue', '')
    exports.append(f"export {{ default as {component_name} }} from './components/ui/{basename}'")

# Optionally export styles if there is an index.css or style
# exports.append("import './assets/main.css'")

index_content = "\n".join(exports)
index_content += "\n\n// Pour l'utilisation de l'ensemble du plugin Vue (optionnel si installation globale)\n"
index_content += "import type { App } from 'vue'\n"
index_content += "import * as components from './components'\n\n"

# But wait, actually explicitly typing them out is better.
# For simplicity, we just export all components. This works beautifully for Tree-Shaking!
index_content = "\n".join(exports)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)
    
print("index.ts generated successfully.")
