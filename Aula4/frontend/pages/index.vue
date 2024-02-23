<script setup>
    let message = ref("")
    let response = ref("")
    const sendMessage = async () => {
        //message.value;
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
                question: message
            }   
        })
        response.value = answer
    }
</script>

<template>
    <div>
        <TextBox name="André" avatarImage="user.png" message="Teste"/>
        <TextBox name="Bot" avatarImage="bot.png" message="Olá sou o Bot!"/>
        <label for=""> Type here your message!</label> <br>
        <textarea v-model="message"/> <br> <br>        
        <Button @click="sendMessage" label="Send"></Button>
        <hr>
        <div>
            <h5>Bard: 😊</h5>
            <p> {{ response }} </p>
        </div>
    </div>
</template>

<style scoped>
     
    /* button{
        background-color: black;
        color: white;
    } */
</style>