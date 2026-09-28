// Interações visuais simples. Os dados monitoráveis permanecem no HTML para facilitar o scraping.
document.querySelectorAll('a[href="#"]').forEach(a=>a.addEventListener('click',e=>e.preventDefault()));
