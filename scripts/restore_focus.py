import codecs
import re

text_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\TextInput.vue'
search_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\SearchInput.vue'
number_input_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\NumberInput.vue'
textarea_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\Textarea.vue'

# 1. TextInput
with codecs.open(text_input_path, 'r', 'utf-8') as f:
    text_content = f.read()

text_content = re.sub(
    r":class=\"cn\(\s*'[^']*',\s*(?:slots\.prefix \? '[^']*' : '',\s*)+(?:slots\.suffix \? '[^']*' : '',\s*)+(?:error \? '[^']*' : '',\s*)+(?:success \? '[^']*' : '',\s*)+(?:\(!error && !success\) \? '[^']*' : '',\s*)+(?:disabled \? '[^']*' : '',\s*)+props\.class\s*\)\"",
    r""":class="cn(
                  'input w-full bg-[#F0F2F5] border border-transparent focus:bg-white transition-all text-[15px] rounded-lg h-11 focus:outline-none shadow-none',
                  slots.prefix ? 'pl-10' : '',
                  slots.suffix ? 'pr-10' : '',
                  error ? 'border-[#E41E3F] focus:border-[#E41E3F] focus:ring-4 focus:ring-[#E41E3F]/20 bg-white' : '',
                  success ? 'border-[#2FA14A] focus:border-[#2FA14A] focus:ring-4 focus:ring-[#2FA14A]/20 bg-white' : '',
                  (!error && !success) ? 'focus:border-[#0866FF] focus:ring-4 focus:ring-[#0866FF]/20' : '',
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
    r"class=\"input input-bordered w-full bg-\[#F0F2F5\][^\"]+\"",
    r"class=\"input w-full bg-[#F0F2F5] border border-transparent focus:bg-white transition-all text-[15px] pl-10 pr-10 rounded-full h-10 focus:outline-none focus:border-[#0866FF] focus:ring-4 focus:ring-[#0866FF]/20 shadow-none\"",
    search_content
)
with codecs.open(search_input_path, 'w', 'utf-8') as f:
    f.write(search_content)

# 3. NumberInput
with codecs.open(number_input_path, 'r', 'utf-8') as f:
    number_content = f.read()

number_content = re.sub(
    r"class=\"input input-bordered w-full bg-\[#F0F2F5\][^\"]+\"\s*:class=\"\[\s*error \? '[^']+' : '',\s*disabled \? '[^']+' : ''\s*\]\"",
    r"""class="input w-full bg-[#F0F2F5] border border-transparent focus:bg-white transition-all text-[#050505] placeholder:text-[#8D949E] px-3 rounded-lg h-11 focus:outline-none input-number-clean shadow-none"
            :class="[
                error ? 'border-[#E41E3F] focus:border-[#E41E3F] focus:ring-4 focus:ring-[#E41E3F]/20 bg-white' : 'focus:border-[#0866FF] focus:ring-4 focus:ring-[#0866FF]/20',
                disabled ? 'opacity-50 cursor-not-allowed' : ''
            ]\"""",
    number_content,
    flags=re.DOTALL
)
with codecs.open(number_input_path, 'w', 'utf-8') as f:
    f.write(number_content)

# 4. Textarea
with codecs.open(textarea_path, 'r', 'utf-8') as f:
    textarea_content = f.read()

textarea_content = re.sub(
    r"class=\"textarea textarea-bordered w-full bg-\[#F0F2F5\][^\"]+\"",
    r"class=\"textarea w-full bg-[#F0F2F5] border border-transparent focus:bg-white transition-all text-[15px] placeholder:[#8D949E] rounded-lg resize-y min-h-[100px] focus:outline-none focus:border-[#0866FF] focus:ring-4 focus:ring-[#0866FF]/20 shadow-none\"",
    textarea_content
)
with codecs.open(textarea_path, 'w', 'utf-8') as f:
    f.write(textarea_content)

print("Restored rounded borders and #0866FF premium focus rings.")
