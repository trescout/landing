/* TreScout · rapor sayfaları · nav scroll state · önceden inline'dı · CSP için harici */
(function(){var n=document.querySelector('nav');if(!n)return;function s(){n.classList.toggle('scrolled',window.scrollY>8);}window.addEventListener('scroll',s,{passive:true});s();})();
