import codecs

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Fix triggerLoading
old_trigger = "const triggerSnackbar = () => {"
new_trigger = """const triggerLoading = () => {
  isLoading.value = true
  setTimeout(() => { isLoading.value = false }, 2000)
}
const triggerSnackbar = () => {"""
if old_trigger in content and "const triggerLoading" not in content:
    content = content.replace(old_trigger, new_trigger)

# Fix missing imports (ImagePreview and Icon) specifically around InvoiceTemplate
old_imp = "import DocumentPreview from './components/ui/DocumentPreview.vue'\\nimport InvoiceTemplate from './components/ui/InvoiceTemplate.vue'"
new_imp = "import DocumentPreview from './components/ui/DocumentPreview.vue'\\nimport ImagePreview from './components/ui/ImagePreview.vue'\\nimport Icon from './components/ui/Icon.vue'\\nimport InvoiceTemplate from './components/ui/InvoiceTemplate.vue'"

# On va être plus large pour le matching
if "import ImagePreview" not in content:
    content = content.replace("import DocumentPreview from './components/ui/DocumentPreview.vue'", 
                              "import DocumentPreview from './components/ui/DocumentPreview.vue'\\nimport ImagePreview from './components/ui/ImagePreview.vue'\\nimport Icon from './components/ui/Icon.vue'")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Synchronisation complete.")
