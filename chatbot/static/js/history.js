const searchResultContainer = $("#containerSearchResult");
const searchInputBox = $("#inputSearch");
const chatAreaContainer = $("#chatcontainer");

/**
 * Request conversations with a suitable message based on query
 * @param query Message query
 */
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

/**
 * Populate the search results using JSON from the server
 * @param json JSON from /search
 */
function populateSearchResults(json) {
    json.result.forEach(v => {
        const el = document.createElement("button");
        el.type = "button";
        el.classList.add("list-group-item");
        el.classList.add("list-group-item-action");
        date = new Date(v.created_at);
        date_string = date.toLocaleDateString('en-US', {  month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric'});
        // todo: make the date smaller, or move it somewhere nicer
        el.innerText = `"${v.message}" - ${date_string}`;
        el.record = v;
        el.onclick = (e) => {
            requestChatHistory(el.record.chat_id)
        };
        searchResultContainer[0].appendChild(el);
    });
}

searchInputBox.on("input", function (e) {
    const value = searchInputBox.val();
    requestSearch(value);
});

/**
 * Request the chat history for a conversation
 * @param chat_id Conversation / chat ID
 */
function requestChatHistory(chat_id) {
    // Wipe current chat history
    chatAreaContainer[0].innerHTML = '';

    // Send a POST to /history with our query
    fetch("/history", {
        method: "POST", headers: {
            'Content-Type': 'application/json'
        }, body: JSON.stringify({chat_id})
    })
        .then(response => response.json())
        .then(json => populateChatHistory(json));
}

/**
 * Populate the chat history using JSON from the server
 * @param json JSON from /history
 */
function populateChatHistory(json) {
    add_ai_response("Greetings, my dear friend! Are you ready for a wild and hilarious adventure?", null)
    json.result.forEach(v => {
        const date = new Date(v.created_at);
        if (v.role === "user")
            add_user_reply(v.message, date);
        else
            add_ai_response(v.message, date);
    });
}

requestSearch("");