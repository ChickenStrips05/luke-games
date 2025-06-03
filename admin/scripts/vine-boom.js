(function() {
  const url = "https://www.myinstants.com/media/sounds/vine-boom.mp3"

  if (!url) return;

  const audio = new Audio(url);
  audio.style.display = 'none';
  document.body.appendChild(audio);

  audio.play().then(() => {
    console.log("Audio is playing...");
  }).catch(err => {
    console.error("Error playing audio:", err);
  });

  audio.addEventListener('ended', () => {
    document.body.removeChild(audio);
  });
})();
