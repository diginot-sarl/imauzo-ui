import codecs

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

imports = """import Heading from './components/ui/Heading.vue'
import Text from './components/ui/Text.vue'
import Menu from './components/ui/Menu.vue'
import MenuItem from './components/ui/MenuItem.vue'
import MenuDivider from './components/ui/MenuDivider.vue'
"""
content = content.replace("import Layout from './components/ui/Layout.vue'", imports + "import Layout from './components/ui/Layout.vue'")

content = content.replace('<h3 class="font-semibold text-sm mb-4 text-[#65676B]">', '<Heading level="5" variant="section" class="mb-4">')
content = content.replace('<h3 class="font-semibold text-sm mb-2 text-[#65676B]">', '<Heading level="5" variant="section" class="mb-2">')
content = content.replace('</h3>', '</Heading>')

content = content.replace('<h2 class="text-lg font-bold">', '<Heading level="3">')
content = content.replace('<h2 class="text-xl font-bold mb-4 fb-text-secondary uppercase text-sm">', '<Heading level="4" variant="section" class="mb-4">')
content = content.replace('<h2 class="font-bold text-lg text-[#050505] leading-tight">', '<Heading level="3" class="leading-tight">')
content = content.replace('<h2 class="font-bold text-2xl text-[#050505]">', '<Heading level="1">')
content = content.replace('</h2>', '</Heading>')

old_dropdown = """                      <DropdownButton label="Actions rapides" variant="primary">
                        <li><a href="#">Modifier le profil</a></li>
                        <li><a href="#">Paramètres de confidentialité</a></li>
                        <li><a href="#" class="text-[#E02636]">Supprimer</a></li>
                      </DropdownButton>"""
new_dropdown = """                      <DropdownButton label="Actions rapides" variant="primary">
                        <MenuItem href="#">Modifier le profil</MenuItem>
                        <MenuItem href="#">Paramètres de confidentialité</MenuItem>
                        <MenuItem href="#" danger>Supprimer</MenuItem>
                      </DropdownButton>"""
content = content.replace(old_dropdown, new_dropdown)

old_popover = """                      <Popover width="w-72" align="end">
                        <template #trigger>
                          <Button variant="secondary">Mon Profil</Button>
                        </template>
                        <div class="flex flex-col gap-2">
                          <div class="flex items-center gap-3 p-2">
                            <div class="avatar shrink-0">
                              <div
                                class="w-10 h-10 rounded-full bg-[#E4E6EB] flex items-center justify-center font-bold text-[#050505]">
                                JD</div>
                            </div>
                            <div>
                              <p class="font-bold text-[15px] leading-tight text-[#050505]">John Doe</p>
                              <p class="text-[13px] text-[#65676B]">john.doe@example.com</p>
                            </div>
                          </div>
                          <div class="h-px bg-[#CED0D4] w-full"></div>
                          <ul class="menu p-1 w-full">
                            <li><a href="#">Paramètres</a></li>
                            <li><a href="#">Se déconnecter</a></li>
                          </ul>
                        </div>
                      </Popover>"""
new_popover = """                      <Popover width="w-72" align="end">
                        <template #trigger>
                          <Button variant="secondary">Mon Profil</Button>
                        </template>
                        <div class="flex flex-col gap-2">
                          <div class="flex items-center gap-3 p-2">
                            <div class="avatar shrink-0">
                              <div class="w-10 h-10 rounded-full bg-[#E4E6EB] flex items-center justify-center font-bold text-[#050505]">JD</div>
                            </div>
                            <div>
                              <Text weight="bold" class="leading-tight">John Doe</Text>
                              <Text variant="secondary" size="sm">john.doe@example.com</Text>
                            </div>
                          </div>
                          <MenuDivider />
                          <Menu class="w-full">
                            <MenuItem href="#">Paramètres</MenuItem>
                            <MenuItem href="#">Se déconnecter</MenuItem>
                          </Menu>
                        </div>
                      </Popover>"""
content = content.replace(old_popover, new_popover)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Replacement done successfully.")
