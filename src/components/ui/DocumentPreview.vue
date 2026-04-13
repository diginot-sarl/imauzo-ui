<script setup lang="ts">
import { Download, Share2, Printer, ExternalLink, FileText } from 'lucide-vue-next'
import Modal from './Modal.vue'
import Button from './Button.vue'
import Heading from './Heading.vue'
import Text from './Text.vue'
import Icon from './Icon.vue'

interface Props {
    modelValue: boolean
    title: string
    url?: string
    fileName?: string
    fileSize?: string
    type?: 'image' | 'pdf' | 'document' | 'video'
}

const props = withDefaults(defineProps<Props>(), {
    type: 'document'
})

const emit = defineEmits(['update:modelValue', 'download', 'share', 'print'])

const isImage = props.type === 'image'
</script>

<template>
    <Modal :modelValue="modelValue" @update:modelValue="emit('update:modelValue', $event)" title="" maxWidth="3xl"
        :classBody="isImage ? 'p-0 bg-transparent' : 'p-0'">
        <div class="flex flex-col h-[80vh] max-h-[800px]">
            <!-- Barre d'outils du document -->
            <div
                class="flex-none h-14 bg-[#FFFFFF] border-b border-[#CED0D4] flex items-center justify-between px-4 sticky top-0 z-10 rounded-t-xl shrink-0">
                <div class="flex items-center gap-3 overflow-hidden">
                    <div class="w-8 h-8 rounded bg-[#F0F2F5] flex items-center justify-center shrink-0">
                        <Icon :icon="FileText" size="sm" color="secondary" />
                    </div>
                    <div class="min-w-0">
                        <Heading level="5" class="truncate leading-tight text-[#050505]">{{ title }}</Heading>
                        <Text v-if="fileSize || fileName" variant="secondary" size="xs"
                            class="truncate hidden sm:block">
                            {{ fileName }} <span v-if="fileSize">• {{ fileSize }}</span>
                        </Text>
                    </div>
                </div>

                <div class="flex items-center gap-1 sm:gap-2 shrink-0">
                    <Button variant="ghost" class="w-10 h-10 p-0 rounded-full" title="Imprimer" @click="emit('print')">
                        <Icon :icon="Printer" size="md" color="secondary" />
                    </Button>
                    <Button variant="ghost" class="w-10 h-10 p-0 rounded-full" title="Partager" @click="emit('share')">
                        <Icon :icon="Share2" size="md" color="secondary" />
                    </Button>
                    <Button variant="primary" class="h-9 px-4 hidden sm:flex" @click="emit('download')">
                        <Icon :icon="Download" size="sm" class="mr-1.5" />
                        Télécharger
                    </Button>
                    <Button variant="primary" class="w-10 h-10 p-0 rounded-full sm:hidden" @click="emit('download')">
                        <Icon :icon="Download" size="sm" />
                    </Button>
                </div>
            </div>

            <!-- Zone de prévisualisation -->
            <div class="flex-1 bg-[#F0F2F5] overflow-auto flex items-center justify-center p-4 relative">
                <template v-if="isImage && url">
                    <img :src="url" :alt="title"
                        class="max-w-full max-h-full object-contain rounded shadow-md border border-[#CED0D4]/40 bg-white" />
                </template>

                <template v-else-if="type === 'pdf' && url">
                    <iframe :src="url" class="w-full h-full border-none bg-white shadow-sm"
                        title="PDF Preview"></iframe>
                </template>

                <template v-else>
                    <!-- Fallback vide pour les documents non affichables online -->
                    <div
                        class="bg-white p-8 rounded-xl shadow-sm border border-[#CED0D4] max-w-sm w-full text-center space-y-4">
                        <div class="w-16 h-16 bg-[#F0F2F5] rounded-full flex items-center justify-center mx-auto">
                            <Icon :icon="FileText" size="xl" color="secondary" />
                        </div>
                        <div>
                            <Heading level="4">Aperçu indisponible</Heading>
                            <Text variant="secondary" class="mt-2 text-sm">Ce type de fichier ne peut pas être
                                prévisualisé directement. Veuillez le télécharger pour le consulter.</Text>
                        </div>
                        <Button variant="primary" class="w-full mt-4" @click="emit('download')">
                            Télécharger le fichier
                        </Button>
                    </div>
                </template>
            </div>
        </div>
    </Modal>
</template>
