import { v4 as uuidv4 } from 'uuid';

document.addEventListener('DOMContentLoaded', () => {
    const taskInput = document.getElementById('taskInput');
    const prioritySelect = document.getElementById('prioritySelect');
    const addTaskBtn = document.getElementById('addTaskBtn');
    const taskList = document.getElementById('taskList');

    let tasks = loadTasks();
    renderTasks();

    addTaskBtn.addEventListener('click', () => {
        const taskText = taskInput.value.trim();
        const priority = prioritySelect.value;
        if (taskText) {
            const newTask = {
                id: uuidv4(),
                text: taskText,
                priority: priority,
                completed: false
            };
            tasks.push(newTask);
            saveTasks();
            renderTasks();
            taskInput.value = '';
        }
    });

    taskList.addEventListener('click', (event) => {
        if (event.target.classList.contains('delete-btn')) {
            const taskId = event.target.parentElement.dataset.id;
            tasks = tasks.filter(task => task.id !== taskId);
            saveTasks();
            renderTasks();
        } else if (event.target.classList.contains('done-btn')) {
            const taskId = event.target.parentElement.dataset.id;
            tasks = tasks.map(task =>
                task.id === taskId ? { ...task, completed: !task.completed } : task
            );
            saveTasks();
            renderTasks();
        }
    });

    function renderTasks() {
        taskList.innerHTML = '';
        const sortedTasks = sortTasks(tasks);
        sortedTasks.forEach(task => {
            const li = document.createElement('li');
            li.dataset.id = task.id;
            if (task.completed) {
                li.classList.add('completed');
            }
            li.innerHTML = `
                <span>${task.text} (Priority: ${task.priority})</span>
                <button class="done-btn">${task.completed ? 'Undo' : 'Done'}</button>
                <button class="delete-btn">Delete</button>
            `;
            taskList.appendChild(li);
        });
    }

    function sortTasks(tasks) {
        const priorityOrder = { 'high': 1, 'medium': 2, 'low': 3 };
        return [...tasks].sort((a, b) => {
            if (a.completed && !b.completed) return 1;
            if (!a.completed && b.completed) return -1;
            return priorityOrder[a.priority] - priorityOrder[b.priority];
        });
    }

    function saveTasks() {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    }

    function loadTasks() {
        const storedTasks = localStorage.getItem('tasks');
        return storedTasks ? JSON.parse(storedTasks) : [];
    }
});
