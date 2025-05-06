// Sidebar toggle
const sidebar = document.getElementById('sidebar');
const sidebarToggle = document.getElementById('sidebar-toggle');
sidebarToggle.addEventListener('click', () => {
    sidebar.classList.toggle('-translate-x-full');
});

// Back to Top button
const backToTop = document.getElementById('back-to-top');
window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        backToTop.classList.remove('hidden');
    } else {
        backToTop.classList.add('hidden');
    }
});
backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Theme toggle
const htmlRoot = document.getElementById('html-root');
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const currentTheme = localStorage.getItem('theme') || 'light';
if (currentTheme === 'dark') {
    htmlRoot.classList.add('dark');
    themeIcon.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/>';
}
themeToggle.addEventListener('click', () => {
    htmlRoot.classList.toggle('dark');
    const isDark = htmlRoot.classList.contains('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    themeIcon.innerHTML = isDark
        ? '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/>'
        : '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/>';
});

// Filter dropdown
const reasonFilter = document.getElementById('reason-filter');
reasonFilter.addEventListener('change', () => {
    fetch('/filter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `reason=${reasonFilter.value}`
    })
    .then(response => response.json())
    .then(data => {
        Plotly.react('reason-chart', JSON.parse(data.reason_plot), { responsive: true });
        Plotly.react('monthly-chart', JSON.parse(data.monthly_plot), { responsive: true });
        Plotly.react('heatmap-chart', JSON.parse(data.heatmap_plot), { responsive: true });
        Plotly.react('map-chart', JSON.parse(data.map_plot), { responsive: true });
        Plotly.react('township-chart', JSON.parse(data.township_plot), { responsive: true });
    });
});

// Share buttons
const shareButtons = document.querySelectorAll('.share-button');
shareButtons.forEach(button => {
    button.addEventListener('click', () => {
        const section = button.dataset.section;
        const url = window.location.href + `#${section}`;
        const text = `Check out the ${section} insights from the 911 Emergency Calls Dashboard!`;
        if (navigator.share) {
            navigator.share({ title: '911 Calls Dashboard', text, url });
        } else {
            const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`;
            window.open(twitterUrl, '_blank');
        }
    });
});

console.log("Dashboard initialized");