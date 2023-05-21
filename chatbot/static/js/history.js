const searchResultContainer = $("#containerSearchResult");
const searchInputBox = $("#inputSearch");

function requestSearch(query) {
    // Wipe container results
    searchResultContainer[0].innerHTML = '';

    // Send a POST to /search with our query
    fetch("/search", {
        method: "POST", headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify({query})
    })
        .then(response => response.json())
        .then(json => populateSearchResults(json));
}

function populateSearchResults(json) {
    json.result.forEach(v => {
        const el = document.createElement("button");
        el.type = "button";
        el.classList.add("list-group-item");
        el.classList.add("list-group-item-action");
        el.innerText = v.message;
        searchResultContainer[0].appendChild(el);
    });
}

searchInputBox.on("input", function (e) {
    const value = searchInputBox.val();
    requestSearch(value);
});

requestSearch("");