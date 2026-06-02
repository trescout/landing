/* TreScout · /discover · komut "Kopyala" butonu · CSP-temiz (harici, inline yok). */
(function () {
  document.querySelectorAll('.disc-copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var box = btn.closest('.disc-cmd');
      var code = box && box.querySelector('code');
      if (!code || !navigator.clipboard) return;
      navigator.clipboard.writeText(code.textContent.trim()).then(function () {
        var prev = btn.textContent;
        btn.textContent = 'Kopyalandı ✓';
        setTimeout(function () { btn.textContent = prev; }, 1500);
      }).catch(function () {});
    });
  });
})();
