<template>
    <div>
        <h2>Monstres sélectionnés</h2>
        <!-- if vide : "Vide" -->
        <div v-if="selectedMonsters.length === 0">🚫</div>
        <div class="selected-monsters-container">
            <draggable class="grid-container" :list="selectedMonsters" group="monsters" @change="updateSelected">
                <div v-for="monster in selectedMonsters" :key="monster.id" @click="unselectMonster(monster)">
                    <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                :alt="monster.name" class="monster-icon" />
            </div>
        </draggable>
    </div>

        <h2>Catégories</h2>
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
        <button @click="addCategory">Ajouter une catégorie</button>
    </div>
</template>
Z

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

button:hover {
    background-color: var(--button-hover-bg-color);
    /* Définissez cette variable dans vos styles globaux ou remplacez-la par une couleur spécifique */
}

.selected-monsters-container {
    display: flex;
    justify-content: center;
    width: 100%;
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(55px, 1fr));
    width: 100%;
    gap: 5px;
    row-gap: 0;
    /* column-gap: 0; */
}

.category-wrapper {
    margin-bottom: 20px;
}

.monster-icon {
    width: 60px;
    height: 60px;
    border: 2px solid black;
    /* margin: 0; */
    /* padding: 0; */
}
</style>
