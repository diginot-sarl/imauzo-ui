<script setup lang="ts">
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
