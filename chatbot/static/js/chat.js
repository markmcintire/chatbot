var new_chat = 1
$("#chattextarea").keypress(function (e) {
    if (e.which === 13 && !e.shiftKey) {
        e.preventDefault();
        var text = $(this).val();
        this.disabled = true;
        $(this).val('');
        add_user_reply(text);

        begin_stream(text, this)
    }
});


function add_user_reply(text, date = new Date()) {
    const rowDiv = document.createElement('div');
    rowDiv.classList.add('row');
    const colDiv1 = document.createElement('div');
    colDiv1.classList.add('col');
    const colDiv2 = document.createElement('div');
    colDiv2.classList.add('col-md-8', 'text-end');
    const cardDiv = document.createElement('div');
    cardDiv.classList.add('card', 'border-0', 'bg-light', 'rounded', 'position-relative', 'mb-5', 'd-inline-block');
    const cardBodyDiv = document.createElement('div');
    cardBodyDiv.classList.add('card-body', 'p-3');
    cardBodyDiv.style.maxWidth = "856px";
    const flexRowReverseDiv = document.createElement('div');
    flexRowReverseDiv.classList.add('d-flex', 'flex-row-reverse');
    const paragraphElem = document.createElement('p');
    paragraphElem.classList.add('ps-0', 'pt-4');
    paragraphElem.style.minWidth = '300px';
    paragraphElem.style.maxWidth = '856px';
    paragraphElem.innerText = text;
    flexRowReverseDiv.appendChild(paragraphElem);
    cardBodyDiv.appendChild(flexRowReverseDiv);
    const authorDateDiv = document.createElement('div');
    authorDateDiv.classList.add('author-date', 'position-absolute', 'top-0', 'end-0', 'p-3');
    const authorSpan = document.createElement('span');
    authorSpan.classList.add('author', 'me-2');
    authorSpan.innerHTML = 'Me';
    const dateSpan = document.createElement('span');
    dateSpan.classList.add('date');
    dateSpan.textContent = date.toLocaleDateString('en-US', {month: 'long', day: 'numeric', year: 'numeric'});
    authorDateDiv.appendChild(authorSpan);
    authorDateDiv.appendChild(dateSpan);
    cardDiv.appendChild(cardBodyDiv);
    cardDiv.appendChild(authorDateDiv);
    rowDiv.appendChild(colDiv1);
    rowDiv.appendChild(colDiv2);
    colDiv2.appendChild(cardDiv);
    const container = document.getElementById("chatcontainer");
    container.appendChild(rowDiv);
}

function add_ai_response(text, date = new Date()) {
    const rowDiv = document.createElement('div');
    rowDiv.classList.add('row');
    const colDiv1 = document.createElement('div');
    colDiv1.classList.add('col');
    const colDiv2 = document.createElement('div');
    colDiv2.classList.add('col-md-8', 'text-start');
    const cardDiv = document.createElement('div');
    cardDiv.classList.add('card', 'border-0', 'bg-light', 'rounded', 'position-relative', 'mb-5', 'd-inline-block');
    const cardBodyDiv = document.createElement('div');
    cardBodyDiv.classList.add('card-body', 'p-3');
    cardBodyDiv.style.maxWidth = "856px";
    const flexRowReverseDiv = document.createElement('div');
    flexRowReverseDiv.classList.add('d-flex', 'flex-row-reverse');
    const paragraphElem = document.createElement('p');
    paragraphElem.classList.add('ps-0', 'pt-4');
    paragraphElem.style.minWidth = '300px';
    paragraphElem.style.maxWidth = '856px';
    paragraphElem.innerText = text;
    flexRowReverseDiv.appendChild(paragraphElem);
    cardBodyDiv.appendChild(flexRowReverseDiv);
    const authorDateDiv = document.createElement('div');
    authorDateDiv.classList.add('author-date', 'position-absolute', 'top-0', 'start-0', 'p-3');
    const authorSpan = document.createElement('span');
    authorSpan.classList.add('author', 'me-2');
    authorSpan.innerHTML =  'James the Wise'
    const dateSpan = document.createElement('span');
    dateSpan.classList.add('date');
    if(date != null) {
      dateSpan.textContent = date.toLocaleDateString('en-US', {month: 'long', day: 'numeric', year: 'numeric'});
    } else {
      dateSpan.textContent = ""
      cardDiv.classList.add('mt-5')
    }
    authorDateDiv.appendChild(authorSpan);
    authorDateDiv.appendChild(dateSpan);
    cardDiv.appendChild(cardBodyDiv);
    cardDiv.appendChild(authorDateDiv);
    rowDiv.appendChild(colDiv2);
    rowDiv.appendChild(colDiv1);
    colDiv2.appendChild(cardDiv);
    const container = document.getElementById("chatcontainer");
    container.appendChild(rowDiv);
    return paragraphElem
}

function begin_stream(input, inputbox) {
    textbox = add_ai_response("")
    const container = document.getElementById("chatcontainer");
    fetch("/stream", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({input: input, new_chat: new_chat})
    })
        .then(response => {
            const reader = response.body.getReader();
            return new ReadableStream({
                start(controller) {
                    function push() {
                        reader.read().then(({done, value}) => {
                            if (done) {
                                controller.close();
                                return;
                            }
                            controller.enqueue(value);
                            push();
                        });
                    }

                    push();
                }
            });
        })
        .then(stream => {
            const decoder = new TextDecoder();
            const reader = stream.getReader();

            function readChunk() {
                reader.read().then(({done, value}) => {
                    if (done) {
                        console.log('End of stream');
                        inputbox.disabled = false
                        return;
                    }
                    textbox.innerText += decoder.decode(value);
                    container.scrollTop = container.scrollHeight;
                    readChunk();
                });
            }

            readChunk();
        })
        .catch(error => {
            console.error(error);
        });
    new_chat = 0

}
