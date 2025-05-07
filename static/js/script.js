document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const lightTheme = document.getElementById('light-theme');
    const darkTheme = document.getElementById('dark-theme');

    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        setDarkTheme();
    } else {
        setLightTheme();
    }

    themeToggle.addEventListener('click', function() {
        if (themeToggle.src.includes('moon.png')) {
            setLightTheme();
        } else {
            setDarkTheme();
        }
    });

    function setDarkTheme() {
        lightTheme.disabled = true;
        darkTheme.disabled = false;
        localStorage.setItem('theme', 'dark');
    
        // Плавна зміна зображення з анімацією
        themeToggle.classList.add('fade-out');
        setTimeout(() => {
            themeToggle.src = themeToggle.getAttribute('data-dark-src');
            themeToggle.classList.remove('fade-out');
            themeToggle.style.transform = 'scale(1.2)';
            setTimeout(() => {
                themeToggle.style.transform = 'scale(1)';
            }, 200);
        }, 300);
    }
    
    function setLightTheme() {
        lightTheme.disabled = false;
        darkTheme.disabled = true;
        localStorage.setItem('theme', 'light');
    
        // Плавна зміна зображення з анімацією
        themeToggle.classList.add('fade-out');
        setTimeout(() => {
            themeToggle.src = themeToggle.getAttribute('data-light-src');
            themeToggle.classList.remove('fade-out');
            themeToggle.style.transform = 'scale(1.2)';
            setTimeout(() => {
                themeToggle.style.transform = 'scale(1)';
            }, 200);
        }, 300);
    }    
});