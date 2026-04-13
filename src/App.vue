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
import Heading from './components/ui/Heading.vue'
import Text from './components/ui/Text.vue'
import Menu from './components/ui/Menu.vue'
import MenuItem from './components/ui/MenuItem.vue'
import MenuDivider from './components/ui/MenuDivider.vue'
import ConfirmDialog from './components/ui/ConfirmDialog.vue'
import HeaderWidget from './components/ui/HeaderWidget.vue'
import TimeSlotSelector from './components/ui/TimeSlotSelector.vue'
import DocumentPreview from './components/ui/DocumentPreview.vue'
import ImagePreview from './components/ui/ImagePreview.vue'
import Icon from './components/ui/Icon.vue'
import InvoiceTemplate from './components/ui/InvoiceTemplate.vue'
import InfoCard from './components/ui/InfoCard.vue'
import Editor from './components/ui/Editor.vue'
import SuccessWidget from './components/ui/SuccessWidget.vue'
import PaymentButton from './components/ui/PaymentButton.vue'
import Link from './components/ui/Link.vue'
import Section from './components/ui/Section.vue'
import Separator from './components/ui/Separator.vue'
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
import Badge from './components/ui/Badge.vue'
import Accordion from './components/ui/Accordion.vue'
import DropdownButton from './components/ui/DropdownButton.vue'
import Popover from './components/ui/Popover.vue'



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
const showImagePreview = ref(false)
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

const tableColumnsSimple = [
  { key: 'id', label: 'ID' },
  { key: 'name', label: 'Client' },
  { key: 'amount', label: 'Montant', align: 'right' as const },
  { key: 'status', label: 'Statut', align: 'center' as const }
]

const tableDataSimple = [
  { id: '#1023', name: 'Acme Corp', amount: '1 250 $', status: 'Payé' },
  { id: '#1024', name: 'Global Tech', amount: '850 $', status: 'En attente' },
  { id: '#1025', name: 'StartUp Inc', amount: '3 400 $', status: 'Payé' }
]

const tableColumns = [
  { key: 'user', label: 'Utilisateur' },
  { key: 'role', label: 'Rôle' },
  { key: 'status', label: 'Statut' },
  { key: 'lastLogin', label: 'Dernière connexion' },
  { key: 'actions', label: '', align: 'right' as const }
]

