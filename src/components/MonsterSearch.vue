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
        return {
            searchQuery: '',
            monsters: monstersData.monsters.filter(monster => monster.obtainable && monster.awaken_level !== 0)
        }
    },
    computed: {
        filteredMonsters() {
            if (!this.searchQuery) {
                return this.monsters;  // Afficher tous les monstres si la recherche est vide
            }
            return this.monsters.filter(monster =>
                monster.name.toLowerCase().includes(this.searchQuery.toLowerCase())
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

</style>