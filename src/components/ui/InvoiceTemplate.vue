<script setup lang="ts">
import { cn } from '../../lib/utils'
import Heading from './Heading.vue'
import Text from './Text.vue'
import Badge from './Badge.vue'
import Separator from './Separator.vue'
import { Download } from 'lucide-vue-next'

export interface InvoiceItem {
    id?: string
    description: string
    quantity?: number
    unitPrice?: string
    amount: string
}

interface Props {
    invoiceNumber: string
    date: string
    dueDate?: string
    customerName: string
    customerEmail?: string
    items: InvoiceItem[]
    subtotal: string
    tax?: string
    total: string
    status: 'paid' | 'pending' | 'overdue' | 'draft'
    class?: any
}

defineProps<Props>()
defineEmits(['download'])

const statusMap = {
    paid: { label: 'Payé', variant: 'success' },
    pending: { label: 'En attente', variant: 'warning' },
    overdue: { label: 'En retard', variant: 'error' },
    draft: { label: 'Brouillon', variant: 'neutral' }
}
</script>

<template>
    <div
        :class="cn('bg-white p-6 sm:p-8 rounded-xl border border-[#CED0D4] shadow-sm max-w-3xl mx-auto', $props.class)">
        <!-- Header -->
        <div class="flex flex-col sm:flex-row justify-between items-start gap-4 mb-8">
            <div>
                <Heading level="2" class="text-2xl mb-1">Facture</Heading>
                <Text variant="secondary" class="font-semibold tracking-wide">#{{ invoiceNumber }}</Text>
            </div>
            <div class="flex flex-row sm:flex-col items-center sm:items-end gap-3 sm:gap-1 w-full sm:w-auto">
                <Badge :variant="statusMap[status].variant as any" class="px-3 py-1 font-bold">{{
                    statusMap[status].label }}</Badge>
                <button @click="$emit('download')"
                    class="text-[#0866FF] hover:underline text-sm font-semibold flex items-center gap-1 mt-2 ml-auto sm:ml-0">
                    <Download class="w-4 h-4" /> PDF
                </button>
            </div>
        </div>

        <!-- Info Bil -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-8 mb-8">
            <div>
                <Heading level="6" variant="section" class="mb-2">Facturé à</Heading>
                <Text weight="semibold">{{ customerName }}</Text>
                <Text variant="secondary" size="sm" v-if="customerEmail">{{ customerEmail }}</Text>
            </div>
            <div class="sm:text-right">
                <div class="mb-2">
                    <Heading level="6" variant="section" class="inline-block sm:block mb-1 sm:mb-2 mr-2 sm:mr-0">Date
                        d'émission :</Heading>
                    <Text size="sm" class="inline-block sm:block">{{ date }}</Text>
                </div>
                <div v-if="dueDate">
                    <Heading level="6" variant="section" class="inline-block sm:block mb-1 sm:mb-2 mr-2 sm:mr-0">
                        Échéance :</Heading>
                    <Text size="sm" class="inline-block sm:block font-semibold">{{ dueDate }}</Text>
                </div>
            </div>
        </div>

        <!-- Items -->
        <div class="overflow-x-auto mb-6 -mx-2 px-2">
            <table class="w-full text-left border-collapse min-w-[450px]">
                <thead>
                    <tr class="border-b-2 border-[#CED0D4]">
                        <th class="py-3 text-xs font-bold text-[#8D949E] tracking-[0.1em] uppercase">Description</th>
                        <th class="py-3 text-xs font-bold text-[#8D949E] tracking-[0.1em] uppercase text-right">Montant
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, index) in items" :key="item.id || index" class="border-b border-[#E4E6EB]">
                        <td class="py-4">
                            <Text weight="medium">{{ item.description }}</Text>
                            <Text v-if="item.quantity && item.unitPrice" variant="secondary" size="sm" class="mt-1">
                                {{ item.quantity }} × {{ item.unitPrice }}
                            </Text>
                        </td>
                        <td class="py-4 text-right">
                            <Text weight="semibold">{{ item.amount }}</Text>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Totals -->
        <div class="flex justify-end mt-4 pt-4 border-t border-dashed border-[#CED0D4]">
            <div class="w-full sm:w-72 space-y-3">
                <div class="flex justify-between items-center text-sm">
                    <Text variant="secondary">Sous-total</Text>
                    <Text weight="medium">{{ subtotal }}</Text>
                </div>
                <div v-if="tax" class="flex justify-between items-center text-sm">
                    <Text variant="secondary">Taxes</Text>
                    <Text weight="medium">{{ tax }}</Text>
                </div>
                <Separator class="my-3 opacity-50" />
                <div class="flex justify-between items-center">
                    <Text weight="bold" size="lg">Total</Text>
                    <Heading level="3" class="text-[#0866FF]">{{ total }}</Heading>
                </div>
            </div>
        </div>
    </div>
</template>
