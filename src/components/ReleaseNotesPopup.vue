<template>
    <div v-if="isVisible" class="release-notes-popup">
        <div class="release-notes-content">
            <div class="wrapper">
                <div v-html="markdownContent"></div>
            </div>
        </div>
        <button @click="closePopup" class="close-button">Fermer</button>
    </div>
</template>

<script>
import MarkdownIt from 'markdown-it';
import axios from 'axios';

export default {
    data() {
        return {
            isVisible: false,
            markdownContent: ''
        };
    },
    methods: {
        async openPopup() {
            this.isVisible = true;
            try {
                const response = await axios.get('data/release.md');
                const md = new MarkdownIt({
                    html: true // Activation de l'interpretation du code HTML
                });
                this.markdownContent = md.render(response.data);
            } catch (error) {
                console.error('Error fetching the markdown file', error);
            }
        },
        closePopup() {
            this.isVisible = false;
        }
    }
};
</script>

<style>
.release-notes-popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
    box-sizing: border-box;
}

.release-notes-content {
    background-color: var(--primary-bg-color);
    padding: 20px;
    border-radius: 16px;
    width: 60%;
    height: 80%;
    overflow-y: auto;
    text-align: left;
    border: 1px solid black;
    position: relative;
}

.wrapper {
    height: 95%;
    overflow-y: scroll;
}

.close-button {
    margin-top: 20px;
    border: none;
    background-color: transparent;
    cursor: pointer;
    font-size: 20px;
    color: var(--primary-text-color);
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background-color: var(--primary-bg-color);
}

/* CSS dans le markdown */
#author-name {
    color: #ff9900; /* Changer la couleur */
    font-weight: bold; /* Rendre le texte en gras */
    background-color: #f2f2f2; /* Fond différent */
    padding: 5px;
    border-radius: 4px; /* Bords arrondis */
}

/* Scroll Bar */
::-webkit-scrollbar
{
    width: 10px;
    background-color: transparent;
}

::-webkit-scrollbar-track
{
	background-color: transparent;
}

::-webkit-scrollbar-thumb
{
	background-color: var(--primary-text-color);
    border-radius: 5px;
}

</style>
