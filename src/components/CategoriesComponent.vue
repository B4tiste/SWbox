<template>
    <div>
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
        updateCategory(category) {
            this.$emit('category-updated', category);
        }
    }
}
</script>

<style scoped>
.category-wrapper {
    margin-bottom: 20px;
    background: var(--category-bg-color, #f0f0f0);
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    /* Ajout d'ombre pour un effet de profondeur */

    /* Assure-toi que les catégories ne dépassent pas de leur conteneur */
    max-width: calc(100% - 20px);
    /* 20px représente le padding total horizontal */
}

input {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid var(--input-border-color, #ccc);
    background-color: var(--input-bg-color, #fff);
    color: var(--input-text-color, #333);
    border-radius: 4px;
    width: 100%;
    font-size: 18px;
    text-align: center;
}

button {
    padding: 5px 15px;
    margin: 5px 0;
    border: none;
    background-color: var(--button-bg-color, #ddd);
    color: var(--button-text-color, #333);
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

input, button {
    max-width: 100%;
}

button:hover {
    background-color: var(--button-hover-bg-color, #ccc);
}

.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
    gap: 10px;
}

.monster-icon {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
}

h2 {
    color: var(--primary-text-color, #333);
    margin-bottom: 0.5rem;
}

/* Définition des variables de thème pour CategoriesComponent */
:root {
    --category-bg-color: #f0f0f0;
    --input-bg-color: #fff;
    --input-border-color: #ccc;
    --input-text-color: #333;
    --button-bg-color: #ddd;
    --button-text-color: #333;
    --button-hover-bg-color: #ccc;
}

[data-theme='dark'] {
    --category-bg-color: #444;
    --input-bg-color: #555;
    --input-border-color: #666;
    --input-text-color: #eee;
    --button-bg-color: #555;
    --button-text-color: #eee;
    --button-hover-bg-color: #666;
    background-color: #3a3a3a;
    /* Un gris plus foncé pour les catégories en thème sombre */
}</style>
