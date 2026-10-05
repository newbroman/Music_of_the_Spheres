# Putting Music of the Spheres on Google Play

The site is already an installable app (a PWA). It has a manifest, icons, and an offline copy of every page and instrument. On Android, Chrome's menu offers **Install app**, and the app then opens full-screen from the home screen.

To list it on Google Play, the same site is wrapped as a **Trusted Web Activity** (TWA). This is a small Android app that opens the site in Chrome with no address bar. Web MIDI, recording, full-screen projection and audio over HDMI all keep working, because it is still Chrome inside.

## 1. Build the Android package (PWABuilder, about 10 minutes)

1. Go to <https://www.pwabuilder.com> and enter `https://newbroman.github.io/Music_of_the_Spheres/`.
2. Choose **Package for stores → Android → Generate package**. Suggested options:
   - Package ID: `io.github.newbroman.spheres`
   - App name: `Music of the Spheres`, short name: `Spheres`
   - Display mode: `standalone`. Keep "Notification delegation" off.
   - Signing key: **Create new**. PWABuilder makes the key and gives it back in the zip.
3. Download the zip. Keep `signing.keystore` and `signing-key-info.txt` somewhere safe and backed up. Every future update must be signed with the same key.
4. The zip also contains `assetlinks.json` and the `.aab` file that goes to Play.

## 2. Prove the site and the app belong together (removes Chrome's address bar)

Android looks for the proof at the root of the domain, `https://newbroman.github.io/.well-known/assetlinks.json`. A project site such as `/Music_of_the_Spheres/` cannot serve that path. It needs the user-site repository `newbroman.github.io`.

Put the zip's `assetlinks.json` in your Downloads folder, then run:

```bash
cd ~ && gh repo create newbroman/newbroman.github.io --public --clone && cd newbroman.github.io
mkdir -p .well-known && cp ~/Downloads/assetlinks.json .well-known/ && touch .nojekyll
printf '<!doctype html><meta http-equiv="refresh" content="0;url=Music_of_the_Spheres/">\n' > index.html
git add -A && git commit -m "Digital asset links for the Music of the Spheres app" && git push -u origin HEAD
```

(If you don't have the `gh` tool, create the repository `newbroman.github.io` on github.com, then clone it and run the rest.) After a minute, <https://newbroman.github.io/.well-known/assetlinks.json> should show the file.

Once Play is set up, Google re-signs the app (Play App Signing). Then add the second fingerprint from **Play Console → Test and release → App integrity → App signing key certificate (SHA-256)** to the `sha256_cert_fingerprints` list in that file and push again. Without it, the Play-installed app shows an address bar.

## 3. Google Play Console

1. Register at <https://play.google.com/console> (a one-off US$25 fee, with ID verification).
2. **Create app**: Music of the Spheres, *App*, *Free*.
3. **Store listing**:
   - Icon: `icons/icon-512.png`.
   - Feature graphic (1024×500).
   - At least two phone screenshots.
   - Short description, for example: *Hear the solar system sung by the Greek gods, as Pythagoras, Plato, Ptolemy and Kepler imagined it.*
4. **Privacy policy**: `https://newbroman.github.io/Music_of_the_Spheres/privacy.html`.
5. **App content**:
   - Data safety: *no data collected or shared*.
   - Ads: *none*.
   - Content rating questionnaire: all "no", which gives *Everyone*.
   - Target audience: 13+ is simplest.
6. **Testing**: new personal developer accounts must run a closed test with at least **12 testers for 14 days** before going to production. Upload the `.aab` to a closed testing track, add testers by email, and after 14 days apply for production.

## Updating

Pushing to this repository updates the app straight away. The TWA shows the live site, and the service worker refreshes its offline copy. A new `.aab` is only needed when the app's name, icon, package settings or Android version requirements change. Build it in PWABuilder with the **same signing key** and a higher version code.
