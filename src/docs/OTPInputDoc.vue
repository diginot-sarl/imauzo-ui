<script setup lang="ts">
import { ref } from 'vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import OTPInput from '../components/ui/OTPInput.vue'
import Card from '@/components/ui/Card.vue'

const code6 = ref('')
const code4 = ref('')
const isComplete = ref(false)

const onComplete = (val: string) => {
    isComplete.value = true
    setTimeout(() => {
        isComplete.value = false
    }, 2000)
}
</script>

<template>
  <Card>
    <div class="space-y-10 animate-in fade-in duration-500">
    <div>
      <Heading level="2" class="mb-2">OTP Input</Heading>
      <Text variant="secondary" size="lg">Composant de saisie de code d'authentification robuste. Gère parfaitement la navigation au clavier (flèches, backspace), l'avance automatique, et supporte le copier-coller intégral.</Text>
    </div>

    <!-- Sécurité classique -->
    <Section title="Standard (6 chiffres)">
      <div class="flex flex-col gap-4">
         <OTPInput :length="6" v-model="code6" @complete="onComplete" />
         
         <div class="h-6">
            <span v-if="isComplete" class="text-sm font-semibold text-[#2FA14A] flex items-center gap-1">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
                Code validé: {{ code6 }}
            </span>
         </div>
      </div>
    </Section>

    <!-- Version courte -->
    <Section title="Version Courte (4 chiffres)">
      <div class="flex flex-col gap-4">
         <OTPInput :length="4" v-model="code4" />
         <Text size="sm" variant="secondary">Valeur actuelle : {{ code4 || '...' }}</Text>
      </div>
    </Section>
  </div>
  </Card>
</template>
