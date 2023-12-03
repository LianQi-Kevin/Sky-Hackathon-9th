<script setup>
// import { RouterLink, RouterView } from 'vue-router'
import pageHeader from '@/components/PageHeader.vue'
import Menu_left from "@/components/LeftMenu.vue";
</script>

<template>
    <div class="content">
        <pageHeader style="z-index: 1;" team-name="逻极"  title="Sky-Hackathon-9th"/>
        <Menu_left class="leftMenu" style="z-index: 1;" />
        <div class="routerView" style="z-index: 1;">
            <router-view class="basic"/>
        </div>
        <div style="user-select: none;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;">
            <div class="basic background" />
            <div class="basic mask1" />
        </div>
    </div>
</template>

<style scoped>
.basic {
    width: 100%;
    height: 100%;
}

div.mask1 {
    background: rgba(255, 255, 255, 20%);
    position: fixed;
    z-index: 0;
}

div.background {
    //filter: ;
    background-size: cover;     /* 基于容器大小伸缩 */
    position: fixed;     /* 跳出dom流 */
    z-index: -1;    /* 设置在底部 */
    background-image: url("assets/img/star_background.jpg");
    /* 背景图垂直、水平均居中 */
    background-position: center center;
    /* 背景图不平铺 */
    background-repeat: no-repeat;
    /* 当内容高度大于图片高度时，背景图像的位置相对于viewport固定 */
    background-attachment: fixed;
    /* 设置背景颜色，背景图加载过程中会显示背景色 */
    background-color: #464646;
}

.leftMenu {
    background: rgba(0, 0, 0, 70%);
    border-top: 20px;
    position: absolute;
    top: 50px;
    height: calc(100vh - 50px );
    width: 200px;
}

.routerView {
    position: absolute;
    top: 50px;
    left: 200px;
    width: calc(100vw - 200px);
    height: calc(100vh - 50px);
    //background: rgba(131, 68, 68, 0.7);
    z-index: 1;
}

</style>
