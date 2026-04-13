<script setup lang="ts">
import { ref } from 'vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import TextInput from '../components/ui/TextInput.vue'
import Textarea from '../components/ui/Textarea.vue'
import Range from '../components/ui/Range.vue'
import OTPInput from '../components/ui/OTPInput.vue'
import SearchInput from '../components/ui/SearchInput.vue'
import NumberInput from '../components/ui/NumberInput.vue'
import Checkbox from '../components/ui/Checkbox.vue'
import Switch from '../components/ui/Switch.vue'
import Radio from '../components/ui/Radio.vue'
import Select from '../components/ui/Select.vue'
import MegaSelect from '../components/ui/MegaSelect.vue'
import MultiSelect from '../components/ui/MultiSelect.vue'
import TextTagInput from '../components/ui/TextTagInput.vue'
import UploadInput from '../components/ui/UploadInput.vue'
import MultiUploadInput from '../components/ui/MultiUploadInput.vue'
import DocumentInput from '../components/ui/DocumentInput.vue'
import { Mail, Lock, CheckCircle, AlertTriangle, Briefcase, CreditCard } from 'lucide-vue-next'
import Card from '@/components/ui/Card.vue'

const email = ref('')
const errorInput = ref('imauzo_user')
const successInput = ref('john.doe@imauzo.com')
const message = ref('')
const volume = ref(40)
const searchVal = ref('')
const numVal = ref<number | null>(null)
const checkVal = ref(true)
const switchVal = ref(false)
const radioVal = ref('option1')
const selectVal = ref('entreprise')
const tagsVal = ref(['VIP'])
const megaSelectVal = ref('pro')
const multiSelectVal = ref(['design'])

const selectOptions = [{ label: 'Entreprise', value: 'entreprise' }, { label: 'Particulier', value: 'particulier' }]
const megaSelectOptions = [
  { label: 'Plan Basic', value: 'basic', description: 'Idéal pour commencer', icon: Briefcase },
  { label: 'Plan Pro', value: 'pro', description: 'Toutes les fonctionnalités', icon: CreditCard }
]
const multiOptions = [{ label: 'Design', value: 'design' }, { label: 'Dev', value: 'dev' }]

const uploadVal = ref(null)
const multiUploadVal = ref([])
const docUploadVal = ref(null)

const code6 = ref('')
const code4 = ref('')
const isComplete = ref(false)

const onComplete = (val: string) => {
    isComplete.value = true
    setTimeout(() => { isComplete.value = false }, 2000)
}

</script>

<template>
  <Card>
    <div class="space-y-10 animate-in fade-in duration-500 pb-16">
    <div>
      <Heading level="2" class="mb-2">Formulaires & Inputs</Heading>
      <Text variant="secondary" size="lg">Catalogue exhaustif des champs de collecte de données.</Text>
    </div>

    <!-- Text Inputs -->
    <Section title="Champs Textuels">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-3xl mb-4">
         <TextInput v-model="email" label="Adresse Email" hint="Votre email professionnel" placeholder="exemple@imauzo.com"><template #prefix><Mail class="w-5 h-5" /></template></TextInput>
         <TextInput label="Mot de passe" type="password" placeholder="••••••••" required><template #prefix><Lock class="w-5 h-5" /></template></TextInput>
         <TextInput v-model="errorInput" label="Nom d'utilisateur" error="Nom pris."><template #suffix><AlertTriangle class="w-5 h-5 text-[#E41E3F]" /></template></TextInput>
         <TextInput v-model="successInput" label="Email Validé" success="Format correct."><template #suffix><CheckCircle class="w-5 h-5 text-[#2FA14A]" /></template></TextInput>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-3xl mt-4">
         <SearchInput v-model="searchVal" placeholder="Rechercher..." />
         <NumberInput v-model="numVal" label="Montant ($)" placeholder="0.00" hint="Valeur positive" />
      </div>
    </Section>

    <Section title="Options & Toggles">
        <div class="flex gap-16 flex-wrap">
            <div class="space-y-2">
                <Checkbox v-model="checkVal" label="Activer notifications" hint="Email requis" />
                <Switch v-model="switchVal" label="Mode sombre" />
            </div>
            <div class="space-y-2">
                <Radio v-model="radioVal" value="option1" name="plan" label="Basic" />
                <Radio v-model="radioVal" value="option2" name="plan" label="Premium" />
            </div>
        </div>
    </Section>

    <Section title="Sélections (Select & Tags)">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-3xl">
            <Select v-model="selectVal" :options="selectOptions" label="Type de compte" />
            <MegaSelect v-model="megaSelectVal" :options="megaSelectOptions" label="Abonnement" />
            <MultiSelect v-model="multiSelectVal" :options="multiOptions" label="Départements" />
            <TextTagInput v-model="tagsVal" label="Tags associés" />
        </div>
    </Section>

    <Section title="Uploads & Médias">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-3xl">
            <UploadInput v-model="uploadVal" label="Photo de profil" accept="image/*" />
            <DocumentInput v-model="docUploadVal" label="Contrat Signé" accept=".pdf" />
        </div>
    </Section>

    <Section title="Multilignes & Range">
      <div class="w-full max-w-2xl mb-6">
         <Textarea v-model="message" placeholder="Message..." rows="4" />
      </div>
      <div class="w-full max-w-md">
         <Text variant="secondary" size="sm" class="font-semibold block mb-2">Volume : {{ volume }}%</Text>
         <Range v-model="volume" color="primary" />
      </div>
    </Section>
  </div>
  
    <Section title="OTP Input (Code PIN)">
      <div class="flex flex-col gap-6">
         <div>
            <Text variant="secondary" size="sm" class="mb-3 block">Format Standard (6 cases)</Text>
            <OTPInput :length="6" v-model="code6" @complete="onComplete" />
            <div class="h-6 mt-2">
                <span v-if="isComplete" class="text-sm font-semibold text-[#2FA14A] flex items-center gap-1"><CheckCircle class="w-4 h-4" /> Code validé: {{ code6 }}</span>
            </div>
         </div>
      </div>
    </Section>
  </Card>
</template>
