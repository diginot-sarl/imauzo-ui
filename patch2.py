import codecs

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    content = f.read()

imports = """import ConfirmDialog from './components/ui/ConfirmDialog.vue'
import HeaderWidget from './components/ui/HeaderWidget.vue'
import TimeSlotSelector from './components/ui/TimeSlotSelector.vue'
import DocumentPreview from './components/ui/DocumentPreview.vue'
import InvoiceTemplate from './components/ui/InvoiceTemplate.vue'
import Editor from './components/ui/Editor.vue'
import SuccessWidget from './components/ui/SuccessWidget.vue'
import PaymentButton from './components/ui/PaymentButton.vue'
import Link from './components/ui/Link.vue'
import Section from './components/ui/Section.vue'
import Separator from './components/ui/Separator.vue'
"""
content = content.replace("import Layout from './components/ui/Layout.vue'", imports + "import Layout from './components/ui/Layout.vue'")

state_vars = """
const selectedTime = ref('10:00')
const timeSlots = [
  { time: '08:00', available: false },
  { time: '09:00', available: true },
  { time: '10:00', available: true },
  { time: '11:00', available: true },
  { time: '14:00', available: true },
  { time: '15:00', available: false },
]
const editorContent = ref('')
const showConfirm = ref(false)
const showDocPreview = ref(false)
"""
content = content.replace("const showModal = ref(false)", state_vars + "const showModal = ref(false)")

new_sec = """        </div>
        <!-- End Grid -->

        <!-- NEW SECTION: Composants Métier -->
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
                  <Heading level="6" variant="section" class="mb-3">Modales d'actions</Heading>
                  <div class="flex flex-wrap gap-3">
                    <Button variant="danger" @click="showConfirm = true">Supprimer l'élément</Button>
                    <Button variant="secondary" @click="showDocPreview = true">Aperçu PDF métier</Button>
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
        </Section>
"""
content = content.replace("        </div>\n        <!-- End Grid -->", new_sec)

content = content.replace("  <!-- The Modal -->", """  
  <ConfirmDialog 
    v-model="showConfirm" 
    title="Supprimer définitivement ?" 
    message="Êtes-vous sûr de vouloir supprimer cet élément ? Cette action est irréversible et toutes les données associées seront perdues."
    confirmText="Oui, supprimer"
  />
  
  <DocumentPreview 
    v-model="showDocPreview"
    title="Conditions Générales.pdf"
    fileSize="2.4 MB"
    type="pdf"
    url="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
  />

  <!-- The Modal -->""")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(content)

print("Patch Phase 4 applied.")
