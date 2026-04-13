<script setup lang="ts">
import { ref } from 'vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import Tabs from '../components/ui/Tabs.vue'
import Breadcrumb from '../components/ui/Breadcrumb.vue'
import Pagination from '../components/ui/Pagination.vue'
import Stepper from '../components/ui/Stepper.vue'
import StepperItem from '../components/ui/StepperItem.vue'

const tabVal = ref('tab1')
const tabValPills = ref('tab1')
const tabOptions = [
  { label: 'Aperçu', value: 'tab1' },
  { label: 'Paramètres', value: 'tab2' },
  { label: 'Avancé', value: 'tab3' }
]
const breadcrumbItems = [
  { label: 'Accueil', to: '#' },
  { label: 'Audience', to: '#' },
  { label: 'Statistiques' }
]
const currentPage = ref(2)
</script>

<template>
  <div class="space-y-10 animate-in fade-in duration-500">
    <div>
      <Heading level="2" class="mb-2">Navigation</Heading>
      <Text variant="secondary" size="lg">Composants de guidage et de progression au sein de l'application.</Text>
    </div>

    <!-- Breadcrumb -->
    <Section title="Fil d'Ariane (Breadcrumb)">
      <Breadcrumb :items="breadcrumbItems" />
    </Section>

    <!-- Tabs -->
    <Section title="Onglets (Tabs)">
      <div class="space-y-6">
        <div>
          <Text variant="secondary" size="sm" class="mb-2 block uppercase tracking-wider">Style Bordure</Text>
          <Tabs v-model="tabVal" :options="tabOptions" />
        </div>
        <div>
          <Text variant="secondary" size="sm" class="mb-2 block uppercase tracking-wider">Style Pilule</Text>
          <Tabs v-model="tabValPills" :options="tabOptions" variant="pills" />
        </div>
      </div>
    </Section>

    <!-- Stepper -->
    <Section title="Progression (Stepper)">
      <Stepper>
        <StepperItem label="Panier" :completed="true" />
        <StepperItem label="Paiement" active />
        <StepperItem label="Confirmation" />
      </Stepper>
    </Section>

    <!-- Pagination -->
    <Section title="Pagination">
      <Pagination v-model:currentPage="currentPage" :totalPages="5" />
    </Section>
  </div>
</template>
