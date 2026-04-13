<script setup lang="ts">
import { ref } from 'vue'
import { Users, DollarSign, Activity, FileText } from 'lucide-vue-next'
import Button from './components/ui/Button.vue'
import Card from './components/ui/Card.vue'
import Modal from './components/ui/Modal.vue'
import StatsCard from './components/ui/StatsCard.vue'
import TextInput from './components/ui/TextInput.vue'
import SearchInput from './components/ui/SearchInput.vue'
import NumberInput from './components/ui/NumberInput.vue'
import Checkbox from './components/ui/Checkbox.vue'
import Radio from './components/ui/Radio.vue'
import Switch from './components/ui/Switch.vue'
import Select from './components/ui/Select.vue'
import MegaSelect from './components/ui/MegaSelect.vue'
import MultiSelect from './components/ui/MultiSelect.vue'
import TextTagInput from './components/ui/TextTagInput.vue'
import UploadInput from './components/ui/UploadInput.vue'
import MultiUploadInput from './components/ui/MultiUploadInput.vue'
import DocumentInput from './components/ui/DocumentInput.vue'
import { Briefcase, CreditCard } from 'lucide-vue-next'
import { Home, Bell, Search, ArrowLeft, Eye, ThumbsUp } from 'lucide-vue-next'
import Layout from './components/ui/Layout.vue'
import Navbar from './components/ui/Navbar.vue'
import NavbarItem from './components/ui/NavbarItem.vue'
import Sidebar from './components/ui/Sidebar.vue'
import SidebarItem from './components/ui/SidebarItem.vue'
import Tabs from './components/ui/Tabs.vue'
import Breadcrumb from './components/ui/Breadcrumb.vue'
import Pagination from './components/ui/Pagination.vue'
import Stepper from './components/ui/Stepper.vue'
import StepperItem from './components/ui/StepperItem.vue'
import Alert from './components/ui/Alert.vue'
import Notice from './components/ui/Notice.vue'
import Snackbar from './components/ui/Snackbar.vue'
import Loader from './components/ui/Loader.vue'
import CircleProgress from './components/ui/CircleProgress.vue'
import ListTile from './components/ui/ListTile.vue'
import DataTable from './components/ui/DataTable.vue'


const showModal = ref(false)
const showSnackbar = ref(false)
const isLoading = ref(false)

const triggerSnackbar = () => {
  showSnackbar.value = true
  setTimeout(() => { showSnackbar.value = false }, 4000)
}
const menuState = ref<'main' | 'stats'>('main')
const transitionName = ref('slide-left')

const goTo = (state: 'main' | 'stats') => {
  transitionName.value = state === 'stats' ? 'slide-left' : 'slide-right'
  menuState.value = state
}

// Input states
const textVal = ref('')
const searchVal = ref('')
const numVal = ref<number | null>(null)
const checkVal = ref(true)
const radioVal = ref('option1')

const tableColumns = [
  { key: 'id', label: 'ID' },
  { key: 'name', label: 'Client' },
  { key: 'amount', label: 'Montant', align: 'right' as const },
  { key: 'status', label: 'Statut', align: 'center' as const }
]

const tableData = [
  { id: '#1023', name: 'Acme Corp', amount: '1 250 $', status: 'Payé' },
  { id: '#1024', name: 'Global Tech', amount: '850 $', status: 'En attente' },
  { id: '#1025', name: 'StartUp Inc', amount: '3 400 $', status: 'Payé' }
]
const switchVal = ref(false)

const selectVal = ref('entreprise')
const selectOptions = [
  { label: 'Entreprise', value: 'entreprise' },
  { label: 'Particulier', value: 'particulier' }
]

const megaSelectVal = ref('pro')
const megaSelectOptions = [
  { label: 'Plan Basic', value: 'basic', description: 'Idéal pour commencer', icon: Briefcase },
  { label: 'Plan Pro', value: 'pro', description: 'Toutes les fonctionnalités', icon: CreditCard }
]

const multiSelectVal = ref(['marketing', 'design'])
const multiOptions = [
  { label: 'Marketing', value: 'marketing' },
  { label: 'Design', value: 'design' },
  { label: 'Développement', value: 'dev' }
]

const tagsVal = ref(['VIP', 'Client Fixe'])

const uploadVal = ref<File | null>(null)
const multiUploadVal = ref<File[]>([])
const docUploadVal = ref<File | null>(null)

// Navigation states
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

const triggerLoading = () => {
  isLoading.value = true
  setTimeout(() => {
    isLoading.value = false
  }, 2000)
}
</script>

