// Simple interactivity for toggling elements and changing the favicon
document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('nav a');
    const favicon = document.getElementById('favicon');  // Select the favicon link tag

    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Show an alert when navigating to a page
            alert(`Navigating to ${link.textContent} page.`);
            
            // Get the icon file name from the data-icon attribute
            const iconName = link.getAttribute('data-icon');
            
            // Update the favicon dynamically
            favicon.setAttribute('href', `/static/icons/${iconName}`);
        });
    });
});



