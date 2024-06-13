<template>
    <div class="container-all">
        <div class="container-monster">
            <h2 >Monstres sélectionnés:</h2>
            <!-- if vide : "Vide" -->
            <div v-if="selectedMonsters.length === 0">🚫</div>
            <div v-else class="selected-monsters-container">
                <draggable class="grid-container-monster" :list="selectedMonsters" group="monsters" @change="updateSelected">
                    <div v-for="monster in selectedMonsters" :key="monster.id" @click="unselectMonster(monster)">
                        <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                    :alt="monster.name" class="monster-icon" />
                </div>
            </draggable>
        </div>

            <h2>Catégories:</h2>
            <div class="categories-container">
                <div v-for="(category, index) in categories" :key="index" class="category-wrapper">
                    <input v-model="category.name" @change="updateCategoryName(category)" />
                    <button class="delete" @click="removeCategory(index)">Supprimer</button>
                    <draggable :list="category.monsters" class="grid-container-categorie" group="monsters" @change="updateCategory(category)">
                        <div v-for="monster in category.monsters" :key="monster.id">
                            <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                                :alt="monster.name" class="monster-icon" />
                        </div>
                    </draggable>
                </div>
            </div>
            <button @click="addCategory">Ajouter une catégorie</button>
        </div>
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
        // Vérification du contenu du local storage
        if (localStorage.getItem('categories')) {
            this.categories = JSON.parse(localStorage.getItem('categories'));
        }
    },
    methods: {
        addCategory() {
            this.categories.push({ name: "Nouvelle catégorie", monsters: [] });

            this.saveData();
        },
        removeCategory(index) {
            // Renvoyer les monstres de la catégorie à la liste principale
            const newSelectedMonsters = this.selectedMonsters.concat(this.categories[index].monsters);

            // Émettez un événement pour informer le composant parent
            this.$emit('update:selectedMonsters', newSelectedMonsters);

            // Supprimer la catégorie
            this.categories.splice(index, 1);

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
            localStorage.setItem('categories', JSON.stringify(this.categories));
            // console.log(localStorage.getItem('categories'));
        }
    }
}
</script>

<style scoped>
.container-all {
    padding-left: 10px;
    border-left: 2px solid var(--input-border-color);
    display: flex;
    flex-direction: column;
    gap: 20px; /* Ajoute un espace entre les sections */
}

/* Styles pour le titre <h2> */
h2 {
    font-size: 24px; /* Réduit la taille de la police pour les titres */
    margin-top: 5px; /* Supprime le padding en haut */
    margin-bottom: 10px; /* Réduit l'espace en bas */
    padding: 0; /* Supprime tout padding */
}

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

.delete {
    margin-left: 10px;
}

button {
    padding: 5px 15px;
    margin: 5px 0;
    border: none;
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border: 1px solid var(--input-border-color);
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

button:hover {
    background-color: var(--button-hover-bg-color);
}

.container-monster {
    display: flex;
    flex-direction: column;
}

/* Styles pour les monstres sélectionnés */
.selected-monsters-container {
    display: flex;
    justify-content: center;
    align-items: flex-start; /* Aligne les éléments en haut */
    width: 450px;
    height: 118px;
    overflow-y: auto; /* Active le défilement vertical si nécessaire */
    padding: 10px; /* Ajoute un peu de padding autour du contenu */
    border: 1px solid var(--input-border-color);
    border-radius: 4px;
    background-color: var(--primary-bg-color);
}

.categories-container {
    max-height: 55vh; /* Hauteur maximale pour permettre le scroll */
    overflow-y: auto; /* Active le défilement vertical si nécessaire */
    padding-right: 10px;
}

/* Styles pour les catégories */
.category-wrapper {
    margin-bottom: 20px;
    width: 450px;
    padding: 10px; /* Ajoute un peu de padding autour du contenu */
    border: 1px solid var(--input-border-color);
    border-radius: 4px;
    background-color: var(--primary-bg-color);
}

/* Styles pour la grille de monstres */
.grid-container-monster {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(55px, 1fr));
    width: 100%;
    /* Ajout du overflow-y pour forcer le scroll dans la grille si nécessaire */
    overflow-y: auto;
    overflow-x: hidden;
    max-height: inherit; /* Utilise la même hauteur maximale que le parent */
}

.grid-container-categorie {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(55px, 1fr));
    width: 100%;
    max-height: 120px;
    /* Ajout du overflow-y pour forcer le scroll dans la grille si nécessaire */
    overflow-y: auto;
    overflow-x: hidden;
    max-height: inherit; /* Utilise la même hauteur maximale que le parent */
}

/* Styles pour les icônes de monstres */
.monster-icon {
    width: 50px;
    height: 50px;
    border: 2px solid black;
}

</style>
