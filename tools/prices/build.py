"""Собирает assets/prices/<id>.js из tools/prices/<id>.py.
Запуск из корня сайта: python tools/prices/build.py"""
import importlib.util, json
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent.parent / "assets" / "prices"
OUT.mkdir(parents=True, exist_ok=True)

for rid in ["almaty", "burabay", "essentuki"]:
    spec = importlib.util.spec_from_file_location(rid, HERE / f"{rid}.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    d = mod.DATA
    total = empty = 0
    for tab in d["tabs"]:
        for g in tab["groups"]:
            if d.get("dual"):  # Ессентуки: руб. + тенге (руб. × 5 по прейскуранту)
                g["cols"], g["curs"] = ["руб.", "тенге"], ["₽", "₸"]
                g["items"] = [[n, u, p, (p * 5 if p is not None else None)] for n, u, p in g["items"]]
            for it in g["items"]:
                total += 1
                empty += any(v is None for v in it[2:])
    d.pop("dual", None)
    js = f"window.PRICES=window.PRICES||{{}};window.PRICES[{json.dumps(rid)}]={json.dumps(d, ensure_ascii=False, separators=(',', ':'))};\n"
    (OUT / f"{rid}.js").write_text(js, encoding="utf-8")
    print(f"{rid}: позиций {total}, без цены {empty}")
