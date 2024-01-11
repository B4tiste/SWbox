<template>
    <!-- Conteneur principal du composant -->
    <div>
        <!-- Champ de saisie pour la recherche de monstres -->
        <input type="text" v-model="searchQuery" placeholder="Recherchez un monstre...">

        <!-- Liste des monstres filtrés -->
        <ul v-if="searchQuery && filteredMonsters.length">
            <li v-for="monster in filteredMonsters" :key="monster.id" @click="selectMonster(monster)">
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
            maxAwakenLevel // Enregistre le dictionnaire pour une utilisation ultérieure
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
        selectMonster(monster) {
            this.$emit('monster-selected', monster);
        },
    }
}
</script>

<style scoped>
input[type="text"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid var(--input-border-color, #ccc);
    background-color: var(--input-bg-color, #fff);
    color: var(--input-text-color, #333);
    border-radius: 4px;
}
.search-results {
  /* Définir un fond pour la zone des résultats de recherche */
  background-color: var(--results-bg-color, #fff);
  /* Ajouter de l'ombre ou une bordure si nécessaire pour distinguer la section */
  box-shadow: 0 2px 5px rgba(0,0,0,0.2);
  /* Limiter la largeur si nécessaire pour ne pas couvrir tout l'écran */
  max-width: 100%;
  margin: auto; /* Cela centrerait la boîte si max-width est défini */
  overflow: auto; /* Assure-toi que le contenu défilable ne dépasse pas */
  padding: 1rem; /* Ajouter un peu d'espace autour du contenu */
  border-radius: 4px; /* Optionnel pour les coins arrondis */
}

/* Style pour la liste des résultats de recherche */
ul {
  list-style: none;
  padding-left: 0;
  margin-top: 0;
}

li {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  padding: 0.5rem;
  transition: background-color 0.3s;
  cursor: pointer;
}

li:hover {
  background-color: var(--list-item-hover-bg-color, #f7f7f7);
}

.monster-icon {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
    object-fit: cover;
}

/* Styles pour le thème sombre */
[data-theme='dark'] {
    --input-border-color: #666;
    --input-bg-color: #444;
    --input-text-color: #eee;
    --list-item-border-color: #555;
    --list-item-bg-color: #333;
    --list-item-hover-bg-color: #3a3a3a;
}
</style>
