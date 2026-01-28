// Dark mode toggle
const toggle = document.getElementById('toggleDark');
toggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
});

// Demo SOS alert function
function sendSOS() {
    const location = prompt("Enter your location for SOS alert:");
    if(location) alert("SOS sent to nearby volunteers at " + location);
}
