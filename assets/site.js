/* Общие элементы сайта: шапка, подвал, иллюстрации, вкладки, форма заявки. */
const CONFIG = {
  // Номер, на который уходят заявки из формы (WhatsApp). ЗАПОЛНИТЬ перед запуском.
  leadWhatsApp: "77017436433",
  phones: {
    almaty: ["+7 727 300 34 00", "+7 701 743 64 33"],
    burabay: ["[телефон отдела бронирования]"],
    issykkul: ["[телефон отдела бронирования]"],
  },
};

const PAGES = [
  ["index.html", "О сети"],
  ["almaty.html", "Алматы"],
  ["burabay.html", "Бурабай"],
  ["issyk-kul.html", "Иссык-Куль"],
  ["clients.html", "Клиентам"],
  ["corporate.html", "Корпоративным"],
];

function header() {
  const here = location.pathname.split("/").pop() || "index.html";
  const links = PAGES.map(([h, t]) => `<a href="${h}" class="${h === here ? "on" : ""}">${t}</a>`).join("");
  return `
  <div class="draft">Черновик для согласования · цены и условия требуют утверждения</div>
  <header class="top"><div class="wrap">
    <a class="brand" href="index.html"><span class="brand-mark">О</span>
      <span><b>Окжетпес</b><small>Сеть здравниц</small></span></a>
    <nav class="nav" id="nav">${links}</nav>
    <button class="burger" onclick="document.getElementById('nav').classList.toggle('open')">Меню</button>
    <a class="btn btn-primary" href="#lead">Подобрать программу</a>
  </div></header>`;
}

function footer() {
  return `
  <footer><div class="wrap">
    <div class="cols">
      <div><h4>АО «ЛОК «Окжетпес»</h4>
        <p>Сеть санаториев: Алматы, Бурабай, Иссык-Куль. Лечение, восстановление и отдых круглый год.</p></div>
      <div><h4>Здравницы</h4>
        <a href="almaty.html">Almaty Resort, Алматы</a><a href="burabay.html">«Окжетпес», Бурабай</a><a href="issyk-kul.html">«Казахстан», Иссык-Куль</a></div>
      <div><h4>Клиентам</h4>
        <a href="clients.html#seg-individual">Гостям и семьям</a><a href="corporate.html">Корпоративным клиентам</a>
        <a href="clients.html#seg-gov">Государственным организациям</a><a href="clients.html#seg-benefit">Льготным категориям</a>
        <a href="clients.html#seg-foreign">Иностранным гостям</a></div>
      <div><h4>Бронирование</h4>
        <a href="tel:${CONFIG.phones.almaty[0].replace(/\s/g, "")}">Алматы: ${CONFIG.phones.almaty[0]}</a>
        <a href="#lead">Оставить заявку</a></div>
    </div>
    <div class="legal"><span>© АО «ЛОК «Окжетпес», ${new Date().getFullYear()}</span>
      <span>Имеются противопоказания. Необходима консультация врача.</span></div>
  </div></footer>
  <a class="float-cta" href="https://wa.me/${CONFIG.leadWhatsApp}" target="_blank" rel="noopener">WhatsApp</a>`;
}

