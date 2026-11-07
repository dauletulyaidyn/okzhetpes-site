"""Достаёт фотографии из презентаций (PPTX) и PDF в папку assets/photos/_inbox/.

Запуск: python tools/extract_photos.py "<папка с презентациями>"
Тексты документов не читаются и никуда не передаются — только картинки, крупнее 600 px по ширине.
Дальше нужные фото переименовываются по слотам сайта (см. README.md) и кладутся в assets/photos/.
"""
import sys
import zipfile
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "photos" / "_inbox"
MIN_W = 600


def from_pptx(p: Path, out: Path):
    n = 0
    with zipfile.ZipFile(p) as z:
        for name in z.namelist():
            if name.startswith("ppt/media/") and name.lower().endswith((".jpg", ".jpeg", ".png")):
                data = z.read(name)
                if len(data) < 60_000:  # мелкие иконки и логотипы пропускаем
                    continue
                (out / f"{p.stem[:30]}_{Path(name).name}").write_bytes(data)
                n += 1
    return n


def from_pdf(p: Path, out: Path):
    import fitz  # PyMuPDF
    n = 0
    doc = fitz.open(str(p))
    for page in doc:
        for img in page.get_images(full=True):
            pix = fitz.Pixmap(doc, img[0])
            if pix.width < MIN_W:
                continue
            if pix.n - pix.alpha >= 4:
                pix = fitz.Pixmap(fitz.csRGB, pix)
            n += 1
            pix.save(str(out / f"{p.stem[:30]}_p{page.number + 1}_{n}.png"))
    return n


def main():
    src = Path(sys.argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    total = 0
    for p in sorted(src.iterdir()):
        ext = p.suffix.lower()
        if ext == ".pptx":
            total += from_pptx(p, OUT)
        elif ext == ".pdf":
            total += from_pdf(p, OUT)
    print(f"Извлечено изображений: {total} → {OUT}")


if __name__ == "__main__":
    main()
