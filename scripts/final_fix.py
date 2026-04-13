import codecs
import re

modal_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\Modal.vue'
text_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\TextInput.vue'
search_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\SearchInput.vue'
number_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\NumberInput.vue'
textarea_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\Textarea.vue'

# 1. Update Modal (Replace Arrow on Left with X on Right)
with codecs.open(modal_path, 'r', 'utf-8') as f:
    modal_content = f.read()

# Make sure X is imported
if "import { X }" not in modal_content:
    if "import" in modal_content:
        modal_content = re.sub(
            r"(<script setup lang=\"ts\">)",
            r"\1\nimport { X } from 'lucide-vue-next'",
            modal_content
        )

# Replace the button markup
old_button = """<button @click="close"
                    class="absolute left-4 top-1/2 -translate-y-1/2 w-[36px] h-[36px] rounded-full bg-[#E4E6EB] hover:bg-[#D8DADF] flex items-center justify-center transition-colors">
                    <svg class="w-5 h-5 text-[#050505]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
                    </svg>
                </button>"""

new_button = """<button @click="close"
                    class="absolute right-4 top-1/2 -translate-y-1/2 w-[36px] h-[36px] rounded-full bg-[#E4E6EB] hover:bg-[#D8DADF] flex items-center justify-center transition-colors text-[#65676B]">
                    <X class="w-5 h-5" stroke-width="2.5" />
                </button>"""

if "d=\"M10 19l-7-7" in modal_content:
    modal_content = modal_content.replace(old_button, new_button)

with codecs.open(modal_path, 'w', 'utf-8') as f:
    f.write(modal_content)

# 2. Strip 'input' class from all Inputs + add 'block appearance-none w-full'
with codecs.open(text_input_path, 'r', 'utf-8') as f:
    content = f.read()
content = content.replace("'input w-full bg-[#F0F2F5]", "'block appearance-none w-full bg-[#F0F2F5]")
with codecs.open(text_input_path, 'w', 'utf-8') as f:
    f.write(content)

with codecs.open(search_input_path, 'r', 'utf-8') as f:
    content = f.read()
content = content.replace("class=\"input w-full bg-[#F0F2F5]", "class=\"block appearance-none w-full bg-[#F0F2F5]")
with codecs.open(search_input_path, 'w', 'utf-8') as f:
    f.write(content)

with codecs.open(number_input_path, 'r', 'utf-8') as f:
    content = f.read()
content = content.replace("class=\"input w-full bg-[#F0F2F5]", "class=\"block appearance-none w-full bg-[#F0F2F5]")
with codecs.open(number_input_path, 'w', 'utf-8') as f:
    f.write(content)

with codecs.open(textarea_path, 'r', 'utf-8') as f:
    content = f.read()
content = content.replace("class=\"textarea w-full bg-[#F0F2F5]", "class=\"block appearance-none w-full bg-[#F0F2F5] p-3")
with codecs.open(textarea_path, 'w', 'utf-8') as f:
    f.write(content)

print("Modal 'X' restored and DaisyUI 'input' class stripped for perfect fidelity rings.")
