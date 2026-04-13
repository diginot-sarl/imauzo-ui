import codecs

# 1. NavDoc.vue
nav_doc = """<script setup lang="ts">
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
"""

# 2. FeedbackDoc.vue
feedback_doc = """<script setup lang="ts">
import { ref } from 'vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import Alert from '../components/ui/Alert.vue'
import Notice from '../components/ui/Notice.vue'
import Loader from '../components/ui/Loader.vue'
import CircleProgress from '../components/ui/CircleProgress.vue'
import Button from '../components/ui/Button.vue'
import Snackbar from '../components/ui/Snackbar.vue'
import Popover from '../components/ui/Popover.vue'
import Menu from '../components/ui/Menu.vue'
import MenuItem from '../components/ui/MenuItem.vue'
import MenuDivider from '../components/ui/MenuDivider.vue'
import Badge from '../components/ui/Badge.vue'
import Accordion from '../components/ui/Accordion.vue'

const showSnackbar = ref(false)
const triggerSnackbar = () => {
  showSnackbar.value = true
  setTimeout(() => showSnackbar.value = false, 3000)
}
</script>

<template>
  <div class="space-y-10 animate-in fade-in duration-500">
    <div>
      <Heading level="2" class="mb-2">Surfaces & Feedback</Heading>
      <Text variant="secondary" size="lg">Retours visuels, badges, et composants flottants.</Text>
    </div>

    <!-- Alerts -->
    <Section title="Alertes">
      <div class="space-y-3">
        <Alert type="info" message="Mise à jour système planifiée ce soir à 2h." />
        <Alert type="success" title="Action réussie" message="Le rapport a été généré et envoyé." dismissible />
        <Alert type="error" title="Erreur inattendue" message="Connexion au serveur perdue." />
      </div>
    </Section>

    <Section title="Notices">
        <Notice title="Nouveau programme Beta" message="Découvrez nos nouvelles fonctionnalités." actionLabel="Rejoindre" />
    </Section>

    <!-- Loaders -->
    <Section title="Attente & Chargement">
      <div class="flex items-center gap-6">
        <Loader size="lg" color="primary" />
        <Loader size="md" color="neutral" />
        <CircleProgress :value="75" size="3.5rem">75%</CircleProgress>
      </div>
    </Section>

    <!-- Badges -->
    <Section title="Badges">
      <div class="flex flex-wrap gap-2">
        <Badge variant="primary">Nouveau</Badge>
        <Badge variant="success">En ligne</Badge>
        <Badge variant="warning">Brouillon</Badge>
        <Badge variant="error" outline>Important</Badge>
        <Badge variant="secondary">Info</Badge>
        <Badge variant="neutral">99+</Badge>
      </div>
    </Section>

    <!-- Accordion -->
    <Section title="Accordéons">
      <div class="space-y-2 max-w-2xl">
        <Accordion title="Comment gérer mes notifications ?" name="faq">Vous pouvez accéder à vos préférences dans les paramètres.</Accordion>
        <Accordion title="Trouver mes factures ?" name="faq" defaultOpen>Elles sont disponibles dans l'onglet Facturation.</Accordion>
      </div>
    </Section>

    <Section title="Snackbar (Toast)">
      <Button variant="secondary" @click="triggerSnackbar">Afficher le Toast</Button>
    </Section>
    
    <Teleport to="body">
       <Snackbar :show="showSnackbar" message="Modifications enregistrées" actionLabel="Annuler" @close="showSnackbar = false" />
    </Teleport>
  </div>
</template>
"""

# 3. AdvancedDoc.vue
advanced_doc = """<script setup lang="ts">
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
"""

# Update Extended InputsDoc.vue
inputs_doc_update = """<script setup lang="ts">
import { ref } from 'vue'
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import TextInput from '../components/ui/TextInput.vue'
import Textarea from '../components/ui/Textarea.vue'
import Range from '../components/ui/Range.vue'
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
</script>

<template>
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
</template>
"""

