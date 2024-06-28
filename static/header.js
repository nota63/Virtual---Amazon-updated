document.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll('.header img');
  let currentIndex = 0;

  function showNextImage() {
    images[currentIndex].style.opacity = 0;
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].style.opacity = 1;
  }

  images.forEach((image, index) => {
    image.style.opacity = index === 0 ? 1 : 0;
  });

  setInterval(showNextImage, 3000);
});
