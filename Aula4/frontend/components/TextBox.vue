<script setup>
    const props = defineProps({
        avatarImage: {type: String},
        name: {type: String},
        message: {type: String},
        type: {type: String}
    })
</script>

<template>
    <div>
        <Fieldset>
            <template #legend>
                <div class="flex align-items-center pl-2">
                    <Avatar :image="props.avatarImage" shape="circle" />
                    <span class="font-bold">{{ props.name }}</span>
                </div>
            </template>
            <p class="m-0">
                {{ props.message }}
            </p>
        </Fieldset>
    </div>
</template>

<style></style>