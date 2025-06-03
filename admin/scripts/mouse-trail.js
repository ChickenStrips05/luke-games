

const trailLength = 15;
const trail = [];

for (let i = 0; i < trailLength; i++) {
  const dot = document.createElement("div");
  dot.style.position = "fixed";
  dot.style.width = dot.style.height = "12px";
  dot.style.borderRadius = "50%";
  dot.style.background = "rgba(0, 200, 255, 0.7)";
  dot.style.pointerEvents = "none";
  dot.style.transition = "transform 0.1s ease-out";
  document.body.appendChild(dot);
  trail.push({ el: dot, x: 0, y: 0 });
}

let mouseX = 0, mouseY = 0;
document.addEventListener("mousemove", e => {
  mouseX = e.clientX;
  mouseY = e.clientY;
});

function animateTrail() {
  let x = mouseX, y = mouseY;

  trail.forEach((dot, i) => {
    const next = trail[i + 1] || trail[i];
    dot.x += (x - dot.x) * 0.3;
    dot.y += (y - dot.y) * 0.3;
    dot.el.style.transform = `translate(${dot.x}px, ${dot.y}px) scale(${1 - i / trailLength})`;
    dot.el.style.opacity = `${1 - i / trailLength}`;
    x = dot.x;
    y = dot.y;
  });

  requestAnimationFrame(animateTrail);
}

animateTrail();