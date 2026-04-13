import codecs
file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# 1. Imports
replacement = """import ControlsDoc from './docs/ControlsDoc.vue'
import InputsDoc from './docs/InputsDoc.vue'
import DataDoc from './docs/DataDoc.vue'"""

if "InputsDoc" not in content:
    content = content.replace("import ControlsDoc from './docs/ControlsDoc.vue'", replacement)
    
# 2. Sidebar Item
sidebar_replacement = """            <SidebarItem title="Contrôles" :icon="Settings" :active="activeDoc === 'controls'" @click="activeDoc = 'controls'" />
            <SidebarItem title="Formulaires" :icon="FileText" :active="activeDoc === 'inputs'" @click="activeDoc = 'inputs'" />
            <SidebarItem title="Données" :icon="Activity" :active="activeDoc === 'data'" @click="activeDoc = 'data'" />"""

if "activeDoc === 'inputs'" not in content:
    content = content.replace("""            <SidebarItem title="Contrôles" :icon="Settings" :active="activeDoc === 'controls'" @click="activeDoc = 'controls'" />""", sidebar_replacement)

# 3. Router logic
router_replacement = """           <ControlsDoc v-else-if="activeDoc === 'controls'" />
           <InputsDoc v-else-if="activeDoc === 'inputs'" />
           <DataDoc v-else-if="activeDoc === 'data'" />"""
           
if "<InputsDoc" not in content:
     content = content.replace("""           <ControlsDoc v-else-if="activeDoc === 'controls'" />""", router_replacement)

# Remove the old static sidebar items
content = content.replace("""            <SidebarItem title="Statistiques" :icon="Activity" hasSubmenu @click="goTo('stats')" />
            <SidebarItem title="Contenu" :icon="FileText" hasSubmenu />
            <SidebarItem title="Monétisation" :icon="DollarSign" hasSubmenu />
            <SidebarItem title="Engagement" :icon="ThumbsUp" hasSubmenu />
            <SidebarItem title="Tous les outils" :icon="Briefcase" />""", "")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
print("Finished final setup update.")
