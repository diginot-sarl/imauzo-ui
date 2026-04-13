import codecs

# 4. App.vue refactor Phase 4 Section
path_app = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(path_app, 'r', 'utf-8') as f:
    app_content = f.read()

# On cherche le bloc de la Phase 4 pour le rendre plus aéré
# On remplace lg:grid-cols-2 par xl:grid-cols-2 et on améliore les Cards
target = """            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-6">
              <Card>
                <template #header>
                  <Heading level="4">Prise de rendez-vous & Édition</Heading>
                </template>
                <div class="space-y-6">
                  <div>
                    <Heading level="6" variant="section" class="mb-3">Créneaux horaires (TimeSlotSelector)</Heading>
                    <TimeSlotSelector v-model="selectedTime" :slots="timeSlots" />
                  </div>
                  <Separator />
                  <div>
                    <Heading level="6" variant="section" class="mb-3">Éditeur de texte (Wysiwyg Mock)</Heading>
                    <Editor v-model="editorContent" placeholder="Tapez votre description ici..."
                      minHeight="min-h-[120px]" />
                  </div>
                  <Separator />
                  <div>
                    <Heading level="6" variant="section" class="mb-3">Modales d'actions & Liens</Heading>
                    <div class="flex flex-wrap gap-3 mb-4">
                      <Button variant="danger" @click="showConfirm = true">Supprimer</Button>
                      <Button variant="secondary" @click="showDocPreview = true">Voir PDF</Button>
                      <Button variant="secondary" @click="showImagePreview = true">Voir Image</Button>
                    </div>
                    <div class="flex gap-4 items-center bg-[#F0F2F5] p-3 rounded-lg">
                      <Link href="#" class="!text-[#65676B]">Retour à la liste</Link>
                      <Separator vertical class="h-4" />
                      <Link href="#" external>
                        <template #icon>
                          <Icon :icon="ThumbsUp" size="sm" />
                        </template>
                        Aimer la page
                      </Link>
                    </div>
                  </div>
                </div>
              </Card>

              <Card class="flex flex-col justify-between">
                <template #header>
                  <Heading level="4">Transactions & Paiements</Heading>
                </template>
                <div class="space-y-6">
                  <PaymentButton amount="129.99" currency="€" showArrow />
                  <Separator />
                  <SuccessWidget title="Paiement validé !" message="Votre commande #1234 a été confirmée avec succès.">
                    <Button variant="secondary">Voir la facture</Button>
                    <Button variant="primary">Continuer</Button>
                  </SuccessWidget>
                </div>
              </Card>
            </div>"""

replacement = """            <div class="grid grid-cols-1 xl:grid-cols-2 gap-8 mt-6">
              <Card class="h-full">
                <template #header>
                  <Heading level="4">Prise de rendez-vous & Édition</Heading>
                </template>
                <div class="space-y-6">
                  <div>
                    <Heading level="6" variant="section" class="mb-4">Créneaux horaires (TimeSlotSelector)</Heading>
                    <TimeSlotSelector v-model="selectedTime" :slots="timeSlots" />
                  </div>
                  <Separator />
                  <div>
                    <Heading level="6" variant="section" class="mb-4">Éditeur de texte (Wysiwyg Mock)</Heading>
                    <Editor v-model="editorContent" placeholder="Tapez votre description ici..."
                      minHeight="min-h-[150px]" />
                  </div>
                  <Separator />
                  <div>
                    <Heading level="6" variant="section" class="mb-4">Modales d'actions & Liens</Heading>
                    <div class="flex flex-wrap gap-3 mb-4">
                      <Button variant="danger" @click="showConfirm = true">Supprimer</Button>
                      <Button variant="secondary" @click="showDocPreview = true">Voir PDF</Button>
                      <Button variant="secondary" @click="showImagePreview = true">Voir Image</Button>
                    </div>
                    <div class="flex flex-wrap gap-4 items-center bg-[#F0F2F5] p-4 rounded-lg">
                      <Link href="#" class="!text-[#65676B]">Retour à la liste</Link>
                      <Separator vertical class="h-4 hidden sm:block" />
                      <Link href="#" external>
                        <template #icon>
                          <Icon :icon="ThumbsUp" size="sm" />
                        </template>
                        Aimer la page
                      </Link>
                    </div>
                  </div>
                </div>
              </Card>

              <div class="space-y-8">
                <Card>
                  <template #header>
                    <Heading level="4">Transactions & Paiements</Heading>
                  </template>
                  <div class="space-y-6">
                    <div class="flex justify-center sm:justify-start">
                      <PaymentButton amount="129.99" currency="€" showArrow />
                    </div>
                    <Separator />
                    <SuccessWidget title="Paiement validé !" message="Votre commande #1234 a été confirmée avec succès.">
                      <Button variant="secondary" class="flex-1 sm:flex-none">Voir la facture</Button>
                      <Button variant="primary" class="flex-1 sm:flex-none">Continuer</Button>
                    </SuccessWidget>
                  </div>
                </Card>

                <Card class="bg-blue-50/30 border-blue-100">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600">
                      <Icon :icon="Briefcase" size="sm" />
                    </div>
                    <div>
                      <Heading level="5">Expertise Business</Heading>
                      <Text variant="secondary" size="xs">Outils spécialisés pour votre croissance.</Text>
                    </div>
                  </div>
                </Card>
              </div>
            </div>"""

if target in app_content:
    app_content = app_content.replace(target, replacement)
    # Patch padding facture
    app_content = app_content.replace('<div class="p-4 sm:p-8">', '<div class="p-2 sm:p-8">')
    print("App.vue refactored.")
else:
    print("Target not found in App.vue manually. Trying more loose match...")
    import re
    app_content = re.sub(r'<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-6">.*?<SuccessWidget title="Paiement validé !" message="Votre commande #1234 a été confirmée avec succès.">.*?<Button variant="primary">Continuer</Button>.*?<\/SuccessWidget>.*?<\/div>.*?<\/Card>.*?<\/div>', replacement, app_content, flags=re.DOTALL)
    print("Regex replacement attempted.")

with codecs.open(path_app, 'w', 'utf-8') as f:
    f.write(app_content)