/* ---------- Иллюстрации-заглушки (пока нет фото) ---------- */
const ART = {
  almaty: `<svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice"><defs>
    <linearGradient id="a1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9cc7d9"/><stop offset=".6" stop-color="#e9d9bd"/><stop offset="1" stop-color="#d9b98a"/></linearGradient></defs>
    <rect width="800" height="600" fill="url(#a1)"/><circle cx="610" cy="150" r="54" fill="#fff4dc" opacity=".9"/>
    <path d="M0 380 L120 210 L190 290 L300 120 L410 270 L480 200 L600 330 L700 230 L800 320 V600 H0Z" fill="#7d9aa8"/>
    <path d="M300 120 L340 175 L318 168 L300 190 L282 165 L262 172Z M120 210 L148 250 L126 244 L110 262Z M700 230 L728 268 L705 262Z" fill="#fff"/>
    <path d="M0 440 L140 330 L260 400 L380 300 L520 410 L640 340 L800 420 V600 H0Z" fill="#4f7468"/>
    <path d="M0 500 Q200 440 400 490 T800 470 V600 H0Z" fill="#2f5a4b"/>
    <path d="M0 560 Q260 520 520 560 T800 545 V600 H0Z" fill="#1f4337"/></svg>`,
  burabay: `<svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice"><defs>
    <linearGradient id="b1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#bcd8e4"/><stop offset="1" stop-color="#f1e6cf"/></linearGradient>
    <linearGradient id="b2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5f93a3"/><stop offset="1" stop-color="#2f5f6c"/></linearGradient></defs>
    <rect width="800" height="600" fill="url(#b1)"/>
    <path d="M420 360 C430 250 470 170 520 150 C560 140 600 190 610 260 C620 300 650 330 700 360Z" fill="#8a8f84"/>
    <path d="M470 360 C480 290 505 230 530 215 C550 210 570 250 575 300 L590 360Z" fill="#a5a89b"/>
    <path d="M0 330 L60 280 L90 300 L150 250 L200 290 L260 260 L320 310 L380 290 L430 360 H0Z" fill="#3c6b55"/>
    <rect y="355" width="800" height="245" fill="url(#b2)"/>
    <path d="M330 420 C335 395 350 380 362 382 C375 384 380 405 382 425Z" fill="#7d8379"/>
    <g fill="#1d3f33">${[20, 70, 110, 690, 740, 780].map((x, i) => `<path d="M${x} ${600 - 0} L${x - 30} 600 L${x} ${330 + (i % 3) * 30} L${x + 30} 600Z"/>`).join("")}</g>
    <path d="M0 470 Q200 455 400 470 T800 465" stroke="#cfe4ea" stroke-width="3" fill="none" opacity=".5"/></svg>`,
  issykkul: `<svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice"><defs>
    <linearGradient id="i1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d0e2"/><stop offset="1" stop-color="#eef3f0"/></linearGradient>
    <linearGradient id="i2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f9db2"/><stop offset="1" stop-color="#1e5f76"/></linearGradient></defs>
    <rect width="800" height="600" fill="url(#i1)"/>
    <path d="M0 330 L90 230 L150 280 L250 160 L340 260 L420 190 L520 280 L620 170 L700 250 L800 210 V360 H0Z" fill="#8fa6b4"/>
    <path d="M250 160 L285 205 L262 200 L248 218 L232 198 L215 204Z M620 170 L650 210 L630 205 L612 222 L598 204Z M420 190 L445 222 L425 218Z" fill="#fff"/>
    <path d="M0 350 L120 300 L240 340 L380 305 L520 345 L660 300 L800 340 V370 H0Z" fill="#6f8f8a"/>
    <rect y="365" width="800" height="235" fill="url(#i2)"/>
    <path d="M0 410 Q200 398 400 410 T800 405" stroke="#d6eef3" stroke-width="3" fill="none" opacity=".55"/>
    <path d="M0 470 Q200 458 400 470 T800 465" stroke="#d6eef3" stroke-width="2" fill="none" opacity=".35"/>
    <path d="M0 560 Q260 530 520 555 T800 545 V600 H0Z" fill="#e7d6b2"/></svg>`,
  spa: `<svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice">
    <rect width="800" height="600" fill="#e8efe9"/><rect y="330" width="800" height="270" fill="#9ccbc9"/>
    <path d="M0 360 Q200 340 400 360 T800 355" stroke="#e5f4f2" stroke-width="5" fill="none"/>
    <path d="M0 420 Q200 400 400 420 T800 415" stroke="#e5f4f2" stroke-width="4" fill="none" opacity=".7"/>
    <g fill="none" stroke="#c9a46a" stroke-width="5" opacity=".7"><path d="M300 300 q-20 -40 0 -80 q20 -40 0 -80"/><path d="M400 300 q-20 -40 0 -80 q20 -40 0 -80"/><path d="M500 300 q-20 -40 0 -80 q20 -40 0 -80"/></g></svg>`,
  care: `<svg viewBox="0 0 800 600" preserveAspectRatio="xMidYMid slice">
    <rect width="800" height="600" fill="#f1ece2"/><circle cx="400" cy="300" r="190" fill="#e3d3b4"/>
    <path d="M400 410 C300 340 260 280 300 230 C335 190 385 210 400 245 C415 210 465 190 500 230 C540 280 500 340 400 410Z" fill="#1f4d3f"/>
    <path d="M330 300 H370 L385 270 L405 330 L420 300 H470" stroke="#e9d6b0" stroke-width="8" fill="none" stroke-linejoin="round" stroke-linecap="round"/></svg>`,
};

function mountArt() {
  document.querySelectorAll("[data-art]").forEach(el => { el.innerHTML = ART[el.dataset.art] || ""; });
  // Фото подставляются, только если файл реально существует
  document.querySelectorAll("[data-photo]").forEach(el => {
    const img = new Image();
    img.onload = () => el.style.setProperty("--img", `url("${el.dataset.photo}")`);
    img.src = el.dataset.photo;
  });
}

