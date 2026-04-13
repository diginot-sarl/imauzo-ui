import codecs

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
with codecs.open(file_path, 'r', 'utf-8') as f:
    app_content = f.read()

# Remplacement 1: InfoCard
target_info = """                <Card class="bg-blue-50/30 border-blue-100">
                  <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center text-blue-600">
                      <Icon :icon="Briefcase" size="sm" />
                    </div>
                    <div>
                      <Heading level="5">Expertise Business</Heading>
                      <Text variant="secondary" size="xs">Outils spécialisés pour votre croissance.</Text>
                    </div>
                  </div>
                </Card>"""

replacement_info = """                <InfoCard 
                  variant="info" 
                  title="Expertise Business" 
                  description="Outils spécialisés pour votre croissance." 
                  :icon="Briefcase" 
                />"""

# Remplacement 2: Card avec InvoiceTemplate
target_card = """              <Card class="bg-[#F0F2F5] overflow-hidden">
                <template #header>
                  <Heading level="4">Modèle de Facture (InvoiceTemplate)</Heading>
                </template>
                <div class="p-2 sm:p-8">
                  <InvoiceTemplate invoiceNumber="INV-2023-001" date="12/10/2023" dueDate="26/10/2023"
                    customerName="Entreprise cliente ABC" status="paid" :items="[
                      { description: 'Conception UI/UX', quantity: 1, unitPrice: '800.00 €', amount: '800.00 €' },
                      { description: 'Développement Frontend', quantity: 1, unitPrice: '1200.00 €', amount: '1200.00 €' }
                    ]" subtotal="2000.00 €" total="2400.00 €" tax="400.00 €" />
                </div>
              </Card>"""

replacement_card = """              <Card variant="muted" bodyClass="p-2 sm:p-8">
                <template #header>
                  <Heading level="4">Modèle de Facture (InvoiceTemplate)</Heading>
                </template>
                <InvoiceTemplate invoiceNumber="INV-2023-001" date="12/10/2023" dueDate="26/10/2023"
                  customerName="Entreprise cliente ABC" status="paid" :items="[
                    { description: 'Conception UI/UX', quantity: 1, unitPrice: '800.00 €', amount: '800.00 €' },
                    { description: 'Développement Frontend', quantity: 1, unitPrice: '1200.00 €', amount: '1200.00 €' }
                  ]" subtotal="2000.00 €" total="2400.00 €" tax="400.00 €" />
              </Card>"""


if target_info in app_content:
    app_content = app_content.replace(target_info, replacement_info)

if target_card in app_content:
    app_content = app_content.replace(target_card, replacement_card)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(app_content)
    
print("Framework components applied in App.vue")