const tableData = [
  { id: 1, name: 'Alice Dubois', email: 'alice@imauzo.com', avatar: 'https://i.pravatar.cc/150?u=a042581f4e29026024d', role: 'Admin', status: 'Actif', lastLogin: 'Il y a 2h' },
  { id: 2, name: 'Marc Leroi', email: 'marc@imauzo.com', avatar: 'https://i.pravatar.cc/150?u=a042581f4e29026704d', role: 'Éditeur', status: 'En attente', lastLogin: 'Hier' },
  { id: 3, name: 'Julie Martin', email: 'julie@imauzo.com', avatar: 'https://i.pravatar.cc/150?u=a04258114e29026702d', role: 'Viewer', status: 'Inactif', lastLogin: '12/10/2023' },
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
              <Heading level="3" class="leading-tight">Tableau de bord<br />professionnel</Heading>
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
              <Heading level="1">Statistiques</Heading>
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
          <Heading level="4" variant="section" class="mb-4">Vue d'ensemble</Heading>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <StatsCard label="Revenus totaux" value="12 450 $" :trend="12.5" :icon="DollarSign"
              trendLabel="ce mois-ci" />
            <StatsCard label="Nouveaux clients" value="342" :trend="-2.4" :icon="Users" trendLabel="cette semaine" />
            <StatsCard label="Taux d'engagement" value="68%" :trend="5.1" :icon="Activity"
              trendLabel="par rapport au mois précédent" />
            <StatsCard label="Factures en attente" value="14" :icon="FileText" />
          </div>
        </section>

        <!-- Main Content Area Grid -->
        <div>
          <div class="space-y-8">
            <!-- Section: Inputs -->
            <section>
              <Card>
                <template #header>
                  <Heading level="3">Inputs & Contrôles</Heading>
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
                      <Heading level="5" class="mb-2">Options</Heading>
                      <Checkbox v-model="checkVal" label="Activer les notifications"
                        hint="Vous recevrez un email à chaque vente." />
                      <Switch v-model="switchVal" label="Mode sombre" hint="Disponible uniquement en bêta" />
                    </div>

                    <div class="bg-[#F0F2F5] p-4 rounded-lg space-y-2">
                      <Heading level="5" class="mb-2">Choisir un plan</Heading>
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
                  <Heading level="5">Fichiers & Documents</Heading>
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
                  <Heading level="3">Navigation Complémentaire</Heading>
                </template>

                <div class="space-y-8">
                  <!-- Breadcrumb -->
                  <div>
                    <Heading level="5" variant="section" class="mb-2">Fil d'Ariane (Breadcrumb)</Heading>
                    <Breadcrumb :items="breadcrumbItems" />
                  </div>

                  <!-- Tabs -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4">Onglets (Tabs)</Heading>
                    <div class="space-y-6">
                      <div>
                        <span class="text-xs text-[#65676B] mb-2 block font-medium uppercase tracking-wider">Style
                          Bordure
                          (Classic)</span>
                        <Tabs v-model="tabVal" :options="tabOptions" />
                      </div>
                      <div>
                        <span class="text-xs text-[#65676B] mb-2 block font-medium uppercase tracking-wider">Style
                          Pilule
                          (Insights)</span>
                        <Tabs v-model="tabValPills" :options="tabOptions" variant="pills" />
                      </div>
                    </div>
                  </div>

                  <!-- Stepper -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4">Progression (Stepper)</Heading>
                    <Stepper>
                      <StepperItem label="Panier" :completed="true" />
                      <StepperItem label="Paiement" active />
                      <StepperItem label="Confirmation" />
                    </Stepper>
                  </div>

                  <!-- Pagination -->
                  <div>
                    <Heading level="5" variant="section" class="mb-2">Pagination</Heading>
                    <Pagination v-model:currentPage="currentPage" :totalPages="5" />
                  </div>
                </div>
              </Card>
            </section>

            <!-- Section: Buttons -->
            <section>
              <Card>
                <template #header>
                  <Heading level="3">Variantes de Boutons</Heading>
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
                  <Heading level="3">Feedback (Retours)</Heading>
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
                    <Heading level="5" variant="section" class="mb-4">Indicateurs d'attente</Heading>
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
                  <Heading level="3">Affichage de données</Heading>
                </template>

                <div class="space-y-8">
                  <!-- ListTile -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4">Listes (ListTile)</Heading>
                    <div class="space-y-2">
                      <ListTile title="John Doe" subtitle="Administrateur système"
                        avatar="https://api.dicebear.com/7.x/avataaars/svg?seed=John" />
                      <ListTile title="Configuration réseau" subtitle="Dernière modification il y a 2h"
                        :icon="Briefcase" />
                    </div>
                  </div>

                  <!-- DataTable Simple -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4">Tableaux Basiques (DataTable Simple)</Heading>
                    <DataTable :columns="tableColumnsSimple" :data="tableDataSimple" striped>
                      <template #cell-status="{ value }">
                        <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-semibold"
                          :class="value === 'Payé' ? 'bg-[#E7F3EB] text-[#2FA14A]' : 'bg-[#FFF5E5] text-[#D88A00]'">
                          {{ value }}
                        </span>
                      </template>
                    </DataTable>
                  </div>

                  <!-- DataTable Avancé -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4 mt-8">Tableaux Avancés (DataTable avec Slots
                      Visuels)
                    </Heading>
                    <DataTable :columns="tableColumns" :data="tableData">
                      <!-- Slot Utilisateur -->
                      <template #cell-user="{ row }">
                        <div class="flex items-center gap-3">
                          <div class="avatar shrink-0">
                            <div class="w-10 h-10 rounded-full border border-[#CED0D4]/50 overflow-hidden shadow-sm">
                              <img :src="row.avatar" alt="Avatar" class="object-cover w-full h-full" />
                            </div>
                          </div>
                          <div>
                            <div class="font-bold text-[#050505] text-[15px]">{{ row.name }}</div>
                            <div class="text-[13px] text-[#65676B]">{{ row.email }}</div>
                          </div>
                        </div>
                      </template>

                      <!-- Slot Rôle -->
                      <template #cell-role="{ value }">
                        <Text weight="semibold" size="sm">{{ value }}</Text>
                      </template>

                      <!-- Slot Statut -->
                      <template #cell-status="{ value }">
                        <Badge
                          :variant="value === 'Actif' ? 'success' : value === 'En attente' ? 'warning' : 'neutral'">
                          {{ value }}
                        </Badge>
                      </template>

                      <!-- Slot Dernière connexion -->
                      <template #cell-lastLogin="{ value }">
                        <Text variant="secondary" size="sm">{{ value }}</Text>
                      </template>

                      <!-- Slot Actions -->
                      <template #cell-actions="{ row }">
                        <div class="flex justify-end">
                          <DropdownButton label="Options" variant="ghost" align="end">
                            <MenuItem>Modifier l'utilisateur</MenuItem>
                            <MenuItem>Changer le rôle</MenuItem>
                            <MenuDivider />
                            <MenuItem class="text-red-600">Désactiver</MenuItem>
                          </DropdownButton>
                        </div>
                      </template>
                    </DataTable>
                  </div>
                </div>
              </Card>
            </section>

            <!-- Section: Overlays & Composants Compactés -->
            <section>
              <Card>
                <template #header>
                  <Heading level="3">Composants Compactés & Menus</Heading>
                </template>

                <div class="space-y-8">
                  <!-- Badges -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4">Badges</Heading>
                    <div class="flex flex-wrap gap-2">
                      <Badge variant="primary">Nouveau</Badge>
                      <Badge variant="success">En ligne</Badge>
                      <Badge variant="warning">Brouillon</Badge>
                      <Badge variant="error" outline>Important</Badge>
                      <Badge variant="secondary">Info</Badge>
                      <Badge variant="neutral">99+</Badge>
                    </div>
                  </div>

                  <!-- Accordion -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4">Accordéons (Accordion)</Heading>
                    <div class="space-y-2 max-w-2xl">
                      <Accordion title="Comment gérer mes notifications ?" name="faq">
                        Vous pouvez accéder à vos préférences de notifications depuis les paramètres de votre compte et
                        définir des alertes spécifiques par e-mail ou push.
                      </Accordion>
                      <Accordion title="Où puis-je trouver mes factures ?" name="faq" defaultOpen>
                        Toutes vos factures sont disponibles dans l'onglet "Facturation" situé dans le panneau latéral
                        gauche. Vous pouvez les télécharger au format PDF.
                      </Accordion>
                    </div>
                  </div>

                  <!-- Dropdowns & Popovers -->
                  <div>
                    <Heading level="5" variant="section" class="mb-4">Menus déroulants (Dropdown & Popover)</Heading>
                    <div class="flex items-center gap-4">
                      <DropdownButton label="Actions rapides" variant="primary">
                        <MenuItem href="#">Modifier le profil</MenuItem>
                        <MenuItem href="#">Paramètres de confidentialité</MenuItem>
                        <MenuItem href="#" danger>Supprimer</MenuItem>
                      </DropdownButton>

                      <Popover width="w-72" align="end">
                        <template #trigger>
                          <Button variant="secondary">Mon Profil</Button>
                        </template>
                        <div class="flex flex-col gap-2">
                          <div class="flex items-center gap-3 p-2">
                            <div class="avatar shrink-0">
                              <div
                                class="w-10 h-10 rounded-full bg-[#E4E6EB] flex items-center justify-center font-bold text-[#050505]">
                                JD</div>
                            </div>
                            <div>
                              <Text weight="bold" class="leading-tight">John Doe</Text>
                              <Text variant="secondary" size="sm">john.doe@example.com</Text>
                            </div>
                          </div>
                          <MenuDivider />
                          <Menu class="w-full">
                            <MenuItem href="#">Paramètres</MenuItem>
                            <MenuItem href="#">Se déconnecter</MenuItem>
                          </Menu>
                        </div>
                      </Popover>
                    </div>
                  </div>
                </div>
              </Card>
            </section>

            <!-- Section: Modal Demo -->
            <section>
              <Card>
                <template #header>
                  <Heading level="3">Interactions</Heading>
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
          <!-- End Grid -->

          <!-- SECTION: Composants Métier (Phase 4) -->

          <!-- SECTION: Tableau Dynamique -->
          <Section class="mt-8 pt-8 border-t border-[#CED0D4]">
            <HeaderWidget title="Tableau de Données"
              subtitle="DataTable avec slots dynamiques (Avatar, Badges, Actions)" />
            <div class="mt-6">
              <DataTable :columns="tableColumns" :data="tableData">
                <!-- Slot Utilisateur -->
                <template #cell-user="{ row }">
                  <div class="flex items-center gap-3">
                    <div class="avatar shrink-0">
                      <div class="w-10 h-10 rounded-full border border-[#CED0D4]/50 overflow-hidden shadow-sm">
                        <img :src="row.avatar" alt="Avatar" class="object-cover w-full h-full" />
                      </div>
                    </div>
                    <div>
                      <div class="font-bold text-[#050505] text-[15px]">{{ row.name }}</div>
                      <div class="text-[13px] text-[#65676B]">{{ row.email }}</div>
                    </div>
                  </div>
                </template>

                <!-- Slot Rôle -->
                <template #cell-role="{ value }">
                  <Text weight="semibold" size="sm">{{ value }}</Text>
                </template>

                <!-- Slot Statut -->
                <template #cell-status="{ value }">
                  <Badge :variant="value === 'Actif' ? 'success' : value === 'En attente' ? 'warning' : 'neutral'">
                    {{ value }}
                  </Badge>
                </template>

                <!-- Slot Dernière connexion -->
                <template #cell-lastLogin="{ value }">
                  <Text variant="secondary" size="sm">{{ value }}</Text>
                </template>

                <!-- Slot Actions -->
                <template #cell-actions="{ row }">
                  <div class="flex justify-end">
                    <DropdownButton label="Options" variant="ghost" align="end">
                      <MenuItem>Modifier l'utilisateur</MenuItem>
                      <MenuItem>Changer le rôle</MenuItem>
                      <MenuDivider />
                      <MenuItem class="text-red-600">Désactiver</MenuItem>
                    </DropdownButton>
                  </div>
                </template>
              </DataTable>
            </div>
          </Section>

          <Section class="mt-8 pt-8 border-t border-[#CED0D4]">
            <HeaderWidget title="Composants Métier & Avancés"
              subtitle="Phase 4 - Modèles de documents, éditeurs et paiements" />

            <div class="grid grid-cols-1 xl:grid-cols-2 gap-8 mt-6">
              <Card class="h-full">
                <template #header>
                  <Heading level="4">Prise de rendez-vous & Édition</Heading>
                </template>
                <div class="space-y-6">
                  <div>
                    <Heading level="6" variant="section" class="mb-4">Créneaux horaires (TimeSlotSelector)</Heading>
                    <TimeSlotSelector v-model="selectedTime" :slots="timeSlots" />
                  </div>
                  <Separator />
                  <div>
                    <Heading level="6" variant="section" class="mb-4">Éditeur de texte (Wysiwyg Mock)</Heading>
                    <Editor v-model="editorContent" placeholder="Tapez votre description ici..."
                      minHeight="min-h-[150px]" />
                  </div>
                  <Separator />
                  <div>
                    <Heading level="6" variant="section" class="mb-4">Modales d'actions & Liens</Heading>
                    <div class="flex flex-wrap gap-3 mb-4">
                      <Button variant="danger" @click="showConfirm = true">Supprimer</Button>
                      <Button variant="secondary" @click="showDocPreview = true">Voir PDF</Button>
                      <Button variant="secondary" @click="showImagePreview = true">Voir Image</Button>
                    </div>
                    <div class="flex flex-wrap gap-4 items-center bg-[#F0F2F5] p-4 rounded-lg">
                      <Link href="#" class="!text-[#65676B]">Retour à la liste</Link>
                      <Separator vertical class="h-4 hidden sm:block" />
                      <Link href="#" external>
                        <template #icon>
                          <Icon :icon="ThumbsUp" size="sm" />
                        </template>
                        Aimer la page
                      </Link>
                    </div>
                  </div>
                </div>
              </Card>

              <div class="space-y-8">
                <Card>
                  <template #header>
                    <Heading level="4">Transactions & Paiements</Heading>
                  </template>
                  <div class="space-y-6">
                    <div class="flex justify-center sm:justify-start">
                      <PaymentButton amount="129.99" currency="€" showArrow />
                    </div>
                    <Separator />
                    <SuccessWidget title="Paiement validé !"
                      message="Votre commande #1234 a été confirmée avec succès.">
                      <Button variant="secondary" class="flex-1 sm:flex-none">Voir la facture</Button>
                      <Button variant="primary" class="flex-1 sm:flex-none">Continuer</Button>
                    </SuccessWidget>
                  </div>
                </Card>

                <InfoCard variant="info" title="Expertise Business"
                  description="Outils spécialisés pour votre croissance." :icon="Briefcase" />
              </div>
            </div>

            <div class="mt-8">
              <Card variant="muted" bodyClass="p-2 sm:p-8">
                <template #header>
                  <Heading level="4">Modèle de Facture (InvoiceTemplate)</Heading>
                </template>
                <InvoiceTemplate invoiceNumber="INV-2023-001" date="12/10/2023" dueDate="26/10/2023"
                  customerName="Entreprise cliente ABC" status="paid" :items="[
                    { description: 'Conception UI/UX', quantity: 1, unitPrice: '800.00 €', amount: '800.00 €' },
                    { description: 'Développement Frontend', quantity: 1, unitPrice: '1200.00 €', amount: '1200.00 €' }
                  ]" subtotal="2000.00 €" total="2400.00 €" tax="400.00 €" />
              </Card>
            </div>
          </Section>
        </div>
      </div>
      <!-- Render Snackbar globally inside Layout but floating -->
      <Snackbar :show="showSnackbar" message="Vos modifications ont été enregistrées avec succès" actionLabel="Annuler"
        @close="showSnackbar = false" />
    </div>
  </Layout>


  <ConfirmDialog v-model="showConfirm" title="Supprimer définitivement ?"
    message="Êtes-vous sûr de vouloir supprimer cet élément ? Cette action est irréversible et toutes les données associées seront perdues."
    confirmText="Oui, supprimer" />

  <DocumentPreview v-model="showDocPreview" title="Conditions Générales.pdf" fileSize="2.4 MB" type="pdf"
    url="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" />

  <ImagePreview v-model="showImagePreview" title="Aperçu_Design_V2.png"
    url="https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=2000&auto=format&fit=crop" />

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
