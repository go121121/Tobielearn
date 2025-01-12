document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const sidebar = document.querySelector(".sidebar");
  const closeSidebar = document.getElementById("close-sidebar");

  // Show the sidebar and hide the menu button
  menuToggle.addEventListener("click", () => {
    sidebar.classList.remove("hidden");
    menuToggle.classList.add("hidden"); // Hide the menu button
  });

  // Hide the sidebar and show the menu button
  closeSidebar.addEventListener("click", () => {
    sidebar.classList.add("hidden");
    menuToggle.classList.remove("hidden"); // Show the menu button
  });
});



// Upload button 

const uploadButton = document.querySelector('.upload-button');
const dropdownMenu = document.querySelector('.dropdown-menu');
const fileInput = document.getElementById('fileInput');

// Toggle dropdown menu
uploadButton.addEventListener('click', () => {
    dropdownMenu.style.display = dropdownMenu.style.display === 'block' ? 'none' : 'block';
});

// Handle option selection
dropdownMenu.addEventListener('click', (event) => {
    if (event.target.tagName === 'LI') {
        const uploadType = event.target.dataset.type;

        alert(`You selected: ${uploadType}`);
        dropdownMenu.style.display = 'none';

        // Open the file input
        fileInput.click();

        // Optional: Add logic to filter file input types based on selection
        if (uploadType === 'video') {
            fileInput.accept = 'video/*';
        } else if (uploadType === 'notebook') {
            fileInput.accept = '.pdf,.doc,.docx';
        } else if (uploadType === 'post') {
            fileInput.accept = 'image/*,text/*';
        }
    }
});

// Close dropdown when clicking outside
document.addEventListener('click', (event) => {
    if (!event.target.closest('.upload-container')) {
        dropdownMenu.style.display = 'none';
    }
});


//persons button 

function toggleDropdown() {
  const dropdown = document.getElementById("person-menu");
  dropdown.classList.toggle("show");
}

// Close dropdown if clicked outside
window.addEventListener("click", function (e) {
  const button = document.querySelector(".image-button");
  const dropdown = document.getElementById("person-menu");
  if (!button.contains(e.target) && !dropdown.contains(e.target)) {
    dropdown.classList.remove("show");
  }
});