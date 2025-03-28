const constrain = 10;
const card = document.getElementById("sprite-stats-card");
const sprite = document.getElementById("sprite-stats-layer");

function getTransform(x, y, el) {
    const { left, top, width, height } = el.getBoundingClientRect();
    const rotateX = (y - top - height / 2) / constrain;
    const rotateY = -(x - left - width / 2) / constrain;

    return `perspective(500px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
}

function handleMouseMove(e) {
    const transform = getTransform(e.clientX, e.clientY, sprite);
    window.requestAnimationFrame(() => {
        sprite.style.transform = transform;
    });
}

function resetTransform() {
    sprite.style.transition = "transform 0.4s ease";
    sprite.style.transform = "perspective(500px) rotateX(0deg) rotateY(0deg)";
}

// Event Listeners
card.addEventListener("mousemove", handleMouseMove);
card.addEventListener("mouseleave", resetTransform);
