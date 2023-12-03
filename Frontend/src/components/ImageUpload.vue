<script setup>
import {UploadFilled} from "@element-plus/icons-vue";
import {ElMessage, genFileId} from "element-plus";

const upload = ref()    // todo: 未进行双向绑定，暂搁置
const fileList = ref([])

function onBeforeUploadImage(file) {
    /* 图片上传前校验 */
    const isIMAGE = file.type === 'image/jpeg' || 'image/jpg' || 'image/png'
    const isLt1M = file.size / 1024 / 1024 < 1
    if (!isIMAGE) {
        ElMessage({
            message: '上传文件只能是图片格式!',
            type: 'error'
        })
    }
    if (!isLt1M) {
        ElMessage({
            message: '上传文件大小不能超1MB!!',
            type: 'error'
        })
    }
    return isIMAGE && isLt1M
}

function handleExceed(files){
    upload.value.clearFiles()
    const file = files[0]
    file.uid = genFileId()
    upload.value.handleStart(file)
}

function fileChange(file) {
    /* 文件状态变更钩子 */
    console.debug(file)
}

</script>

<template>
    <div class="content">
        <el-upload drag ref="upload" list-type="picture"
                   action="/apiDev/upload" accept="image/jpeg,image/jpg"
                   :auto-upload="false" :file-list="fileList" :before-upload="onBeforeUploadImage"
                   :limit="1" :on-exceed="handleExceed" :on-change="fileChange"
        >
            <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            <template #tip>
                <div class="el-upload__tip" style="text-align: left">
                    jpg 文件的大小必须小于 1MB
                </div>
            </template>
        </el-upload>
    </div>
</template>

<style scoped>

</style>