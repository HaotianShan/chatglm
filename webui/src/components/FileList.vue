<template>
    <div class="mouseover-button" @mouseover="showButton" @mouseleave="hideButton">
        <div class="content">
            <slot></slot>
        </div>
        <button class="button" v-show="show">
            <el-table :data="tableData">
                <el-table-column prop="id" label="ID" width="50px"></el-table-column>
                <el-table-column prop="name" label="文件名称" width="150px"></el-table-column>
            </el-table>
        </button>
    </div>
</template>
   
<script lang = "ts" setup>
import axios from 'axios';
import { ref } from 'vue';

const show = ref(false);
const showButton = () => {
    show.value = true
};
const hideButton = () => {
    show.value = false
};

interface File {
    id: string
    name: unknown
}
const tableData = ref<File[]>([])

const getFileList = async () => {
    try {
        const response = await axios.get(`${import.meta.env.VITE_WENDA_URL}/api/fileList`)
        const { fileList } = response.data
        tableData.value = Object.entries(fileList).map(([id, name]) => ({ id, name }))
    } catch (error) {
        console.error(error)
    }
}

getFileList()
show;
showButton;
hideButton;
tableData;
</script>
   
<style scoped>
.mouseover-button {
    position: relative;
    display: inline-block;
}

.content {
    display: inline-block;
}

.button {
    position: absolute;
    top: 0%;
    right: 0%;
    transform: translate(0%, 20%);
    padding: 10px 10px;
    background-color: #42b983;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
</style>