import codecs

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

# Insertion de la section Phase 4 avant le commentaire <!-- End Grid -->
# On cherche le bloc exact
target = """          </div>
          <!-- End Grid -->"""

replacement = """          </div>
          <!-- End Grid -->

          <!-- SECTION: Composants Métier (Phase 4) -->
          <Section class="mt-8 pt-8 border-t border-[#CED0D4]">
            <HeaderWidget title="Composants Métier & Avancés" subtitle="Phase 4 - Modèles de documents, éditeurs et paiements" />
            
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mt-6">
              <Card>
                <template #header><Heading level="4">Prise de rendez-vous & Édition</Heading></template>
                <div class="space-y-6">
                  <div>
                    <Heading level="6" variant="section" class="mb-3">Créneaux horaires (TimeSlotSelector)</Heading>
                    <TimeSlotSelector v-model="selectedTime" :slots="timeSlots" />
                  </div>
                  <Separator />
                  <div>
                    <Heading level="6" variant="section" class="mb-3">Éditeur de texte (Wysiwyg Mock)</Heading>
                    <Editor v-model="editorContent" placeholder="Tapez votre description ici..." minHeight="min-h-[120px]" />
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
                        <template #icon><Icon :icon="ThumbsUp" size="sm" /></template>
                        Aimer la page
                      </Link>
                    </div>
                  </div>
                </div>
              </Card>

              <Card class="flex flex-col justify-between">
                <template #header><Heading level="4">Transactions & Paiements</Heading></template>
                <div class="space-y-6">
                  <PaymentButton amount="129.99" currency="€" showArrow />
                  <Separator />
                  <SuccessWidget title="Paiement validé !" message="Votre commande #1234 a été confirmée avec succès.">
                    <Button variant="secondary">Voir la facture</Button>
                    <Button variant="primary">Continuer</Button>
                  </SuccessWidget>
                </div>
              </Card>
            </div>
            
            <div class="mt-8">
              <Card class="bg-[#F0F2F5] overflow-hidden">
                <template #header><Heading level="4">Modèle de Facture (InvoiceTemplate)</Heading></template>
                <div class="p-4 sm:p-8">
                  <InvoiceTemplate 
                    invoiceNumber="INV-2023-001"
                    date="12/10/2023"
                    dueDate="26/10/2023"
                    customerName="Entreprise cliente ABC"
                    status="paid"
                    :items="[
                      { description: 'Conception UI/UX', quantity: 1, unitPrice: '800.00 €', amount: '800.00 €' },
                      { description: 'Développement Frontend', quantity: 1, unitPrice: '1200.00 €', amount: '1200.00 €' }
                    ]"
                    subtotal="2000.00 €"
                    total="2400.00 €"
                    tax="400.00 €"
                  />
                </div>
              </Card>
            </div>
          </Section>"""

if target in content:
    content = content.replace(target, replacement)
    print("Insertion done.")
else:
    # Try with 10 spaces instead of 10? Let's check the grep output or just use a more lenient replace
    import re
    # Match 10 spaces followed by </div> then 10 spaces followed by <!-- End Grid -->
    content = re.sub(r'\s+</div>\s+<!-- End Grid -->', replacement, content)
    print("Regex replacement attempted.")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)
