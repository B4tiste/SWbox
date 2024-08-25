<template>
    <div>
        <h2>Monstres sélectionnés</h2>
        <!-- Message pour les monstres sélectionnés vides -->
        <div v-if="selectedMonsters.length === 0">🚫 Aucun monstre sélectionné</div>
        <div class="selected-monsters-container">
            <draggable class="grid-container" :list="selectedMonsters" group="monsters" @change="updateSelected">
                <div v-for="monster in selectedMonsters" :key="monster.id" @click="unselectMonster(monster)">
                    <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                         :alt="monster.name" class="monster-icon" />
                </div>
            </draggable>
        </div>

        <h2>Catégories</h2>
        <!-- Début du conteneur scrollable -->
        <div class="categories-container">
            <div v-for="(category, index) in categories" :key="index" class="category-wrapper">
                <input v-model="category.name" @change="updateCategoryName(category)" />
                <button @click="removeCategory(index)">Supprimer</button>
                <draggable :list="category.monsters" class="grid-container" group="monsters" @change="updateCategory(category)">
                    <div v-for="monster in category.monsters" :key="monster.id">
                        <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                             :alt="monster.name" class="monster-icon" />
                    </div>
                </draggable>
            </div>
        </div>
        <!-- Fin du conteneur scrollable -->

        <button @click="addCategory">Ajouter une catégorie</button>
        <button @click="resetCategories">Réinitialiser les catégories</button>
    </div>
</template>

<script>
import draggable from 'vuedraggable';

export default {
    props: ['selectedMonsters'],
    components: {
        draggable
    },
    data() {
        return {
            categories: [
                { name: "Catégorie 1", monsters: [] },
                { name: "Catégorie 2", monsters: [] },
                { name: "Catégorie 3", monsters: [] }
            ]
        };
    },
    mounted() {
        // Chargement des catégories depuis le localStorage
        if (localStorage.getItem('categories')) {
            this.categories = JSON.parse(localStorage.getItem('categories'));
        }
    },
    methods: {
        addCategory() {
            const newCategoryName = "Nouvelle catégorie";

            this.categories.push({ name: newCategoryName, monsters: [] });
            this.saveData();
        },
        removeCategory(index) {
            // Renvoyer les monstres de la catégorie supprimée à la liste principale
            const newSelectedMonsters = this.selectedMonsters.concat(this.categories[index].monsters);

            // Émettre un événement pour informer le composant parent
            this.$emit('update:selectedMonsters', newSelectedMonsters);

            // Supprimer la catégorie
            this.categories.splice(index, 1);

            this.saveData();
        },
        resetCategories() {
            // Renvoyer tous les monstres des catégories à la liste principale
            const newSelectedMonsters = this.selectedMonsters.concat(...this.categories.map(category => category.monsters));

            // Émettre un événement pour informer le composant parent
            this.$emit('update:selectedMonsters', newSelectedMonsters);

            // Réinitialiser les catégories à l'état initial
            this.categories = [
                { name: "Catégorie 1", monsters: [] },
                { name: "Catégorie 2", monsters: [] },
                { name: "Catégorie 3", monsters: [] }
            ];
            this.saveData();
        },
        unselectMonster(monster) {
            this.$emit('monster-unselected', monster);
        },
        updateSelected(event) {
            this.$emit('selected-monsters-updated', event);
        },
        updateCategory(category) {
            this.$emit('category-updated', category);
            this.saveData();
        },
        updateCategoryName(category) {
            this.$emit('category-name-updated', category);
            this.saveData();
        },
        saveData() {
            // Sauvegarder les catégories dans le localStorage
            localStorage.setItem('categories', JSON.stringify(this.categories));
        }
    }
}
</script>

<style scoped>
/* Styles pour les inputs */
input {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid var(--input-border-color);
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border-radius: 4px;
    width: 300px;
    font-size: 18px;
    text-align: center;
}

input:focus {
    outline: 2px solid var(--focus-border-color);
}

/* Styles pour les boutons */
button {
    padding: 5px 15px;
    margin: 5px 0;
    border: none;
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:focus {
    outline: 2px solid var(--focus-border-color);
}

button:hover {
    background-color: var(--button-hover-bg-color);
}

/* Styles pour la section des monstres sélectionnés */
.selected-monsters-container {
    display: flex;
    justify-content: center;
    width: 100%;
}

/* Styles pour la grille des monstres */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(55px, 1fr));
    width: 100%;
    gap: 5px;
}

/* Styles pour le conteneur scrollable des catégories */
.categories-container {
    max-height: 500px; /* Hauteur maximale pour le conteneur des catégories */
    overflow-y: auto; /* Activer le défilement vertical si le contenu dépasse */
}

/* Styles pour chaque catégorie */
.category-wrapper {
    margin-bottom: 20px;
}

/* Styles pour les images des monstres */
.monster-icon {
    width: 60px;
    height: 60px;
    border: 2px solid black;
}
</style>
