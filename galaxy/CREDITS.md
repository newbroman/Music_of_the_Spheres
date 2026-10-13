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

## Software

Python 3.13, numpy 2.5, pandas 3.0, galpy 1.12.0 (Bovy 2015), curl. No Astropy. Build scripts: `common.py`,
`build_stars.py`, `build_stars_large.py`, `build_pulsars.py`, `build_radio.py`, `build_rotation.py`, `build_sunorbit.py`,
`build_seismo.py`, `tests.py`, `build_all.sh`.

## Short credits for the app

> Stars: HYG Database v4.4 (David Nash, astronexus.com, CC BY-SA 4.0), with Gaia DR3 (ESA/DPAC) and the GCVS
> (Samus et al. 2017) via VizieR/CDS. Pulsars: ATNF Pulsar Catalogue 2.9.0 (Manchester et al. 2005). Fast radio
> bursts: CHIME/FRB Catalog 1 (CHIME/FRB Collaboration 2021). Rotation curve: Eilers et al. 2019; Sofue 2020;
> mass model McMillan 2017 via galpy (Bovy 2015). Spiral arms: Reid et al. 2019. Solar motion: Schönrich et al.
> 2010. Solar oscillations: BiSON (Broomhall et al. 2009). Radio sources: Baars et al. 1977; Trotter et al. 2017;
> GRAVITY and EHT Collaborations.
>
> Large star pack (optional download): Gaia DR3, ESA/Gaia/DPAC (Gaia Collaboration, Vallenari et al. 2023), with
> HYG v4.4 names (CC BY-SA 4.0); show the full ESA acknowledgement above with it.
