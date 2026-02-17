// Static script for web interface functionality and API interactions

// Function to create a new item
async function createItem(data) {
    const response = await fetch('/api/items', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

// Function to fetch items
async function fetchItems() {
    const response = await fetch('/api/items');
    return response.json();
}

// Function to update an item
async function updateItem(id, data) {
    const response = await fetch(`/api/items/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}

// Function to delete an item
async function deleteItem(id) {
    await fetch(`/api/items/${id}`, {
        method: 'DELETE'
    });
}

// Example usage
fetchItems().then(items => console.log(items));