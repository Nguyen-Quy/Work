<template>
    <div class="tasks_container">
        <div class="tasks_content">
            <h1>Tasks</h1>
            <ul class="tasks_list">
                <li v-for="task in tasks" :key="task.id">
                    <h2>{{task.title}}</h2>
                    <p>{{task.description}}</p>
                    <button @click="toggleTask(task)">
                        {{task.completed ? 'Undo' : 'Complete'}}
                    </button>
                    <button @click="deleteTask(task)">Delete</button>
                </li>
            </ul>
            <div class="add_task">
            <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                    <label for="title">Title</label>
                    <input type="text" class="form-control" id="title" v-model="title">
                </div>
                <div class="form-group">
                    <label for="description">Description</label>
                    <textarea class="form-control" id="description" v-model="description"></textarea>
                </div>
                <div class="form-group">
                    <button type="submit">Add Task</button>
                </div>
            </form>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            tasks:[],
            title:'',
            description:''
        }
    },
    // mounted () {
    // axios
    // .get('http://localhost:8000/api/tasks/')
    // .then(response => (this.info = response))
    // },
    methods: {
        async getData () {
            try {
                const response=await axios.get('http://localhost:8000/api/tasks/');
                this.tasks=response.data;
            } catch (error) {
                console.log(error);
            }
        },
        async submitForm(){
            try {
                // Send a POST request to the API
                const response = await this.$http.post('http://localhost:8000/api/tasks/', {
                    title: this.title,
                    description: this.description,
                    completed: false
                });
                // Append the returned data to the tasks array
                this.tasks.push(response.data);
                // Reset the title and description field values.
                this.title = '';
                this.description = '';
            } catch (error) {
                // Log the error
                console.log(error);
            }
        }
    },
    create() {
        this.getData();
    }
    
}
</script>