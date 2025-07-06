
// Mejora de accesibilidad básica: enfocar secciones por teclado
document.addEventListener("DOMContentLoaded", function () {
  const skipLink = document.createElement("a");
  skipLink.href = "#main";
  skipLink.innerText = "Ir al contenido principal";
  skipLink.className = "skip-link";
  skipLink.style.position = "absolute";
  skipLink.style.top = "-40px";
  skipLink.style.left = "0";
  skipLink.style.background = "#000";
  skipLink.style.color = "#fff";
  skipLink.style.padding = "8px";
  skipLink.style.zIndex = "1000";
  skipLink.style.transition = "top 0.3s";

  skipLink.onfocus = () => {
    skipLink.style.top = "0";
  };
  skipLink.onblur = () => {
    skipLink.style.top = "-40px";
  };

  document.body.prepend(skipLink);
});
