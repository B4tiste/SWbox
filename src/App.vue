<template>
    <div id="app">
        <header>
            <LogoComponent />
            <MonsterSearch @monster-selected="addSelectedMonster" />
        </header>

        <main>
            <aside class="left-section">
                <SelectedMonstersList :selectedMonsters="selectedMonsters" />
            </aside>

            <section class="right-section">
                <TabsBar @change-tab="changeTab" />
                <component :is="currentTabComponent" v-bind:selectedMonsters="selectedMonsters" />
            </section>
        </main>

        <footer>
            <button @click="toggleTheme" id="theme-toggle">
                Passer au thème {{ getCurrentTheme }}
            </button>
            <a @click.prevent="openReleaseNotes" id="release-toggle">Release Notes</a>
        </footer>

        <ReleaseNotesPopup ref="releaseNotesPopup" />
    </div>
</template>

<script>
import LogoComponent from './components/LogoComponent.vue';
import MonsterSearch from './components/MonsterSearch.vue';
import SelectedMonstersList from './components/SelectedMonstersList.vue';
import TabsBar from './components/TabsBar.vue';
import CategoriesComponent from './components/CategoriesComponent.vue';
import GameOrderComponent from './components/GameOrderComponent.vue'; // À développer
import DraftComponent from './components/DraftComponent.vue'; // À développer
import ReleaseNotesPopup from './components/ReleaseNotesPopup.vue';

export default {
    name: 'App',
    components: {
        LogoComponent,
        MonsterSearch,
        SelectedMonstersList,
        TabsBar,
        CategoriesComponent,
        GameOrderComponent,
        DraftComponent,
        ReleaseNotesPopup
    },
    data() {
        return {
            selectedMonsters: [],
            currentTab: 'categories' // Onglet par défaut
        };
    },
    computed: {
        currentTabComponent() {
            return {
                categories: CategoriesComponent,
                gameOrder: GameOrderComponent,
                draft: DraftComponent
            }[this.currentTab] || CategoriesComponent;
        },
        getCurrentTheme() {
            // Cette méthode renvoie le thème actuel, 'dark' ou 'light'
            return document.documentElement.getAttribute('data-theme') === 'dark' ? 'clair' : 'sombre';
        }
    },
    methods: {
        toggleTheme() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);

            this.updateButtonText(newTheme === 'dark' ? 'clair' : 'sombre');
        },
        updateButtonText(theme) {
            const themeToggle = document.getElementById('theme-toggle');
            themeToggle.innerText = 'Passer au thème ' + theme;
        },
        openReleaseNotes() {
            this.$refs.releaseNotesPopup.openPopup();
        },
        addSelectedMonster(monster) {
            if (!this.selectedMonsters.includes(monster)) {
                this.selectedMonsters.push(monster);
            }
        },
        updateSelectedMonsters(newSelectedMonsters) {
            this.selectedMonsters = newSelectedMonsters;
        },
        changeTab(newTab) {
            this.currentTab = newTab;
        }
    }
};
</script>

<style>
#app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
    background: var(--primary-bg-color, #fff);
    color: var(--primary-text-color, #333);
}

header {
    display: flex;
    justify-content: left;
    padding: 1rem;
    background: var(--header-bg-color, #f5f5f5);
    max-height: 200px;
}

main {
    display: flex;
    flex: 1;
}

.left-section {
    width: 33.333%;
    background: var(--left-section-bg-color, #e9e9e9);
    padding: 1rem;
}

.right-section {
    width: 66.666%;
    padding: 1rem;
    overflow: hidden;
}

footer {
    padding: 1rem;
    background: var(--footer-bg-color, #f5f5f5);
}

/* Définition des thèmes */
:root {
    --primary-bg-color: #fff;
    --primary-text-color: #333;
    --header-bg-color: #f5f5f5;
    --left-section-bg-color: #e9e9e9;
    --footer-bg-color: #f5f5f5;
}

[data-theme='dark'] {
    --primary-bg-color: #333;
    --primary-text-color: #eee;
    --header-bg-color: #444;
    --left-section-bg-color: #555;
    --footer-bg-color: #444;
}
</style>