/* ---------- Вкладки сегментов ---------- */
function mountTabs() {
  document.querySelectorAll("[data-tabs]").forEach(box => {
    const btns = box.querySelectorAll(".seg-tabs button");
    const show = id => {
      btns.forEach(b => b.classList.toggle("on", b.dataset.seg === id));
      box.querySelectorAll(".seg").forEach(s => s.classList.toggle("on", s.id === id));
    };
    btns.forEach(b => b.addEventListener("click", () => { show(b.dataset.seg); history.replaceState(null, "", "#" + b.dataset.seg); }));
    const fromHash = location.hash.slice(1);
    show(box.querySelector("#" + CSS.escape(fromHash)) ? fromHash : btns[0].dataset.seg);
    if (fromHash && box.querySelector("#" + CSS.escape(fromHash))) box.scrollIntoView();
  });
}

/* ---------- Блок заявки (одинаковый на всех страницах) ---------- */
function leadBlock(resort, who) {
  const opt = (list, sel) => list.map(x => `<option${x === sel ? " selected" : ""}>${x}</option>`).join("");
  return `
  <section class="dark" id="lead"><div class="wrap grid-2">
    <div class="rv">
      <span class="eyebrow">Заявка</span>
      <h2>Подберём программу за один звонок</h2>
      <p class="lead">Расскажите, кто едет и с какой целью. Менеджер предложит здравницу, программу лечения, даты и условия — для одного гостя, семьи или всего коллектива.</p>
      <ul class="ticks">
        <li>Ответ в рабочее время в течение часа</li>
        <li>Персональный менеджер для организаций</li>
        <li>Коммерческое предложение и договор под ваши условия</li>
      </ul>
    </div>
    <form class="lead-form rv">
      <h3>Оставить заявку</h3>
      <div class="row2">
        <div class="fld"><label>Имя</label><input name="Имя" required></div>
        <div class="fld"><label>Телефон</label><input name="Телефон" type="tel" required></div>
      </div>
      <div class="row2">
        <div class="fld"><label>Кто вы</label><select name="Тип клиента">${opt(["Частный гость / семья", "Компания", "Государственная организация", "Льготная категория", "Иностранный гость", "Группа / мероприятие"], who)}</select></div>
        <div class="fld"><label>Здравница</label><select name="Здравница">${opt(["Пока не знаю — посоветуйте", "Алматы", "Бурабай", "Иссык-Куль", "Несколько / маршрут"], resort)}</select></div>
      </div>
      <div class="row2">
        <div class="fld"><label>Сколько человек</label><input name="Количество" type="number" min="1" value="1"></div>
        <div class="fld"><label>Желаемые даты</label><input name="Даты" placeholder="например, март, 10 дней"></div>
      </div>
      <div class="fld"><label>Цель поездки, пожелания</label><textarea name="Комментарий" rows="3" placeholder="лечение суставов, check-up, отдых, корпоративная программа…"></textarea></div>
      <button class="btn btn-primary" type="submit">Отправить в WhatsApp</button>
      <div class="form-note">Нажимая кнопку, вы соглашаетесь на обработку персональных данных для ответа на заявку.</div>
    </form>
  </div></section>`;
}

/* ---------- Форма заявки: без сервера, уходит в WhatsApp ---------- */
function mountForms() {
  const slot = document.getElementById("lead-slot");
  if (slot) slot.outerHTML = leadBlock(slot.dataset.resort, slot.dataset.who);
  document.querySelectorAll("form.lead-form").forEach(f => {
    f.addEventListener("submit", e => {
      e.preventDefault();
      const d = new FormData(f);
      const lines = ["Заявка с сайта"];
      for (const [k, v] of d.entries()) if (String(v).trim()) lines.push(`${k}: ${v}`);
      window.open(`https://wa.me/${CONFIG.leadWhatsApp}?text=${encodeURIComponent(lines.join("\n"))}`, "_blank", "noopener");
    });
  });
}

function mountReveal() {
  const io = new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }), { threshold: .12 });
  document.querySelectorAll(".rv").forEach(el => io.observe(el));
}

