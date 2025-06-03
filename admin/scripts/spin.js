// Trippy text rotator
let angle = 0;
let hue = 0;

setInterval(() => {
  angle += 1;
  hue = (hue + 3) % 360;
  document.body.style.transform = `rotate(${angle}deg)`;
  document.body.style.transition = 'transform 0.1s linear';

  document.querySelectorAll('*').forEach(el => {
    el.style.color = `hsl(${(hue + Math.random() * 60) % 360}, 100%, 70%)`;
  });
}, 100);