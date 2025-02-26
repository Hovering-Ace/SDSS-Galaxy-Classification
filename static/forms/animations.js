// GSAP Animations for Form Elements
gsap.from(".title", { duration: 2, opacity: 0, y: -50, ease: "power2.out" });
gsap.from("form", { duration: 2, opacity: 0, y: 50, ease: "power2.out", delay: 0.5 });

// Background Star Animation
const canvas = document.getElementById("stars");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const stars = [];
for (let i = 0; i < 150; i++) {
    stars.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 2,
        speed: Math.random() * 1.5
    });
}

function drawStars() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.fillStyle = "white";
    stars.forEach((star) => {
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.radius, 0, Math.PI * 2);
        ctx.fill();
    });
}

function animateStars() {
    stars.forEach((star) => {
        star.y += star.speed;
        if (star.y > canvas.height) {
            star.y = 0;
            star.x = Math.random() * canvas.width;
        }
    });
    drawStars();
    requestAnimationFrame(animateStars);
}

animateStars();
