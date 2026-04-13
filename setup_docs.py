import codecs

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Inject activeDoc state and Vue component tracking
if "const activeDoc = ref('legacy')" not in content:
    content = content.replace(
        "import { ref } from 'vue'",
        "import { ref, defineAsyncComponent } from 'vue'"
    )
    # import AvatarDoc somewhere
    content = content.replace(
        "import Avatar from './components/ui/Avatar.vue'",
        "import Avatar from './components/ui/Avatar.vue'\nimport AvatarDoc from './docs/AvatarDoc.vue'"
    )
    if "import AvatarDoc" not in content: # If Avatar itself wasn't directly imported
        content = content.replace(
            "import Checkbox from './components/ui/Checkbox.vue'",
            "import Checkbox from './components/ui/Checkbox.vue'\nimport AvatarDoc from './docs/AvatarDoc.vue'"
        )

    # State activeDoc
    content = content.replace(
        "const selectedTime = ref('10:00')",
        "const activeDoc = ref('legacy')\nconst selectedTime = ref('10:00')"
    )

# 2. Update Sidebar links
sidebar_anchor = """            <SidebarItem icon="Home" label="Vue d'ensemble" active />
            <SidebarItem icon="Users" label="Clients" />
            <SidebarItem icon="FileText" label="Devis" />
            <SidebarItem icon="Activity" label="Rapports" />
            <SidebarItem icon="Briefcase" label="Paramètres" />"""

sidebar_replacement = """            <SidebarItem icon="Home" label="Vue d'ensemble" :active="activeDoc === 'legacy'" @click="activeDoc = 'legacy'" />
            <SidebarItem icon="Users" label="Avatar" :active="activeDoc === 'avatar'" @click="activeDoc = 'avatar'" />
            <SidebarItem icon="FileText" label="Bouton (WIP)" disabled />
            <SidebarItem icon="Activity" label="Rapports" disabled />
            <SidebarItem icon="Briefcase" label="Paramètres" disabled />"""

content = content.replace(sidebar_anchor, sidebar_replacement)

# 3. Main layout wrapper
wrap_anchor_start = '<main class="flex-1 p-4 sm:p-10 z-0 overflow-y-auto">\n      <div class="max-w-7xl mx-auto space-y-12">'
wrap_anchor_alt = '<main class="flex-1 p-6 sm:p-10 z-0 overflow-y-auto">\n      <div class="max-w-7xl mx-auto space-y-12">'

wrap_replacement_start = """<main class="flex-1 p-6 sm:p-10 z-0 overflow-y-auto">
      <div class="max-w-7xl mx-auto space-y-12">
        <KeepAlive>
           <AvatarDoc v-if="activeDoc === 'avatar'" />
        </KeepAlive>
        
        <div v-show="activeDoc === 'legacy'" class="space-y-12">"""

# Close the wrapper div just above Render Snackbar
wrap_anchor_end = '<!-- Render Snackbar'
wrap_replacement_end = """        </div> <!-- End of Legacy Layout -->
      <!-- Render Snackbar"""

# Perform replacement
if '<div v-show="activeDoc === \'legacy\'" class="space-y-12">' not in content:
    if wrap_anchor_start in content:
        content = content.replace(wrap_anchor_start, wrap_replacement_start)
        content = content.replace(wrap_anchor_end, wrap_replacement_end)
    elif wrap_anchor_alt in content:
        content = content.replace(wrap_anchor_alt, wrap_replacement_start)
        content = content.replace(wrap_anchor_end, wrap_replacement_end)
    else:
        print("Could not find wrap anchors")
else:
    print("Already wrapped!")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
print("Docs setup successful.")
