import codecs
import re

text_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\TextInput.vue'
search_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\SearchInput.vue'
number_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\NumberInput.vue'
textarea_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\Textarea.vue'

# 1. TextInput
with codecs.open(text_input_path, 'r', 'utf-8') as f:
    text_content = f.read()

# Replace cn(...) content for input
text_content = re.sub(
    r":class=\"cn\(\s*'[^']*',\s*'[^']*',\s*(.*?\s*)\)\"",
    r""":class="cn(
                  'input input-bordered w-full bg-[#F0F2F5] focus:bg-white transition-colors text-[15px]',
                  slots.prefix ? 'pl-10' : '',
                  slots.suffix ? 'pr-10' : '',
                  error ? 'input-error bg-white' : '',
                  success ? 'input-success bg-white' : '',
                  (!error && !success) ? 'focus:input-primary' : '',
                  disabled ? 'opacity-50 cursor-not-allowed select-none' : '',
                  props.class
                )\"""",
    text_content,
    flags=re.DOTALL
)
with codecs.open(text_input_path, 'w', 'utf-8') as f:
    f.write(text_content)

# 2. SearchInput
with codecs.open(search_input_path, 'r', 'utf-8') as f:
    search_content = f.read()

search_content = re.sub(
    r"class=\"w-full bg-\[#F0F2F5\][^\"]+\"",
    r"class=\"input input-bordered w-full bg-[#F0F2F5] focus:bg-white focus:input-primary transition-colors text-[15px] pl-10 pr-10 rounded-full\"",
    search_content
)
with codecs.open(search_input_path, 'w', 'utf-8') as f:
    f.write(search_content)

# 3. NumberInput
with codecs.open(number_input_path, 'r', 'utf-8') as f:
    number_content = f.read()

number_content = re.sub(
    r"class=\"input w-full bg-\[#F0F2F5\][^\"]+\"",
    r"class=\"input input-bordered w-full bg-[#F0F2F5] focus:bg-white focus:input-primary transition-colors text-[#050505] placeholder-[#8D949E] px-3 rounded-lg input-number-clean\"",
    number_content
)
number_content = re.sub(
    r"error \? 'border-error focus:border-error bg-white' : ''",
    r"error ? 'input-error bg-white' : ''",
    number_content
)
with codecs.open(number_input_path, 'w', 'utf-8') as f:
    f.write(number_content)

# 4. Textarea
with codecs.open(textarea_path, 'r', 'utf-8') as f:
    textarea_content = f.read()

textarea_content = re.sub(
    r"class=\"w-full bg-\[#F0F2F5\][^\"]+\"",
    r"class=\"textarea textarea-bordered w-full bg-[#F0F2F5] focus:bg-white focus:textarea-primary transition-colors text-[15px] placeholder-[#8D949E] rounded-lg resize-y min-h-\[100px\]\"",
    textarea_content
)
with codecs.open(textarea_path, 'w', 'utf-8') as f:
    f.write(textarea_content)

print("DaisyUI native styles applied successfully.")
