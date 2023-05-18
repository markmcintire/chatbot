$("#chattextarea").keypress(function (e) {
    if(e.which === 13 && !e.shiftKey) {
        e.preventDefault();
    var text = $(this).val();
    $(this).val('');
    add_user_reply(text);
    
    $.ajax({
    type: "POST",
    url: "/home",
    data: { prompt: text },
    success: function(data) {
        add_ai_response(data.answer);
        const element = document.getElementById("chatcontainer");
    element.scrollTop = element.scrollHeight;
    }
    });

    
    }
});


function add_user_reply(text) {
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
authorSpan.textContent = 'Me';
const dateSpan = document.createElement('span');
dateSpan.classList.add('date');
const today = new Date();
dateSpan.textContent = today.toLocaleDateString('en-US', {month: 'long', day: 'numeric', year: 'numeric'});
authorDateDiv.appendChild(authorSpan);
authorDateDiv.appendChild(dateSpan);
cardDiv.appendChild(cardBodyDiv);
cardDiv.appendChild(authorDateDiv);
rowDiv.appendChild(colDiv1);
rowDiv.appendChild(colDiv2);
colDiv2.appendChild(cardDiv);
const container = document.querySelector('div.container-sm.overflow-auto');
container.appendChild(rowDiv);
}

function add_ai_response(text) {
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
    authorSpan.textContent = 'ChatGPT';
    const dateSpan = document.createElement('span');
    dateSpan.classList.add('date');
    const today = new Date();
    dateSpan.textContent = today.toLocaleDateString('en-US', {month: 'long', day: 'numeric', year: 'numeric'});
    authorDateDiv.appendChild(authorSpan);
    authorDateDiv.appendChild(dateSpan);
    cardDiv.appendChild(cardBodyDiv);
    cardDiv.appendChild(authorDateDiv);
    rowDiv.appendChild(colDiv2);
    rowDiv.appendChild(colDiv1);
    colDiv2.appendChild(cardDiv);
    const container = document.querySelector('div.container-sm.overflow-auto');
    container.appendChild(rowDiv);
}