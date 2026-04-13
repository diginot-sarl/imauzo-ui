import codecs
import re

file_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\docs\InputsDoc.vue'
app_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\App.vue'
feedback_path = r'c:\Users\aron\hologram\backup\imauzo\apps\imauzo-ui\src\docs\FeedbackDoc.vue'

# 1. Update InputsDoc.vue
with codecs.open(file_path, 'r', 'utf-8') as f:
    inputs_content = f.read()

otp_import = "import OTPInput from '../components/ui/OTPInput.vue'\n"
if "OTPInput" not in inputs_content:
    inputs_content = inputs_content.replace(
        "import SearchInput", 
        otp_import + "import SearchInput"
    )

otp_vars = """const docUploadVal = ref(null)

const code6 = ref('')
const code4 = ref('')
const isComplete = ref(false)

const onComplete = (val: string) => {
    isComplete.value = true
    setTimeout(() => { isComplete.value = false }, 2000)
}
"""
if "code6 = ref('')" not in inputs_content:
    inputs_content = inputs_content.replace("const docUploadVal = ref(null)", otp_vars)

otp_section = """
    <Section title="OTP Input (Code PIN)">
      <div class="flex flex-col gap-6">
         <div>
            <Text variant="secondary" size="sm" class="mb-3 block">Format Standard (6 cases)</Text>
            <OTPInput :length="6" v-model="code6" @complete="onComplete" />
            <div class="h-6 mt-2">
                <span v-if="isComplete" class="text-sm font-semibold text-[#2FA14A] flex items-center gap-1"><CheckCircle class="w-4 h-4" /> Code validé: {{ code6 }}</span>
            </div>
         </div>
      </div>
    </Section>
"""
if "OTP Input (Code PIN)" not in inputs_content:
    inputs_content = inputs_content.replace("</Card>", otp_section + "  </Card>")

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(inputs_content)

# 2. Update App.vue
with codecs.open(app_path, 'r', 'utf-8') as f:
    app_content = f.read()

app_content = app_content.replace("<SidebarItem title=\"OTP Input\" :icon=\"Lock\" :active=\"activeDoc === 'otp'\" @click=\"activeDoc = 'otp'\" />", "")

with codecs.open(app_path, 'w', 'utf-8') as f:
    f.write(app_content)

# 3. Update FeedbackDoc.vue
with codecs.open(feedback_path, 'r', 'utf-8') as f:
    feedback_content = f.read()
    
feedback_vars_imports = """
import Modal from '../components/ui/Modal.vue'
import ConfirmDialog from '../components/ui/ConfirmDialog.vue'

const showSnackbar = ref(false)
const showModal = ref(false)
const showConfirm = ref(false)
"""

if "Modal from" not in feedback_content:
    feedback_content = feedback_content.replace("const showSnackbar = ref(false)", feedback_vars_imports.strip())

modal_section = """
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
"""

if "Modale d'Information" not in feedback_content:
    feedback_content = feedback_content.replace("</template>", modal_section + "\n</template>")
    
with codecs.open(feedback_path, 'w', 'utf-8') as f:
    f.write(feedback_content)
    
print("Updated OTPInput integration and Feedback Modals.")
