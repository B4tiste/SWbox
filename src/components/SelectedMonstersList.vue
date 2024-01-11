<template>
    <div>
        <h2>Monstres sélectionnés</h2>
        <div v-if="selectedMonsters.length === 0">🚫</div>
        <draggable class="grid-container" :list="selectedMonsters" group="monsters" @change="updateSelected">
            <div v-for="monster in selectedMonsters" :key="monster.id" @click="unselectMonster(monster)">
                <img :src="'https://swarfarm.com/static/herders/images/monsters/' + monster.image_filename"
                    :alt="monster.name" class="monster-icon" />
            </div>
        </draggable>
    </div>
</template>

<script>
import draggable from 'vuedraggable';

export default {
    props: ['selectedMonsters'],
    components: {
        draggable
    },
    methods: {
        unselectMonster(monster) {
            this.$emit('monster-unselected', monster);
        },
        updateSelected(event) {
            this.$emit('selected-monsters-updated', event);
        }
    }
}
</script>

<style scoped>
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(70px, 1fr));
    gap: 10px;
    margin-bottom: 20px;
}

.monster-icon {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    object-fit: cover;
}

h2,
.empty-message {
    color: var(--primary-text-color, #333);
    margin-bottom: 0.5rem;
}

.empty-message {
    text-align: center;
}
</style>

