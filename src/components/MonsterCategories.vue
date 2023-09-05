<template>
    <div>
        <h2>Catégories</h2>
        <div v-for="(category, index) in categories" :key="index">
            <input v-model="category.name" />
            <draggable :list="category.monsters">
                <div v-for="monster in category.monsters" :key="monster.id">
                    <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                        :alt="monster.name" class="monster-icon" />
                </div>
            </draggable>
        </div>
    </div>
</template>
  
<script>
import draggable from 'vuedraggable';

export default {
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
    }
}
</script>
  
<style scoped>
.monster-icon {
    width: 60px;
    height: 60px;
}
</style>
  