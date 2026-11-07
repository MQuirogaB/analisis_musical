# Musicalidad para bailarines

Material de clase para aprender a **escuchar la estructura de una canción** y distinguir:

| Concepto | Pregunta que responde | Ficha |
|---|---|---|
| Compás | ¿Cómo se agrupan los pulsos? | [docs/00-base-pulso-y-compas.md](docs/00-base-pulso-y-compas.md) |
| Anacrusa | ¿Qué suena *antes* del primer tiempo fuerte? | [docs/01-anacrusa.md](docs/01-anacrusa.md) |
| Síncopa | ¿Dónde cae un acento inesperado? | [docs/02-sincopa.md](docs/02-sincopa.md) |
| Frase musical | ¿Dónde empieza y termina una "idea"? | [docs/03-frase-musical.md](docs/03-frase-musical.md) |
| Bloque musical | ¿Qué frases forman una unidad mayor? | [docs/04-bloque-musical.md](docs/04-bloque-musical.md) |
| Intro | ¿Cómo arranca la canción? | [docs/05-intro.md](docs/05-intro.md) |
| Puente | ¿Dónde cambia el paisaje a mitad de canción? | [docs/06-puente.md](docs/06-puente.md) |
| Coda | ¿Cómo se cierra la canción? | [docs/07-coda.md](docs/07-coda.md) |

## Canción analizada

- **O vento traz o teu perfume** — vjgalaxy / Alejandro Piñero Amerio (Pixabay, 3:07), 90 BPM. [Análisis](analisis/o-vento-traz-o-teu-perfume.md)

Música de la segunda canción: Alejandro Piñero Amerio, de [Pixabay](https://pixabay.com/music/) (Pixabay Content License).

## Cómo usar este repo en clase

1. Leer la ficha del concepto (1 página cada una).
2. Hacer la actividad de escucha que cierra cada ficha.
3. Escuchar la canción con el análisis delante y comprobar cada sección por tiempos.
4. Repetir el ejercicio con una canción nueva usando [analisis/plantilla.md](analisis/plantilla.md).

## Web

`index.html` es una página estática (sin dependencias) que muestra los conceptos y la línea de tiempo de la canción a partir de `data/o-vento-traz-o-teu-perfume.json`. Para verla en local: `python3 -m http.server` dentro de esta carpeta y abrir `http://localhost:8000`.

## Estado

- [x] Fichas de teoría
- [x] Plantilla de análisis
- [x] Mapa de secciones, tempo (90 BPM) y compases de *O vento traz o teu perfume*
- [ ] Confirmar al oído qué bloques son estrofa / estribillo y si hay anacrusa en la voz

## Audio

Los mp3 están en `audio/` y la web los reproduce directamente. La forma de onda (`data/*-peaks.json`) se genera con `tools/peaks.py`.

- *O vento traz o teu perfume*: Alejandro Piñero Amerio, de [Pixabay](https://pixabay.com/music/) (Pixabay Content License).
