<template>
    <div>
        <h2>Monstres sélectionnés</h2>
        <!-- if vide : "Vide" -->
        <div v-if="selectedMonsters.length === 0">🚫</div>
        <draggable class="grid-container" :list="selectedMonsters" group="monsters" @change="updateSelected">
            <div v-for="monster in selectedMonsters" :key="monster.id" @click="unselectMonster(monster)">
                <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                    :alt="monster.name" class="monster-icon" />
            </div>
        </draggable>

        <h2>Catégories</h2>
        <div v-for="(category, index) in categories" :key="index" class="category-wrapper">
            <input v-model="category.name" />
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
    methods: {
        addCategory() {
            this.categories.push({ name: "Nouvelle catégorie", monsters: [] });
        },
        removeCategory(index) {
            // Renvoyer les monstres de la catégorie à la liste principale
            const newSelectedMonsters = this.selectedMonsters.concat(this.categories[index].monsters);

            // Émettez un événement pour informer le composant parent
            this.$emit('update:selectedMonsters', newSelectedMonsters);

            // Supprimer la catégorie
            this.categories.splice(index, 1);
        },
        unselectMonster(monster) {
            this.$emit('monster-unselected', monster);
        },
        updateSelected(event) {
            this.$emit('selected-monsters-updated', event);
        },
        updateCategory(category) {
            this.$emit('category-updated', category);
        }

    }
}
</script>

<style scoped>
input {
    padding: 10px;
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

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
    gap: 10px;
}

.category-wrapper {
  margin-bottom: 20px;
}

.monster-icon {
    width: 60px;
    height: 60px;
    margin-right: 10px;
}
</style>
