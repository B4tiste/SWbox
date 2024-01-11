<template>
    <!-- Conteneur principal du composant -->
    <div>
        <!-- Logo ajouté ici -->
        <img src="@/assets/logo.png" class="logo" />

        <!-- Champ de saisie pour la recherche de monstres -->
        <input type="text" v-model="searchQuery" placeholder="Recherchez un monstre..." ref="searchInput"
            @keydown="handleKeydown">

        <!-- Liste des monstres filtrés -->
        <ul v-if="searchQuery && filteredMonsters.length">
            <li v-for="(monster, index) in filteredMonsters" :key="monster.id" @click="selectMonster(monster)"
                :class="{ 'highlighted': index === highlightedIndex }">
                <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                    :alt="monster.name" class="monster-icon" />
                {{ monster.name }}
            </li>
        </ul>
    </div>
</template>

<script>
// Importation des données des monstres
import monstersData from '@/data/monsters.json';

export default {
    name: 'MonsterSearch',
    data() {
        // Construction initiale du dictionnaire pour les niveaux d'éveil maximaux
        const maxAwakenLevel = {};
        monstersData.monsters.forEach(monster => {
            if (monster.obtainable && monster.awaken_level !== 0 && monster.base_stars !== 1) {
                const existingMax = maxAwakenLevel[monster.family_id] || 0;
                maxAwakenLevel[monster.family_id] = Math.max(existingMax, monster.awaken_level);
            }
        });

        // Filtre initial des monstres
        const filteredMonsters = monstersData.monsters.filter(monster =>
            monster.obtainable &&
            monster.awaken_level !== 0 &&
            monster.base_stars !== 1 &&
            monster.awaken_level === maxAwakenLevel[monster.family_id]
        );

        return {
            searchQuery: '',
            monsters: filteredMonsters,
            maxAwakenLevel, // Enregistre le dictionnaire pour une utilisation ultérieure
            highlightedIndex: -1
        }
    },
    computed: {
        filteredMonsters() {
            if (!this.searchQuery) {
                return this.monsters;  // Afficher tous les monstres si la recherche est vide
            }
            return this.monsters.filter(monster =>
                monster.name.toLowerCase().includes(this.searchQuery.toLowerCase()) &&
                monster.awaken_level === this.maxAwakenLevel[monster.family_id]
            );
        }
    },
    methods: {
        handleKeydown(event) {
            const UP = 38, DOWN = 40, ENTER = 13;
            const itemCount = this.filteredMonsters.length;

            switch (event.keyCode) {
                case UP:
                    this.highlightedIndex = (this.highlightedIndex + itemCount - 1) % itemCount;
                    break;
                case DOWN:
                    this.highlightedIndex = (this.highlightedIndex + 1) % itemCount;
                    break;
                case ENTER:
                    if (this.highlightedIndex !== -1) {
                        this.selectMonster(this.filteredMonsters[this.highlightedIndex]);
                    }
                    break;
            }
        },
        selectMonster(monster) {
            this.$emit('monster-selected', monster);
            this.searchQuery = '';
            this.highlightedIndex = -1;
            this.$nextTick(() => {
                this.$refs.searchInput.focus();
            });
        },
    }
}
</script>

<style scoped>
.logo {
    width: 200px;
    /* Ajustez la taille selon vos besoins */
    height: auto;
    display: block;
    margin: 10px auto;
    /* Centre le logo horizontalement */
    border-radius: 50%;
}

input {
    padding: 10px;
    border: 1px solid var(--input-border-color);
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border-radius: 4px;
    width: 300px;
    font-size: 24px;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: flex;
    align-items: center;
    width: 300px;
    padding: 8px;
    border: 1px solid var(--list-item-border-color);
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border-radius: 4px;
    margin-top: 5px;
}

li:hover {
    border: 5px solid var(--list-item-border-color);
}

.highlighted {
    background-color: #e0e0e0; /* Couleur de fond gris clair */
    color: #333;              /* Couleur de texte foncé */
    cursor: pointer;          /* Change le curseur en pointeur */
    border-left: 3px solid #007bff; /* Ajoute une bordure à gauche pour un effet de sélection */
    padding-left: 5px;        /* Un peu de padding à gauche pour l'esthétique */
}
</style>
