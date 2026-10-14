# Credits, sources and licences — Galaxy data bundle

All data were gathered on 2026-10-12. Each entry gives the exact version or query, the licence or terms, and
the citation to show in the app. Short-form credits for the app's credits screen are at the end.

## Stars (`stars.json`, `seismo.json` stellar part)

**HYG Database v4.4** — David Nash (astronexus), released 2026-07-12.
File `data/hyg/CURRENT/hyg_v44.csv.gz` from https://codeberg.org/astronexus/hyg (commit 53e3df3; the GitHub
repository astronexus/HYG-Database now only points to Codeberg). SHA-256 `00b349893b9a5310…`, 119 613 stars.
Licence **CC BY-SA 4.0** (https://creativecommons.org/licenses/by-sa/4.0/). HYG combines Hipparcos (ESA 1997;
van Leeuwen 2007 re-reduction), the Yale Bright Star Catalogue 5th ed. (Hoffleit & Warren 1991) and the Gliese–
Jahreiß Catalogue of Nearby Stars 3rd ed. (1991), with IAU proper names. Because stars.json is a derivative of
HYG, **stars.json itself is CC BY-SA 4.0**. Credit line: "Star data from the HYG Database v4.4 by David Nash
(astronexus.com), CC BY-SA 4.0."

**Gaia DR3** — Gaia Collaboration, Vallenari et al. 2023, A&A 674, A1 (DR3 release); Gaia Collaboration, Prusti
et al. 2016, A&A 595, A1 (mission). Queried on 2026-10-12 from the ESA Gaia Archive TAP
(https://gea.esac.esa.int/tap-server/tap/sync): `gaiadr3.gaia_source` joined to
`gaiadr3.hipparcos2_best_neighbour` for 1 000 Hipparcos ids, and 120″ cone searches for 170 nearby stars; the
exact ADQL is in `build_stars.py`, the responses are cached in `data/gaia_*.csv`. Used for positions, proper
motions, radial velocities and the distance cross-check / substitution (`ps`, `ds`, `rvs` = `"gaia"`). Terms:
ESA Gaia data are free to use with the acknowledgement "This work has made use of data from the European Space
Agency (ESA) mission Gaia (https://www.cosmos.esa.int/gaia), processed by the Gaia Data Processing and Analysis
Consortium (DPAC, https://www.cosmos.esa.int/web/gaia/dpac/consortium). Funding for the DPAC has been provided by
national institutions, in particular the institutions participating in the Gaia Multilateral Agreement."

**GCVS 5.1** — Samus, Kazarovets, Durlevich, Kireeva & Pastukhova 2017, Astronomy Reports 61, 80, "General
Catalogue of Variable Stars: Version GCVS 5.1" (VizieR B/gcvs, version Oct 2020). Query 2026-10-12:
`asu-tsv?-source=B/gcvs/gcvs_cat&magMax=<8` (4 280 variables), matched to stars by position within 60″. Fields
VarType, Period, magMax, Min1, Epoch, M-m/D. CDS/VizieR data are freely usable with acknowledgement: "This
research has made use of the VizieR catalogue access tool, CDS, Strasbourg, France (DOI 10.26093/cds/vizier)."
Ochsenbein, Bauer & Marcout 2000, A&AS 143, 23.

**RECONS** — "The one hundred nearest star systems", Research Consortium On Nearby Stars (Henry et al.), list
dated 2012-01-01, https://www.astro.gsu.edu/RECONS/TOP100.posted.htm (read 2026-10-12; first 30 systems saved in
`data/recons_top30.tsv`). Used only for the distance cross-check in `stars_crosscheck.json`.

**Temperature, bolometric correction, mass–luminosity relations (formulae, no data licence):**
- Ballesteros, F. J. 2012, EPL 97, 34008, "New insights into black bodies" — the B−V → T relation.
- Pecaut, M. J. & Mamajek, E. E. 2013, ApJS 208, 9, "Intrinsic colors, temperatures, and bolometric corrections
  of pre-main-sequence stars"; E. Mamajek's maintained table "A Modern Mean Dwarf Stellar Color and Effective
  Temperature Sequence", version 2022.04.16, https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt
  (cached in `data/`). Cite Pecaut & Mamajek 2013.
- Flower, P. J. 1996, ApJ 469, 355, bolometric corrections; coefficients as corrected by Torres, G. 2010, AJ 140,
  1158.
- Eker, Z. et al. 2018, MNRAS 479, 5491, "Interrelated main-sequence mass–luminosity, mass–radius, and
  mass–effective temperature relations".
- Giant/supergiant temperature table: rounded from Cox, A. N. (ed.) 2000, *Allen's Astrophysical Quantities*,
  4th ed., tables 15.7–15.8.
- IAU 2015 Resolution B3 nominal values (Mbol,☉ = 4.74, T☉ = 5772 K; Prša et al. 2016, AJ 152, 41).
- Capella spectral types: Torres, G. et al. 2015, ApJ 807, 26.
- Literature distances: μ Cep — Montargès, M. et al. 2019, A&A 625, A48 (641 +148/−144 pc; the literature spans
  390–940 pc: Perrin et al. 2005, Davies & Beasor 2020, Wiesemeyer et al. 2026); V382 Car / HR 4337 — Kasikov,
  Mehner, Kolka & Aret 2026, A&A (arXiv:2602.02449), 2623 +88/−83 pc; μ Sgr — Gaia DR3 parallaxes of the
  companions μ Sgr D/E (0.645 mas, ~1 520 pc), via SIMBAD.
- Barnard's Star proper motion: van Leeuwen, F. 2007, A&A 474, 653 (Hipparcos, the new reduction).

## Optional large star pack (`stars_large.json`)

**Gaia DR3** — Gaia Collaboration, Vallenari, A. et al. 2023, A&A 674, A1, "Gaia Data Release 3: Summary of the
content and survey properties"; Gaia Collaboration, Prusti, T. et al. 2016, A&A 595, A1 (the mission). Tables
`gaiadr3.gaia_source`, `gaiadr3.astrophysical_parameters` and `gaiadr3.hipparcos2_best_neighbour`, queried on
2026-10-12 from the ESA Gaia Archive TAP (https://gea.esac.esa.int/tap-server/tap/sync) in six chunks
(G < 8; parallax > 10 mas with parallax_over_error > 10 and RUWE < 1.4); the exact ADQL is in
`build_stars_large.py`, the responses are cached in `data/gaia_large_*.csv` (~60 MB, not shipped). Astrophysical
parameters: Andrae, R. et al. 2023, A&A 674, A27 (GSP-Phot: `teff_gspphot`, `logg_gspphot`); Creevey, O. L. et
al. 2023, A&A 674, A26 and Fouesneau, M. et al. 2023, A&A 674, A28 (FLAME: `lum_flame`, `radius_flame`,
`mass_flame`). Astrometry: Lindegren, L. et al. 2021, A&A 649, A2 (RUWE). Radial velocities: Katz, D. et al. 2023,
A&A 674, A5. Photometric relation G−V(BP−RP): Riello, M. et al. 2021, A&A 649, A3, Table C.2. Hipparcos
cross-match: Marrese, P. M. et al. 2019, A&A 621, A144.

Gaia data are free to use; ESA asks that the following acknowledgement be shown wherever they are used, and the
app should show it with the large pack:

> This work has made use of data from the European Space Agency (ESA) mission Gaia
> (https://www.cosmos.esa.int/gaia), processed by the Gaia Data Processing and Analysis Consortium (DPAC,
> https://www.cosmos.esa.int/web/gaia/dpac/consortium). Funding for the DPAC has been provided by national
> institutions, in particular the institutions participating in the Gaia Multilateral Agreement.

Short form for the download screen: "Star catalogue: Gaia DR3 (ESA/Gaia/DPAC); names and spectral types from
HYG v4.4 (CC BY-SA 4.0)."

The pack also uses **HYG v4.4** (names, HD/Gliese numbers, V magnitudes, B−V, spectral types for the 17 104 Hipparcos
stars) and **GCVS 5.1** via VizieR (variables), with the same terms as `stars.json` above, and the same
Pecaut & Mamajek (2013) / Mamajek 2022.04.16 table (here also its G−V, Bp−Rp, M_G and log L columns), Ballesteros
(2012), Flower (1996)/Torres (2010) and Eker et al. (2018) relations. White-dwarf colours: the Montréal synthetic
photometry of DA white dwarfs (Bergeron, P. et al. 2019, ApJ 876, 67; Gaia bands from Gentile Fusillo, N. P. et
al. 2021, MNRAS 508, 3877), rounded. Because it contains HYG-derived fields, **stars_large.json is CC BY-SA 4.0**,
like stars.json.

## Pulsars (`pulsars.json`)

**ATNF Pulsar Catalogue v2.9.0** — Manchester, R. N., Hobbs, G. B., Teoh, A. & Hobbs, M. 2005, AJ 129, 1993,
"The Australia Telescope National Facility Pulsar Catalogue". File `psrcat.db` (4 503 pulsars, header
"#CATALOGUE 2.9.0", produced with psrcatV2 from the version-2 database, dated 2025-10-07 inside the tarball)
from `psrcat_pkg.tar.gz` downloaded 2026-10-12 from
https://www.atnf.csiro.au/research/pulsar/psrcat/downloads/psrcat_pkg.tar.gz (SHA-256 `55daa29f71f344c8…`).
Terms: the catalogue is publicly available for research and educational use; cite Manchester et al. 2005 and
the catalogue URL https://www.atnf.csiro.au/research/pulsar/psrcat/. Each parameter in psrcat.db carries its own
literature reference; `build_pulsars.py` keeps the catalogue's preferred values. Derived fields: characteristic
age P/2Ṗ and dipole field 3.2×10¹⁹√(PṖ) G (standard formulae, Lorimer & Kramer 2004 *Handbook of Pulsar
Astronomy*). Glitch counts from the NGLT field (Jodrell Bank glitch catalogue, Espinoza et al. 2011, MNRAS 414,
1679, as compiled in psrcat). Distances: parallax when ϖ/σ > 3, else the catalogue's independent distance,
else DM with YMW16 (Yao, Manchester & Wang 2017, ApJ 835, 29) or NE2001 (Cordes & Lazio 2002, astro-ph/0207156).

## Radio sources (`radio.json`)

Curated from:
- Baars, J. W. M., Genzel, R., Pauliny-Toth, I. I. K. & Witzel, A. 1977, A&A 61, 99, "The absolute spectrum of
  Cas A; an accurate flux density scale and a set of secondary calibrators" — spectral fits for Cas A (epoch
  1980), Cyg A, Tau A, Vir A (Table 5) and the Cas A fading formula (eq. 1). The coefficients were transcribed from
  the paper as commonly quoted; the modern scale of Perley & Butler 2017 (ApJS 230, 7) agrees to a few per cent.
- Trotter, A. S. et al. 2017, MNRAS 469, 1299, "The fading of Cassiopeia A, and improved models for the absolute
  spectrum of primary radio calibration sources" — Cas A 0.670 ± 0.019 %/yr and Tau A 0.102 %/yr at 1.4 GHz
  (read via arXiv:1704.00002 on 2026-10-12).
- Aller, H. D. & Reynolds, S. P. 1985, ApJ 293, L73 — Crab Nebula secular decrease 0.167 %/yr.
- Cas A explosion date: Thorstensen, Fesen & van den Bergh 2001, AJ 122, 297; Fesen et al. 2006, ApJ 645, 283.
- Cyg A: Carilli, C. L. & Barthel, P. D. 1996, A&ARv 7, 1.
- Cen A: Israel, F. P. 1998, A&ARv 8, 237 (review; total 1.4-GHz flux ~1 330 Jy from Cooper, Price & Cole 1965).
- Sgr A*: GRAVITY Collaboration 2019, A&A 625, L10 (mass 4.154 × 10⁶ M☉, distance 8.178 kpc); Event Horizon
  Telescope Collaboration 2022, ApJL 930, L12 (ring diameter 51.8 µas, 2.4 Jy at 230 GHz); Melia, F. & Falcke, H.
  2001, ARA&A 39, 309 (radio spectrum S ∝ ν^0.3); Bower, G. C. et al. 2015, ApJ 802, 69 (radio variability);
  Genzel, R. et al. 2003, Nature 425, 934 and Do, T. et al. 2019, ApJL 882, L27 (near-infrared flares); Neilsen, J.
  et al. 2013, ApJ 774, 42 (X-ray flare rate 1.1/day); Wielgus, M. et al. 2022, ApJL 930, L19 (sub-mm variability).
  The 1.4-GHz flux (~0.4 Jy) is an extrapolation of the inverted spectrum and is marked approximate.

## Fast radio bursts (`frb.json`)

**CHIME/FRB Catalog 1** — The CHIME/FRB Collaboration (Amiri, M. et al.) 2021, ApJS 257, 59, "The First
CHIME/FRB Fast Radio Burst Catalog". Obtained from VizieR J/ApJS/257/59/table2 on 2026-10-12 (600 burst rows,
536 sources, 18 repeaters); cached in `data/chimefrbcat1_vizier.tsv`. CHIME/FRB asks that publications using the
catalogue cite that paper and acknowledge: "We acknowledge that CHIME is located on the traditional, ancestral,
and unceded territory of the Syilx/Okanagan people." The official download page is https://www.chime-frb.ca/catalog.

Curated bursts: Lorimer, D. R. et al. 2007, Science 318, 777 (FRB 010724); Spitler, L. G. et al. 2016, Nature
531, 202 and Chatterjee, S. et al. 2017, Nature 541, 58 (FRB 20121102A); Rajwade, K. M. et al. 2020, MNRAS 495,
3551 and Cruces, M. et al. 2021, MNRAS 500, 448 (its ~157–161-day cycle); The CHIME/FRB Collaboration 2020, Nature
582, 351 (FRB 20180916B, 16.35 ± 0.15 d) and Marcote, B. et al. 2020, Nature 577, 190 (its host); The CHIME/FRB
Collaboration 2020, Nature 587, 54 and Bochenek, C. D. et al. 2020, Nature 587, 59 (FRB 20200428 from SGR
1935+2154); Bannister, K. W. et al. 2019, Science 365, 565 (FRB 20180924B); Bhardwaj, M. et al. 2021, ApJL 910,
L18 and Kirsten, F. et al. 2022, Nature 602, 585 (FRB 20200120E in M81); Lanman, A. E. et al. 2022, ApJ 927, 59
and Xu, H. et al. 2022, Nature 609, 685 (FRB 20201124A).

## Rotation curve (`rotation.json`)

- Eilers, A.-C., Hogg, D. W., Rix, H.-W. & Ness, M. K. 2019, ApJ 871, 120, "The circular velocity curve of the
  Milky Way from 5 to 25 kpc" — Table 1 transcribed in full (38 points; read from arXiv:1810.09466 on 2026-10-12).
  R₀ = 8.122 kpc, v_c(R₀) = 229.0 km/s.
- Sofue, Y. 2020, Galaxies 8, 37, "Rotation curve of the Milky Way and its dark matter halo" — Appendix 1 Tables
  5–6 (running-averaged unified rotation curve), rows R ≤ 6.02 kpc transcribed (read from arXiv:2004.11688v3).
  R₀ = 8.0 kpc, V₀ = 238 km/s. Open access (CC BY 4.0, MDPI).
- McMillan, P. J. 2017, MNRAS 465, 76, "The mass distribution and gravitational potential of the Milky Way" —
  best-fit parameters; evaluated with **galpy** 1.12.0 (`galpy.potential.mwpotentials.McMillan17`): Bovy, J.
  2015, ApJS 216, 29, "galpy: A Python library for Galactic dynamics" (BSD-3 licence).

## The Sun's orbit and the spiral arms (`sunorbit.json`)

- Potential and integration: McMillan 2017 via galpy 1.12.0 (above).
- Schönrich, R., Binney, J. & Dehnen, W. 2010, MNRAS 403, 1829 — solar peculiar motion (11.1, 12.24, 7.25) km/s.
- Bennett, M. & Bovy, J. 2019, MNRAS 482, 1417 — Sun's height z₀ = 20.8 ± 0.3 pc.
- GRAVITY Collaboration 2019, A&A 625, L10 — R₀ = 8.178 kpc; Reid, M. J. & Brunthaler, A. 2020, ApJ 892, 39 —
  Sgr A* proper motion; Reid, M. J. et al. 2019, ApJ 885, 131, "Trigonometric parallaxes of high-mass
  star-forming regions: our view of the Milky Way" — Table 2 spiral-arm fits and Table 3 (fit A5) constants
  (read from the published PDF on 2026-10-12). Vallée, J. P. 2017, Ap&SS 362, 79 — mean pitch angle 13°.
- Bahcall, J. N. & Bahcall, S. 1985, Nature 316, 706 — the Sun's vertical oscillation (52–74 Myr, 49–93 pc).
- Pattern speeds and bar: Dias, W. S. et al. 2019, MNRAS 486, 5726 (spiral Ω_p = 28.2 ± 2.1 km/s/kpc); Gerhard,
  O. 2011, Mem. S.A.It. Suppl. 18, 185 (review, 20–30); Portail, M. et al. 2017, MNRAS 465, 1621 (bar 39 ± 3.5);
  Sanders, J. L. et al. 2019, MNRAS 488, 4552 (41 ± 3); Clarke, J. P. & Gerhard, O. 2022, MNRAS 512, 2171
  (33.3 ± 1.8); Wegg, C. & Gerhard, O. 2013, MNRAS 435, 1874 (bar angle 27 ± 2°); Wegg, C., Gerhard, O. &
  Portail, M. 2015, MNRAS 450, 4050 (half-length 5.0 ± 0.2 kpc).

## Starquakes (`seismo.json`)

- Broomhall, A.-M. et al. 2009, MNRAS 396, L100, "Definitive Sun-as-a-star p-mode frequencies: 23 years of BiSON
  observations" — Table 1 (raw best-fitting frequencies, 1985-04-04 to 2008-12-16), transcribed from
  arXiv:0903.5219 on 2026-10-12. BiSON (Birmingham Solar-Oscillations Network) is funded by the UK STFC.
- Huber, D. et al. 2011, ApJ 743, 143 — νmax,☉ = 3090 ± 30 µHz, Δν☉ = 135.1 ± 0.1 µHz.
- Kjeldsen, H. & Bedding, T. R. 1995, A&A 293, 87 — scaling relations and the 23.4 cm/s amplitude scaling;
  Brown, T. M. et al. 1991, ApJ 368, 599 — νmax ∝ g/√T; Mosser, B. et al. 2012, A&A 537, A30 — envelope width.

## The Local Group (`localgroup.json`)

**McConnachie, A. W. 2012, AJ 144, 4, "The observed properties of dwarf galaxies in and around the Local Group"** —
VizieR J/AJ/144/4 (`catalog` table, 102 rows: every galaxy within ~3 Mpc as of 2012; `refs` table for the
original sources), obtained 2026-10-13 from https://vizier.cds.unistra.fr/viz-bin/asu-tsv?-source=J/AJ/144/4 and
cached in `data/mcconnachie2012_raw.tsv`. Positions, Hubble types, distances, heliocentric radial velocities, Galactocentric
distances and velocities, V magnitudes, half-light radii, central surface brightnesses, position angles, ellipticities,
absolute magnitudes, [Fe/H], velocity dispersions and HI masses are the catalogue's (each with its own reference in the
paper's tables). CDS/VizieR data are freely usable with the acknowledgement "This research has made use of the VizieR
catalogue access tool, CDS, Strasbourg, France (DOI 10.26093/cds/vizier)." The two HIZSS 3 clouds (HI only, no
magnitude) are dropped.

Standard values added for the large galaxies (the catalogue gives them by name only):
- Distances: M31 761 ± 11 kpc — Li, S., Riess, A. G. et al. 2021, ApJ 920, 84 (Cepheids and eclipsing binaries;
  the catalogue's 783 kpc is kept in `dcat`); M33 859 ± 24 kpc — Breuval, L. et al. 2023, ApJ 951, 118 (catalogue 809);
  LMC 49.59 ± 0.09 (stat) ± 0.54 (sys) kpc — Pietrzyński, G. et al. 2019, Nature 567, 200; SMC 62.44 ± 0.47 kpc —
  Graczyk, D. et al. 2020, ApJ 904, 13; the Milky Way row sits at Sgr A*, R₀ = 8.178 kpc (GRAVITY Collaboration 2019).
- M31: V = 3.44, M_V = −21.2 (de Vaucouleurs et al. 1991, RC3, corrected for extinction; range −21.0…−21.5 in the
  literature); inclination 77°, position angle 38° (de Vaucouleurs 1958, ApJ 128, 465; Walterbos & Kennicutt 1988);
  disc scale length 5.3 kpc (Courteau, S. et al. 2011, ApJ 739, 20). Rotation curve read (±10 km/s) from Corbelli, E.,
  Lorenzoni, S., Walterbos, R., Braun, R. & Thilker, D. 2010, A&A 511, A89 (HI, 30-m + Arecibo, Fig. 3 and Table 1) and
  Chemin, L., Carignan, C. & Foster, T. 2009, ApJ 705, 1395; baryonic masses for the no-dark-matter curve: bulge
  3.2 × 10¹⁰, stellar disc 7 × 10¹⁰, gas 7 × 10⁹ M☉ (Corbelli et al. 2010; Tamm, A. et al. 2012, A&A 546, A4).
- M33: M_V = −18.9, inclination 56°, PA 23°, disc scale length 1.8 kpc, rotation curve from Corbelli, E., Thilker, D.,
  Zibetti, S., Giovanardi, C. & Salucci, P. 2014, A&A 572, A23 (HI, VLA + GBT; stellar disc 4.8 × 10⁹, gas 3.2 × 10⁹ M☉);
  earlier Corbelli & Salucci 2000, MNRAS 311, 441.
- LMC: inclination 34°, PA 140°, disc scale length 1.5 kpc (van der Marel, R. P. 2001, AJ 122, 1827; van der Marel &
  Cioni 2001), bar half-length 1.5 kpc at PA 115° (Zaritsky, D. 2004); rotation curve 91.7 ± 18.8 km/s flat beyond ~4 kpc
  from van der Marel, R. P. & Kallivayalil, N. 2014, ApJ 781, 121 (HST proper motions and line-of-sight velocities), in
  agreement with Gaia Collaboration, Helmi, A. et al. 2018, A&A 616, A12; stellar mass 2.7 × 10⁹ M☉ (van der Marel et al.
  2002, AJ 124, 2639), HI 4.8 × 10⁸ M☉ (Kim et al. 1998).
- SMC: nominal inclination 65°, PA 45°, scale length 1 kpc; rotation ~60 km/s from Di Teodoro, E. M. et al. 2019, MNRAS
  483, 392 (ASKAP HI) and Stanimirović, S., Staveley-Smith, L. & Jones, P. A. 2004, ApJ 604, 176 — **APPROX**: the SMC
  is elongated along the line of sight and far from an equilibrium disc; stellar mass 3 × 10⁸, HI 4.6 × 10⁸ M☉.
- Integrated colours: RC3 (de Vaucouleurs, G. et al. 1991, *Third Reference Catalogue of Bright Galaxies*) B−V, corrected
  for Galactic extinction, for the bright galaxies; typical values by Hubble type for the dwarfs (`bvs:"type"`:
  dSph 0.75, dE 0.85, cE 0.90, dIrr 0.45, transition 0.55 — Mateo 1998, ARA&A 36, 435). The temperature `T` is the
  Ballesteros (2012) black body of that colour, the rule the app states for the "integrated starlight tone".
- Baryons-only rotation curves: Freeman (1970, ApJ 160, 811) exponential discs plus a Hernquist (1990, ApJ 356, 359)
  bulge with the masses above, evaluated with SciPy's modified Bessel functions. No dark halo. These are illustrative
  mass models, not fits.

## Names for the search (`names.json`)

A hand-written dictionary (CC0): the 88 IAU constellations with their Latin nominative and genitive and their names in
the twelve languages; the common names of about eighty bright or famous stars where a language spells them differently
(IAU WGSN names; Wikipedia in each language; the Chinese traditional names, e.g. 天狼星 for Sirius, from the Chinese
star catalogue tradition as given on Chinese Wikipedia); household names for the Crab and Vela pulsars, Sgr A*, the
bright radio sources and the Local Group galaxies; and the Greek letters with the Latin and three-letter spellings used
for Bayer designations.

## The stars' radio emission and the famous binaries' orbits (`starradio.json`)

A hand-curated table (step 4c of the extension): order-of-magnitude radio properties of 42 notable stars of stars.json,
and the orbital periods of 18 famous binaries among them. Every row carries its own `ref`; rows marked `est` are
class-typical values, not measurements of that star. Any star not in the table is radio-quiet, below detection (upper
limits of 0.1–1 mJy are typical). The main sources:

- The Sun: Dulk, G. A. 1985, ARA&A 23, 169, "Radio emission from the Sun and stars"; Tapping, K. F. 2013, Space Weather
  11, 394 (the 10.7-cm flux).
- Flare stars: Güdel, M. 2002, ARA&A 40, 217, "Stellar radio astronomy" (the review the class-typical values follow);
  Zic, A. et al. 2020, ApJ 905, 23 (Proxima, ASKAP 888 MHz); MacGregor, M. A. et al. 2018, ApJL 855, L2 (Proxima, ALMA);
  Pérez-Torres, M. et al. 2021, A&A 645, A77 (Proxima, 1.6 GHz); Lynch, C. R. et al. 2017, ApJL 836, L30 (UV Cet, MWA);
  Benz, A. O., Conway, J. & Güdel, M. 1998, A&A 331, 596 (UV Cet, VLBI); Güdel, M. et al. 1989, A&A 220, L5 and Osten,
  R. A. & Bastian, T. S. 2008, ApJ 674, 1078 (AD Leo); Osten, R. A. et al. 2005, ApJ 621, 398 (EV Lac); Villadsen, J. &
  Hallinan, G. 2019, ApJ 871, 214 (coherent bursts of AD Leo, UV Cet, EV Lac, EQ Peg, YZ CMi).
- Masers and red (super)giants: Pardo, J. R. et al. 2004, A&A 424, 145 (SiO monitoring of Mira and χ Cyg); Cotton,
  W. D. et al. 2010, ApJS 187, 107 (VLBA SiO); Bowers, P. F. & Johnston, K. J. 1994, ApJS 92, 189 (H₂O); Sivagnanam, P.
  et al. 1990, A&AS 86, 1 (OH); Richards, A. M. S. et al. 2012, A&A 546, A16 and Lane, A. P. et al. 1987, ApJ 323, 756
  (μ Cep H₂O); Nakashima, J. & Deguchi, S. 2003, PASJ 55, 229 (SiO in μ Cep, α Ori, α Sco); Lim, J. et al. 1998, Nature
  392, 575 and O'Gorman, E. et al. 2015, A&A 580, A101 (Betelgeuse continuum); Hjellming, R. M. & Newell, R. T. 1983,
  ApJ 275, 704 and O'Gorman, E. et al. 2020, A&A 638, A65 (Antares); Matthews, L. D. & Karovska, M. 2006, ApJL 637, L49
  (Mira A and B continuum). Line rest frequencies: the JPL / CDMS / NRAO spectral-line lists (H₂O 22 235.08 MHz, SiO
  v=1 43 122.08 and v=2 42 820.59 MHz, OH 1612.231, 1665.402, 1667.359 MHz).
- Hot-star winds: Bieging, J. H., Abbott, D. C. & Churchwell, E. B. 1989, ApJ 340, 518; Blomme, R. et al. 2002, A&A 382,
  921 and 2003, A&A 408, 715; Scuderi, S. et al. 1998, A&A 332, 251.
- Active binaries: Lestrade, J.-F. et al. 1988, ApJ 328, 232 and Peterson, W. M. et al. 2010, Nature 463, 207 (Algol);
  Richards, M. T. et al. 2003, ApJS 147, 337; Drake, S. A., Simon, T. & Linsky, J. L. 1989, ApJS 71, 905 (the VLA survey
  of RS CVn and Algol systems, and the A-star non-detections); Bastian, T. S. et al. 1992, ApJ 384, L47 (λ And); Umana,
  G. et al. 1993, A&A 267, 126 (σ Gem) and 2000, A&A 358, 229 (β Lyr); Güdel, M. et al. 1993, ApJ 405, L63 and Schmitt,
  J. H. M. M. et al. 1994, ApJ 433, 268 (Castor).
- Thermal chromospheres: Drake, S. A. & Linsky, J. L. 1986, AJ 91, 602; O'Gorman, E. et al. 2013, AJ 146, 98 (Arcturus,
  Aldebaran); Trigilio, C. et al. 2018, MNRAS 481, 217 and Liseau, R. et al. 2015, A&A 573, L4 (α Cen A and B); Drake,
  S. A., Simon, T. & Brown, A. 1993, ApJ 406, 247 and Villadsen, J. et al. 2014, ApJ 788, 112 (Procyon and other dwarfs);
  Bastian, T. S. et al. 2018, ApJ 857, 133, Suresh, A. et al. 2020, ApJ 904, 138 and MacGregor, M. A. et al. 2015, ApJ
  809, 47 (ε Eri).
- Radio-quiet stars: Callingham, J. R. et al. 2021, Nature Astronomy 5, 1233 (V-LoTSS) and Pritchard, J. et al. 2021,
  MNRAS 502, 5438 (ASKAP; non-detections of the nearest stars); Lawler, S. M. et al. 2014, MNRAS 444, 2665 (τ Cet);
  Boley, A. C. et al. 2012, ApJL 750, L21 (Fomalhaut).
- Orbits: Bond, H. E. et al. 2017, ApJ 840, 70 (Sirius) and 2015, ApJ 813, 106 (Procyon); Pourbaix, D. & Boffin, H. M. J.
  2016, A&A 586, A90 (α Cen); Kervella, P., Thévenin, F. & Lovis, C. 2017, A&A 598, L7 (Proxima's orbit); Kervella, P.
  et al. 2016, A&A 593, A127 (UV Cet) and 2008, A&A 488, 667 (61 Cyg); Kolbas, V. et al. 2015, MNRAS 451, 4150 (Algol);
  Torres, G. et al. 2015, ApJ 807, 26 (Capella) and 2022, ApJ 941, 8 (Castor); Reimers, D. et al. 2008, A&A 491, 229
  (Antares); Evans, N. R. et al. 2008, AJ 136, 1137 (Polaris); Harmanec, P. 2002, AN 323, 87 (β Lyr); Tkachenko, A. et
  al. 2016, MNRAS 458, 1964 (Spica); Harvin, J. A. et al. 2002, ApJ 565, 1216 (δ Ori); Prieur, J.-L. et al. 2002, ApJS
  139, 249 (Mira); Mason, B. D. et al. 2001, AJ 122, 3466 (the Washington Double Star Catalog: η Cas, ξ Boo, Aldebaran).

The table is CC0; cite the papers above for the numbers.

## The planets', moons', minor bodies' and comets' spectra (`bodyspectra.json`)

A hand-curated table (step 4e): the reflected-light spectrum of every body of the app from 350 nm to 2.5 µm, read from
published spectra and rounded (APPROX: band depths and widths ±30 %; centres the literature values). Each body lists its
own sources in the file. The main ones:

- The Sun's lines: Kurucz, R. L., Furenlid, I., Brault, J. & Testerman, L. 1984, *Solar Flux Atlas from 296 to 1300 nm*,
  NSO Atlas No. 1; Livingston, W. & Wallace, L. 1991, *An Atlas of the Solar Spectrum in the Infrared from 1850 to 9000
  cm⁻¹ (1.1 to 5.4 µm)*, NSO Technical Report 91-001.
- Giant planets and Titan: Karkoschka, E. 1994, Icarus 111, 174 and 1998, Icarus 133, 134 (full-disc albedo spectra
  300–1000 nm and methane absorption); Clark, R. N. & McCord, T. B. 1979, Icarus 40, 180 (Jupiter and Saturn,
  0.65–2.5 µm); Fink, U. & Larson, H. P. 1979, ApJ 233, 1021 (Uranus, Neptune and Titan, 0.8–2.5 µm).
- Earth: Woolf, N. J. et al. 2002, ApJ 574, 430 and Turnbull, M. C. et al. 2006, ApJ 644, 551 (earthshine).
- Mars: McCord, T. B. & Westphal, J. A. 1971, ApJ 168, 141; Mustard, J. F. & Bell, J. F. 1994, GRL 21, 353; Erard, S. &
  Calvin, W. 1997, Icarus 130, 449.
- Venus: Barker, E. S. 1979, GRL 6, 117 (SO₂ and the ultraviolet); Pollack, J. B. et al. 1993, Icarus 103, 1; Mallama, A., Krobusek, B. &
  Pavlov, H. 2017, Icarus 282, 19.
- Mercury and the Moon: Warell, J. 2003, Icarus 161, 199; McClintock, W. E. et al. 2008, Science 321, 62; Lane, A. P. &
  Irvine, W. M. 1973, AJ 78, 267; Pieters, C. M. 1986, Rev. Geophys. 24, 557.
- Io and the icy moons: Carlson, R. W. et al. 2007, in *Io After Galileo* (Springer); Clark, R. N. & McCord, T. B. 1980,
  Icarus 41, 323; Calvin, W. M. et al. 1995, JGR 100, 19041; Clark, R. N. et al. 1984, Icarus 58, 265; Grundy, W. M. et al. 2006, Icarus 184, 543 (CO₂ ice on the Uranian moons).
- Triton, Pluto, Charon, Nix and Hydra: Cruikshank, D. P. et al. 1993, Science 261, 742; Quirico, E. et al. 1999, Icarus
  139, 159; Owen, T. C. et al. 1993, Science 261, 745; Grundy, W. M. & Fink, U. 1996, Icarus 124, 329; Protopapa, S. et
  al. 2017, Icarus 287, 218; Brown, M. E. & Calvin, W. M. 2000, Science 287, 107; Cook, J. C. et al. 2018, Icarus 315, 30.
- Dwarf planets: Brown, M. E., Trujillo, C. A. & Rabinowitz, D. L. 2005, ApJ 635, L97 (Eris); Trujillo, C. A. et al. 2007,
  ApJ 655, 1172 (Haumea); Licandro, J. et al. 2006, A&A 445, L35 (Makemake); Barucci, M. A. et al. 2005, A&A 439, L1 and
  Emery, J. P. et al. 2007, A&A 466, 395 (Sedna); Brown, M. E. & Butler, B. J. 2018, AJ 156, 164 (Dysnomia).
- Asteroids: DeMeo, F. E. et al. 2009, Icarus 202, 160 (the Bus–DeMeo taxonomy, 0.45–2.45 µm); McCord, T. B., Adams,
  J. B. & Johnson, T. V. 1970, Science 168, 1445 (Vesta); Gaffey, M. J. 1997, Icarus 127, 130 (Vesta's pyroxene); Rivkin, A. S. et
  al. 2002, Icarus 156, 64; Murchie, S. & Erard, S. 1996, Icarus 123, 63 (Phobos); Takato, N. et al. 2004, Science 306,
  2224 (Amalthea).
- Comets: Cochran, A. L. & Cochran, W. D. 2002, Icarus 157, 297 (an atlas of cometary emission lines); A’Hearn, M. F. et
  al. 1995, Icarus 118, 223; Feldman, P. D., Cochran, A. L. & Combi, M. R. 2004, in *Comets II*; Lamy, P. L. et al. 2004,
  in *Comets II* (nuclei); Cremonese, G. et al. 1997, ApJ 490, L199 (Hale–Bopp's sodium tail); Capaccioni, F. et al. 2015,
  Science 347, aaa0628 (67P).
- Band shapes of ices and minerals: the USGS Spectral Library version 7 (Kokaly, R. F. et al. 2017, USGS Data Series 1035)
  and the RELAB spectral library (Brown University).

The table is CC0; cite the papers above for the numbers.

## The black holes (`blackholes.json`)

A hand-curated table (step 4f of the extension); every row carries its own `ref`; `est` marks illustrative values.

- Sagittarius A*: GRAVITY Collaboration 2022, A&A 657, L12, "Mass distribution in the Galactic Center based on
  interferometric astrometry of multiple stellar orbits" (M = 4.297 × 10⁶ M☉, R₀ = 8 277 pc; Table 5: the orbits of S2,
  S29, S38, S42, S55, S60); Event Horizon Telescope Collaboration 2022, ApJL 930, L12 (the 51.8 ± 2.3 µas ring);
  GRAVITY Collaboration 2018, A&A 618, L10 (orbital motion of the near-infrared flares near the last stable orbit);
  GRAVITY Collaboration 2020, A&A 636, L5 (S2's Schwarzschild precession) and 2018, A&A 615, L15 (S2's gravitational
  redshift); Peißker, F. et al. 2022, ApJ 933, 49 (S4716, a 4-year orbit, B8/9 V, ~12 500 K); Habibi, M. et al. 2017,
  ApJ 847, 120 (S2: B0–2.5 V, 28 500 K, 13.6 M☉, log g 4.1); Eisenhauer, F. et al. 2005, ApJ 628, 246 (the fainter
  S-stars B4–B9 V); Fritz, T. K. et al. 2011, ApJ 737, 73 (A_K = 2.42); Falcke, H. et al. 1998, ApJ 499, 731 (the radio
  spectrum ν^0.3 and the sub-mm bump); Do, T. et al. 2019, ApJL 882, L27 and Witzel, G. et al. 2018, ApJ 863, 15 (the
  near-infrared flux distribution and red-noise power spectrum); Neilsen, J. et al. 2013, ApJ 774, 42 (X-ray flares);
  Baganoff, F. K. et al. 2003, ApJ 591, 891 (the quiescent X-rays); Schödel, R. et al. 2018, A&A 609, A27 (the nuclear
  star cluster's density profile, used statistically for the drawing).
- Gaia BH1: El-Badry, K. et al. 2023, MNRAS 518, 1057. Gaia BH2: El-Badry, K. et al. 2023, MNRAS 521, 4323 (Table 2).
  Gaia BH3: Gaia Collaboration, Panuzzo, P. et al. 2024, A&A 686, L2 (Table 2).
- Cygnus X-1: Miller-Jones, J. C. A. et al. 2021, Science 371, 1046; Orosz, J. A. et al. 2011, ApJ 742, 84; Nowak,
  M. A. 2000, MNRAS 318, 361 and Pottschmidt, K. et al. 2003, A&A 407, 1039 (the hard-state power spectrum); Stirling,
  A. M. et al. 2001, MNRAS 327, 1273 (the jet).
- V404 Cygni: Miller-Jones, J. C. A. et al. 2009, ApJL 706, L230 (distance); Khargharia, J. et al. 2010, ApJ 716, 1105
  (mass); Casares, J. et al. 1992, Nature 355, 614 (orbit); Radhika, D. et al. 2016, MNRAS 462, 1834 and Rodriguez, J.
  et al. 2015, A&A 581, L9 (the 2015 outburst).
- A0620−00: Cantrell, A. G. et al. 2010, ApJ 710, 1127; Neilsen, J. et al. 2008, ApJ 673, 1110.
- M31*: Bender, R. et al. 2005, ApJ 631, 280; Garcia, M. R. et al. 2010, ApJ 710, 755; Li, Z. et al. 2011, ApJ 728, L10.
  M32: van den Bosch, R. C. E. & de Zeeuw, P. T. 2010, MNRAS 401, 1770. M33: Gebhardt, K. et al. 2001, AJ 122, 2469;
  Merritt, D. et al. 2001, Science 293, 1116.
- GW150914: Abbott, B. P. et al. (LIGO Scientific and Virgo Collaborations) 2016, PRL 116, 061102. The app synthesises a
  waveform of the published shape (no LIGO audio or data is used); ringdown frequency and damping from the Berti et al.
  2006 fits for the final mass and spin.

## Software

Python 3.13, numpy 2.5, pandas 3.0, galpy 1.12.0 (Bovy 2015), curl. No Astropy. Build scripts: `common.py`,
`build_stars.py`, `build_stars_large.py`, `build_pulsars.py`, `build_radio.py`, `build_rotation.py`, `build_sunorbit.py`,
`build_seismo.py`, `build_localgroup.py`, `build_names.py`, `build_starradio.py`, `build_bodyspectra.py`, `build_blackholes.py`, `tests.py`, `build_all.sh`. SciPy 1.18 for the Bessel functions of the galaxies' disc models.

## Short credits for the app

> Stars: HYG Database v4.4 (David Nash, astronexus.com, CC BY-SA 4.0), with Gaia DR3 (ESA/DPAC) and the GCVS
> (Samus et al. 2017) via VizieR/CDS. Pulsars: ATNF Pulsar Catalogue 2.9.0 (Manchester et al. 2005). Fast radio
> bursts: CHIME/FRB Catalog 1 (CHIME/FRB Collaboration 2021). Rotation curve: Eilers et al. 2019; Sofue 2020;
> mass model McMillan 2017 via galpy (Bovy 2015). Spiral arms: Reid et al. 2019. Solar motion: Schönrich et al.
> 2010. Solar oscillations: BiSON (Broomhall et al. 2009). Radio sources: Baars et al. 1977; Trotter et al. 2017;
> GRAVITY and EHT Collaborations. Local Group: McConnachie 2012 via VizieR/CDS; distances Li et al. 2021 (M31), Breuval
> et al. 2023 (M33), Pietrzyński et al. 2019 (LMC), Graczyk et al. 2020 (SMC); rotation curves Corbelli et al. 2010 and
> 2014, van der Marel & Kallivayalil 2014, Di Teodoro et al. 2019. Stellar radio emission: Güdel 2002 and the papers
> listed under starradio.json (Zic et al. 2020; Lynch et al. 2017; Lim et al. 1998; Peterson et al. 2010; Pardo et al. 2004…).
> Planets', moons' and comets' spectra: Karkoschka 1994, 1998; Clark & McCord 1979, 1980; Fink & Larson 1979; Turnbull et
> al. 2006; Grundy & Fink 1996; DeMeo et al. 2009; Cochran & Cochran 2002; the Kurucz et al. 1984 solar atlas; USGS and RELAB.
>
> Black holes: GRAVITY Collaboration 2018–2022; EHT Collaboration 2022; Peißker et al. 2022; El-Badry et al. 2023 (Gaia
> BH1, BH2); Gaia Collaboration, Panuzzo et al. 2024 (Gaia BH3); Miller-Jones et al. 2021 (Cygnus X-1); Radhika et al. 2016
> (V404 Cygni); Cantrell et al. 2010 (A0620−00); Bender et al. 2005 (M31*); van den Bosch & de Zeeuw 2010 (M32); Gebhardt
> et al. 2001 (M33); Abbott et al. 2016 (GW150914, synthesised from its parameters).
>
> Large star pack (optional download): Gaia DR3, ESA/Gaia/DPAC (Gaia Collaboration, Vallenari et al. 2023), with
> HYG v4.4 names (CC BY-SA 4.0); show the full ESA acknowledgement above with it.