<template>
  <Layout drawerId="imauzo-sidebar-drawer">
    <template #navbar>
      <Navbar title="iMauzo UI" drawerId="imauzo-sidebar-drawer">
        <template #right>
          <NavbarItem :icon="Search" />
          <NavbarItem :icon="Bell" badge="3" />
          <NavbarItem class="hidden sm:flex">
            <div class="avatar">
              <div
                class="w-8 rounded-full bg-[#E4E6EB] flex items-center justify-center text-sm font-bold text-[#050505] cursor-pointer hover:opacity-80">
                JD
              </div>
            </div>
          </NavbarItem>
        </template>
      </Navbar>
    </template>

    <template #sidebar>
      <transition :name="transitionName">
        <div v-if="menuState === 'main'" class="absolute inset-0 w-full h-full bg-[#FFFFFF] overflow-y-auto" key="main">
          <Sidebar class="w-full">
            <div class="px-3 pt-4 pb-4">
              <h2 class="font-bold text-lg text-[#050505] leading-tight">Tableau de bord<br />professionnel</h2>
            </div>
            <SidebarItem title="Accueil" :icon="Home" active />
            <SidebarItem title="Statistiques" :icon="Activity" hasSubmenu @click="goTo('stats')" />
            <SidebarItem title="Contenu" :icon="FileText" hasSubmenu />
            <SidebarItem title="Monétisation" :icon="DollarSign" hasSubmenu />
            <SidebarItem title="Engagement" :icon="ThumbsUp" hasSubmenu />
            <SidebarItem title="Tous les outils" :icon="Briefcase" />
          </Sidebar>
        </div>

        <div v-else class="absolute inset-0 w-full h-full bg-[#FFFFFF] overflow-y-auto" key="stats">
          <Sidebar class="w-full">
            <!-- Back button header -->
            <div class="px-2 pt-2">
              <button @click="goTo('main')"
                class="flex items-center gap-2 text-[#65676B] hover:bg-[#F0F2F5] px-2 py-1.5 mb-1 rounded-md w-full transition-colors text-[13px] font-semibold tracking-wide">
                <ArrowLeft class="w-4 h-4 text-[#050505]" />
                <span>Tableau de bord professionnel</span>
              </button>
            </div>
            <div class="px-3 pb-4 pt-1">
              <h2 class="font-bold text-2xl text-[#050505]">Statistiques</h2>
            </div>

            <SidebarItem title="Vues" :icon="Eye" active />
            <SidebarItem title="Revenus" :icon="DollarSign" />
            <SidebarItem title="Interactions" :icon="ThumbsUp" />
            <SidebarItem title="Audience" :icon="Users" />
          </Sidebar>
        </div>
      </transition>
    </template>

    <div class="bg-[#F0F2F5] min-h-full pb-12 w-full">
      <div class="max-w-6xl mx-auto mt-8 px-4 space-y-8">
        <!-- Section: Stats Cards -->
        <section>
          <h2 class="text-xl font-bold mb-4 fb-text-secondary uppercase text-sm">Vue d'ensemble</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <StatsCard label="Revenus totaux" value="12 450 $" :trend="12.5" :icon="DollarSign"
              trendLabel="ce mois-ci" />
            <StatsCard label="Nouveaux clients" value="342" :trend="-2.4" :icon="Users" trendLabel="cette semaine" />
            <StatsCard label="Taux d'engagement" value="68%" :trend="5.1" :icon="Activity"
              trendLabel="par rapport au mois précédent" />
            <StatsCard label="Factures en attente" value="14" :icon="FileText" />
          </div>
        </section>

        <div class="lg:col-span-2 space-y-8">
          <!-- Section: Inputs -->
          <section>
            <Card>
              <template #header>
                <h2 class="text-lg font-bold">Inputs & Contrôles</h2>
              </template>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <!-- Text Inputs -->
                <div class="space-y-4">
                  <TextInput v-model="textVal" label="Nom complet" placeholder="Ex: John Doe" required />
                  <SearchInput v-model="searchVal" placeholder="Rechercher des clients..." />
                  <NumberInput v-model="numVal" label="Montant ($)" placeholder="0.00"
                    hint="Entrez une valeur positive" />
                </div>

                <!-- Toggles & Radios -->
                <div class="space-y-4">
                  <div class="bg-[#F0F2F5] p-4 rounded-lg space-y-2">
                    <h3 class="font-semibold text-sm mb-2">Options</h3>
                    <Checkbox v-model="checkVal" label="Activer les notifications"
                      hint="Vous recevrez un email à chaque vente." />
                    <Switch v-model="switchVal" label="Mode sombre" hint="Disponible uniquement en bêta" />
                  </div>

                  <div class="bg-[#F0F2F5] p-4 rounded-lg space-y-2">
                    <h3 class="font-semibold text-sm mb-2">Choisir un plan</h3>
                    <Radio v-model="radioVal" value="option1" name="plan" label="Plan Basique"
                      hint="Gratuit pour 1 magasin" />
                    <Radio v-model="radioVal" value="option2" name="plan" label="Plan Premium" hint="29.99$/mois" />
                  </div>
                </div>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mt-6 pt-6 border-t border-[#CED0D4]">
                <!-- Selects -->
                <div class="space-y-4">
                  <Select v-model="selectVal" :options="selectOptions" label="Type de compte" />
                  <MegaSelect v-model="megaSelectVal" :options="megaSelectOptions" label="Abonnement"
                    hint="Vous pourrez changer plus tard" />
                </div>

                <!-- Multi Selects & Tags -->
                <div class="space-y-4">
                  <MultiSelect v-model="multiSelectVal" :options="multiOptions" label="Départements" />
                  <TextTagInput v-model="tagsVal" label="Tags associés" hint="Appuyez sur Entrée pour ajouter" />
                </div>
              </div>

              <!-- Uploads -->
              <div class="mt-6 pt-6 border-t border-[#CED0D4] space-y-6">
                <h3 class="font-semibold text-sm">Fichiers & Documents</h3>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                  <div class="space-y-4">
                    <UploadInput v-model="uploadVal" label="Photo de profil" accept="image/*"
                      hint="JPG, PNG. Max 5MB." />
                    <MultiUploadInput v-model="multiUploadVal" label="Pièces jointes" accept=".pdf,.doc,.docx" />
                  </div>
                  <div>
                    <DocumentInput v-model="docUploadVal" label="Contrat Signé" accept=".pdf" :maxSizeMB="10" />
                  </div>
                </div>
              </div>
            </Card>
          </section>

          <!-- Section: Navigation Complémentaire -->
          <section>
            <Card>
              <template #header>
                <h2 class="text-lg font-bold">Navigation Complémentaire</h2>
              </template>

              <div class="space-y-8">
                <!-- Breadcrumb -->
                <div>
                  <h3 class="font-semibold text-sm mb-2 text-[#65676B]">Fil d'Ariane (Breadcrumb)</h3>
                  <Breadcrumb :items="breadcrumbItems" />
                </div>

                <!-- Tabs -->
                <div>
                  <h3 class="font-semibold text-sm mb-4 text-[#65676B]">Onglets (Tabs)</h3>
                  <div class="space-y-6">
                    <div>
                      <span class="text-xs text-[#65676B] mb-2 block font-medium uppercase tracking-wider">Style Bordure
                        (Classic)</span>
                      <Tabs v-model="tabVal" :options="tabOptions" />
                    </div>
                    <div>
                      <span class="text-xs text-[#65676B] mb-2 block font-medium uppercase tracking-wider">Style Pilule
                        (Insights)</span>
                      <Tabs v-model="tabValPills" :options="tabOptions" variant="pills" />
                    </div>
                  </div>
                </div>

                <!-- Stepper -->
                <div>
                  <h3 class="font-semibold text-sm mb-4 text-[#65676B]">Progression (Stepper)</h3>
                  <Stepper>
                    <StepperItem label="Panier" :completed="true" />
                    <StepperItem label="Paiement" active />
                    <StepperItem label="Confirmation" />
                  </Stepper>
                </div>

                <!-- Pagination -->
                <div>
                  <h3 class="font-semibold text-sm mb-2 text-[#65676B]">Pagination</h3>
                  <Pagination v-model:currentPage="currentPage" :totalPages="5" />
                </div>
              </div>
            </Card>
          </section>

          <!-- Section: Buttons -->
          <section>
            <Card>
              <template #header>
                <h2 class="text-lg font-bold">Variantes de Boutons</h2>
              </template>

              <div class="flex flex-wrap gap-4 mb-6">
                <Button variant="primary">Primaire</Button>
                <Button variant="secondary">Secondaire</Button>
                <Button variant="ghost">Fantôme</Button>
                <Button variant="danger">Danger</Button>
              </div>

              <div class="flex flex-wrap gap-4 items-center">
                <Button variant="primary" size="sm">Petit</Button>
                <Button variant="primary" size="md">Normal</Button>
                <Button variant="primary" size="lg">Grand</Button>
                <Button variant="secondary" :loading="isLoading" @click="triggerLoading">
                  Test Chargement
                </Button>
                <Button variant="primary" disabled>Désactivé</Button>
              </div>
            </Card>
          </section>
        </div>

        <div class="space-y-8">
          <!-- Section: Feedbacks & Notifications -->
          <section>
            <Card>
              <template #header>
                <h2 class="text-lg font-bold">Feedback (Retours)</h2>
              </template>

              <div class="space-y-6">
                <!-- Alerts -->
                <div class="space-y-3">
                  <Alert type="info" message="Mise à jour système planifiée ce soir à 2h." />
                  <Alert type="success" title="Action réussie"
                    message="Le rapport a été généré et vous a été envoyé par email." dismissible />
                  <Alert type="error" title="Erreur inattendue" message="La connexion au serveur a été perdue." />
                </div>

                <!-- Notice -->
                <div>
                  <Notice title="Nouveau programme Beta"
                    message="Découvrez en avant-première nos nouvelles fonctionnalités de statistiques."
                    actionLabel="Rejoindre" />
                </div>

                <!-- Loaders & Radial Progress -->
                <div class="pt-4 border-t border-[#CED0D4]">
                  <h3 class="font-semibold text-sm mb-4 text-[#65676B]">Indicateurs d'attente</h3>
                  <div class="flex items-center gap-6">
                    <Loader size="lg" color="primary" />
                    <Loader size="md" color="neutral" />
                    <CircleProgress :value="75" size="3.5rem">75%</CircleProgress>
                  </div>
                </div>

                <div class="pt-4">
                  <Button variant="secondary" @click="triggerSnackbar">Afficher un Snackbar (Toast)</Button>
                </div>
              </div>
            </Card>
          </section>

          <!-- Section: Data Display -->
          <section>
            <Card>
              <template #header>
                <h2 class="text-lg font-bold">Affichage de données</h2>
              </template>

              <div class="space-y-8">
                <!-- ListTile -->
                <div>
                  <h3 class="font-semibold text-sm mb-4 text-[#65676B]">Listes (ListTile)</h3>
                  <div class="space-y-2">
                    <ListTile title="John Doe" subtitle="Administrateur système"
                      avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=John" />
                    <ListTile title="Configuration réseau" subtitle="Dernière modification il y a 2h"
                      :icon="Briefcase" />
                  </div>
                </div>

                <!-- DataTable -->
                <div>
                  <h3 class="font-semibold text-sm mb-4 text-[#65676B]">Tableaux (DataTable)</h3>
                  <DataTable :columns="tableColumns" :data="tableData" striped>
                    <template #cell-status="{ value }">
                      <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold"
                        :class="value === 'Payé' ? 'bg-[#E7F3EB] text-[#2FA14A]' : 'bg-[#FFF5E5] text-[#D88A00]'">
                        {{ value }}
                      </span>
                    </template>
                  </DataTable>
                </div>
              </div>
            </Card>
          </section>

          <!-- Section: Modal Demo -->
          <section>
            <Card>
              <template #header>
                <h2 class="text-lg font-bold">Interactions</h2>
              </template>

              <p class="fb-text-secondary text-sm mb-4">
                Les modales utilisent l'élément HTML dialog nativement stylisé par DaisyUI avec un comportement
                mobile-first.
              </p>

              <Button class="w-full" @click="showModal = true">
                Ouvrir la Modale
              </Button>
            </Card>
          </section>
        </div>
      </div>
      <!-- Render Snackbar globally inside Layout but floating -->
      <Snackbar :show="showSnackbar" message="Vos modifications ont été enregistrées avec succès" actionLabel="Annuler"
        @close="showSnackbar = false" />
    </div>
  </Layout>

  <!-- The Modal -->
  <Modal v-model="showModal" title="Créer un rapport">
    <div class="space-y-4">
      <p class="text-base-content">
        Choisissez le type de rapport et la période. Ce composant est conçu pour s'afficher en bas de l'écran sur
        mobile
        (bottom sheet) et au centre sur desktop.
      </p>

      <!-- Dummy form items -->
      <div
        class="p-3 border border-base-300 rounded-lg hover:bg-base-200 cursor-pointer transition-colors flex items-center gap-3">
        <div class="bg-primary/10 p-2 rounded-full">
          <Activity class="w-5 h-5 text-primary" />
        </div>
        <div>
          <div class="font-semibold">Rapport de performance</div>
          <div class="text-xs fb-text-secondary">Consultez les données de la semaine.</div>
        </div>
      </div>
    </div>

    <template #footer>
      <Button variant="secondary" @click="showModal = false" class="w-full sm:w-auto">Annuler</Button>
      <Button variant="primary" @click="showModal = false" class="w-full sm:w-auto">Confirmer</Button>
    </template>
  </Modal>
</template>
