<template>
    <div class="logo-container">
        <img src="@/assets/logo.png" alt="Logo" />
    </div>
</template>

<script>
export default {
    name: 'LogoComponent',
    // Tu peux ajouter ici des props, des données, des méthodes si nécessaire
};
</script>

<style scoped>
.logo-container img {
    width: 100px;
    /* ou la taille que tu préfères */
    height: auto;
    /* Autres styles si nécessaire */
}
</style>
