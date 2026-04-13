import codecs

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Fix import
if "import ButtonDoc from './docs/ButtonDoc.vue'" not in content:
    content = content.replace(
        "import AvatarDoc from './docs/AvatarDoc.vue'",
        "import AvatarDoc from './docs/AvatarDoc.vue'\nimport ButtonDoc from './docs/ButtonDoc.vue'"
    )

if "PlusSquare" not in content:
    content = content.replace("Shield, Briefcase", "Shield, Briefcase, PlusSquare")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
print("Updated App.vue imports")
