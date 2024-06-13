<template>
    <div class="navbar">
        <img src="@/assets/nameLogo.png" alt="SWbox logo" class="logo" />
        <a href="#" @click.prevent="notifyOpenReleaseNotes" class="release-notes">Info & Release Notes</a>
    </div>
</template>

<script>
export default {
    name: 'NavbarCustom',
    methods: {
        notifyOpenReleaseNotes() {
            this.$emit('open-release-notes'); // Émet un événement personnalisé
        }
    }
};
</script>

<style scoped>
.logo {
    height: 50px; /* Ajustez selon la taille souhaitée du logo */
    margin-left: 20px; /* Espace à gauche pour le logo */
}
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between; /* Assure que les éléments sont espacés */
    padding: 10px; /* Ajoute un peu de padding autour de la barre de navigation */
}
.release-notes {
    color: white; /* Couleur du texte */
    text-decoration: none; /* Supprimez le soulignement */
    font-size: 20px; /* Taille de la police */
    cursor: pointer; /* Curseur pointer pour indiquer un lien cliquable */
    margin-right: 20px; /* Espace à droite pour le lien */
}

.release-notes:hover {
    text-decoration: underline; /* Ajouter un soulignement au survol */
}
</style>
