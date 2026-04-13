<script setup lang="ts">
import { ref, computed } from 'vue'
import { Filter } from 'lucide-vue-next'

export interface Column {
    key: string
    label: string
    align?: 'left' | 'center' | 'right'
    sortable?: boolean
    filterable?: boolean
}

interface Props {
    columns: Column[]
    data: any[]
    striped?: boolean
    hoverable?: boolean
}

const props = withDefaults(defineProps<Props>(), {
    striped: false,
    hoverable: true
})

const emit = defineEmits(['sort', 'filter', 'row-click'])

const sortKey = ref<string | null>(null)
const sortOrder = ref<'asc' | 'desc' | null>(null)

const toggleSort = (key: string) => {
    if (sortKey.value === key) {
        if (sortOrder.value === 'asc') sortOrder.value = 'desc'
        else if (sortOrder.value === 'desc') {
            sortOrder.value = null
            sortKey.value = null
        }
    } else {
        sortKey.value = key
        sortOrder.value = 'asc'
    }
    emit('sort', { key: sortKey.value, order: sortOrder.value })
}

// Tris local intelligent et automatique
const sortedData = computed(() => {
    if (!sortKey.value || !sortOrder.value) return props.data
    
    return [...props.data].sort((a, b) => {
        const valA = a[sortKey.value!]
        const valB = b[sortKey.value!]
        
        // Handling nulls/undefined safely
        if (valA == null) return sortOrder.value === 'asc' ? -1 : 1
        if (valB == null) return sortOrder.value === 'asc' ? 1 : -1
            
        if (typeof valA === 'string' && typeof valB === 'string') {
            return sortOrder.value === 'asc' 
                ? valA.localeCompare(valB)
                : valB.localeCompare(valA)
        }
        
        if (valA < valB) return sortOrder.value === 'asc' ? -1 : 1
        if (valA > valB) return sortOrder.value === 'asc' ? 1 : -1
        return 0
    })
})
</script>

<template>
    <div class="overflow-x-auto rounded-lg border border-[#E4E6EB] bg-white shadow-sm scrollbar-hide">
        <table class="w-full text-[14px]">
            <thead class="bg-[#FAFAFA] text-[#050505] text-[13px] font-semibold border-b border-[#E4E6EB]">
                <tr>
                    <th v-for="col in columns" :key="col.key" 
                        class="py-3.5 px-4 whitespace-nowrap transition-colors"
                        :class="[
                            col.align === 'center' ? 'text-center' : (col.align === 'right' ? 'text-right' : 'text-left'),
                            col.sortable ? 'hover:bg-[#F0F2F5] select-none cursor-pointer group' : ''
                        ]"
                        @click="col.sortable ? toggleSort(col.key) : null">
                        
                        <div class="inline-flex items-center gap-1.5" 
                             :class="{ 'justify-center': col.align === 'center', 'justify-end w-full': col.align === 'right', 'justify-start w-full': col.align === 'left' || !col.align }">
                            
                            <span>{{ col.label }}</span>
                            
                            <div v-if="col.sortable || col.filterable" class="flex items-center gap-1">
                                <!-- Sort Arrows (Naive UI Style) -->
                                <div v-if="col.sortable" class="flex flex-col gap-[2px] ml-1 opacity-60 group-hover:opacity-100 transition-opacity">
                                    <svg class="w-2.5 h-2.5 transition-colors" :class="{ 'text-[#0866FF]': sortKey === col.key && sortOrder === 'asc', 'text-[#CED0D4]': !(sortKey === col.key && sortOrder === 'asc') }" viewBox="0 0 24 24" fill="currentColor">
                                        <path d="M12 4L4 16H20L12 4Z" />
                                    </svg>
                                    <svg class="w-2.5 h-2.5 transition-colors" :class="{ 'text-[#0866FF]': sortKey === col.key && sortOrder === 'desc', 'text-[#CED0D4]': !(sortKey === col.key && sortOrder === 'desc') }" viewBox="0 0 24 24" fill="currentColor">
                                        <path d="M12 20L20 8H4L12 20Z" />
                                    </svg>
                                </div>
                                
                                <!-- Filter Icon -->
                                <button v-if="col.filterable" @click.stop="emit('filter', col.key)" 
                                        class="ml-0.5 text-[#8D949E] hover:text-[#0866FF] transition-colors p-[2px] rounded hover:bg-[#E4E6EB]">
                                    <Filter class="w-3.5 h-3.5" />
                                </button>
                            </div>
                        </div>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, i) in sortedData" :key="row.id || i" 
                    class="border-b border-[#E4E6EB] transition-colors last:border-b-0 cursor-default"
                    :class="[
                        hoverable ? 'hover:bg-[#F9FAFB]' : '',
                        striped && i % 2 !== 0 ? 'bg-[#FAFAFA]' : 'bg-white'
                    ]"
                    @click="emit('row-click', row)">
                    <td v-for="col in columns" :key="col.key" 
                        class="py-3 px-4 text-[#050505]"
                        :class="[
                            col.align === 'center' ? 'text-center' : (col.align === 'right' ? 'text-right' : 'text-left')
                        ]">
                        <slot :name="`cell-${col.key}`" :row="row" :value="row[col.key]">
                            {{ row[col.key] }}
                        </slot>
                    </td>
                </tr>

                <tr v-if="data.length === 0">
                    <td :colspan="columns.length" class="py-12 text-center">
                        <div class="flex flex-col items-center justify-center text-[#8D949E]">
                            <svg class="w-10 h-10 mb-2 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path>
                            </svg>
                            <span class="text-[13px] font-medium">Aucune donnée trouvée</span>
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<style scoped>
.scrollbar-hide::-webkit-scrollbar {
    display: none;
}
.scrollbar-hide {
    -ms-overflow-style: none;
    scrollbar-width: none;
}
</style>
