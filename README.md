# Music of the Spheres

*ἡ τῶν σφαιρῶν ἁρμονία*

**Play it here:**
- **2D dial:** https://newbroman.github.io/Music_of_the_Spheres/
- **3D flight:** https://newbroman.github.io/Music_of_the_Spheres/flight.html

A live orrery that you can hear. Every planet, moon, dwarf planet and comet sings with the voice of a Greek god. The music comes from the real motions of the solar system, and you choose where you stand and listen.

Headphones give the best result. Browsers only allow sound after a tap, so press **Begin the harmony** or tap a planet.

## The idea

In Plato's Myth of Er, a Siren rides each celestial sphere singing a single note, and together they make one harmony. In 1619, Johannes Kepler's *Harmonices Mundi* gave the idea numbers. He read each planet's angular speed at perihelion and aphelion as a musical interval. This app does the same thing live, from orbital elements, for the whole solar system.

## How the sky becomes sound

| Celestial measure | Becomes | How you hear it |
|---|---|---|
| Orbital speed, moment by moment | Pitch | Faster bodies sing higher. Eccentric orbits rise toward perihelion and sink toward aphelion. |
| Apparent size (radius ÷ distance from your listening post) | Loudness | Bodies are as loud as they look big in your sky. Voices too faint to hear drop out. |
| Direction from your listening post | Position | Bodies are placed around you in stereo or 3D. |
| Orbital inclination | Elevation, sway | Inclined bodies rise and fall in space, and their pitch sways with them. |
| Axial tilt | Wobble | A tilted spinner wobbles in pitch with its day. Uranus, on its side, wobbles most. |
| Rotation, length of day | Pulse | Fast spinners pulse quickly. Backward spinners pulse in reversed swells. |
| Dwarf planets & asteroids | Perturbation | They tug the pitch of the nearest planet, more the bigger and closer they are. They can also sing as children's voices. |
| Moons | Melody | Each moon's phase against the Sun walks an arch through the chosen Greek mode: home note at new moon, up to the octave at full moon, and back. |
| Comets | Breath | A comet's size is its coma, so it fades in as a whisper near the Sun. |
| The Sun | Drone | Apollo holds the tonic and fifth of the chosen mode. |

## The voices

- **Instruments** mode uses synthesised tones shaped by each god's vowel.
- **Human choir** mode has each god sing their own name in a voice that suits them:
  - Basses: Zeus, Kronos, Ouranos and Poseidon.
  - Tenor: Ares. Countertenor: Hermes.
  - Alto: Gaia. Soprano: Aphrodite.
  - Children: the dwarf planets, asteroids and moons.
  - Comets whisper *kometes*, the long-haired star.
- Tap a body to hear it alone. Its god can introduce themselves, using your device's speech voices.
- **Enter a planet's system** (for example Jupiter or Saturn) to hear its moons as a miniature solar system circling you. You can listen from the planet or from any moon.

## Flight (3D)

`flight.html` puts you in a spaceship. The same orbital data and the same choir surround you, and your ears ride in the cockpit, so the voices are placed by where you are and which way you face.

- **Travel to** any body. The autopilot flies you there, and once you arrive you stay in orbit with it.
- **Fly by hand.** On a computer, drag to look, use W/S to fly, A/D to slide, R/F for up and down, Q/E to roll, and Shift to boost. On a phone, drag to look and use the ▲ ▼ buttons.
- **Speed adapts** to what is near: gentle beside a planet, faster than light between them.
- **Fly among a planet's moons** and they start singing around you, each one's melody following its phase. Time slows so you can hear them circle.
- Planets, moons and the Sun are drawn larger than life so you can find them. The distances along their orbits are true.

## Tuning

You can choose free glide (Kepler), Pythagorean diatonic or Pythagorean pentatonic tuning. Apollo's drone can sit in the Dorian, Phrygian, Lydian, Mixolydian, Hypodorian, Hypophrygian or Hypolydian mode.

## Data and accuracy

- Planet positions use JPL's approximate Keplerian elements (good from about 1800 to 2050).
- Dwarf planets, asteroids and comets use rounded elements, so their positions are illustrative.
- Only major moons are included, on circular orbits in their planet's equatorial plane.
- Distances on the dial are logarithmic.

## Technical

Two self-contained pages: `index.html` (the 2D dial, Canvas) and `flight.html` (3D, three.js r128 from cdnjs). Both use vanilla JavaScript and the Web Audio API. There is no build step and nothing to install. Fonts come from Google Fonts.
