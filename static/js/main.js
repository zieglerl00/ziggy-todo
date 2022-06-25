function searchTable() {

    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("default-search");
    filter = input.value.toUpperCase();
    table = document.getElementById("data-table-all");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }

}

function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("data-table-all");
    switching = true;
    dir = "asc";
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 0; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}

function copyToClipboard(pk) {
    let url = document.getElementById(`copy_to_clipboard${pk}`)
    if (url){
        navigator.clipboard.writeText(url.getAttribute("target"));
        // Get the snackbar DIV
        var x = document.getElementById("snackbar");

        // Add the "show" class to DIV
        x.className = "show";

        // After 3 seconds, remove the show class from DIV
        setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
    }
}

let nav_mode = document.getElementById("nav--mode")
function changeMode() {

    let el = document.getElementById('change--mode')
    if (el.classList.contains("dark")) {
        el.classList.remove("dark")
        nav_mode.innerHTML = "Dark Mode\n" +
            "                    <svg xmlns=\"http://www.w3.org/2000/svg\" class=\"ml-2 h-5 w-5\" fill=\"none\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" stroke-width=\"2\">\n" +
            "                      <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z\" />\n" +
            "                    </svg>"
    }
    else {
        el.classList.add("dark")
        nav_mode.innerHTML = "Light Mode\n" +
            "<svg xmlns=\"http://www.w3.org/2000/svg\" class=\"ml-2 h-5 w-5\" fill=\"none\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" stroke-width=\"2\">\n" +
            "  <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z\" />\n" +
            "</svg>"
    }
}

// On page load or when changing themes, best to add inline in `head` to avoid FOUC
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark');
        nav_mode.innerHTML = "Light Mode\n" +
            "<svg xmlns=\"http://www.w3.org/2000/svg\" class=\"ml-2 h-5 w-5\" fill=\"none\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" stroke-width=\"2\">\n" +
            "  <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z\" />\n" +
            "</svg>"
    } else {
        document.documentElement.classList.remove('dark')
        nav_mode.innerHTML = "Dark Mode\n" +
            "                    <svg xmlns=\"http://www.w3.org/2000/svg\" class=\"ml-2 h-5 w-5\" fill=\"none\" viewBox=\"0 0 24 24\" stroke=\"currentColor\" stroke-width=\"2\">\n" +
            "                      <path stroke-linecap=\"round\" stroke-linejoin=\"round\" d=\"M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z\" />\n" +
            "                    </svg>"
    }