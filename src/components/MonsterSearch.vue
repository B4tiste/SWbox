<template>
    <div class="search-container">
        <input type="text" v-model="searchQuery" placeholder="Recherchez un monstre..." ref="searchInput"
            @keydown="handleKeydown">
        <ul v-if="searchQuery.length >= 2 && filteredMonsters.length">
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
import monstersData from '@/data/monsters.json';

export default {
    name: 'MonsterSearch',
    data() {
        // Initialisation des données
        const maxAwakenLevel = {};
        monstersData.monsters.forEach(monster => {
            if (monster.obtainable && monster.awaken_level !== 0 && monster.base_stars !== 1) {
                const existingMax = maxAwakenLevel[monster.family_id] || 0;
                maxAwakenLevel[monster.family_id] = Math.max(existingMax, monster.awaken_level);
            }
        });

        const filteredMonsters = monstersData.monsters.filter(monster =>
            monster.obtainable &&
            monster.awaken_level !== 0 &&
            monster.base_stars !== 1 &&
            monster.awaken_level === maxAwakenLevel[monster.family_id]
        );

        return {
            searchQuery: '',
            monsters: filteredMonsters,
            maxAwakenLevel,
            highlightedIndex: -1
        }
    },
    computed: {
        filteredMonsters() {
            if (this.searchQuery.length < 2) {
                return []; // Ne rien retourner si moins de 3 caractères
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
.search-container {
    margin-left: 20px;
    margin-right: 4vw;
}

input {
    padding: 5px;
    border: 1px solid var(--input-border-color);
    background-color: var(--primary-bg-color);
    color: var(--primary-text-color);
    border-radius: 30px;
    width: 40vw;
    font-size: 24px;
    margin-bottom: 10px; /* Espace en dessous de l'input */
    text-indent: 30px; /* Indente le texte à l'intérieur de l'input */

}

ul {
    list-style-type: none;
    padding: 0;
    margin-top: 0; /* Supprime l'espace par défaut au-dessus de la liste */
    display: flex;
    flex-direction: column;
    align-items: center; /* Centre horizontalement les éléments */
    width: 100%; /* S'assure que le conteneur utilise toute la largeur disponible */
    max-height: 400px; /* Hauteur maximale du ul */
    overflow-y: auto; /* Active la barre de défilement verticale si nécessaire */
}

li {
    display: flex; /* Utilise flexbox pour aligner les éléments horizontalement */
    align-items: center; /* Centre les éléments verticalement dans chaque li */
    justify-content: flex-start; /* Aligne les enfants (image et texte) à gauche */
    width: 300px; /* Taille fixe pour le centrage */
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

.monster-icon {
    margin-right: 10px; /* Espace entre l'image et le texte */
    width: 40px; /* Taille fixe pour les images des monstres */
    height: 40px; /* Taille fixe pour les images des monstres */
}

.highlighted {
    background-color: #e0e0e0; /* Couleur de fond gris clair */
    color: #333;              /* Couleur de texte foncé */
    cursor: pointer;          /* Change le curseur en pointeur */
    border-left: 3px solid #007bff; /* Ajoute une bordure à gauche pour un effet de sélection */
    padding-left: 5px;        /* Un peu de padding à gauche pour l'esthétique */
}

</style>
