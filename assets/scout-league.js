/**
 * TreScout · Açık Kaynak Fantasy Borsa & Scout Ligi (Fantasy League Engine)
 * =========================================================================
 * Geliştiricilere sanal 1.000 TreScout puanı ile açık kaynak projelere
 * yatırım yapma, portföy yönetme ve "En İyi Teknoloji Avcısı" liginde
 * yarışma imkanı sunan oyunlaştırma (gamification) motoru.
 */

(function () {
  'use strict';

  var STORAGE_KEY = 'trescout_scout_league_v1';
  var INITIAL_BALANCE = 1000;

  function loadGameState() {
    try {
      var data = localStorage.getItem(STORAGE_KEY);
      if (data) return JSON.parse(data);
    } catch (e) {}

    return {
      balance: INITIAL_BALANCE,
      portfolio: {},
      history: []
    };
  }

  function saveGameState(state) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {}
  }

  function getRank(score) {
    if (score >= 5000) return { title: '🦄 Unicorn Hunter', color: '#8B5CF6' };
    if (score >= 2500) return { title: '🏆 Master Scout', color: '#F59E0B' };
    if (score >= 1500) return { title: '⭐ Senior Scout', color: '#3B82F6' };
    return { title: '🌱 Junior Scout', color: '#10B981' };
  }

  function calculateTotalNetWorth(state, currentStarsMap) {
    var total = state.balance;
    Object.keys(state.portfolio).forEach(function (slug) {
      var item = state.portfolio[slug];
      var currentStars = (currentStarsMap && currentStarsMap[slug]) || item.boughtAtStars;
      var growthRatio = currentStars / Math.max(item.boughtAtStars, 1);
      var currentValue = Math.round(item.investedCoins * growthRatio);
      total += currentValue;
    });
    return total;
  }

  function renderLeagueUI(container) {
    var state = loadGameState();
    var netWorth = calculateTotalNetWorth(state);
    var rank = getRank(netWorth);

    var portfolioItemsHtml = '';
    var portfolioKeys = Object.keys(state.portfolio);

    if (portfolioKeys.length === 0) {
      portfolioItemsHtml = '<p class="sl-empty">Henüz hiçbir açık kaynak projeye yatırım yapmadınız. Aşağıdan gelecek vadeden projelere puan yatırın!</p>';
    } else {
      portfolioKeys.forEach(function (slug) {
        var item = state.portfolio[slug];
        portfolioItemsHtml += [
          '<div class="sl-item">',
          '  <div class="sl-item-info">',
          '    <strong>' + item.title + '</strong>',
          '    <small>Alış: ★ ' + item.boughtAtStars.toLocaleString() + ' · Yatırım: ' + item.investedCoins + ' Puan</small>',
          '  </div>',
          '  <button type="button" class="btn btn-ghost sl-btn-sell" data-slug="' + slug + '">Sat & Karı Al</button>',
          '</div>'
        ].join('\n');
      });
    }

    container.innerHTML = [
      '<div class="sl-wrap">',
      '  <div class="sl-header">',
      '    <div class="sl-profile">',
      '      <span class="sl-rank-badge" style="background:' + rank.color + '20; color:' + rank.color + '; border:1px solid ' + rank.color + '40;">' + rank.title + '</span>',
      '      <h3 class="sl-title">🎮 TreScout Açık Kaynak Scout Ligi</h3>',
      '    </div>',
      '    <div class="sl-stats">',
      '      <div class="sl-stat"><span class="sl-stat-val">🪙 ' + state.balance.toLocaleString() + '</span><span class="sl-stat-label">Nakit Bakiye</span></div>',
      '      <div class="sl-stat"><span class="sl-stat-val">📈 ' + netWorth.toLocaleString() + '</span><span class="sl-stat-label">Toplam Varlık</span></div>',
      '    </div>',
      '  </div>',
      '  <div class="sl-portfolio">',
      '    <h4>📁 Aktif Portföyünüz (' + portfolioKeys.length + ' Proje)</h4>',
      '    <div class="sl-portfolio-list">' + portfolioItemsHtml + '</div>',
      '  </div>',
      '</div>'
    ].join('\n');

    // Sell buttons
    var sellBtns = container.querySelectorAll('.sl-btn-sell');
    sellBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var slug = btn.getAttribute('data-slug');
        var item = state.portfolio[slug];
        if (item) {
          // Satış simülasyonu (rastgele %5-25 organik yıldız primi)
          var profitMultiplier = 1 + (Math.random() * 0.2);
          var payout = Math.round(item.investedCoins * profitMultiplier);
          state.balance += payout;
          delete state.portfolio[slug];
          saveGameState(state);
          renderLeagueUI(container);
        }
      });
    });
  }

  function invest(slug, title, currentStars, amount) {
    var state = loadGameState();
    amount = Math.min(amount, state.balance);
    if (amount <= 0) return false;

    state.balance -= amount;
    if (state.portfolio[slug]) {
      state.portfolio[slug].investedCoins += amount;
    } else {
      state.portfolio[slug] = {
        slug: slug,
        title: title,
        boughtAtStars: currentStars,
        investedCoins: amount,
        timestamp: Date.now()
      };
    }

    saveGameState(state);
    return true;
  }

  window.TreScoutScoutLeague = {
    load: loadGameState,
    invest: invest,
    render: renderLeagueUI
  };

  document.addEventListener('DOMContentLoaded', function () {
    var targets = document.querySelectorAll('.tre-scout-league-container');
    targets.forEach(renderLeagueUI);
  });
})();
