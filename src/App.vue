<template>
    <div id="app-container">
        <!-- Contenu de l'application -->
        <div id="app">
            <!-- Container pour les deux composants principaux -->
            <div class="components-container">
                <navbarCustom @open-release-notes="openReleaseNotes" />
                <div class="monsterContainer">
                    <MonsterSearch @monster-selected="addSelectedMonster" />
                    <SelectedMonsters 
                        @monster-unselected="updateSelectedMonster"
                        @selected-monsters-updated="updateSelectedMonster"
                        @update:selectedMonsters="newMonsters => selectedMonsters = newMonsters"
                        :selectedMonsters="selectedMonsters" 
                    />
                </div>
            </div>
            <button @click="toggleTheme" id="theme-toggle">
                <img class = "img-switch-mod" src="@/assets/sun-moon.png"/>
            </button>
            <release-notes-popup ref="releaseNotesPopup" />
        </div>
    </div>
</template>

<script>
import NavbarCustom from './components/NavbarCustom.vue';
import MonsterSearch from './components/MonsterSearch.vue';
import SelectedMonsters from './components/SelectedMonsters.vue';
import ReleaseNotesPopup from './components/ReleaseNotesPopup.vue';

export default {
    name: 'App',
    components: {
        NavbarCustom,
        MonsterSearch,
        SelectedMonsters,
        ReleaseNotesPopup
    },
    data() {
        return {
            selectedMonsters: [],
            scoreData: null,
        }
    },
    mounted() {
        // Vérification du thème préféré de l'utilisateur
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
        }

        // Check localStorage
        if (localStorage.selectedMonsters) {
            this.selectedMonsters = localStorage.getItem('selectedMonsters');
            this.selectedMonsters = JSON.parse(this.selectedMonsters)
        }
    },
    metaInfo(){
        // Si les données sont disponibles, mettre à jour les meta tags Open Graph
        return {
            title: 'Classement SW',
            // meta: [
            //     { property: 'og:title', content: 'Classement SW' },
            //     { property: 'og:description', content: `Score S3: ${this.scoreData?.s3}, G1: ${this.scoreData?.g1}, G2: ${this.scoreData?.g2}, G3: ${this.scoreData?.g3}` },
            //     { property: 'og:image', content: 'URL_DE_VOTRE_IMAGE_DE_PREVIEW' }, // Image que vous souhaitez afficher dans la preview
            //     { property: 'og:url', content: 'https://swbox.netlify.app/rank' },
            // ]
            meta:[
                {property: 'og:title', content: 'test'},
            ]
        }
    },
    computed: {
        getCurrentTheme() {
            return document.documentElement.getAttribute('data-theme') === 'dark' ? 'clair' : 'sombre';
        }
    },
    methods: {
        toggleTheme() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);

        },
        addSelectedMonster(monster) {
            if (!this.selectedMonsters.includes(monster)) {
                this.selectedMonsters.push(monster);
            }
            this.refreshSelectedMonsterLocalStorageValue();
        },
        updateSelectedMonster(monster) {
            this.selectedMonsters = this.selectedMonsters.filter(selectedMonster => selectedMonster !== monster);
            this.refreshSelectedMonsterLocalStorageValue();
        },
        openReleaseNotes() {
            this.$refs.releaseNotesPopup.openPopup();
        },
        refreshSelectedMonsterLocalStorageValue() {
            localStorage.setItem('selectedMonsters', JSON.stringify(this.selectedMonsters))
        }
    }
};
</script>

<style>


:root {
    --bg-image: url('@/assets/bg_white.png');
    --primary-bg-color: #ffffff;
    --primary-text-color: #000000;
    --input-border-color: #000000;
    --list-item-border-color: #ddd;
    --button-hover-bg-color: #f0f0f0;
}

[data-theme='dark'] {
    --bg-image: url('@/assets/bg_black.png');
    --primary-bg-color: #333;
    --primary-text-color: #eee;
    --input-border-color: #555;
    --list-item-border-color: #444;
    --button-hover-bg-color: #404040;
}

#app {
    text-align: center;
    max-width: auto;
    /* Ajusté pour tenir compte du nouveau design */
    margin-left: auto;
    margin-right: auto;
    color: var(--primary-text-color);
}
html {
    background-image: var(--bg-image);
    background-repeat: no-repeat;
    background-color: #000;
    overflow: hidden;
}
body {
    font-family: 'Roboto', sans-serif;
    font-weight: 500;
    font-size: 20px;
}
button {
    padding: 10px;
    border: 1px solid var(--input-border-color);
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border-radius: 4px;
    margin-top: 10px;
    padding-bottom: 12px;
}

button:hover {
    cursor: pointer;
    background-color: var(--input-border-color);
}

.monsterContainer {
    margin-top: 15vh;
    display: flex;
}

button:hover {
    cursor: pointer;
    background-color: var(--input-border-color);
}

#theme-toggle {
    position: fixed;
    bottom: 10px;
    right: 10px;
    width: 50px;
    height: 50px;
    border-radius: 50%; /* Assure que le bouton reste circulaire */
    display: flex; /* Utilise flexbox pour centrer le contenu */
    justify-content: center; /* Centre le contenu horizontalement */
    align-items: center; /* Centre le contenu verticalement */
}

[data-theme='light'] #theme-toggle {
    background-color: #333;
    color: #eee;
}

[data-theme='dark'] #theme-toggle {
    background-color: #eee;
    color: #333;
}

.img-switch-mod {
    width: 30px; /* Largeur de l'image */
    height: 30px; /* Hauteur de l'image */
}


.monster-icon {
    width: 80px;
    height: 80px;
    margin-right: 10px;
    border: 2px solid black;
}

#release-toggle {
    /* Position */
    position: fixed;
    bottom: 10px;
    right: 10px;

    /* Style */
    padding: 10px;
    border: 1px solid var(--input-border-color);
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border-radius: 4px;
}

MonsterSearch {
    flex: 1;
    margin-right: 20px;
}

SelectedMonsters {
    flex: 2;
}
.img-switch-mod{
    width: 35px;
    height: 35px;
}
</style>

