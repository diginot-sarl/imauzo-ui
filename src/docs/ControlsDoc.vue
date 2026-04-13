<script setup lang="ts">
import { ref } from 'vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import BackButton from '../components/ui/BackButton.vue'
import SegmentedControl from '../components/ui/SegmentedControl.vue'
import { MousePointer2, Minus, Square, Circle } from 'lucide-vue-next'
import Card from '@/components/ui/Card.vue'

const selectedTool = ref('select')
const toolOptions = [
    { value: 'select', icon: MousePointer2 },
    { value: 'line', icon: Minus },
    { value: 'rect', icon: Square },
    { value: 'ellipse', icon: Circle },
]

const selectedTab = ref('jour')
const tabOptions = [
    { value: 'jour', label: 'Aujourd\'hui' },
    { value: 'semaine', label: 'Cette semaine' },
    { value: 'mois', label: 'Ce mois' },
]
</script>

<template>
  <Card>
   <div class="space-y-10 animate-in fade-in duration-500">
    <div>
      <Heading level="2" class="mb-2">Contrôles Divers (Controls)</Heading>
      <Text variant="secondary" size="lg">Des composants spécifiques d'interactions UI (Bouton retour, switchers) reproduisant rigoureusement le style premium et moderne.</Text>
    </div>

    <!-- Segmented Control -->
    <Section title="Segmented Control (Button Switch)">
      <div class="flex flex-col gap-8">
         <div>
            <Text variant="secondary" size="sm" class="mb-3 block">Icon Only (Outils Dessin)</Text>
            <SegmentedControl 
               v-model="selectedTool" 
               :options="toolOptions" 
            />
         </div>

         <div>
            <Text variant="secondary" size="sm" class="mb-3 block">Texte (Onglets temporels)</Text>
            <SegmentedControl 
               v-model="selectedTab" 
               :options="tabOptions" 
            />
         </div>
      </div>
    </Section>

    <!-- Back Button -->
    <Section title="Bouton de Retour (BackButton)">
      <div class="flex items-center gap-4">
         <BackButton />
         <Text variant="secondary">Le bouton gris classique utilisé dans les headers.</Text>
      </div>
    </Section>

  </div>
  </Card>
</template>
