// Script para o carousel automático
const carouselInner = document.querySelector('.carousel-inner');
const carouselItems = document.querySelectorAll('.carousel-item');
const prevButton = document.querySelector('.carousel-control.prev');
const nextButton = document.querySelector('.carousel-control.next');
let currentIndex = 0;
let autoSlideInterval;

// Função para atualizar o carousel
function updateCarousel() {
    const offset = -currentIndex * 100;
    carouselInner.style.transform = `translateX(${offset}%)`;
}

// Função para avançar para o próximo slide
function nextSlide() {
    if (currentIndex < carouselItems.length - 1) {
        currentIndex++;
    } else {
        currentIndex = 0;
    }
    updateCarousel();
}

// Função para voltar ao slide anterior
function prevSlide() {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = carouselItems.length - 1;
    }
    updateCarousel();
}

// Iniciar o carousel automático
function startAutoSlide() {
    autoSlideInterval = setInterval(nextSlide, 5000); // Troca de slide a cada 5 segundos
}

// Parar o carousel automático
function stopAutoSlide() {
    clearInterval(autoSlideInterval);
}

// Event listeners para os controles do carousel
prevButton.addEventListener('click', () => {
    stopAutoSlide();
    prevSlide();
    startAutoSlide();
});

nextButton.addEventListener('click', () => {
    stopAutoSlide();
    nextSlide();
    startAutoSlide();
});

// Iniciar o carousel automático ao carregar a página
startAutoSlide();

// Script para o menu toggle (responsivo)
const menuToggle = document.querySelector('.menu-toggle');
const navbarLinks = document.querySelector('.navbar-links');

menuToggle.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
});