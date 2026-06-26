const toggleButton = document.querySelector('#Container header .toggle-button');
const headerElement = document.querySelector('#Container header');

if (toggleButton && headerElement) {
    toggleButton.addEventListener('click', () => {
        headerElement.classList.toggle('active');
    });
}















