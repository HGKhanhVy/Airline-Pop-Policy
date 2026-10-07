// Picks the page language: the visitor's earlier choice, else their browser's language,
// and lets them switch. Every text is written in both languages in the page itself, so
// the content is complete without this script; it only chooses which one shows.
(function () {
    var KEY = "airlinepop-lang";
    var root = document.documentElement;

    function stored() {
        try {
            return localStorage.getItem(KEY);
        } catch (e) {
            return null;
        }
    }

    function remember(lang) {
        try {
            localStorage.setItem(KEY, lang);
        } catch (e) {
            // Private windows may refuse storage; the choice just lasts for this page.
        }
    }

    function apply(lang) {
        root.setAttribute("data-lang", lang);
        root.setAttribute("lang", lang);
        var buttons = document.querySelectorAll("[data-lang-toggle]");
        for (var i = 0; i < buttons.length; i++) {
            buttons[i].textContent = lang === "vi" ? "EN" : "VI";
            buttons[i].setAttribute("aria-label", lang === "vi" ? "Switch to English" : "Chuyển sang tiếng Việt");
        }
        var title = document.querySelector("meta[name='title-" + lang + "']");
        if (title) {
            document.title = title.getAttribute("content");
        }
    }

    var browser = (navigator.language || "en").toLowerCase().indexOf("vi") === 0 ? "vi" : "en";
    var query = new URLSearchParams(window.location.search).get("lang");
    var initial = query === "vi" || query === "en" ? query : stored() || browser;
    apply(initial);

    document.addEventListener("click", function (event) {
        var target = event.target.closest("[data-lang-toggle]");
        if (!target) {
            return;
        }
        var next = root.getAttribute("data-lang") === "vi" ? "en" : "vi";
        remember(next);
        apply(next);
    });
})();
