<script setup lang="ts">
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

import Modal from '../components/ui/Modal.vue'
import ConfirmDialog from '../components/ui/ConfirmDialog.vue'

const showSnackbar = ref(false)
const showModal = ref(false)
const showConfirm = ref(false)
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

    <Section title="Modales (Dialog)">
      <div class="flex flex-wrap gap-4">
        <Button @click="showModal = true">Modale d'Information</Button>
        <Button variant="danger" @click="showConfirm = true">Modale de Confirmation</Button>
      </div>
    </Section>
    
    <Modal v-model="showModal" title="Conditions Générales d'Utilisation" actionLabel="Accepter et fermer" @action="showModal = false">
        <p>En continuant d'utiliser iMauzo, vous acceptez l'ensemble des conditions en vigueur concernant l'hébergement et le traitement de vos données d'entreprise structurées.</p>
    </Modal>
    
    <ConfirmDialog v-model="showConfirm" title="Archiver ce rapport ?" message="Attention, si vous archivez ce rapport, aucun membre ne pourra plus le modifier. Voulez-vous tout de même procéder ?" confirmText="Archiver" />

</template>
