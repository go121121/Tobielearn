function toggleAddressPopup() {
  const popup = document.getElementById("addressPopup");
  if (popup.style.display === "none" || popup.style.display === "") {
    popup.style.display = "block";
  } else {
    popup.style.display = "none";
  }
}

function outsideClickListener(event) {
  const popup = document.getElementById("addressPopup");
  if (popup && !popup.contains(event.target)) {
    popup.style.display = "none";
    console.log("Popup closed by clicking outside");

    // Remove the listener once the popup is closed
    window.removeEventListener("click", outsideClickListener);
  }
}

function saveAddress(event) {
  event.preventDefault(); // Prevent default form submission behavior
  const address1 = document.getElementById("address1").value;
  const address2 = document.getElementById("address2").value;
  const state = document.getElementById("state").value;
  const postal = document.getElementById("postal").value;
  const saveButton = document.getElementById("saveButton");

  // Disable the save button to prevent multiple submissions
  saveButton.disabled = true;

  // Basic validation
  if (!address1 || !state || !postal) {
    alert("Please fill in all required fields.");
    saveButton.disabled = false; // Re-enable the button
    return;
  }

  fetch("/save_address/", {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ address1, address2, state, postal }),
  })
    .then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Failed to save address");
      }
    })
    .then((data) => {
      if (data.success) {
        updateAddressDisplay(address1, address2, state, postal);
        toggleAddressPopup();
        alert(data.message); // Optional success alert
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred while saving the address.");
    })
    .finally(() => {
      saveButton.disabled = false; // Re-enable the button
    });
}

// Function to dynamically update the displayed address
function updateAddressDisplay(address1, address2, state, postal) {
  document.querySelector(".address strong").textContent = `${address1}, ${
    address2 ? address2 + ", " : ""
  }${state}, ${postal}`;
}

// Function to get the CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith(name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
