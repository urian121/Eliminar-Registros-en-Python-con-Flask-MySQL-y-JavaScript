

/** Alerta personalizadas */
function mensaje(lenguaje) {
    let text = document.querySelector('.text-2').textContent = `
            El lenguaje ${lenguaje} fue eliminado 😀 `;

    const toast = document.querySelector(".toast");
        closeIcon = document.querySelector(".close"),
        progress = document.querySelector(".progress");


    toast.classList.add("active");
    progress.classList.add("active");

    setTimeout(() => {
        toast.classList.remove("active");
    }, 5000);

    closeIcon.addEventListener("click", () => {
        toast.classList.remove("active");
    });
}