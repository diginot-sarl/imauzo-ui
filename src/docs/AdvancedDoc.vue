<script setup lang="ts">
import { ref } from 'vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import TimeSlotSelector from '../components/ui/TimeSlotSelector.vue'
import Editor from '../components/ui/Editor.vue'
import Button from '../components/ui/Button.vue'
import Link from '../components/ui/Link.vue'
import Separator from '../components/ui/Separator.vue'
import Icon from '../components/ui/Icon.vue'
import PaymentButton from '../components/ui/PaymentButton.vue'
import SuccessWidget from '../components/ui/SuccessWidget.vue'
import InfoCard from '../components/ui/InfoCard.vue'
import InvoiceTemplate from '../components/ui/InvoiceTemplate.vue'
import DocumentPreview from '../components/ui/DocumentPreview.vue'
import ImagePreview from '../components/ui/ImagePreview.vue'
import ConfirmDialog from '../components/ui/ConfirmDialog.vue'
import { ThumbsUp, Briefcase } from 'lucide-vue-next'

const selectedTime = ref('10:00')
const timeSlots = [
  { time: '08:00', available: false },
  { time: '09:00', available: true },
  { time: '10:00', available: true }
]
const editorContent = ref('')
const showConfirm = ref(false)
const showDocPreview = ref(false)
const showImagePreview = ref(false)
</script>

<template>
  <div class="space-y-10 animate-in fade-in duration-500 pb-16">
    <div>
      <Heading level="2" class="mb-2">Composants Métier (Avancés)</Heading>
      <Text variant="secondary" size="lg">Structures complexes pour les modules SaaS (Facturation, Éditeurs, Réservations).</Text>
    </div>

    <Section title="Prise de rendez-vous">
      <TimeSlotSelector v-model="selectedTime" :slots="timeSlots" />
    </Section>

    <Section title="Éditeur de texte riche">
      <Editor v-model="editorContent" placeholder="Tapez votre description ici..." minHeight="min-h-[150px]" />
    </Section>

    <Section title="Modales & Visionneuses">
      <div class="flex flex-wrap gap-3">
        <Button variant="danger" @click="showConfirm = true">Modale Supression</Button>
        <Button variant="secondary" @click="showDocPreview = true">Modale PDF</Button>
        <Button variant="secondary" @click="showImagePreview = true">Modale Image</Button>
      </div>
    </Section>

    <Section title="Paiements & Succès">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <PaymentButton amount="129.99" currency="€" showArrow class="w-fit" />
        <InfoCard variant="info" title="Expertise Business" description="Outils spécialisés pour votre croissance." :icon="Briefcase" />
      </div>
      <div class="mt-4">
        <SuccessWidget title="Paiement validé !" message="Votre commande a été confirmée.">
          <Button variant="secondary">Facture</Button>
          <Button variant="primary">Continuer</Button>
        </SuccessWidget>
      </div>
    </Section>

    <Section title="Modèle Facture">
      <InvoiceTemplate invoiceNumber="INV-2023-001" date="12/10/2023" dueDate="26/10/2023" customerName="Entreprise ABC" status="paid" :items="[{ description: 'Développement Frontend', quantity: 1, unitPrice: '1200.00 €', amount: '1200.00 €' }]" subtotal="1200.00 €" total="1200.00 €" tax="0.00 €" />
    </Section>

    <ConfirmDialog v-model="showConfirm" title="Supprimer définitivement ?" message="Êtes-vous sûr de vouloir supprimer ?" confirmText="Oui, supprimer" />
    <DocumentPreview v-model="showDocPreview" title="Conditions.pdf" fileSize="2.4 MB" type="pdf" url="dummy.pdf" />
    <ImagePreview v-model="showImagePreview" title="Design.png" url="https://picsum.photos/1000/600" />
  </div>
</template>
