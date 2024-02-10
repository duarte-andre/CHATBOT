<script setup>
    let message = ref("")
    const sendMenssage = async () => {
        //message.value;
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
                question: message
            }
        })
    }
</script>

<template>
    <div>
        <label for=""> Type here your message!</label> <br>
        <textarea v-model="message"/> <br> <br>
        <button @click="sendMenssage"> Send</button>
    </div>
</template>

<style scoped>
     
    button{
        background-color: black;
        color: white;
    }
</style>