/* app-shim.js - chỉ chạy trong vỏ Android (WebView). Không đổi logic game.
   Mục tiêu: trang luôn vừa khung, không bị lệch/cuộn khi thanh hệ thống ẩn hiện. */
(function () {
  var de = document.documentElement;
  var st = document.createElement("style");
  st.textContent =
    "html{width:100%;height:100%;height:100dvh;overflow:hidden!important;overscroll-behavior:none;" +
    "-webkit-text-size-adjust:100%;text-size-adjust:100%;touch-action:manipulation}" +
    "body{max-width:100vw;overflow-x:hidden!important;overscroll-behavior:none;-webkit-tap-highlight-color:transparent}" +
    "html{padding:env(safe-area-inset-top) env(safe-area-inset-right) env(safe-area-inset-bottom) env(safe-area-inset-left);box-sizing:border-box}";
  (document.head || de).appendChild(st);

  var busy = false;
  function reset() {
    try {
      de.scrollLeft = 0; de.scrollTop = 0;
      if (document.body) { document.body.scrollLeft = 0; }
      window.scrollTo(0, 0);
    } catch (e) {}
  }
  function relayout() {
    reset();
    if (busy) return;
    busy = true;
    try { window.dispatchEvent(new Event("resize")); } catch (e) {}
    busy = false;
  }
  function burst() {
    relayout();
    [100, 400, 1000].forEach(function (ms) { setTimeout(relayout, ms); });
  }
  window.addEventListener("resize", function () { if (!busy) reset(); });
  window.addEventListener("orientationchange", burst);
  window.addEventListener("pageshow", burst);
  window.addEventListener("focus", burst);
  document.addEventListener("visibilitychange", function () { if (!document.hidden) burst(); });
  window.addEventListener("scroll", reset, { passive: true });
  if (window.visualViewport) window.visualViewport.addEventListener("resize", burst);
  window.addEventListener("load", burst);
  document.addEventListener("DOMContentLoaded", burst);
  /* chặn cử chỉ zoom 2 ngón và double-tap zoom */
  document.addEventListener("gesturestart", function (e) { e.preventDefault(); });
})();
