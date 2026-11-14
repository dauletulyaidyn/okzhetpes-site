"""Build the separate, buildless light presentation. Run from any directory."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import json
import re
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'light'
OUT.mkdir(exist_ok=True)
DATA = [
 dict(id='almaty', city='Алматы', name='Almaty Resort', place='Казахстан · у подножия Алатау', photo='almaty-card.jpg', tagline='Термальная вода и современная медицина', intro='Клинический санаторий для обследования, санаторного лечения и восстановления рядом с Алматы.', features=['Собственный термальный источник', 'Диагностика и check-up', 'Грязелечение и реабилитация'], services=[('Санаторная путёвка', 'Проживание, питание и лечебный курс. Состав процедур и длительность подбираются с врачом.'), ('Обследование и восстановление', 'Консультации специалистов, функциональная и ультразвуковая диагностика, физиотерапия и лечебная физкультура.'), ('Термальный отдых', 'Термальный бассейн, водолечение, массаж и SPA. Доступность и условия посещения уточняет отдел бронирования.')], address='Казахстан, г. Алматы, ул. Альмерек, 1/1', phone='+7 778 499 66 42', wa='77784996642', email='reception.almatyresort@okzhetpes-esk.kz', source='https://almatyresort.kz/contacts/', route='Трансфер из аэропорта или с вокзала — по запросу.'),
 dict(id='burabay', city='Бурабай', name='«Окжетпес»', place='Казахстан · национальный парк Бурабай', photo='burabay-card.jpg', tagline='Сосновый бор, озеро и природные факторы', intro='Санаторное лечение и отдых на берегу озера Аулиеколь, среди сосен и скал Бурабая.', features=['Климатотерапия и минеральные воды', 'Грязелечение и кумысолечение', 'Бассейн, хамам и прогулки'], services=[('Санаторная путёвка', 'Проживание, диетическое питание и процедуры по назначению врача. Программу согласуют с учётом показаний.'), ('Лечение и оздоровление', 'Минеральные воды, грязи озера Балпаш-Сор, физиотерапия, кумысолечение и лечебная физкультура.'), ('Отдых и досуг', 'Бассейн, хамам, тренажёрный зал и прогулки в национальном парке. Условия включения в путёвку уточняются.')], address='Казахстан, Акмолинская область, Бурабайский район, посёлок Бурабай, санаторий «Окжетпес»', phone='+7 702 059 20 20', wa='77020592020', email='bron@okzhetpes-esk.kz', source='https://okzhetpes-burabay.kz/kontakty/', route='Варианты трансфера из Астаны и Кокшетау уточняйте при бронировании.'),
 dict(id='issyk-kul', city='Иссык-Куль', name='«Казахстан»', place='Кыргызстан · северный берег Иссык-Куля', photo=None, tagline='Озёрный курорт для отдыха и восстановления', intro='Курорт на северном берегу Иссык-Куля: горный воздух, проживание у озера и оздоровительная инфраструктура.', features=['Отдых у горного озера', 'Номера и коттеджи', 'Оздоровление и семейный отдых'], services=[('Путёвки и размещение', 'Номера и коттеджи для отдыха у озера. Категорию размещения, питание и даты заезда уточняет менеджер.'), ('Оздоровительные программы', 'Возможности медицинского блока и доступные процедуры необходимо согласовать перед поездкой.'), ('Семейный отдых', 'Отдых на территории курорта и прогулки у озера. Услуги и инфраструктура уточняются к открытию.')], address='Кыргызстан, Иссык-Кульская область, с. Бактуу-Долоноту, Кыргызская улица, 42/2', phone='+996 503 707 709', wa='996503707709', email='kazakhstanhealthresort@gmail.com', source='https://kazakhstanhealthresort.com/contacts/', route='Северный берег озера, 6 км к востоку от Чолпон-Аты. Трансфер — по запросу.', notice='Предварительные заявки · открытие заявлено на декабрь 2026 года'),
 dict(id='essentuki', city='Ессентуки', name='«Казахстан»', place='Россия · Кавказские Минеральные Воды', photo='essentuki-card.jpg', tagline='Минеральные воды и санаторное лечение', intro='Здравница в курортной зоне Ессентуков с лечебно-диагностической базой, диетическим питанием и парком.', features=['Питьевое лечение минеральными водами', 'Бальнеология и диагностика', 'Бассейн, парк и досуг'], services=[('Лечебные путёвки', 'Общетерапевтическая, «Премиум», «Оптима» и детская общетерапевтическая программы. Подбор — по показаниям.'), ('Оздоровление и выходные', 'Оздоровительная путёвка и тур выходного дня для короткой поездки. Состав услуг зависит от программы.'), ('Лечение и отдых', 'Питьевые курсы минеральной воды, бальнеология, диагностика, диетическое питание, бассейн и культурная программа.')], address='Россия, Ставропольский край, г. Ессентуки, ул. Пятигорская, 44', phone='+7 928 308 24 51', wa=None, email='san@kazakhstan-kmv.ru', source='https://kazakhstan-kmv.ru/contacts/', route='Ближайший аэропорт — Минеральные Воды. Далее — до Ессентуков; маршрут и трансфер уточняйте в санатории.'),
]

def image(d, cls=''):
    if d['photo']:
        return f'<img class="{cls}" src="../assets/photos/{d["photo"]}" alt="{e(d["name"])} — {d["city"]}" width="900" height="600">'
    return '<div class="lake '+cls+'" role="img" aria-label="Стилизованный пейзаж Иссык-Куля"><span>Иссык-Куль</span><small>Горный воздух · озёрный простор</small></div>'

def official_groups(rid):
    """Утверждённый прейскурант 2026 (tools/prices/<id>.py), если он есть."""
    import importlib.util
    f = ROOT / 'tools' / 'prices' / (rid + '.py')
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location('p_' + rid.replace('-', '_'), f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    D = m.DATA
    money = lambda v, c: None if v is None else f"{v:,}".replace(',', ' ') + ' ' + c
    groups = []
    for tab in D['tabs']:
        for g in tab['groups']:
            rows = []
            for name, unit, *pr in g['items']:
                if D.get('dual'):  # Ессентуки: руб. и тенге (руб. × 5)
                    rows.append((name, unit + (' · ' + money(pr[0] * 5, '₸') if pr[0] is not None else ''), money(pr[0], '₽')))
                elif g.get('cols'):
                    for col, v in zip(g['cols'], pr):
                        rows.append((name, unit + ' · ' + col, money(v, D['cur'])))
                else:
                    rows.append((name, unit, money(pr[0], D['cur'])))
            groups.append((g['g'], rows))
    return groups, D['src']

def catalog(d):
    """Reuse every catalog entry from the full site; never invent a tariff."""
    soup = BeautifulSoup((ROOT / (d['id']+'.html')).read_text(encoding='utf-8'), 'html.parser')
    currency = {'almaty':'₸', 'burabay':'₸', 'issyk-kul':'сом', 'essentuki':'₽'}[d['id']]
    off = official_groups(d['id'])
    if off:
        return render_catalog(d, off[0], currency, off[1])
    groups = []
    packs = []
    for pack in soup.select('.pack'):
        title = pack.select_one('h3')
        if not title:
            continue
        dur = pack.select_one('.dur')
        desc = [x.get_text(' ',strip=True) for x in pack.select('.ticks li, p.muted')]
        price = pack.select_one('.price')
        amount = ''.join(str(x) for x in price.find_all(string=True,recursive=False)).strip() if price else ''
        unit = price.select_one('small') if price else None
        note = ' · '.join(x for x in [dur.get_text(' ',strip=True) if dur else '',unit.get_text(' ',strip=True) if unit else '', '; '.join(desc)] if x)
        packs.append((title.get_text(' ',strip=True), note, amount if re.search(r'\d',amount) else None))
    if packs:
        groups.append(('Путёвки и программы', packs))
    for script in soup.select('script[id^="svc-"]'):
        for group in json.loads(script.string):
            rows=[]
            for item in group['items']:
                variants=group.get('cols', [''])
                for variant in variants:
                    note='Размещение '+variant+' · единица тарифа уточняется' if variant else ''
                    rows.append((item,note,None))
            groups.append((group['g'],rows))
    for table in soup.select('table.terms'):
        rows=[]
        for tr in table.select('tr'):
            cells=[td.get_text(' ',strip=True) for td in tr.select('td')]
            if not cells:
                continue
            amount=cells[-1] if re.search(r'\d.*[₽₸]',cells[-1]) else None
            note=' · '.join(cells[1:-1] if amount else cells[1:])
            if amount:
                note+=' · за сутки, от'
            rows.append((cells[0],note,amount))
        if rows:
            groups.append(('Проживание',rows))
    known={row[0].casefold() for _,rows in groups for row in rows}
    extra=[]
    for chip in soup.select('.feature .chip'):
        name=chip.get_text(' ',strip=True)
        if name.casefold() not in known:
            extra.append((name,'Доступность и включение в путёвку уточняются',None))
            known.add(name.casefold())
    if extra:
        groups.append(('Инфраструктура и дополнительные возможности',extra))
    return render_catalog(d, groups, currency, None)

def render_catalog(d, groups, currency, src):
    links=[]
    sections=[]
    for i,(name,rows) in enumerate(groups):
        anchor=f'category-{i+1}'
        links.append(f'<a href="#{anchor}">{e(name)}</a>')
        items=[]
        for title,note,amount in rows:
            price=e(amount) if amount else '____ '+currency
            status='published' if amount else 'unfilled'
            label=('Цена по прейскуранту' if src else 'Цена из полной презентации') if amount else 'Цена не заполнена'
            items.append(f'<li class="tariff-row"><div><span class="tariff-name">{e(title)}</span>'+ (f'<small>{e(note)}</small>' if note else '')+f'</div><span class="tariff-price {status}" aria-label="{label}: {price}">{price}</span></li>')
        sections.append(f'<section class="tariff-group" id="{anchor}"><h2>{e(name)}</h2><ul class="tariff-list">'+''.join(items)+'</ul><a class="to-categories" href="#catalog">К категориям ↑</a></section>')
    count=sum(len(rows) for _,rows in groups)
    print(d['id'],len(groups),'categories;',count,'price rows')
    return f'<section id="catalog" class="catalog"><span class="eyebrow">Услуги и цены · {count} позиций</span><h2>Выберите вид услуг</h2><p class="catalog-note">Красное поле «____ {currency}» — цена уточняется. Состав путёвки и отдельная оплата процедур уточняются при бронировании.</p>'+(f'<p class="catalog-note">{e(src)}</p>' if src else '')+'<nav class="category-nav" aria-label="Виды услуг">'+''.join(links)+'</nav><div class="tariff-groups">'+''.join(sections)+'</div></section>'

CORP_OUT = ROOT / 'corp'

def page(title, body, filename, step=1, corp=False):
    out, pre = (CORP_OUT, '../light/') if corp else (OUT, '')
    nav=''.join(f'<a href="{d["id"]}.html" '+('aria-current="page"' if filename.startswith(d['id']) else '')+f'>{d["city"]}</a>' for d in DATA)
    nav+=('<a href="../light/index.html">Гостям</a>' if corp else '<a href="../corp/index.html">Компаниям</a>')
    steps=('Выбор филиала','Предложения для компаний','Контакты') if corp else ('Выбор санатория','Услуги санатория','Контакты и расположение')
    warn='' if corp else '<p>Имеются противопоказания. Необходима консультация врача.</p>'
    brand_small='Корпоративным клиентам' if corp else 'Сеть здравниц'
    html=f'''<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{title} · Окжетпес</title><link rel="stylesheet" href="{pre}style.css?v=3"></head>
<body><a class="skip" href="#main">К содержанию</a><header><a class="brand" href="index.html"><b class="mark">О</b><span>Окжетпес<small>{brand_small}</small></span></a><nav aria-label="Филиалы">{nav}</nav><button id="fullscreen" type="button">На весь экран ↗</button></header>
<main id="main">{body}</main><footer><a href="index.html">Все филиалы</a><span class="steps">{steps[step-1]} · {step} / 3</span><a href="../index.html">Полная презентация ↗</a>{warn}</footer><script src="{pre}app.js?v=2"></script></body></html>'''
    out.mkdir(exist_ok=True)
    (out/filename).write_text(html, encoding='utf-8')

cards=''.join(f'<a class="resort" href="{d["id"]}.html">{image(d)}<div class="card-body"><span class="eyebrow">{d["city"]}</span><h2>{d["name"]}</h2><p>{d["tagline"]}</p><ul>'+''.join(f'<li>{x}</li>' for x in d['features'])+f'</ul><span class="card-link">Услуги и путёвки <b>↗</b></span></div></a>' for d in DATA)
page('Четыре направления для вашего здоровья', '<section class="intro"><span class="eyebrow">Лечение · восстановление · отдых</span><h1>Четыре курорта.<br><em>Одна забота о вас.</em></h1><p>Здравницы сети «Окжетпес» объединяют санаторное лечение, оздоровление и отдых. Выберите подходящий климат и познакомьтесь с возможностями каждого филиала.</p></section><section class="resorts" aria-label="Выберите санаторий">'+cards+'</section><a class="corp-banner" href="../corp/index.html"><span class="eyebrow">Компаниям и организациям</span><b>Конференц-залы, банкеты, командный отдых — цены в одном месте</b><span class="card-link">Версия для корпоративных клиентов <b>↗</b></span></a>', 'index.html')

for d in DATA:
    notice=f'<p class="notice">{d["notice"]}</p>' if d.get('notice') else ''
    services=''.join(f'<article class="service"><span class="number">0{i+1}</span><h2>{t}</h2><p>{text}</p></article>' for i,(t,text) in enumerate(d['services']))
    page(d['name']+' · '+d['city'],f'<a class="back" href="index.html">← Все четыре санатория</a><section class="resort-hero"><div><span class="eyebrow">{d["place"]}</span><h1>{d["name"]}<br><em>{d["city"]}</em></h1><p class="lead">{d["intro"]}</p>{notice}<div class="tags">'+''.join(f'<span>{x}</span>' for x in d['features'])+f'</div></div>{image(d,"hero-image")}</section>{catalog(d)}<div class="next"><p>Стоимость и состав путёвки уточняются при обращении.<br><small>Лечение и процедуры — по назначению врача.</small></p><a class="button" href="{d["id"]}-contacts.html">Контакты и расположение →</a></div>',d['id']+'.html',2)
    phone=''.join(c for c in d['phone'] if c.isdigit() or c=='+')
    maps='https://www.google.com/maps/search/?api=1&query='+quote(d['name']+' '+d['address'])
    whatsapp=f'<a class="button" href="https://wa.me/{d["wa"]}" target="_blank" rel="noopener">Написать в WhatsApp ↗</a>' if d['wa'] else f'<a class="button" href="mailto:{d["email"]}">Написать в санаторий ↗</a>'
    page('Контакты · '+d['city'],f'<a class="back" href="{d["id"]}.html">← Услуги и путёвки</a><section class="contact-title"><span class="eyebrow">Следующий шаг · {d["city"]}</span><h1>Спланируем<br><em>вашу поездку.</em></h1><p class="lead">{d["name"]}, {d["city"]}. Свяжитесь с санаторием, чтобы уточнить даты, наличие мест и состав путёвки.</p>{notice}</section><section class="contact-grid"><article class="contact"><span class="eyebrow">Бронирование</span><h2>Будем на связи</h2><a class="phone" href="tel:{phone}">{d["phone"]}</a><a class="email" href="mailto:{d["email"]}">{d["email"]}</a>{whatsapp}<p class="hint">Для подбора путёвки сообщите даты, количество гостей и пожелания к отдыху.</p></article><article class="location"><span class="eyebrow">Как нас найти</span><h2>{d["city"]}</h2><address>{d["address"]}</address><p>{d["route"]}</p><a class="button outline" href="{maps}" target="_blank" rel="noopener">Открыть на карте ↗</a><a class="source" href="{d["source"]}" target="_blank" rel="noopener">Контакты на официальном сайте ↗</a></article></section><p class="verified">Контакты сверены с официальным сайтом 10 ноября 2026 года.</p>',d['id']+'-contacts.html',3)
# ---------- Версия для корпоративных клиентов (corp/): те же 3 шага, по филиалам только то, что важно компаниям ----------
# (раздел, [(группа прейскуранта, фильтр строк: None = все, иначе функция по названию)])
has = lambda *w: (lambda n: any(x.casefold() in n.casefold() for x in w))
hasnt = lambda *w: (lambda n: not any(x.casefold() in n.casefold() for x in w))
CORP = {
 'almaty': [
  ('Проживание', [('Standart', has('Командировочный'))]),
  ('Конференц-залы и площадки', [('Залы и площадки', None)]),
  ('Кофе-брейки и банкеты', [('Кофе-брейки и питание гостей', None), ('Банкетные пакеты', None)]),
  ('Командный отдых', [('SPA-зона: финская и русская сауны, мини-бассейн', has('Группа', 'группа')), ('Досуг', has('Спортплощадка', 'Фотосессия'))]),
 ],
 'burabay': [
  ('Конференц-залы', [('Залы и мероприятия', hasnt('бракосочетание'))]),
  ('Питание группы', [('Питание отдыхающих (средняя стоимость)', has('Взрослый'))]),
  ('Командный отдых и трансфер', [('Активный отдых', None), ('Трансфер и прачечная', has('Трансфер'))]),
 ],
 'essentuki': [
  ('Проживание без лечения', [(g, hasnt('доп. место', 'ребёнок')) for g in ['Только проживание', 'Проживание + питание (без лечения)']]),
  ('Питание группы', [('Питание', has('Взрослый', 'Экспресс'))]),
  ('Командный отдых и трансфер', [('Досуг', has('командная', 'Аренда зала')), ('Трансфер и минеральная вода', has('трансфер'))]),
 ],
}
# Проживание без лечения есть не во всех прейскурантах — там, где его нет, только пометка
CORP_NOTE = {
 'almaty': 'Номера по прейскуранту продаются как путёвки с лечением; для командировок — тариф «Командировочный». Проживание групп без лечения — по запросу.',
 'burabay': 'Номера по прейскуранту продаются как путёвки с лечением. Проживание групп без лечения — по запросу.',
}
CORP_CUR = {'almaty': '₸', 'burabay': '₸', 'essentuki': '₽'}

def corp_row(title, note, amount):
    price = e(amount) if amount else '____ ' + CORP_CUR_NOW
    status = 'published' if amount else 'unfilled'
    return f'<li class="tariff-row"><div><span class="tariff-name">{e(title)}</span>' + (f'<small>{e(note)}</small>' if note else '') + f'</div><span class="tariff-price {status}">{price}</span></li>'

def corp_catalog(d):
    global CORP_CUR_NOW
    rid = d['id']
    if rid not in CORP:
        return '<section id="catalog" class="catalog"><span class="eyebrow">Для компаний</span><h2>Предварительные заявки</h2><p class="catalog-note">Филиал открывается в 2026 году. Принимаем предварительные заявки на выездные мероприятия и размещение групп; цены по запросу.</p></section>', 0
    CORP_CUR_NOW = CORP_CUR[rid]
    groups = dict(official_groups(rid)[0])
    blocks, links, total = [], [], 0
    for i, (title, parts) in enumerate(CORP[rid]):
        anchor = f'category-{i+1}'
        body = []
        for gname, flt in parts:
            rows = [r for r in groups[gname] if flt is None or flt(r[0])]
            total += len(rows)
            if len(parts) > 1:
                body.append(f'<li class="tariff-sub">{e(gname)}</li>')
            body += [corp_row(*r) for r in rows]
        links.append(f'<a href="#{anchor}">{e(title)}</a>')
        blocks.append(f'<section class="tariff-group" id="{anchor}"><h2>{e(title)}</h2><ul class="tariff-list">' + ''.join(body) + '</ul><a class="to-categories" href="#catalog">К разделам ↑</a></section>')
    note = f'<p class="catalog-note">{CORP_NOTE[rid]}</p>' if rid in CORP_NOTE else ''
    html = (f'<section id="catalog" class="catalog"><span class="eyebrow">Для компаний · {total} позиций</span><h2>Выберите раздел</h2>'
            f'<p class="catalog-note">Цены по прейскуранту 2026. Красное поле «____ {CORP_CUR_NOW}» — цена уточняется. Условия договора и скидки за объём — индивидуально.</p>{note}'
            '<nav class="category-nav" aria-label="Разделы">' + ''.join(links) + '</nav><div class="tariff-groups">' + ''.join(blocks) + '</div></section>')
    return html, total

def corp_features(d):
    return [t for t, _ in CORP[d['id']]] if d['id'] in CORP else ['Выездные мероприятия', 'Размещение групп', 'Предварительные заявки']

corp_total = 0
cards = ''.join(f'<a class="resort" href="{d["id"]}.html">{image(d)}<div class="card-body"><span class="eyebrow">{d["city"]}</span><h2>{d["name"]}</h2><ul>' + ''.join(f'<li>{x}</li>' for x in corp_features(d)) + '</ul><span class="card-link">Предложения для компаний <b>↗</b></span></div></a>' for d in DATA)
page('Корпоративным клиентам', '<section class="intro"><span class="eyebrow">Компаниям и организациям</span><h1>Четыре филиала.<br><em>Для вашей команды.</em></h1><p>Конференц-залы, кофе-брейки и банкеты, питание групп, командный отдых, трансфер и проживание. Выберите филиал — покажем только то, что нужно компаниям, с ценами по прейскуранту 2026.</p></section><section class="resorts" aria-label="Выберите филиал">' + cards + '</section>', 'index.html', 1, corp=True)
for d in DATA:
    cat, n = corp_catalog(d)
    corp_total += n
    page(d['name'] + ' · ' + d['city'] + ' · Компаниям', f'<a class="back" href="index.html">← Все филиалы</a><section class="resort-hero"><div><span class="eyebrow">{d["place"]}</span><h1>{d["name"]}<br><em>{d["city"]}</em></h1><p class="lead">Для компаний: ' + ', '.join(x.lower() for x in corp_features(d)) + '.</p><div class="tags">' + ''.join(f'<span>{x}</span>' for x in corp_features(d)) + f'</div></div>{image(d, "hero-image")}</section>{cat}<div class="next"><p>Сообщите даты, количество участников и формат — подготовим предложение.</p><a class="button" href="{d["id"]}-contacts.html">Контакты →</a></div>', d['id'] + '.html', 2, corp=True)
    phone = ''.join(c for c in d['phone'] if c.isdigit() or c == '+')
    maps = 'https://www.google.com/maps/search/?api=1&query=' + quote(d['name'] + ' ' + d['address'])
    whatsapp = f'<a class="button" href="https://wa.me/{d["wa"]}" target="_blank" rel="noopener">Написать в WhatsApp ↗</a>' if d['wa'] else f'<a class="button" href="mailto:{d["email"]}">Написать в филиал ↗</a>'
    page('Контакты · ' + d['city'] + ' · Компаниям', f'<a class="back" href="{d["id"]}.html">← Предложения для компаний</a><section class="contact-title"><span class="eyebrow">Следующий шаг · {d["city"]}</span><h1>Обсудим<br><em>ваше мероприятие.</em></h1><p class="lead">{d["name"]}, {d["city"]}. Свяжитесь с филиалом, чтобы уточнить даты, количество участников и формат.</p></section><section class="contact-grid"><article class="contact"><span class="eyebrow">Корпоративные заявки</span><h2>Будем на связи</h2><a class="phone" href="tel:{phone}">{d["phone"]}</a><a class="email" href="mailto:{d["email"]}">{d["email"]}</a>{whatsapp}<p class="hint">Для предложения сообщите компанию, даты, количество участников и что нужно: зал, питание, проживание, трансфер.</p></article><article class="location"><span class="eyebrow">Как нас найти</span><h2>{d["city"]}</h2><address>{d["address"]}</address><p>{d["route"]}</p><a class="button outline" href="{maps}" target="_blank" rel="noopener">Открыть на карте ↗</a><a class="source" href="{d["source"]}" target="_blank" rel="noopener">Контакты на официальном сайте ↗</a></article></section>', d['id'] + '-contacts.html', 3, corp=True)
print('corp:', corp_total, 'price rows')
print('Built light/ (9 pages) and corp/ (9 pages)')
