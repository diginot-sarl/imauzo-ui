<script setup lang="ts">
export interface Column {
    key: string
    label: string
    align?: 'left' | 'center' | 'right'
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
</script>

<template>
    <div class="overflow-x-auto rounded-lg border border-[#CED0D4] bg-[#FFFFFF] shadow-sm">
        <table class="table w-full text-[14px]">
            <!-- head -->
            <thead class="bg-[#F0F2F5] text-[#65676B] text-[13px] font-semibold border-b border-[#CED0D4]">
                <tr>
                    <th v-for="col in columns" :key="col.key" :class="{
                        'text-left': col.align === 'left' || !col.align,
                        'text-center': col.align === 'center',
                        'text-right': col.align === 'right'
                    }" class="py-3 px-4 whitespace-nowrap">
                        {{ col.label }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(row, i) in data" :key="row.id || i" class="border-t border-[#CED0D4]/50 transition-colors"
                    :class="[
                        hoverable ? 'hover:bg-[#F0F2F5]/60' : '',
                        striped && i % 2 !== 0 ? 'bg-[#F9FAFB]' : ''
                    ]">
                    <td v-for="col in columns" :key="col.key" :class="{
                        'text-left': col.align === 'left' || !col.align,
                        'text-center': col.align === 'center',
                        'text-right': col.align === 'right'
                    }" class="py-3 px-4 text-[#050505]">
                        <!-- Slot dynamique par colonne (ex: #cell-status="{ row, value }") -->
                        <slot :name="`cell-${col.key}`" :row="row" :value="row[col.key]">
                            {{ row[col.key] }}
                        </slot>
                    </td>
                </tr>

                <tr v-if="data.length === 0">
                    <td :colspan="columns.length" class="py-8 text-center text-[#65676B]">
                        Aucune donnée à afficher.
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
