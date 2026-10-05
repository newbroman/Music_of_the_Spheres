# Putting Music of the Spheres on Google Play

The site is already an installable app (a PWA). It has a manifest, icons, and an offline copy of every page and instrument. On Android, Chrome's menu offers **Install app**, and the app then opens full-screen from the home screen.

To list it on Google Play, the same site is wrapped as a **Trusted Web Activity** (TWA). This is a small Android app that opens the site in Chrome with no address bar. Web MIDI, recording, full-screen projection and audio over HDMI all keep working, because it is still Chrome inside.

## 1. Build the Android package (PWABuilder, about 10 minutes)

1. Go to <https://www.pwabuilder.com> and enter `https://newbroman.github.io/Music_of_the_Spheres/`.
2. Choose **Package for stores → Android → Generate package**. Suggested options:
   - Package ID: `io.github.newbroman.spheres`
   - App name: `Music of the Spheres`, short name: `Spheres`
   - Display mode: `standalone`. Keep "Notification delegation" off.
   - Google Play billing: **on** (for the supporter purchase, see step 4).
   - Signing key: **Create new**. PWABuilder makes the key and gives it back in the zip.
3. Download the zip. Keep `signing.keystore` and `signing-key-info.txt` somewhere safe and backed up. Every future update must be signed with the same key.
4. The zip also contains `assetlinks.json` and the `.aab` file that goes to Play.

## 2. Prove the site and the app belong together (removes Chrome's address bar)

Android looks for the proof at the root of the domain: `https://newbroman.github.io/.well-known/assetlinks.json`. That file already exists in the `newbroman.github.io` repository, for another app (`io.github.newbroman.twa`). So the Spheres entry is **added** to it, not written over it.

Put the zip's `assetlinks.json` in your Downloads folder, then run:

```bash
cd ~ && { [ -d newbroman.github.io ] || git clone https://github.com/newbroman/newbroman.github.io; } && cd newbroman.github.io && git pull
python3 - <<'PY'
import json,os
p='.well-known/assetlinks.json';cur=json.load(open(p))
new=json.load(open(os.path.expanduser('~/Downloads/assetlinks.json')))
have={e['target']['package_name'] for e in cur}
cur+=[e for e in new if e['target']['package_name'] not in have]
json.dump(cur,open(p,'w'),indent=2)
print('apps now listed:',[e['target']['package_name'] for e in cur])
PY
git add .well-known/assetlinks.json && git commit -m "Asset links: add Music of the Spheres app" && git push
```

After a minute, <https://newbroman.github.io/.well-known/assetlinks.json> should list both apps.

Once Play is set up, Google re-signs the app (Play App Signing). Its key has a second fingerprint, which must be added too, or the Play-installed app shows an address bar. Copy it from **Play Console → Test and release → App integrity → App signing key certificate (SHA-256)**, then run:

```bash
cd ~/newbroman.github.io && git pull && python3 - <<'PY'
import json;p='.well-known/assetlinks.json';a=json.load(open(p))
fp=input('Paste the Play app signing SHA-256: ').strip()
for e in a:
    t=e['target']
    if t['package_name']=='io.github.newbroman.spheres' and fp not in t['sha256_cert_fingerprints']:t['sha256_cert_fingerprints'].append(fp)
json.dump(a,open(p,'w'),indent=2);print('done')
PY
git commit -am "Asset links: Play signing key for Music of the Spheres" && git push
```

## 3. Google Play Console

1. Register at <https://play.google.com/console> (a one-off US$25 fee, with ID verification).
2. **Create app**: Music of the Spheres, *App*, *Free*.
3. **Store listing**:
   - Icon: `icons/icon-512.png`.
   - Feature graphic (1024×500): `store/feature-graphic.png`.
   - Phone screenshots: `store/1-dial.png` to `store/4-flight.png`.
   - Short description, for example: *Hear the solar system sung by the Greek gods, as Pythagoras, Plato, Ptolemy and Kepler imagined it.*
4. **Privacy policy**: `https://newbroman.github.io/Music_of_the_Spheres/privacy.html`.
5. **App content**:
   - Data safety: *no data collected or shared*.
   - Ads: *none*.
   - Content rating questionnaire: all "no", which gives *Everyone*.
   - Target audience: 13+ is simplest.
6. **Testing**: new personal developer accounts must run a closed test with at least **12 testers for 14 days** before going to production. Upload the `.aab` to a closed testing track, add testers by email, and after 14 days apply for production.

## 4. Supporter purchase (unlocks the Stage panel in the Play app)

In the Play app, the Stage panel (PA, 5.1, MIDI for lights, projector view) opens with a one-off supporter purchase at one of three amounts. The website keeps it free. The code is already in the site. It recognises the Play app because Android opens the site from `android-app://io.github.newbroman.spheres`, and it uses Google Play Billing through Chrome's Digital Goods API.

1. In PWABuilder's Android options, switch **Google Play billing on** before downloading the package.
2. In the Play Console, set up a **payments profile** (Settings → Payments profile).
3. Under **Monetize with Play → Products → One-time products**, create three products with exactly these IDs, and make each one active:

   | Product ID | Name | Price |
   |---|---|---|
   | `supporter_small` | Supporter | £1.99 |
   | `supporter_medium` | Friend | £4.99 |
   | `supporter_large` | Patron | £9.99 |

   The app shows Play's own price for each one, in the buyer's currency.
4. Add your testers as **licence testers** (Settings → License testing). They can then buy without being charged.

Each purchase is consumed straight away. Google counts that as acknowledging it, so no server is needed and nothing is refunded after three days. The app remembers on the phone that you are a supporter. Anyone who clears Chrome's data for the site loses the unlock, and you can send them a refund or ask them to buy again.

## Updating

Pushing to this repository updates the app straight away. The TWA shows the live site, and the service worker refreshes its offline copy. A new `.aab` is only needed when the app's name, icon, package settings or Android version requirements change. Build it in PWABuilder with the **same signing key** and a higher version code.