# Update DataDoc.vue
data_doc_update = """<script setup lang="ts">
import Heading from '../components/ui/Heading.vue'
import Text from '../components/ui/Text.vue'
import Section from '../components/ui/Section.vue'
import Stat from '../components/ui/Stat.vue'
import StatsCard from '../components/ui/StatsCard.vue'
import ListTile from '../components/ui/ListTile.vue'
import DataTable from '../components/ui/DataTable.vue'
import Badge from '../components/ui/Badge.vue'
import DropdownButton from '../components/ui/DropdownButton.vue'
import MenuItem from '../components/ui/MenuItem.vue'
import MenuDivider from '../components/ui/MenuDivider.vue'
import { DollarSign, Users, Activity, FileText, Briefcase } from 'lucide-vue-next'

const tableColumnsSimple = [
  { key: 'id', label: 'ID' },
  { key: 'name', label: 'Client' },
  { key: 'amount', label: 'Montant', align: 'right' as const },
  { key: 'status', label: 'Statut', align: 'center' as const }
]

const tableDataSimple = [
  { id: '#1023', name: 'Acme Corp', amount: '1 250 $', status: 'Payé' },
  { id: '#1024', name: 'Global Tech', amount: '850 $', status: 'En attente' }
]

const tableColumns = [
  { key: 'user', label: 'Utilisateur' },
  { key: 'role', label: 'Rôle' },
  { key: 'status', label: 'Statut' },
  { key: 'actions', label: '', align: 'right' as const }
]

const tableData = [
  { id: 1, name: 'Alice Dubois', email: 'alice@imauzo.com', avatar: 'https://i.pravatar.cc/150?u=a042581f4e29026024d', role: 'Admin', status: 'Actif' },
  { id: 2, name: 'Marc Leroi', email: 'marc@imauzo.com', avatar: 'https://i.pravatar.cc/150?u=a042581f4e29026704d', role: 'Viewer', status: 'En attente' },
]
</script>

<template>
  <div class="space-y-10 animate-in fade-in duration-500 pb-16">
    <div>
      <Heading level="2" class="mb-2">Données & Listes</Heading>
      <Text variant="secondary" size="lg">Restitution d'informations, KPI, et flux de données formatés.</Text>
    </div>

    <!-- Stat -->
    <Section title="KPI / Métriques">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
         <StatsCard label="Revenus totaux" value="12 450 $" :trend="12.5" :icon="DollarSign" trendLabel="ce mois-ci" />
         <StatsCard label="Nouveaux clients" value="342" :trend="-2.4" :icon="Users" trendLabel="cette semaine" />
         <StatsCard label="Taux engagement" value="68%" :trend="5.1" :icon="Activity" trendLabel="mensuel" />
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
         <Stat title="Chiffre d'affaires" value="8 400 $" description="+ 14% de croissance" :icon="DollarSign" />
         <Stat title="Abonnés" value="1 250" description="Derniers 7 jours" />
      </div>
    </Section>

    <Section title="Tuiles (ListTile)">
        <div class="max-w-md space-y-2">
            <ListTile title="John Doe" subtitle="Admin" avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=John" />
            <ListTile title="Configuration" subtitle="Créé hier" :icon="Briefcase" />
        </div>
    </Section>

    <Section title="DataTables (Tableaux)">
        <div class="space-y-8">
            <div>
                <Heading level="5" class="mb-2">Basique (Striped)</Heading>
                <DataTable :columns="tableColumnsSimple" :data="tableDataSimple" striped>
                    <template #cell-status="{ value }">
                        <Badge :variant="value === 'Payé' ? 'success' : 'warning'">{{ value }}</Badge>
                    </template>
                </DataTable>
            </div>

            <div>
                <Heading level="5" class="mb-2">Avancé (Custom Slots)</Heading>
                <DataTable :columns="tableColumns" :data="tableData">
                    <template #cell-user="{ row }">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-gray-200 overflow-hidden"><img :src="row.avatar" /></div>
                            <div><div class="font-bold">{{ row.name }}</div><div class="text-xs text-gray-500">{{ row.email }}</div></div>
                        </div>
                    </template>
                    <template #cell-status="{ value }"><Badge :variant="value === 'Actif' ? 'success' : 'warning'">{{ value }}</Badge></template>
                    <template #cell-actions>
                        <DropdownButton label="Options" variant="ghost" align="end">
                            <MenuItem>Modifier</MenuItem>
                            <MenuDivider />
                            <MenuItem class="text-red-500">Désactiver</MenuItem>
                        </DropdownButton>
                    </template>
                </DataTable>
            </div>
        </div>
    </Section>
  </div>
</template>
"""

with codecs.open(r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\docs\NavDoc.vue', 'w', 'utf-8') as f: f.write(nav_doc)
with codecs.open(r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\docs\FeedbackDoc.vue', 'w', 'utf-8') as f: f.write(feedback_doc)
with codecs.open(r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\docs\AdvancedDoc.vue', 'w', 'utf-8') as f: f.write(advanced_doc)
with codecs.open(r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\docs\InputsDoc.vue', 'w', 'utf-8') as f: f.write(inputs_doc_update)
with codecs.open(r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\docs\DataDoc.vue', 'w', 'utf-8') as f: f.write(data_doc_update)
