(function () {
  var root = document.documentElement;
  var saved = localStorage.getItem("theme");

  if (saved === "light" || saved === "dark") {
    root.setAttribute("data-theme", saved);
  } else {
    root.setAttribute("data-theme", "dark");
  }

  var updateAllPressed = function () {
    var theme = root.getAttribute("data-theme");
    var pressed = theme === "dark" ? "true" : "false";
    document.querySelectorAll(".theme-toggle").forEach(function (btn) {
      btn.setAttribute("aria-pressed", pressed);
    });
  };

  updateAllPressed();
  document.querySelectorAll(".theme-toggle").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var theme = root.getAttribute("data-theme");
      var next = theme === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      localStorage.setItem("theme", next);
      updateAllPressed();
    });
  });
})();
