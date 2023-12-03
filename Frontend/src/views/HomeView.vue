<script setup>
import {Promotion, UploadFilled, Refresh} from "@element-plus/icons-vue";
import {ElMessage, genFileId} from "element-plus";
import StyleSelect from "@/components/StyleSelect.vue";
import {Generate} from "@/network/imgAPI.js";

const upload = ref()
const fileList = ref([])

// result refs
const SDXLStyles = ref()
//访问demo组件的方法或对象
// function getChild() {
    //获取到子组件的 styles 数据
    // const styles = JSON.parse(JSON.stringify(SDXLStyles.value.styles.styleList))
    // console.log(styles)
    //调用子组件的 getSDXLStyles 方法
    // return  SDXLStyles.value.getSDXLStyles()
// }

function reGenerateSDXL(){
    const styleList = SDXLStyles.value.getSDXLStyles()
    Generate(
        resultForm.chatStory,
        "",
        styleList
    ).then(res => {
        SDXLb64.value = [`data:image/jpeg;base64,${res.data.data.b64_json}`]
    }).catch(err => {
        console.error(err)
    })
}

const SDXLb64 = ref([])

const resultForm = reactive({
    detectResult: '',
    chatStory: '',
})

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


function fileChange(file) {
    /* 文件状态变更钩子 */
    console.debug(file)
}

function handleExceed(files){
    upload.value.clearFiles()
    const file = files[0]
    file.uid = genFileId()
    upload.value.handleStart(file)
}

</script>

<template>
    <div class="content">
        <div class="left">
            <span class="title --el-box-shadow-dark"><strong>Upload & Run</strong></span>
            <el-card class="box-card uploadCard itemDefault">
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
            </el-card>
            <el-button class="runButton itemDefault" type="primary" plain size="large" :icon="Promotion" @click="upload.submit()">
                Start
            </el-button>
        </div>
        <el-divider direction="vertical" style="height: 100%"/>
        <div class="right">
            <span class="title --el-box-shadow-dark"><strong>Result</strong></span>
            <el-card class="box-card itemDefault resultFormCard">
                <el-scrollbar height="500px">
                    <el-form
                        class="resultForm"
                        label-position="top"
                        :model="resultForm"
                        style="margin: 0"
                    >
                        <el-form-item label="图片检测结果" >
                            <el-input v-model="resultForm.detectResult" />
                        </el-form-item>
                        <el-form-item label="图像故事" >
                            <el-input
                                v-model="resultForm.chatStory"
                                type="textarea"
                                :autosize="{ minRows: 2, maxRows: 4 }"
                            />
                        </el-form-item>
                        <el-form-item label="SDXL 图像生成设置">
                            <StyleSelect ref="SDXLStyles"
                                style="width: calc(70% - 10px); flex-grow: 1"
                            />
                            <el-divider direction="vertical"/>
<!--                            todo: 暂时禁用详细设置-->
<!--                            <el-button :icon="Operation" style="width: calc(30% - 10px); flex-basis: 85px">-->
<!--                                Options-->
<!--                            </el-button>-->
                            <el-button
                                @click="reGenerateSDXL"
                                :icon="Refresh"
                                class="reGenerate"
                                style="width: calc(30% - 10px); flex-basis: 85px"
                            >
                                重新生成
                            </el-button>
                        </el-form-item>
                        <el-form-item label="SDXL 图像" >
                        </el-form-item>
                    </el-form>
                    <el-image
                        style="width: 180px; height: 180px"
                        :src="SDXLb64[0]"
                        :zoom-rate="1.2"
                        :max-scale="7"
                        :min-scale="0.2"
                        :preview-src-list="SDXLb64"
                        :initial-index="3"
                        fit="cover"
                    >
                    </el-image>
                </el-scrollbar>
            </el-card>
        </div>
    </div>
</template>

<style scoped lang="scss">
.itemDefault {
    background: rgba(0, 0, 0, 80%);
    margin: 0 15px;
    width: calc(100% - 30px);
}

.title {
    margin: 10px 15px 0 15px;
    padding: 5px 0 5px 10px;
    text-align: left;
    font-size: larger;
    background: rgba(0, 0, 0, 80%);
    border: 1px solid var(--el-border-color);
    border-radius: 6px;
    //box-shadow: 0 2px 4px rgba(0,0,0,0.12),0 0 6px rgba(0,0,0,0.04);
    box-shadow: 0 2px 4px var(--el-box-shadow-dark),0 0 6px var(--el-box-shadow-dark);
    color: rgb(207, 211, 220);
}

.content{
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: row;

    .left {
        //max-height: calc(100% - 50px);
        height: 100%;
        max-width: 50%;
        flex-grow: 1;
        //flex-flow: column;

        display: flex;
        flex-direction: column;
        justify-items: center;

        .uploadCard {
            margin: 15px;
        }

        .imgCard {
            width: 50%;
            height: 50%;
            .image {
                width: 100%;
                display: block;
            }
            span {
                font-size: 15px;
            }
        }
    }
    .right {
        height: 100%;
        max-width: 50%;
        flex-grow: 1;

        display: flex;
        flex-direction: column;
        justify-items: center;

        .resultFormCard {
            max-height: calc(100% - 50px - 40px);
            margin: 15px;

            .resultForm {
                .reGenerate {
                    width: 100%;
                    //margin-bottom: 15px;
                }
            }
        }
    }
}
</style>