import codecs
file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Fix the missing imports
replacement = """import OTPInputDoc from './docs/OTPInputDoc.vue'
import DropdownDoc from './docs/DropdownDoc.vue'
import ControlsDoc from './docs/ControlsDoc.vue'"""

if "DropdownDoc" not in content:
    content = content.replace("import OTPInputDoc from './docs/OTPInputDoc.vue'", replacement)
    
with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
print("Finished imports update.")
