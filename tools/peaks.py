"""Calcula la forma de onda (picos mín/máx) de un mp3 y la guarda como JSON.
Uso: python3 tools/peaks.py audio/o-vento-traz-o-teu-perfume.mp3 data/o-vento-traz-o-teu-perfume-peaks.json
Requiere ffmpeg y numpy."""
import subprocess, sys, json, numpy as np
src, out = sys.argv[1], sys.argv[2]
SR, BINS = 8000, 1600
raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-ac","1","-ar",str(SR),"-f","s16le","-"],
                     capture_output=True, check=True).stdout
y = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768
edges = np.linspace(0, len(y), BINS + 1).astype(int)
mn = [float(y[a:b].min()) for a, b in zip(edges[:-1], edges[1:])]
mx = [float(y[a:b].max()) for a, b in zip(edges[:-1], edges[1:])]
json.dump({"duracion_s": round(len(y)/SR, 3), "min": [round(v,3) for v in mn], "max": [round(v,3) for v in mx]},
          open(out, "w"), separators=(",", ":"))
print("ok", len(y)/SR, "s")
