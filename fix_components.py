import codecs

# 1. TimeSlotSelector.vue
path_ts = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\TimeSlotSelector.vue'
with codecs.open(path_ts, 'r', 'utf-8') as f:
    ts_content = f.read()
ts_content = ts_content.replace("grid-cols-3 sm:grid-cols-4 md:grid-cols-5 gap-2.5", "grid-cols-[repeat(auto-fill,minmax(85px,1fr))] gap-2.5 w-full")
with codecs.open(path_ts, 'w', 'utf-8') as f:
    f.write(ts_content)

# 2. PaymentButton.vue
path_pb = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\PaymentButton.vue'
with codecs.open(path_pb, 'r', 'utf-8') as f:
    pb_content = f.read()
pb_content = pb_content.replace("'w-full sm:w-auto min-w-[280px] shadow-[0_4px_12px_rgba(8,102,255,0.25)] hover:shadow-[0_6px_16px_rgba(8,102,255,0.3)] transition-all'", 
                            "'w-full sm:w-auto min-w-full sm:min-w-[320px] shadow-[0_4px_12px_rgba(8,102,255,0.25)] hover:shadow-[0_6px_16px_rgba(8,102,255,0.3)] transition-all h-[52px]'")
with codecs.open(path_pb, 'w', 'utf-8') as f:
    f.write(pb_content)

# 3. InvoiceTemplate.vue
path_it = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\components\ui\InvoiceTemplate.vue'
with codecs.open(path_it, 'r', 'utf-8') as f:
    it_content = f.read()
it_content = it_content.replace("<div class=\"overflow-x-auto mb-6\">", "<div class=\"overflow-x-auto mb-6 -mx-2 px-2\">")
it_content = it_content.replace("min-w-[500px]", "min-w-[450px]")
with codecs.open(path_it, 'w', 'utf-8') as f:
    f.write(it_content)

print("Business components updated.")
