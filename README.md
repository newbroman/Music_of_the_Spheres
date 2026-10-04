# Music of the Spheres

*ἡ τῶν σφαιρῶν ἁρμονία*

**Play it here: https://newbroman.github.io/Music_of_the_Spheres/**

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

## Tuning

You can choose free glide (Kepler), Pythagorean diatonic or Pythagorean pentatonic tuning. Apollo's drone can sit in the Dorian, Phrygian, Lydian, Mixolydian, Hypodorian, Hypophrygian or Hypolydian mode.

## Data and accuracy

- Planet positions use JPL's approximate Keplerian elements (good from about 1800 to 2050).
- Dwarf planets, asteroids and comets use rounded elements, so their positions are illustrative.
- Only major moons are included, on circular orbits in their planet's equatorial plane.
- Distances on the dial are logarithmic.

## Technical

One self-contained `index.html` file, built with vanilla JavaScript, the Web Audio API and Canvas. There is no build step and nothing to install. Fonts come from Google Fonts.
