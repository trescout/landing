/**
 * TreScout · Web NFC Akıllı Çip Programlayıcısı
 * ============================================
 * Web NFC API (NDEFReader / NDEFWriter) üzerinden fiziksel NTAG213/215
 * çiplere tek tıkla TreScout anında sesli bülten komutunu yazar.
 */

(function () {
  'use strict';

  var TARGET_URI = 'https://trescout.com/reports/?autoplay=audio&utm_source=nfc_puck';

  function isNfcSupported() {
    return 'NDEFReader' in window;
  }

  async function writePuckTag(onStatus) {
    if (!isNfcSupported()) {
      onStatus('❌ Bu tarayıcıda Web NFC desteklenmiyor. (Android Chrome veya NFC destekli tarayıcı gereklidir.)', 'error');
      return;
    }

    try {
      var ndef = new NDEFReader();
      onStatus('📱 Telefonunuzu masadaki NFC etiketine / diske yaklaştırın...', 'scanning');

      await ndef.write({
        records: [
          { recordType: 'url', data: TARGET_URI }
        ]
      });

      onStatus('✅ Başarılı! TreScout Akıllı Çipiniz programlandı. Artık telefonunuzu her dokundurduğunuzda günün 1 dakikalık sesli bülteni anında çalacak!', 'success');
    } catch (err) {
      onStatus('❌ Yazma hatası: ' + err.message, 'error');
    }
  }

  async function readPuckTag(onResult, onStatus) {
    if (!isNfcSupported()) {
      onStatus('❌ Web NFC desteklenmiyor.', 'error');
      return;
    }

    try {
      var ndef = new NDEFReader();
      await ndef.scan();
      onStatus('📡 NFC etiketi taranıyor...', 'scanning');

      ndef.addEventListener('reading', function (event) {
        onStatus('✅ Çip okundu!', 'success');
        onResult(event.message);
      });
    } catch (err) {
      onStatus('❌ Okuma hatası: ' + err.message, 'error');
    }
  }

  window.TreScoutNfc = {
    isSupported: isNfcSupported,
    writePuck: writePuckTag,
    readPuck: readPuckTag
  };
})();
