<script setup lang="ts">
import { computed } from 'vue'
import { ChevronLeft, ChevronRight } from 'lucide-vue-next'

interface Props {
    currentPage: number
    totalPages: number
}

const props = defineProps<Props>()
const emit = defineEmits<{
    'update:currentPage': [page: number]
    'page-change': [page: number]
}>()

const setPage = (page: number) => {
    if (page >= 1 && page <= props.totalPages) {
        emit('update:currentPage', page)
        emit('page-change', page)
    }
}

const pages = computed(() => {
    const arr = []
    for (let i = 1; i <= props.totalPages; i++) {
        arr.push(i)
    }
    // Pour rester simple, on affiche juste toutes les pages ou on pourrait tronquer...
    return arr
})
</script>

<template>
    <div class="join shadow-[0_1px_2px_rgba(0,0,0,0.05)] rounded-md overflow-hidden">
        <button @click="setPage(currentPage - 1)"
            class="join-item btn btn-sm bg-[#FFFFFF] border-[#CED0D4] hover:bg-[#F0F2F5] text-[#050505] disabled:opacity-50 disabled:bg-[#F0F2F5]"
            :disabled="currentPage <= 1">
            <ChevronLeft class="w-4 h-4" />
            <span class="sr-only">Précédent</span>
        </button>

        <button v-for="page in pages" :key="page" @click="setPage(page)" class="join-item btn btn-sm border-[#CED0D4]"
            :class="page === currentPage ? 'bg-[#EAF3FF] text-[#0866FF] border-[#EAF3FF] hover:bg-[#dcebfe]' : 'bg-[#FFFFFF] text-[#050505] hover:bg-[#F0F2F5]'">
            {{ page }}
        </button>

        <button @click="setPage(currentPage + 1)"
            class="join-item btn btn-sm bg-[#FFFFFF] border-[#CED0D4] hover:bg-[#F0F2F5] text-[#050505] disabled:opacity-50 disabled:bg-[#F0F2F5]"
            :disabled="currentPage >= totalPages">
            <ChevronRight class="w-4 h-4" />
            <span class="sr-only">Suivant</span>
        </button>
    </div>
</template>