/* ---------- Перечень услуг с пустыми (красными) ценами ---------- */
function mountServices() {
  document.querySelectorAll("[data-services]").forEach(box => {
    const data = JSON.parse(document.getElementById(box.dataset.services).textContent);
    let empty = 0, total = 0;
    const html = data.map(g => {
      const cols = g.cols || ["Цена"];
      const head = cols.length > 1 ? `<div class="svc-cols-head">${cols.map(c => `<span>${c}</span>`).join("")}</div>` : "";
      const rows = g.items.map(it => {
        total += 1;
        const cells = cols.map(() => { empty += 1; return `<span class="pr empty" title="Цена не заполнена">____ ₸</span>`; }).join("");
        return `<div class="svc-row"><span class="nm">${it}</span>${cells}</div>`;
      }).join("");
      return `<div class="svc-group"><h4>${g.g}${g.note ? ` <small>${g.note}</small>` : ""}</h4>${head}${rows}</div>`;
    }).join("");
    box.innerHTML = html;
    const cnt = document.querySelector(`[data-count-for="${box.dataset.services}"]`);
    if (cnt) cnt.innerHTML = `Услуг: <b style="color:var(--ink)">${total}</b> · цен не заполнено: <b>${empty}</b>`;
  });
}

/* ---------- Режим презентации: один жест = один блок ---------- */
function mountSlides() {
  const wide = () => matchMedia("(min-width: 900px) and (min-height: 620px)").matches;
  const slides = () => [...document.querySelectorAll("body > section")];
  const HEAD = 0;
  const dots = document.createElement("nav");
  dots.className = "dots";
  slides().forEach((s, i) => {
    const b = document.createElement("button");
    b.title = (s.querySelector("h1, h2")?.textContent || "").trim();
    b.addEventListener("click", () => go(i));
    dots.appendChild(b);
  });
  document.body.appendChild(dots);

  const current = () => {
    const y = window.scrollY + HEAD + 4;
    let idx = 0;
    slides().forEach((s, i) => { if (s.offsetTop <= y) idx = i; });
    return idx;
  };
  let lock = false;
  function go(i) {
    const list = slides();
    if (i < 0) return;
    lock = true;
    if (i >= list.length) document.querySelector("footer").scrollIntoView({ behavior: "smooth", block: "end" });
    else window.scrollTo({ top: list[i].offsetTop - HEAD, behavior: "smooth" });
    setTimeout(() => { lock = false; }, 850);
  }
  // можно ли листать внутри текущего блока (если он выше экрана)
  function innerRoom(dir) {
    const s = slides()[current()];
    if (!s) return false;
    const top = s.offsetTop - HEAD, bottom = s.offsetTop + s.offsetHeight;
    const viewTop = window.scrollY, viewBottom = window.scrollY + window.innerHeight;
    return dir > 0 ? bottom - viewBottom > 8 : viewTop - top > 8;
  }
  function step(dir) {
    const atFooter = window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 4;
    if (dir < 0 && atFooter) return go(slides().length - 1);
    go(current() + dir);
  }
  window.addEventListener("wheel", e => {
    if (!wide() || e.ctrlKey || Math.abs(e.deltaY) < 4) return;
    if (e.target.closest("textarea, select, .terms")) return;
    const dir = e.deltaY > 0 ? 1 : -1;
    if (innerRoom(dir)) return;          // сначала долистываем длинный блок
    e.preventDefault();
    if (!lock) step(dir);
  }, { passive: false });
  window.addEventListener("keydown", e => {
    if (!wide() || e.target.closest("input, textarea, select")) return;
    const k = { ArrowDown: 1, PageDown: 1, " ": 1, ArrowUp: -1, PageUp: -1 }[e.key];
    if (!k) return;
    if (innerRoom(k)) return;
    e.preventDefault();
    if (!lock) step(k);
  });
  const paint = () => {
    const i = current(), list = slides();
    [...dots.children].forEach((b, j) => b.classList.toggle("on", j === i));
    const s = list[i];
    dots.classList.toggle("light", !!s && (s.classList.contains("hero") || s.classList.contains("dark")));
  };
  window.addEventListener("scroll", paint, { passive: true });
  paint();
}

/* ---------- Шапка темнеет при прокрутке; бегущая строка на первом экране ---------- */
function mountChrome() {
  const top = document.querySelector(".top");
  const onScroll = () => top.classList.toggle("solid", window.scrollY > 40);
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  const hero = document.querySelector("body > section.hero");
  if (hero && !hero.classList.contains("short")) {
    const words = ["Алматы", "Бурабай", "Иссык-Куль", "Лечение", "Восстановление", "Тишина", "Горный воздух", "Термальные воды"];
    const line = words.map(w => `<span>${w}</span><i>✦</i>`).join("");
    const m = document.createElement("div");
    m.className = "marquee";
    m.innerHTML = `<div>${line}${line}</div>`;
    hero.appendChild(m);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("site-header").outerHTML = header();
  document.getElementById("site-footer").outerHTML = footer();
  mountChrome(); mountArt(); mountServices(); mountTabs(); mountForms(); mountReveal(); mountSlides();
});
