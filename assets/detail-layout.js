/* Progressive detail layout: move existing nodes, retaining forms and handlers. */
(function () {
  var article = document.querySelector('main > article.disc');
  if (!article || article.querySelector('.detail-shell')) return;
  var cta = article.querySelector(':scope > aside.disc-cta');
  if (!cta || !cta.querySelector('form.js-subscribe')) return;
  var submit = cta.querySelector('button[type="submit"]');
  if (!submit) return;
  var copy = {
    tr: ['Haberdar olun', 'Erken erişim başladığında haberdar olmak için listeye katılabilirsiniz.', 'Listeye katılın'],
    en: ['Stay informed', 'Join the list to hear when early access opens.', 'Join the list'],
    fr: ['Restez informés', "Inscrivez-vous pour être averti de l'ouverture de l'accès anticipé.", 'Rejoindre la liste'],
    pt: ['Fique por dentro', 'Entre na lista para saber quando o acesso antecipado abrir.', 'Entrar na lista'],
    es: ['Manténgase al día', 'Únase a la lista para saber cuándo se abre el acceso anticipado.', 'Unirse a la lista'],
    de: ['Bleiben Sie informiert', 'Tragen Sie sich ein, um zu erfahren, wann der Vorabzugang öffnet.', 'Eintragen']
  };
  var text = copy[(document.documentElement.lang || 'tr').split('-')[0]] || copy.tr;
  var shell = document.createElement('div'); shell.className = 'detail-shell';
  var reading = document.createElement('div'); reading.className = 'detail-reading';
  var sidebar = document.createElement('aside'); sidebar.className = 'detail-sidebar';
  var nodes = Array.from(article.childNodes);
  var links = [], facts = [], related = [];
  nodes.forEach(function (node) {
    if (node === cta) return;
    if (node.nodeType !== 1) { reading.append(node); return; }
    if (node.matches('section.disc-sec') && node.querySelector('.disc-links')) links.push(node);
    else if (node.matches('.disc-facts')) facts.push(node);
    else if (node.matches('section.disc-sec') && node.querySelector('.dict-related, .disc-related')) related.push(node);
    else reading.append(node);
  });
  sidebar.append.apply(sidebar, links.concat(facts, related));
  var heading = document.createElement('h2'); heading.textContent = text[0];
  var intro = cta.querySelector(':scope > p');
  if (intro) { intro.textContent = text[1]; cta.insertBefore(heading, intro); }
  else cta.prepend(heading);
  submit.textContent = text[2];
  var email = cta.querySelector('input[type="email"]');
  if (email && !email.labels.length && !email.hasAttribute('aria-label')) email.setAttribute('aria-label', email.placeholder);
  sidebar.append(cta);
  shell.append(reading, sidebar);
  article.append(shell);
})();
