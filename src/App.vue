<template>
    <div id="app">
        <!-- Container pour les deux composants principaux -->
        <div class="components-container">
            <MonsterSearch @monster-selected="addSelectedMonster" />
            <SelectedMonsters @monster-unselected="removeSelectedMonster"
                @update:selectedMonsters="newMonsters => selectedMonsters = newMonsters"
                :selectedMonsters="selectedMonsters" />
        </div>
        <button @click="toggleTheme" id="theme-toggle">
            Passer au thème {{ getCurrentTheme }}
        </button>
        <a href="#" @click.prevent="openReleaseNotes" id="release-toggle">Release Notes</a>
        <release-notes-popup ref="releaseNotesPopup" />
    </div>
</template>

<script>
import MonsterSearch from './components/MonsterSearch.vue';
import SelectedMonsters from './components/SelectedMonsters.vue';
import ReleaseNotesPopup from './components/ReleaseNotesPopup.vue';

export default {
    name: 'App',
    components: {
        MonsterSearch,
        SelectedMonsters,
        ReleaseNotesPopup
    },
    data() {
        return {
            selectedMonsters: []
        }
    },
    mounted() {
        // Vérification du thème préféré de l'utilisateur
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
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

            // Changer le texte du bouton
            const themeToggle = document.getElementById('theme-toggle');
            if (newTheme === 'dark') {
                themeToggle.innerText = 'Passer au thème clair';
            } else {
                themeToggle.innerText = 'Passer au thème sombre';
            }
        },
        addSelectedMonster(monster) {
            if (!this.selectedMonsters.includes(monster)) {
                this.selectedMonsters.push(monster);
            }
        },
        removeSelectedMonster(monster) {
            this.selectedMonsters = this.selectedMonsters.filter(selectedMonster => selectedMonster !== monster);
        },
        openReleaseNotes() {
            this.$refs.releaseNotesPopup.openPopup();
        }
    }
};
</script>

<style>
* {
    background-color: var(--primary-bg-color);
}

body {
    font-family: 'Roboto', sans-serif;
    font-weight: 500;
    font-size: 20px;
}

:root {
    --primary-bg-color: #ffffff;
    --primary-text-color: #333;
    --input-border-color: #ccc;
    --list-item-border-color: #ddd;
}

[data-theme='dark'] {
    --primary-bg-color: #333;
    --primary-text-color: #eee;
    --input-border-color: #555;
    --list-item-border-color: #444;
}

#app {
    text-align: center;
    margin-top: 50px;
    max-width: 1200px;
    /* Ajusté pour tenir compte du nouveau design */
    margin-left: auto;
    margin-right: auto;
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
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

#theme-toggle {
    position: fixed;
    bottom: 10px;
    left: 10px;
    font-size: 18px;
}

[data-theme='light'] #theme-toggle {
    background-color: #333;
    color: #eee;
}

[data-theme='dark'] #theme-toggle {
    background-color: #eee;
    color: #333;
}

.monster-icon {
    width: 80px;
    height: 80px;
    margin-right: 10px;
}

.components-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin: 0 auto;
    padding: 20px;
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
</style>
